#!/bin/sh
set -eu
if [ ! -d .git ]; then
  echo 'Run this script from your Git repository root.' >&2
  exit 1
fi
mkdir -p .git/hooks
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo 'Pre-commit hook installed.'
