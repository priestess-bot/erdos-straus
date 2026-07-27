#!/usr/bin/env python3
"""Audit the size obstruction for two full external-source tails.

After retaining 1/(k*n_k) in a source identity, the residual is

    (4*k-1)/(k*n_k) = 4*(4*k-1)/((4*k-1)*p+1).

Every external source n_j is at least (3*p+1)/4.  Hence two denominators
which are positive integer multiples of external sources contribute at most

    2 / n_1 = 8/(3*p+1),

strictly below the residual.  This excludes two full-source tails pointwise,
without an affine or uniformity assumption.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "reproductions" / "two-source-full-tail-size-obstruction.json"


def core_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for divisor in range(2, math.isqrt(limit) + 1):
        if sieve[divisor]:
            sieve[divisor * divisor : limit + 1 : divisor] = b"\x00" * (
                (limit - divisor * divisor) // divisor + 1
            )
    return [prime for prime in range(2, limit + 1) if sieve[prime] and prime % 24 == 1]


def divisors(value: int) -> list[int]:
    result = [1]
    remaining = value
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor:
            factor = 3 if factor == 2 else factor + 2
            continue
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        result = [
            divisor * factor**power
            for divisor in result
            for power in range(exponent + 1)
        ]
        factor = 3 if factor == 2 else factor + 2
    if remaining > 1:
        result = [divisor * remaining for divisor in result] + result
    return sorted(result)


def source_denominator(prime: int, scale: int) -> int:
    q = 4 * scale - 1
    numerator = q * prime + 1
    if numerator % (4 * scale):
        raise ValueError("scale is not stationary at this prime")
    return numerator // (4 * scale)


def residual_after_preserved_term(prime: int, scale: int) -> Fraction:
    q = 4 * scale - 1
    return Fraction(4 * q, q * prime + 1)


def full_source_tail_bound(prime: int) -> Fraction:
    return Fraction(8, 3 * prime + 1)


def verify_pointwise_obstruction(prime: int, scale: int) -> bool:
    """Check the sharp source-independent inequality for one retained scale."""
    base = (prime - 1) // 4
    if prime % 24 != 1 or base % scale:
        return False
    source = source_denominator(prime, scale)
    if source < (3 * prime + 1) // 4:
        return False
    return residual_after_preserved_term(prime, scale) > full_source_tail_bound(prime)


def run_audit(limit: int = 10_000) -> dict[str, object]:
    if limit < 73:
        raise ValueError("limit must be at least 73")
    profiles: list[dict[str, object]] = []
    total_scale_states = 0
    for prime in core_primes(limit):
        scales = divisors((prime - 1) // 4)
        for scale in scales:
            if not verify_pointwise_obstruction(prime, scale):
                raise AssertionError("two-full-source tail obstruction failed")
            total_scale_states += 1
        if len(profiles) < 8:
            first_scale = scales[0]
            profiles.append(
                {
                    "prime": prime,
                    "scale": first_scale,
                    "residual": [
                        residual_after_preserved_term(prime, first_scale).numerator,
                        residual_after_preserved_term(prime, first_scale).denominator,
                    ],
                    "two_full_source_bound": [
                        full_source_tail_bound(prime).numerator,
                        full_source_tail_bound(prime).denominator,
                    ],
                }
            )
    return {
        "arithmetic": (
            "exact rational comparison of the retained-source residual against "
            "the maximal reciprocal mass of two full external sources"
        ),
        "scope_note": (
            "This is a pointwise size obstruction for tails that are positive "
            "integer multiples of complete external-source denominators. It "
            "does not exclude factor tails or other coupled denominators."
        ),
        "prime_limit": limit,
        "core_prime_count": len(core_primes(limit)),
        "stationary_scale_state_count": total_scale_states,
        "sample_profiles": profiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000)
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
