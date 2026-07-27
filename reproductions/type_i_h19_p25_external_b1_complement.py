#!/usr/bin/env python3
"""Cross-check that the p=25 (mod 48) B=1 boundary is externally covered."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
B1 = ROOT / "reproductions" / "type-i-h19-b1-source-state-boundary-1b-results.json"
K2 = ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json"
K6 = ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json"
VARIABLE = ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-p25-external-b1-complement-1b-results.json"


def run_audit(b1: dict[str, object], k2: dict[str, object], k6: dict[str, object], variable: dict[str, object]) -> dict[str, object]:
    k2_hits = {int(record["prime"]) for record in k2["records"]}
    k6_hits = {int(record["prime"]) for record in k6["records"]}
    variable_hits = {int(record["prime"]) for record in variable["records"]}
    external_residuals = {int(record["prime"]) for record in variable["variable_even_scale_misses"]}
    p25 = k2_hits | k6_hits | variable_hits | external_residuals
    b1_misses = {int(record["prime"]) for record in b1["B_eq_1_misses"] if int(record["p_mod_48"]) == 25}
    b1_hits = p25 - b1_misses
    if len(p25) != 243 or len(b1_misses) != 6 or not b1_misses <= (k2_hits | k6_hits | variable_hits):
        raise AssertionError("p=25 B=1 and external coverage did not compose")
    if external_residuals & b1_misses:
        raise AssertionError("external residue boundary overlapped the B=1 boundary")
    return {
        "arithmetic": (
            "intersect the complete p=25 (mod 48) external-scale partition with the independently "
            "enumerated B=1 source-state realization boundary"
        ),
        "scope_note": (
            "A finite overlap-coverage statement, not a disjoint partition and not a uniform external-or-B=1 theorem."
        ),
        "p_eq_25_mod_48_count": len(p25),
        "B_eq_1_realization_count": len(b1_hits),
        "B_eq_1_miss_count": len(b1_misses),
        "B_eq_1_misses": sorted(b1_misses),
        "B_eq_1_miss_fixed_k2_count": len(b1_misses & k2_hits),
        "B_eq_1_miss_fixed_k6_count": len(b1_misses & k6_hits),
        "B_eq_1_miss_variable_scale_count": len(b1_misses & variable_hits),
        "external_residue_boundary_count": len(external_residuals),
        "external_residue_boundary_B_eq_1_realization_count": len(external_residuals - b1_misses),
        "external_or_B_eq_1_covered_count": len((k2_hits | k6_hits | variable_hits) | b1_hits),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--b1", type=Path, default=B1)
    parser.add_argument("--k2", type=Path, default=K2)
    parser.add_argument("--k6", type=Path, default=K6)
    parser.add_argument("--variable", type=Path, default=VARIABLE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.b1.read_text(encoding="utf-8")),
        json.loads(args.k2.read_text(encoding="utf-8")),
        json.loads(args.k6.read_text(encoding="utf-8")),
        json.loads(args.variable.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
