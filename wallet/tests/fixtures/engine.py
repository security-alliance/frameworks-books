#!/usr/bin/env python3
"""Simulated CLI for wrapper regression tests; never starts a container."""

import json
import os
from pathlib import Path
import sys

engine = Path(sys.argv[0]).name
args = sys.argv[1:]
record = {"engine": engine, "args": args}
for key in (
    "REGISTRY_AUTH_FILE", "DOCKER_CONFIG", "DOCKER_AUTH_CONFIG",
    "CONTAINERS_REGISTRIES_CONF", "DOCKER_HOST", "DOCKER_CONTEXT",
    "BUILDX_BUILDER",
):
    record[key] = os.environ.get(key)
for env_key, record_key, suffix in (
    ("REGISTRY_AUTH_FILE", "podman_config", ""),
    ("DOCKER_CONFIG", "docker_config", "config.json"),
    ("CONTAINERS_REGISTRIES_CONF", "registries_config", ""),
):
    value = os.environ.get(env_key)
    if value:
        path = Path(value) / suffix if suffix else Path(value)
        if path.is_file():
            record[record_key] = path.read_text()
with Path(os.environ["FAKE_ENGINE_LOG"]).open("a") as log:
    log.write(json.dumps(record) + "\n")

# Remove Docker's global options before dispatching the subcommand.
while args and args[0] in ("--config", "--host"):
    args = args[2:]
if args[:2] == ["context", "inspect"]:
    print(os.environ.get("FAKE_DOCKER_HOST", "unix:///run/user/1000/docker.sock"))
elif args[:2] == ["image", "inspect"]:
    sys.exit(0 if os.environ.get("FAKE_IMAGE_PRESENT") == "1" else 1)
elif args and args[0] in ("build", "run"):
    sys.exit(int(os.environ.get("FAKE_" + args[0].upper() + "_EXIT", "0")))
else:
    sys.exit("unexpected simulated CLI command")
