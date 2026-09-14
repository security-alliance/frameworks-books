"""Run with: python3 -m unittest discover -s tests -v."""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
FIXTURES = PROJECT / "tests" / "fixtures"


class ContainerWrapperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="book-wrapper-test-", dir=PROJECT.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        (self.bin / "id").symlink_to(FIXTURES / "id")
        for engine in ("podman", "docker"):
            (self.bin / engine).symlink_to(FIXTURES / "engine.py")
        self.log = self.root / "commands.jsonl"
        self.env = os.environ.copy()
        for key in ("FRAMEWORKS_REPO", "BOOK_BUILD_PULL", "BOOK_BUILD_IMAGE", "DOCKER_HOST",
                    "REF", "BASE_URL", "FAKE_HOST_UID"):
            self.env.pop(key, None)
        self.env.update(
            PATH=str(self.bin) + os.pathsep + self.env["PATH"],
            TMPDIR=str(self.root),
            FAKE_ENGINE_LOG=str(self.log),
            FAKE_IMAGE_PRESENT="0",
            FAKE_BUILD_EXIT="0",
            FAKE_RUN_EXIT="0",
            REGISTRY_AUTH_FILE="/unavailable/saved-registry-credentials.json",
            DOCKER_CONFIG="/unavailable/saved-docker-config",
            CONTAINERS_REGISTRIES_CONF="/unavailable/saved-registry-config",
            DOCKER_AUTH_CONFIG='{"auths":{"docker.io":{"auth":"synthetic-test-value"}}}',
            DOCKER_CONTEXT="desktop-linux",
            BUILDX_BUILDER="unrelated-private-builder",
            FAKE_DOCKER_HOST="unix:///run/user/1000/docker.sock",
        )

    def invoke(self, engine=None, args=(), **overrides):
        env = self.env.copy()
        if engine:
            env["CONTAINER_ENGINE"] = engine
        else:
            env.pop("CONTAINER_ENGINE", None)
        env.update(overrides)
        result = subprocess.run(
            [str(PROJECT / "container" / "build.sh"), *args],
            env=env, capture_output=True, text=True,
        )
        records = [json.loads(line) for line in self.log.read_text().splitlines()] if self.log.exists() else []
        return result, records

    def command(self, records, subcommand):
        return next(record for record in records if subcommand in record["args"])

    def assert_runtime_offline(self, record):
        self.assertIn("--pull=never", record["args"])
        self.assertIn("--read-only", record["args"])
        self.assertIn("--user", record["args"])
        self.assertIn("1000:1000", record["args"])
        offset = record["args"].index("--network")
        self.assertEqual(record["args"][offset + 1], "none")

    def test_podman_explicit_anonymous_file_and_no_helpers(self):
        result, records = self.invoke("podman")
        self.assertEqual(result.returncode, 0, result.stderr)
        build = self.command(records, "build")
        self.assertEqual(json.loads(build["podman_config"]), {"auths": {}})
        offset = build["args"].index("--authfile")
        self.assertEqual(build["args"][offset + 1], build["REGISTRY_AUTH_FILE"])
        self.assertIn('credential-helpers = ["containers-auth.json"]', build["registries_config"])
        self.assertIsNone(build["DOCKER_AUTH_CONFIG"])
        self.assertFalse(Path(build["REGISTRY_AUTH_FILE"]).parent.exists())
        run = self.command(records, "run")
        self.assert_runtime_offline(run)
        self.assertIn("--userns=keep-id", run["args"])
        self.assertIn("USE_GENERATED=1", run["args"])

    def test_docker_isolated_config_and_selected_rootless_socket(self):
        result, records = self.invoke("docker")
        self.assertEqual(result.returncode, 0, result.stderr)
        build = self.command(records, "build")
        self.assertEqual(json.loads(build["docker_config"]), {"auths": {"book-build.invalid": {}}})
        self.assertNotIn("credsStore", json.loads(build["docker_config"]))
        self.assertNotIn("credHelpers", json.loads(build["docker_config"]))
        self.assertEqual(build["DOCKER_HOST"], self.env["FAKE_DOCKER_HOST"])
        for key in ("DOCKER_CONTEXT", "DOCKER_AUTH_CONFIG", "BUILDX_BUILDER", "REGISTRY_AUTH_FILE"):
            self.assertIsNone(build[key])
        self.assertFalse(Path(build["DOCKER_CONFIG"]).exists())
        self.assert_runtime_offline(self.command(records, "run"))

    def test_explicit_docker_host_is_preserved_without_context_lookup(self):
        result, records = self.invoke("docker", DOCKER_HOST="unix:///custom/docker.sock", DOCKER_CONTEXT="")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any("context" in record["args"] for record in records))
        self.assertEqual(self.command(records, "build")["DOCKER_HOST"], "unix:///custom/docker.sock")

    def test_docker_context_takes_precedence_over_inherited_host(self):
        result, records = self.invoke("docker", DOCKER_HOST="unix:///wrong/docker.sock")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.command(records, "build")["DOCKER_HOST"], self.env["FAKE_DOCKER_HOST"])

    def test_local_npipe_context_is_supported(self):
        result, records = self.invoke("docker", FAKE_DOCKER_HOST="npipe:////./pipe/docker_engine")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_runtime_offline(self.command(records, "run"))

    def test_cached_toolchain_skips_build_for_both_engines(self):
        for engine in ("podman", "docker"):
            with self.subTest(engine=engine):
                if self.log.exists():
                    self.log.unlink()
                result, records = self.invoke(engine, FAKE_IMAGE_PRESENT="1")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse(any("build" in record["args"] for record in records))
                self.assert_runtime_offline(self.command(records, "run"))

    def test_force_refresh_rebuilds_even_if_image_exists(self):
        for engine, flag in (("podman", "--pull=always"), ("docker", "--pull")):
            with self.subTest(engine=engine):
                if self.log.exists():
                    self.log.unlink()
                result, records = self.invoke(engine, FAKE_IMAGE_PRESENT="1", BOOK_BUILD_PULL="1")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(flag, self.command(records, "build")["args"])

    def test_target_and_make_variables_are_forwarded(self):
        result, records = self.invoke("podman", args=("render", "LATEXMK_ENGINE=-lualatex", "USE_GENERATED=1"))
        self.assertEqual(result.returncode, 0, result.stderr)
        run = self.command(records, "run")
        self.assertEqual(run["args"][-4:], ["render", "USE_GENERATED=1", "LATEXMK_ENGINE=-lualatex", "USE_GENERATED=1"])

    def test_framework_checkout_with_spaces_is_read_only(self):
        checkout = self.root / "framework checkout"
        checkout.mkdir()
        result, records = self.invoke("podman", FRAMEWORKS_REPO=str(checkout), REF="main")
        self.assertEqual(result.returncode, 0, result.stderr)
        run = self.command(records, "run")
        self.assertIn(f"type=bind,src={checkout},dst=/frameworks,ro", run["args"])
        self.assertIn("FRAMEWORKS_REPO=/frameworks", run["args"])
        self.assertIn("BASE_URL=https://frameworks.securityalliance.org", run["args"])
        self.assertNotIn("USE_GENERATED=1", run["args"])

    def test_build_failure_is_preserved_and_configuration_cleaned(self):
        for engine in ("podman", "docker"):
            with self.subTest(engine=engine):
                if self.log.exists():
                    self.log.unlink()
                result, records = self.invoke(engine, FAKE_BUILD_EXIT="42")
                self.assertEqual(result.returncode, 42)
                build = self.command(records, "build")
                config = Path(build["REGISTRY_AUTH_FILE"]).parent if engine == "podman" else Path(build["DOCKER_CONFIG"])
                self.assertFalse(config.exists())
                self.assertFalse(any("run" in record["args"] for record in records))

    def test_runtime_failure_is_preserved_and_configuration_cleaned(self):
        result, records = self.invoke("docker", FAKE_RUN_EXIT="37")
        self.assertEqual(result.returncode, 37)
        self.assertFalse(Path(self.command(records, "run")["DOCKER_CONFIG"]).exists())

    def test_remote_docker_context_fails_before_any_pull(self):
        result, records = self.invoke("docker", FAKE_DOCKER_HOST="tcp://remote.example:2376")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local Docker socket", result.stderr)
        self.assertFalse(any("build" in record["args"] for record in records))
        self.assertEqual(list(self.root.glob("book-build.*")), [])

    def test_podman_is_preferred_when_both_engines_exist(self):
        result, records = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({record["engine"] for record in records}, {"podman"})

    def test_root_invocation_is_rejected_without_engine_calls(self):
        result, records = self.invoke("podman", FAKE_HOST_UID="0")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unprivileged user", result.stderr)
        self.assertEqual(records, [])

    def test_invalid_engine_is_rejected_without_engine_calls(self):
        result, records = self.invoke("unsupported")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(records, [])


if __name__ == "__main__":
    unittest.main()
