#!/usr/bin/env python3
"""Targeted arithmetic fixtures for escaped-primary source-switch dispatch.

This is deliberately not a census.  It fixes the two boundary cases that
separate candidate-specific shared-q accounting from raw Type II fallback.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for a nonzero integer."""
    if value == 0:
        raise ValueError("the fixture only evaluates nonzero differences")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def shared_q_height_fixture() -> dict[str, object]:
    """Show that three one-layer sources cannot create a 7^3 candidate."""
    prime = 215_617
    denominator = 1_247
    target_denominator = 43
    target_a = 1
    q = 7
    source_as = (1, 29, 43)
    source_values = [denominator * source_a for source_a in source_as]
    candidate = target_a * target_denominator
    source_heights = [
        valuation(prime + 4 * source_value, q) for source_value in source_values
    ]
    compatible_heights = [
        min(height, valuation(candidate - source_value, q))
        for height, source_value in zip(source_heights, source_values)
    ]
    available = min(
        sum(compatible_heights), valuation(prime + 4 * candidate, q)
    )
    requested = 3
    bad_h = q**requested
    bad_k = (bad_h + 1) // (4 * target_denominator)

    assert prime % 24 == 1
    assert source_heights == [1, 1, 1]
    assert compatible_heights == [1, 1, 1]
    assert available == 1
    assert requested > available
    assert (prime + 4 * candidate) % bad_h != 0
    assert bad_h % (4 * target_denominator) == -1 % (4 * target_denominator)
    assert (bad_k * prime + target_a) % bad_h == 84

    return {
        "prime": prime,
        "D": denominator,
        "candidate": {"D_prime": target_denominator, "A": target_a, "s": candidate},
        "q": q,
        "sources": [
            {
                "a": source_a,
                "Da": source_value,
                "source_q_height": height,
                "compatible_q_height": compatible,
            }
            for source_a, source_value, height, compatible in zip(
                source_as, source_values, source_heights, compatible_heights
            )
        ],
        "requested_height": requested,
        "available_height": available,
        "bad_h": bad_h,
        "bad_normal_form_remainder": (bad_k * prime + target_a) % bad_h,
    }


def raw_fallback_fixture() -> dict[str, object]:
    """Show that an empty D-lattice can still have a raw Type II terminal."""
    prime = 73
    h = 15
    product = (h + 1) // 4
    candidates: list[tuple[int, int, int, int]] = []
    for a in range(1, product + 1):
        if product % a:
            continue
        for c in range(1, product // a + 1):
            if (product // a) % c:
                continue
            k = product // (a * c)
            numerator = k * prime + a
            if numerator % h:
                continue
            b = numerator // h
            if a <= b:
                candidates.append((a, c, k, b))

    assert candidates == [(2, 2, 1, 5)]
    a, c, k, b = candidates[0]
    x = a * b * c
    divisor = a * a * c
    gap = (a + b) // k
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    assert Fraction(4, prime) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

    return {
        "prime": prime,
        "h": h,
        "raw_factor_product": product,
        "raw_candidates": [
            {"A": candidate_a, "C": candidate_c, "K": candidate_k, "B": candidate_b}
            for candidate_a, candidate_c, candidate_k, candidate_b in candidates
        ],
        "certificate": {"gap": gap, "x": x, "divisor": divisor, "y": y, "z": z},
    }


def run_fixture() -> dict[str, object]:
    """Run both constant-size fixtures."""
    return {
        "scope_note": (
            "Two fixed arithmetic boundary examples only; this is not a prime "
            "scan or a completeness test."
        ),
        "shared_q_height": shared_q_height_fixture(),
        "raw_fallback": raw_fallback_fixture(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify",
        action="store_true",
        help="run the fixed shared-q and raw-fallback assertions",
    )
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    print(json.dumps(run_fixture(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
