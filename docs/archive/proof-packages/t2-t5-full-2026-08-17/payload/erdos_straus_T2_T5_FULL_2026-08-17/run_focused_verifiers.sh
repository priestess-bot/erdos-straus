#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/T2_atomic_admission_v1/reproductions/type_i_atomic_admission_v1_contract.py"
python3 "$HERE/T5_global_well_foundedness_full/reproductions/type_i_t5_full_global_well_foundedness.py"
python3 "$HERE/T5_global_well_foundedness_full/reproductions/type_i_t5_transition_surface_audit.py"
python3 -m json.tool "$HERE/T5_global_well_foundedness_full/data/t5-full-phase-registry-v2.json" >/dev/null
python3 -m json.tool "$HERE/T5_global_well_foundedness_full/data/t5-full-transition-taxonomy-v2.json" >/dev/null
printf '%s\n' 'T2 + T5 FULL focused checks passed'
