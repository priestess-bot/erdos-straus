#!/usr/bin/env python3
"""Profile the B=1 source-state realization boundary on all 1B H19 even bridges."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
REALIZATION = ROOT / "reproductions" / "type_i_normal_source_state_realization.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-b1-source-state-boundary-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


realization = load_module("h19_b1_source_state_realization", REALIZATION)


def run_audit(support: dict[str, object]) -> dict[str, object]:
    if len(support["records"]) != 664:
        raise AssertionError("input is not the exact 1B H19 bridge profile")
    records, misses = [], []
    for entry in support["records"]:
        prime = int(entry["prime"])
        edge = entry["selected_edge"]
        source = int(edge["reverse_two_tail_lift"]["source_denominator"])
        bridge = int(edge["E"])
        forms = realization.source_state_forms(prime, source, bridge)
        B_one_count = sum(form["B"] == 1 for form in forms)
        record = {
            "prime": prime,
            "p_mod_48": prime % 48,
            "compatible_normal_form_count": len(forms),
            "B_eq_1_form_count": B_one_count,
        }
        records.append(record)
        if not B_one_count:
            misses.append(record)
    p25_records = [record for record in records if record["p_mod_48"] == 25]
    p25_misses = [record["prime"] for record in misses if record["p_mod_48"] == 25]
    return {
        "arithmetic": (
            "for every independently minimized H19 even bridge (p,n,E), enumerate all source-state "
            "normal realizations via divisor pairs BC|K and count those with B=1"
        ),
        "scope_note": (
            "A finite B=1 realization profile on the stored H19 source-free subset. It does not prove a "
            "uniform B=1 selector or an external-source complement beyond this input."
        ),
        "h19_even_bridge_count": len(records),
        "B_eq_1_realization_count": len(records) - len(misses),
        "B_eq_1_miss_count": len(misses),
        "B_eq_1_misses": misses,
        "p_eq_25_mod_48_count": len(p25_records),
        "p_eq_25_mod_48_B_eq_1_realization_count": len(p25_records) - len(p25_misses),
        "p_eq_25_mod_48_B_eq_1_misses": p25_misses,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.support.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "B_eq_1_misses"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
