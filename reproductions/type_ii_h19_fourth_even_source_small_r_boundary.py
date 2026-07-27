#!/usr/bin/env python3
"""Find the least compatible even-source tail modulus at the 1b pressure point."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
PRIME = 640_775_689
DEFAULT_R_CAP = 15
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-ii-h19-fourth-even-source-small-r-boundary-640775689-results.json"
)


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return sorted(divisors)


def compatible_rays(prime: int, r: int) -> list[dict[str, int]]:
    """Recover every ordered (distance, source-divisor) pair from r*p+1."""
    if r <= 0 or r % 4 != 3:
        raise ValueError("r must be positive and 3 modulo 4")
    if prime % 8 == 1 and r % 8 != 7:
        return []
    product = r * prime + 1
    rays: list[dict[str, int]] = []
    for first in sympy.divisors(product):
        second = product // first
        if first <= 1 or second <= 1 or (first - 1) % r or (second - 1) % r:
            continue
        distance = (first - 1) // r
        divisor = (second - 1) // r
        if distance <= 0 or divisor <= 0 or distance % 2 == 0 or divisor % 4 != 1:
            continue
        rays.append({"distance": int(distance), "d": int(divisor)})
    return sorted(rays, key=lambda row: (row["distance"], row["d"]))


def tail_factor_count(prime: int, r: int) -> tuple[int, int]:
    """Count exact M1-squared tail factors in the unique r state."""
    m1 = (r * prime + 1) // 4
    factorization = {
        int(prime): 2 * int(exponent)
        for prime, exponent in sympy.factorint(m1).items()
    }
    target = (-m1) % r
    hits = [
        divisor
        for divisor in divisors_from_factorization(factorization)
        if divisor <= m1 and divisor % r == target
    ]
    return m1, len(hits)


def run_audit(r_cap: int = DEFAULT_R_CAP) -> dict[str, object]:
    """Exhaust all positive r=3 mod 4 through r_cap for the fixed pressure point."""
    if r_cap < 3 or r_cap % 4 != 3:
        raise ValueError("r cap must be at least three and 3 modulo 4")
    records: list[dict[str, object]] = []
    for r in range(3, r_cap + 1, 4):
        rays = compatible_rays(PRIME, r)
        m1, hits = tail_factor_count(PRIME, r)
        records.append(
            {
                "r": r,
                "m1": m1,
                "compatible_rays": rays,
                "tail_residue_factor_count": hits,
            }
        )
    successful = [row for row in records if row["compatible_rays"] and row["tail_residue_factor_count"]]
    return {
        "arithmetic": (
            "exact factor-pair enumeration of r*p+1 and exhaustive divisors "
            "of M1 squared in every r state"
        ),
        "scope_note": (
            "A finite small-r boundary for one named pressure point. It does "
            "not establish a universal r selector."
        ),
        "prime": PRIME,
        "r_cap": r_cap,
        "first_compatible_tail_hit_r": min(row["r"] for row in successful)
        if successful
        else None,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r-cap", type=int, default=DEFAULT_R_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_audit(args.r_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
