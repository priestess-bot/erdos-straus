#!/usr/bin/env python3
"""Audit a bounded r selector on the 1b H19 quadratic-descent pressure set."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
DEFAULT_R_CAP = 103
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [
            divisor * prime**power
            for divisor in divisors
            for power in range(exponent + 1)
        ]
    return divisors


def compatible_rays(prime: int, r: int) -> list[dict[str, int]]:
    """Enumerate ordered source representations from the factor pairs of r*p+1."""
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


def tail_hit_count(prime: int, r: int) -> int:
    """Count tail factors in the unique r state."""
    m1 = (r * prime + 1) // 4
    factors = {
        int(prime): 2 * int(exponent)
        for prime, exponent in sympy.factorint(m1).items()
    }
    target = (-m1) % r
    return sum(
        divisor <= m1 and divisor % r == target
        for divisor in divisors_from_factorization(factors)
    )


def run_audit(payload: dict[str, object], r_cap: int = DEFAULT_R_CAP) -> dict[str, object]:
    """Find the first compatible square-tail hit for every stored quadratic miss."""
    if r_cap < 3 or r_cap % 4 != 3:
        raise ValueError("r cap must be at least three and 3 modulo 4")
    pressure_primes = [
        int(record["prime"])
        for record in payload["records"]
        if record["quadratic_factor_external_source_descent"] is None
    ]
    records: list[dict[str, object]] = []
    for prime in pressure_primes:
        selected = None
        for r in range(7, r_cap + 1, 8):
            rays = compatible_rays(prime, r)
            hits = tail_hit_count(prime, r)
            if rays and hits:
                selected = {
                    "r": r,
                    "m1": (r * prime + 1) // 4,
                    "compatible_rays": rays,
                    "tail_residue_factor_count": hits,
                }
                break
        records.append({"prime": prime, "first_small_r_tail_hit": selected})
    return {
        "arithmetic": (
            "exact factor-pair enumeration of r*p+1 for the necessary class "
            "r=7 mod 8, and exhaustive divisors of each selected M1 squared"
        ),
        "scope_note": (
            "A finite small-r audit on a stored pressure set. It does not "
            "prove a universal r bound or a general descent selector."
        ),
        "prime_limit": payload["prime_limit"],
        "r_cap": r_cap,
        "quadratic_descent_miss_count": len(pressure_primes),
        "unclosed_through_r_cap": [
            record["prime"]
            for record in records
            if record["first_small_r_tail_hit"] is None
        ],
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--r-cap", type=int, default=DEFAULT_R_CAP)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = run_audit(payload, args.r_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
