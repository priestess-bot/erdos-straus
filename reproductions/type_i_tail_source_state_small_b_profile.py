#!/usr/bin/env python3
"""Minimize B among source-state normal realizations on the 500M tail-miss bridge set."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORT = ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json"
REALIZATION = ROOT / "reproductions" / "type_i_normal_source_state_realization.py"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-tail-source-state-small-b-profile-500m-results.json"
H19_MENU = {1, 2, 4, 7, 13}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


realization = load_module("tail_source_state_small_b_realization", REALIZATION)


def run_audit(support: dict[str, object]) -> dict[str, object]:
    if len(support["records"]) != 1717:
        raise AssertionError("input is not the exact 500M tail-miss bridge profile")
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
        rows.append({"prime": prime, "least_B_form": forms[0]})
    histogram = Counter(str(row["least_B_form"]["B"]) for row in rows)
    outside = [row for row in rows if row["least_B_form"]["B"] not in H19_MENU]
    max_row = max(rows, key=lambda row: (row["least_B_form"]["B"], row["prime"]))
    return {
        "arithmetic": (
            "for every 500M ordinary-tail miss with its independently minimized even source state, enumerate "
            "all source-state normal realizations via BC|K and select lexicographically by (B,C,A,m)"
        ),
        "scope_note": (
            "A cross-sample finite small-B profile. It tests the H19 menu but does not prove any uniform B bound."
        ),
        "ordinary_tail_miss_count": len(rows),
        "least_B_histogram": dict(sorted(histogram.items(), key=lambda item: int(item[0]))),
        "maximum_least_B_record": max_row,
        "H19_menu": sorted(H19_MENU),
        "outside_H19_menu_count": len(outside),
        "outside_H19_menu_records": outside,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.support.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "outside_H19_menu_records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
