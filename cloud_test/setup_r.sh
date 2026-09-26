#!/usr/bin/env bash
# Cloud environment setup script: installs R from Ubuntu's own apt archive.
# Paste into the environment's "Setup script" field; runs as root at session start.
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive

if ! command -v Rscript >/dev/null; then
  apt-get update -qq
  # r-base-dev brings compilers/headers so source packages can build later.
  apt-get install -y -qq --no-install-recommends r-base-core r-base-dev
fi

Rscript --version
