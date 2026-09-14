#!/usr/bin/env bash
set -Eeuo pipefail

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
image="${BOOK_BUILD_IMAGE:-seal-physical-security-book:anonymous-v2}"
target="${1:-package}"
if (( $# > 0 )); then
  shift
fi

if [[ "$(id -u)" == 0 ]]; then
  die 'run this wrapper as an unprivileged user'
fi

engine="${CONTAINER_ENGINE:-}"
if [[ -z "$engine" ]]; then
  if command -v podman >/dev/null 2>&1; then
    engine=podman
  elif command -v docker >/dev/null 2>&1; then
    engine=docker
  else
    die 'Podman or Docker is required'
  fi
fi

case "$engine" in
  podman|docker) ;;
  *) die 'CONTAINER_ENGINE must be podman or docker' ;;
esac
command -v "$engine" >/dev/null 2>&1 || die "$engine is not installed"

# Registry credentials are deliberately excluded. Do not alter the caller's
# saved configuration, container storage, or engine socket.
book_config_dir="$(mktemp -d "${TMPDIR:-/tmp}/book-build.XXXXXXXX")"
cleanup() {
  rm -rf -- "$book_config_dir"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

unset DOCKER_AUTH_CONFIG
engine_cmd=("$engine")
build_args=(--file "$project_dir/Containerfile" --tag "$image")

if [[ "$engine" == podman ]]; then
  cp "$project_dir/container/anonymous/podman.json" "$book_config_dir/auth.json"
  # Also exclude globally configured external registry credential helpers.
  export CONTAINERS_REGISTRIES_CONF="$project_dir/container/anonymous/registries.conf"
  export REGISTRY_AUTH_FILE="$book_config_dir/auth.json"
  build_args+=(--authfile "$REGISTRY_AUTH_FILE")
else
  # Resolve a local Docker context before replacing its client configuration.
  # This preserves Docker Desktop and rootless Docker socket selection.
  if [[ -n "${DOCKER_HOST:-}" && -z "${DOCKER_CONTEXT:-}" ]]; then
    book_docker_host="$DOCKER_HOST"
  else
    book_docker_host="$(docker context inspect --format '{{.Endpoints.docker.Host}}')"
  fi
  case "$book_docker_host" in
    unix://*|npipe://*) ;;
    *) die 'this wrapper requires a local Docker socket; select a local Docker context' ;;
  esac
  cp "$project_dir/container/anonymous/docker.json" "$book_config_dir/config.json"
  unset DOCKER_CONTEXT BUILDX_BUILDER REGISTRY_AUTH_FILE
  export DOCKER_CONFIG="$book_config_dir"
  export DOCKER_HOST="$book_docker_host"
  engine_cmd+=(--config "$book_config_dir" --host "$book_docker_host")
fi

if [[ "${BOOK_BUILD_PULL:-0}" == 1 ]]; then
  if [[ "$engine" == podman ]]; then
    build_args+=(--pull=always)
  else
    build_args+=(--pull)
  fi
fi
if [[ "${BOOK_BUILD_PULL:-0}" == 1 ]] || ! "${engine_cmd[@]}" image inspect "$image" >/dev/null 2>&1; then
  "${engine_cmd[@]}" build "${build_args[@]}" "$project_dir"
fi

run_args=(
  --rm
  --pull=never
  --network none
  --cap-drop ALL
  --security-opt no-new-privileges=true
  --pids-limit 512
  --read-only
  --tmpfs /tmp:rw,nosuid,nodev,noexec,size=512m
  --user "$(id -u):$(id -g)"
  --mount "type=bind,src=$project_dir,dst=/work"
)

if [[ "$engine" == podman ]]; then
  run_args+=(--userns=keep-id)
fi

ref="${REF:-develop}"
if [[ -n "${BASE_URL:-}" ]]; then
  base_url="$BASE_URL"
elif [[ "$ref" == main ]]; then
  base_url=https://frameworks.securityalliance.org
else
  base_url=https://frameworks.securityalliance.dev
fi

frameworks_repo="${FRAMEWORKS_REPO:-}"
if [[ -z "$frameworks_repo" ]]; then
  in_repo_candidate="$(cd -- "$project_dir/../.." 2>/dev/null && pwd -P || true)"
  adjacent_candidate="$(cd -- "$project_dir/../frameworks" 2>/dev/null && pwd -P || true)"
  if [[ -d "$in_repo_candidate/docs/pages/physical-security" ]]; then
    frameworks_repo="$in_repo_candidate"
  elif [[ -d "$adjacent_candidate/docs/pages/physical-security" ]]; then
    frameworks_repo="$adjacent_candidate"
  fi
fi

make_args=("$target")
if [[ -n "$frameworks_repo" ]]; then
  [[ -d "$frameworks_repo" ]] || die "FRAMEWORKS_REPO is not a directory: $frameworks_repo"
  frameworks_repo="$(cd -- "$frameworks_repo" && pwd -P)"
  run_args+=(--mount "type=bind,src=$frameworks_repo,dst=/frameworks,ro")
  make_args+=("FRAMEWORKS_REPO=/frameworks" "REF=$ref" "BASE_URL=$base_url")
else
  make_args+=("USE_GENERATED=1")
fi

make_args+=("$@")
"${engine_cmd[@]}" run "${run_args[@]}" "$image" "${make_args[@]}"
