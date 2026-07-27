#!/usr/bin/env python3
"""Profile the source states behind the 28 external residue-only misses."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VARIABLE = ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json"
SUPPORT = ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-h19-p25-residue-boundary-source-profile-1b-results.json"


def run_audit(variable: dict[str, object], support: dict[str, object]) -> dict[str, object]:
    residuals = {int(entry["prime"]) for entry in variable["variable_even_scale_misses"]}
    if len(residuals) != 28:
        raise AssertionError("input is not the exact external residue-only boundary")
    edges = {int(record["prime"]): record["selected_edge"] for record in support["records"]}
    records = []
    for prime in sorted(residuals):
        edge = edges.get(prime)
        if edge is None:
            raise AssertionError("residue boundary prime is missing an internal bridge")
        A, B, C = (int(value) for value in edge["normal_form"])
        R, K, E = (int(edge[key]) for key in ("R", "K", "E"))
        source = int(edge["reverse_two_tail_lift"]["source_denominator"])
        H = A * R - B
        if 4 * K != prime * R + 1 or E % R != 1:
            raise AssertionError("normal bridge did not have the expected target residue")
        offset = (E - 1) // R
        if source != prime - offset or source % 2 or not 0 < offset < prime:
            raise AssertionError("source offset reconstruction failed")
        a = source * K // E
        x, y = A * B * C, A * C * H
        source_square_normalizer = math.gcd(E, 4)
        if E * a != source * K or (source * source) % E or (source * source // source_square_normalizer) % E:
            raise AssertionError("source first denominator was not integral")
        if Fraction(4, source) != Fraction(1, a) + Fraction(1, x) + Fraction(1, y):
            raise AssertionError("source identity did not verify")
        if Fraction(4, prime) != Fraction(1, x) + Fraction(1, y) + Fraction(1, prime * K):
            raise AssertionError("target identity did not verify")
        standard_even_source = sorted((source // 2, source, source))
        source_solution = sorted((a, x, y))
        if source_solution == standard_even_source:
            raise AssertionError("bridge unexpectedly reduced to the standard even source")
        records.append(
            {
                "prime": prime,
                "source_denominator": source,
                "source_offset": offset,
                "normal_form": [A, B, C],
                "B": B,
                "bridge_factor": E,
                "bridge_support": int(edge["E_prime_support_count"]),
                "source_square_normalizer": source_square_normalizer,
                "source_solution": source_solution,
            }
        )
    offset_histogram = Counter(str(record["source_offset"]) for record in records)
    source_state_histogram = Counter(
        "p_minus_1" if record["source_offset"] == 1 else "shifted" for record in records
    )
    B_histogram = Counter("B_eq_1" if record["B"] == 1 else "B_gt_1" for record in records)
    cross_histogram = Counter(
        f"{'p_minus_1' if record['source_offset'] == 1 else 'shifted'}_support_{record['bridge_support']}"
        for record in records
    )
    return {
        "arithmetic": (
            "for every external residue-only miss, reconstruct its selected minimum-support Type I normal "
            "bridge, write its source as n=p-s from E=1+sR, and verify both source and target identities"
        ),
        "scope_note": (
            "A finite source-state profile of the independently verified low-support fallback. It suggests "
            "a switching target but does not prove that external residue failure forces these states."
        ),
        "input_external_residue_boundary_count": len(records),
        "source_offset_histogram": dict(sorted(offset_histogram.items(), key=lambda item: int(item[0]))),
        "source_state_histogram": dict(sorted(source_state_histogram.items())),
        "normal_B_histogram": dict(sorted(B_histogram.items())),
        "source_state_support_histogram": dict(sorted(cross_histogram.items())),
        "all_bridge_factors_divide_source_square": True,
        "all_bridge_conditions_match_normalized_source_square": True,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variable", type=Path, default=VARIABLE)
    parser.add_argument("--support", type=Path, default=SUPPORT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(
        json.loads(args.variable.read_text(encoding="utf-8")),
        json.loads(args.support.read_text(encoding="utf-8")),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
