#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 sp04_constructor.py
python3 sp04_verifier.py
