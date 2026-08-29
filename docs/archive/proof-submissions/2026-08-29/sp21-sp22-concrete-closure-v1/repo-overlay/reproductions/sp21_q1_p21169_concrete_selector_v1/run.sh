#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$ROOT/reproductions/sp21_q1_p21169_concrete_selector_v1"
python "$ROOT/scripts/t6_sp21_q1_p21169_concrete_selector_v1.py" \
  --repo-root "$ROOT" \
  --output "$OUT/evidence-v1.json"
python "$ROOT/scripts/t6_sp21_q1_p21169_independent_replayer_v1.py" \
  --repo-root "$ROOT" \
  --evidence "$OUT/evidence-v1.json" \
  --output "$OUT/independent-replay-v1.json"
python -m unittest tests.test_t6_sp21_q1_p21169_concrete_selector_v1 -v
