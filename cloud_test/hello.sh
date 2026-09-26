#!/usr/bin/env bash
# Minimal cloud-execution smoke test: prints host/runtime info, nothing sensitive.
echo "Cloud test OK: $(date -u +%FT%TZ)"
uname -a
echo "R:      $(command -v Rscript >/dev/null && Rscript --version 2>&1 || echo 'not installed')"
echo "Python: $(python3 --version 2>&1)"
echo "Git:    $(git --version)"
echo "Repo:   $(git remote get-url origin) @ $(git rev-parse --abbrev-ref HEAD)"
