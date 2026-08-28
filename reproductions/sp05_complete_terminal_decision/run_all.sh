#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT"
python "$ROOT/generate_evidence.py"
python -m unittest -v "$ROOT/test_sp05.py"
python "$ROOT/validate_schemas.py"
python -m py_compile "$ROOT"/*.py
