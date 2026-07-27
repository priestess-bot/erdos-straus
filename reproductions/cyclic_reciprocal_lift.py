#!/usr/bin/env python3
"""Audit the minimal cyclic reciprocal-coupled lift.

For a source solution 4/n = 1/a + 1/b + 1/c, the real identity

    1/A = n/(2p) (1/a + 1/b)
    1/B = n/(2p) (1/b + 1/c)
    1/C = n/(2p) (1/c + 1/a)

has sum 4/p. This script checks the induced integrality marker exactly.
The accompanying proof card shows that it is empty for every core prime;
the finite audit is an independent implementation check of the formula.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "cyclic-reciprocal-lift-core-200-results.json"


def core_primes(limit: int) -> list[int]:
    """Return primes p <= limit with p == 1 modulo 24."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for divisor in range(2, int(limit**0.5) + 1):
        if sieve[divisor]:
            sieve[divisor * divisor : limit + 1 : divisor] = b"\x00" * (
                ((limit - divisor * divisor) // divisor) + 1
            )
    return [
        value
        for value in range(2, limit + 1)
        if sieve[value] and value % 24 == 1
    ]


def source_solutions(denominator: int):
    """Yield every ordered positive solution (a, b, c) of 4/n."""
    for first in range(denominator // 4 + 1, 3 * denominator // 4 + 1):
        residual_numerator = 4 * first - denominator
        residual_denominator = denominator * first
        lower = max(
            first,
            (residual_denominator + residual_numerator - 1) // residual_numerator,
        )
        upper = 2 * residual_denominator // residual_numerator
        for second in range(lower, upper + 1):
            tail_denominator = residual_numerator * second - residual_denominator
            if tail_denominator <= 0:
                continue
            numerator = residual_denominator * second
            if numerator % tail_denominator:
                continue
            third = numerator // tail_denominator
            if third >= second:
                yield (first, second, third)


def cyclic_reciprocals(
    prime: int, source_denominator: int, source_solution: tuple[int, int, int]
) -> tuple[Fraction, Fraction, Fraction]:
    """Return the equal-weight cyclic target reciprocal values."""
    return weighted_cyclic_reciprocals(
        prime, source_denominator, source_solution, 1, 2
    )


def weighted_cyclic_reciprocals(
    prime: int,
    source_denominator: int,
    source_solution: tuple[int, int, int],
    numerator: int,
    denominator: int,
) -> tuple[Fraction, Fraction, Fraction]:
    """Return a rationally weighted cyclic transport on source reciprocals.

    The weight on the first member of every ordered pair is numerator /
    denominator. The complementary weight is used on the second member.
    """
    if (
        numerator <= 0
        or numerator >= denominator
        or math.gcd(numerator, denominator) != 1
    ):
        raise ValueError("weights must satisfy 0 < numerator < denominator and be reduced")
    a, b, c = source_solution
    scale = Fraction(source_denominator, prime * denominator)
    complement = denominator - numerator
    values = (
        scale * (Fraction(numerator, a) + Fraction(complement, b)),
        scale * (Fraction(numerator, b) + Fraction(complement, c)),
        scale * (Fraction(numerator, c) + Fraction(complement, a)),
    )
    if sum(values, Fraction()) != Fraction(4, prime):
        raise AssertionError("cyclic reciprocal transport identity failed")
    return values


def cyclic_target(
    prime: int, source_denominator: int, source_solution: tuple[int, int, int]
) -> tuple[int, int, int] | None:
    """Return the target triple exactly when the cyclic marker is integral."""
    return weighted_cyclic_target(prime, source_denominator, source_solution, 1, 2)


def weighted_cyclic_target(
    prime: int,
    source_denominator: int,
    source_solution: tuple[int, int, int],
    numerator: int,
    denominator: int,
) -> tuple[int, int, int] | None:
    """Return the weighted cyclic target exactly when all three terms are unit."""
    values = weighted_cyclic_reciprocals(
        prime, source_denominator, source_solution, numerator, denominator
    )
    if any(value.numerator != 1 for value in values):
        return None
    target = tuple(value.denominator for value in values)
    if sum((Fraction(1, value) for value in target), Fraction()) != Fraction(4, prime):
        raise AssertionError("integral cyclic target failed exact reconstruction")
    return target


def run_audit(limit: int) -> dict[str, object]:
    """Exhaustively check all n < p and all source solutions in a finite range."""
    if limit < 2:
        raise ValueError("limit must be at least 2")
    records = []
    total_sources = 0
    for prime in core_primes(limit):
        checked = 0
        hits = []
        for source_denominator in range(2, prime):
            for source_solution in source_solutions(source_denominator):
                checked += 1
                target = cyclic_target(prime, source_denominator, source_solution)
                if target is not None:
                    hits.append(
                        {
                            "source_denominator": source_denominator,
                            "source_solution": list(source_solution),
                            "target_solution": list(target),
                        }
                    )
        total_sources += checked
        records.append(
            {
                "prime": prime,
                "source_solutions_checked": checked,
                "integer_cyclic_lifts": hits,
            }
        )
    return {
        "arithmetic": "exact integers and fractions.Fraction",
        "scope_note": (
            "This finite audit checks the cyclic formula only. Its empty output "
            "is independently implied for all core primes by the proof card "
            "cyclic-reciprocal-transport-obstruction."
        ),
        "limit": limit,
        "core_primes": len(records),
        "source_solutions_checked": total_sources,
        "records": records,
        "integer_cyclic_lifts": sum(
            len(record["integer_cyclic_lifts"]) for record in records
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--output", type=Path, default=RESULTS)
    args = parser.parse_args()
    payload = run_audit(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
