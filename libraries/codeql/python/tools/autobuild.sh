#!/bin/sh

set -eu

# Legacy environment variables for the autobuild infrastructure.
LGTM_SRC="$(pwd)"
LGTM_WORKSPACE="$CODEQL_EXTRACTOR_PYTHON_SCRATCH_DIR"
export LGTM_SRC
export LGTM_WORKSPACE

if which python >/dev/null; then
    exec python "$CODEQL_EXTRACTOR_PYTHON_ROOT/tools/index.py"
elif which python3 >/dev/null; then
    exec python3 "$CODEQL_EXTRACTOR_PYTHON_ROOT/tools/index.py"
elif which python2 >/dev/null; then
    exec python2 "$CODEQL_EXTRACTOR_PYTHON_ROOT/tools/index.py"
else
    echo "ERROR: Could not find a valid Python distribution. It should be available when running 'which python', 'which python3' or 'which python2' in your shell"
    exit 1
fi