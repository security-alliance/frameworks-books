# Container build

The image contains only the document toolchain. The source is bind-mounted at
runtime, so rebuilding the image is unnecessary for content or layout changes.

## Commands

Build the bundled snapshot:

```sh
./container/build.sh
```

Synchronize from a local Frameworks checkout and build:

```sh
FRAMEWORKS_REPO=/absolute/path/to/frameworks ./container/build.sh
```

Run another Make target or override a Make variable:

```sh
./container/build.sh render USE_GENERATED=1
FRAMEWORKS_REPO=/absolute/path/to/frameworks ./container/build.sh package REF=main
```

Force the runtime or refresh the pinned base image:

```sh
CONTAINER_ENGINE=docker ./container/build.sh
BOOK_BUILD_PULL=1 ./container/build.sh
```

Artifacts are written to `output/` in the host source directory.

## Anonymous public pulls

No registry account, login, password, or push step is needed. The wrapper
automatically excludes saved registry credentials; do not delete your host
credential files or change your other projects' settings.

- Podman receives an explicit empty credential file and a project-scoped
  registry configuration that disables external credential helpers. It pulls
  directly from the fully qualified public Docker Hub base image, without
  host-configured registry mirrors or remapping.
- Docker receives a temporary credential-free client configuration, while
  preserving the selected local engine socket (including rootless Docker and
  Docker Desktop). The empty `book-build.invalid` entry contains no credentials;
  it prevents Docker from automatically discovering a host credential helper.
- Inherited `DOCKER_AUTH_CONFIG` is excluded. Temporary configuration is removed
  on completion or failure. Host credential files are never modified.
- The document container uses `--pull=never`, so runtime cannot access a
  registry at all.

Docker Hub's public registry protocol still obtains an anonymous bearer token;
this is not a user login and cannot be removed from the client-side script.
See the [registry protocol](https://docs.docker.com/reference/api/registry/auth/)
and [Podman credential-file option](https://docs.podman.io/en/stable/markdown/podman-build.1.html#authfile-path).

The wrapper targets local Linux container engines. Remote Docker contexts are
not supported because the project is bind-mounted from the local host. Docker
Desktop must be using Linux containers.

## Execution model

- Debian 13.6 slim base image pinned to a multi-platform OCI digest.
- Debian-packaged Python, pypdf, Pandoc, Poppler, TeX Live, and Latin Modern.
- Build process runs as the invoking host UID/GID.
- Container root filesystem is read-only; only the project mount and `/tmp`
  are writable.
- Frameworks checkout is mounted read-only.
- Runtime networking is disabled.
- All Linux capabilities are dropped and privilege escalation is disabled.
- No container engine socket, home directory, SSH agent, or credentials are
  mounted.

Image construction requires network access for the base image and signed Debian
packages. Runtime compilation does not.

The base is the official `trixie-20260824-slim` image, pinned to the
[published multi-platform index](https://hub.docker.com/layers/library/debian/trixie-slim/)
`sha256:d7e12182ce18b85b93007c1dedf31f2d29e01ccf3182cc4017c709b6259bc132`.

## Wrapper tests

With Python 3 on the host:

```sh
python3 -m unittest discover -s tests -v
```

These use simulated container CLIs to check anonymous configuration, engine
selection, offline runtime, cache refresh, argument forwarding, and cleanup.
They do not replace an end-to-end container build.
