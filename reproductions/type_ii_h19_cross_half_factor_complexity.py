#!/usr/bin/env python3
"""Measure the shortest cross-half-factor residue witnesses in H19 states."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-cross-half-factor-complexity-1b-results.json"


def omega(value: int) -> int:
    """Return the prime-factor multiplicity Omega(value)."""
    return sum(int(exponent) for exponent in sympy.factorint(value).values())


def shortest_cross_witness(a: int, b: int, r: int) -> tuple[int, int, int]:
    """Find the target pair minimizing Omega(alpha)+Omega(beta), then lexicographically."""
    beta_by_residue: dict[int, list[int]] = {}
    for beta in sympy.divisors(b):
        beta = int(beta)
        beta_by_residue.setdefault(beta % r, []).append(beta)
    best: tuple[int, int, int] | None = None
    for alpha in sympy.divisors(a):
        alpha = int(alpha)
        for beta in beta_by_residue.get((-pow(alpha, -1, r)) % r, []):
            candidate = (omega(alpha) + omega(beta), alpha, beta)
            if best is None or candidate < best:
                best = candidate
    if best is None:
        raise AssertionError("a cross-essential state lacks a cross witness")
    return best


def run_audit(payload: dict[str, object]) -> dict[str, object]:
    """Profile exact minimum multiplicities on the cross-essential rows only."""
    records = []
    for row in payload["records"]:
        if row["zero_overflow_kind"] != "cross_essential":
            continue
        a, b, r = int(row["left_half_factor"]), int(row["right_half_factor"]), int(row["r"])
        length, alpha, beta = shortest_cross_witness(a, b, r)
        if alpha == 1 or beta == 1 or (alpha * beta) % r != r - 1:
            raise AssertionError("shortest witness is not genuinely cross-essential")
        records.append(
            {
                "prime": int(row["prime"]),
                "r": r,
                "minimum_cross_omega": length,
                "left_divisor": alpha,
                "right_divisor": beta,
            }
        )
    histogram = Counter(int(record["minimum_cross_omega"]) for record in records)
    return {
        "arithmetic": (
            "exact divisor-pair enumeration on each cross-essential half-factor state, "
            "minimizing total prime multiplicity Omega(alpha)+Omega(beta) subject to alpha*beta=-1 modulo r"
        ),
        "scope_note": (
            "A finite complexity profile. It does not establish a general bound on cross-half-factor witnesses."
        ),
        "prime_limit": payload["prime_limit"],
        "cross_essential_state_count": len(records),
        "minimum_cross_omega_histogram": {str(key): value for key, value in sorted(histogram.items())},
        "maximum_minimum_cross_omega": max(histogram, default=None),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
