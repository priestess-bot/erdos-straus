#!/usr/bin/env python3
"""Minimize B among source-state normal realizations on the 1B H19 bridge set."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
REALIZATION = ROOT / "reproductions" / "type_i_normal_source_state_realization.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-source-state-small-b-profile-1b-results.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


realization = load_module("h19_source_state_small_b_realization", REALIZATION)


def histogram(rows: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(str(row["least_B_form"]["B"]) for row in rows)
    return dict(sorted(counts.items(), key=lambda item: int(item[0])))


def run_audit(support: dict[str, object]) -> dict[str, object]:
    if len(support["records"]) != 664:
        raise AssertionError("input is not the exact 1B H19 bridge profile")
    rows = []
    for entry in support["records"]:
        prime = int(entry["prime"])
        edge = entry["selected_edge"]
        forms = realization.source_state_forms(
            prime,
            int(edge["reverse_two_tail_lift"]["source_denominator"]),
            int(edge["E"]),
        )
        if not forms:
            raise AssertionError("stored source state lost all normal realizations")
        rows.append({"prime": prime, "p_mod_48": prime % 48, "least_B_form": forms[0]})
    p25 = [row for row in rows if row["p_mod_48"] == 25]
    max_row = max(rows, key=lambda row: (row["least_B_form"]["B"], row["prime"]))
    max_m_row = max(rows, key=lambda row: (row["least_B_form"]["m"], row["prime"]))
    max_p25_row = max(p25, key=lambda row: (row["least_B_form"]["B"], row["prime"]))
    max_p25_m_row = max(p25, key=lambda row: (row["least_B_form"]["m"], row["prime"]))
    exceptions = [row for row in rows if row["least_B_form"]["B"] > 1]
    return {
        "arithmetic": (
            "for every independently selected H19 even source state, enumerate all normal realizations "
            "from BC|K and select lexicographically by (B,C,A,m); verify every selected form exactly"
        ),
        "scope_note": (
            "A finite small-B realization profile conditional on the stored gap-at-most-215 source states. "
            "The re-realized normal gaps m need not be uniformly small, and the result is not a global bound."
        ),
        "h19_even_bridge_count": len(rows),
        "least_B_histogram": histogram(rows),
        "maximum_least_B_record": max_row,
        "maximum_selected_m_record": max_m_row,
        "B_gt_1_records": exceptions,
        "p_eq_25_mod_48_count": len(p25),
        "p_eq_25_mod_48_least_B_histogram": histogram(p25),
        "p_eq_25_mod_48_maximum_least_B_record": max_p25_row,
        "p_eq_25_mod_48_maximum_selected_m_record": max_p25_m_row,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.support.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "B_gt_1_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
