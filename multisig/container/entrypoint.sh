#!/bin/sh
set -eu

mkdir -p "$HOME"
umask 022

exec make "$@"
