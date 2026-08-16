#!/usr/bin/env python3
"""Verify the bounded fixed-AC-fan intersection of an H4 fresh q carrier.

The controls reuse two local H4 arithmetic fixtures. They do not scan primes,
denominators, or reachability histories.
"""

from __future__ import annotations

import argparse
from math import gcd, prod

from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import FIXTURES


FAN = tuple((a, c) for a in range(1, 4) for c in range(1, 4))


def fresh_q(fixture: object) -> tuple[int, int]:
    prime = int(getattr(fixture, "prime"))
    peeled_part = int(getattr(fixture, "peeled_part"))
    residue = 1 + prime * peeled_part
    multiplier = (prime * residue + 1) // 4
    half = (prime + 1) // 2
    divisor = gcd(half, multiplier)
    q = half // divisor
    if q != int(getattr(fixture, "expected_q")):
        raise AssertionError("local H4 fixture no longer has its recorded fresh q")
    return prime, q


def fixed_fan_intersection(prime: int, q: int) -> int:
    shifts = prod(prime + 4 * a * a * c for a, c in FAN)
    constants = prod(4 * a * a * c - 1 for a, c in FAN)
    shifted_intersection = gcd(q, shifts)
    constant_intersection = gcd(q, constants)
    if shifted_intersection != constant_intersection:
        raise AssertionError("fixed-fan congruence intersection failed")
    return shifted_intersection


def verify_q_carried_ac_factor() -> None:
    prime, a, c, k, h = 241, 1, 3, 1, 11
    q = 121
    shift = prime + 4 * a * a * c
    b = (k * prime + a) // h
    gap = (a + b) // k
    if not (
        h == 4 * a * c * k - 1
        and q % h == 0
        and shift % h == 0
        and (4 * a * a * c - 1) % h == 0
        and k <= a
        and (k * prime + a) % h == 0
        and b >= a
        and prime == 4 * a * b * c - gap
    ):
        raise AssertionError("direct q-carried AC certificate control changed")


def verify() -> None:
    receipts = []
    for fixture in FIXTURES:
        prime, q = fresh_q(fixture)
        receipts.append((str(getattr(fixture, "name")), prime, q, fixed_fan_intersection(prime, q)))
    if receipts != [
        ("prime_q37_atomic_split_strict", 73, 37, 1),
        ("composite_q121_atomic_split_strict", 241, 121, 11),
    ]:
        raise AssertionError("H4 fresh-q fixed-fan controls changed")
    verify_q_carried_ac_factor()
    print("verified 2 H4 fresh-q fixed-fan intersections and 1 bounded-K AC factor")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact fixed-fan controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
