#!/usr/bin/env python3
"""Separate collision and private variable cofactors on the H19-k23 global tail menu."""

from __future__ import annotations

import argparse
from itertools import combinations
import json
import math
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "h19-k23-global-tail-private-cofactors.json"
TAIL_DENOMINATORS = (32, 36, 40, 48, 60, 72, 80, 92, 96)


def collision_primes(denominators: tuple[int, ...] = TAIL_DENOMINATORS) -> tuple[int, ...]:
    """Return all primes that can divide two different variable tail factors."""
    return tuple(
        sorted(
            {
                int(prime)
                for left, right in combinations(denominators, 2)
                for prime in sympy.factorint(abs(right - left))
            }
        )
    )


def strip_primes(value: int, primes: tuple[int, ...]) -> int:
    """Remove every power of the listed collision primes."""
    result = value
    for prime in primes:
        while result % prime == 0:
            result //= prime
    return result


def verify_private_separation(prime: int) -> dict[str, object]:
    """Factor one eligible p and verify pairwise coprimality after collision removal."""
    if any((prime - 1) % denominator for denominator in TAIL_DENOMINATORS):
        raise ValueError("prime is not eligible for every global tail denominator")
    collision = collision_primes()
    rows = []
    private_values = []
    for denominator in TAIL_DENOMINATORS:
        gap = denominator - 1
        u = (prime + gap) // denominator
        private = strip_primes(u, collision)
        rows.append(
            {
                "tail_gap": gap,
                "u": u,
                "private_cofactor": private,
            }
        )
        private_values.append(private)
    if any(
        math.gcd(left, right) != 1 for left, right in combinations(private_values, 2)
    ):
        raise AssertionError("private cofactors share a noncollision prime")
    return {"prime": prime, "tail_rows": rows}


def run_audit() -> dict[str, object]:
    collision = collision_primes()
    difference_prime_support = {
        f"{left}-{right}": [int(prime) for prime in sympy.factorint(abs(right - left))]
        for left, right in combinations(TAIL_DENOMINATORS, 2)
    }
    return {
        "arithmetic": (
            "for d*u_d=p+d-1 and e*u_e=p+e-1, every common prime divisor of "
            "u_d and u_e divides d-e; complete pairwise difference factorization "
            "therefore identifies the full collision-prime set"
        ),
        "scope_note": (
            "The separation concerns variable u-factors on the fixed global tail menu. "
            "It does not by itself force a target residue in any individual divisor product set."
        ),
        "tail_denominators": list(TAIL_DENOMINATORS),
        "tail_gaps": [denominator - 1 for denominator in TAIL_DENOMINATORS],
        "collision_primes": list(collision),
        "pair_difference_prime_support": difference_prime_support,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS)
    parser.add_argument(
        "--verify-prime",
        type=int,
        action="append",
        default=[],
        help="factor and check an eligible concrete H19-k23 prime",
    )
    args = parser.parse_args()
    payload = run_audit()
    if args.verify_prime:
        payload["concrete_checks"] = [
            verify_private_separation(prime) for prime in args.verify_prime
        ]
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
