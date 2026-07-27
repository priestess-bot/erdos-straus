#!/usr/bin/env python3
"""Compose the external-scale partition with the low-support internal Type I bridge."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
K2 = ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json"
K6 = ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json"
VARIABLE = ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json"
SUPPORT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-p25-external-internal-hybrid-1b-results.json"


def run_audit(
    k2: dict[str, object], k6: dict[str, object], variable: dict[str, object], support: dict[str, object]
) -> dict[str, object]:
    k2_hits = {int(record["prime"]) for record in k2["records"]}
    k6_hits = {int(record["prime"]) for record in k6["records"]}
    variable_hits = {int(record["prime"]) for record in variable["records"]}
    residuals = {int(entry["prime"]) for entry in variable["variable_even_scale_misses"]}
    p25 = k2_hits | k6_hits | variable_hits | residuals
    if len(p25) != 243 or len(k2_hits) != 124 or len(k6_hits) != 48 or len(variable_hits) != 43 or len(residuals) != 28:
        raise AssertionError("external partition did not reconstruct the 243-point p=25 (mod 48) class")
    if any(k2_hits & group for group in (k6_hits, variable_hits, residuals)) or k6_hits & (variable_hits | residuals) or variable_hits & residuals:
        raise AssertionError("external partition overlapped")
    by_prime = {int(record["prime"]): record["selected_edge"] for record in support["records"]}
    terminal_records = []
    for prime in sorted(residuals):
        edge = by_prime.get(prime)
        if edge is None:
            raise AssertionError("residual was absent from the independently audited H19 bridge profile")
        source = int(edge["reverse_two_tail_lift"]["source_denominator"])
        support_count = int(edge["E_prime_support_count"])
        if source % 2 or source >= prime or support_count > 2:
            raise AssertionError("residual did not have a strict low-support even bridge")
        terminal_records.append(
            {
                "prime": prime,
                "bridge_support": support_count,
                "gap": int(edge["gap"]),
                "source_denominator": source,
                "bridge_factor": int(edge["E"]),
            }
        )
    bridge_histogram = Counter(str(record["bridge_support"]) for record in terminal_records)
    return {
        "arithmetic": (
            "take the disjoint k=2, k=6, and full variable-even-scale external partition of the stored "
            "H19 p=25 (mod 48) residuals; for its 28 residue-only external misses, read the independently "
            "exhaustive Type I normal-form bridge minimization and retain the strict even-source bridge"
        ),
        "scope_note": (
            "A finite hybrid closure. The final branch uses an independently verified internal normal-form "
            "search and does not establish a uniform external-or-internal selector theorem."
        ),
        "p_eq_25_mod_48_count": len(p25),
        "fixed_k2_terminal_count": len(k2_hits),
        "fixed_k6_terminal_count": len(k6_hits),
        "variable_even_scale_terminal_count": len(variable_hits),
        "external_residue_boundary_count": len(residuals),
        "internal_support_at_most_two_terminal_count": len(terminal_records),
        "internal_bridge_support_histogram": dict(sorted(bridge_histogram.items(), key=lambda item: int(item[0]))),
        "uncovered_count": len(residuals) - len(terminal_records),
        "records": terminal_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k2", type=Path, default=K2)
    parser.add_argument("--k6", type=Path, default=K6)
    parser.add_argument("--variable", type=Path, default=VARIABLE)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.k2.read_text(encoding="utf-8")),
        json.loads(args.k6.read_text(encoding="utf-8")),
        json.loads(args.variable.read_text(encoding="utf-8")),
        json.loads(args.support.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
