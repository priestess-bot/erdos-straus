#!/usr/bin/env python3
"""Verify that the actual-H4 q endpoint has a nonempty y-side block.

The controls reuse two fixed local H4 arithmetic fixtures. They do not scan
primes, denominators, or raw reachability histories.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import (
    FIXTURES,
    complete_excess,
)


def audit(fixture: object) -> dict[str, int | str]:
    prime = int(getattr(fixture, "prime"))
    peeled_part = int(getattr(fixture, "peeled_part"))
    residue = 1 + prime * peeled_part
    carrier = (prime * residue + 1) // 4
    height = gcd(residue - 1, carrier)
    half = (prime + 1) // 2
    divisor = gcd(half, carrier)
    q = half // divisor
    endpoint_y = (residue - height) // q
    y_block = complete_excess(endpoint_y, carrier)

    if not (
        prime % 24 == 1
        and 2 * prime * residue > prime**4 - 2
        and height == 2 * divisor
        and height * q == prime + 1
        and height <= (prime + 1) // 2
        and q <= (prime + 1) // 2
        and endpoint_y > prime * height + 1
        and (prime * residue + 1) % endpoint_y == (prime * height + 1) % endpoint_y
        and carrier % endpoint_y != 0
        and y_block > 1
    ):
        raise AssertionError(f"{getattr(fixture, 'name')}: y-block lower bound changed")

    return {
        "name": str(getattr(fixture, "name")),
        "q": q,
        "y": endpoint_y,
        "ph_plus_one": prime * height + 1,
        "y_block": y_block,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "prime_q37_atomic_split_strict",
            "q": 37,
            "y": 6_641,
            "ph_plus_one": 147,
            "y_block": 6_641,
        },
        {
            "name": "composite_q121_atomic_split_strict",
            "q": 121,
            "y": 59_525,
            "ph_plus_one": 483,
            "y_block": 59_525,
        },
    ]:
        raise AssertionError("H4 q-bridge y-block controls changed")
    print("verified 2 H4 q-bridge controls: y-side complete-excess block is nonempty")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact endpoint controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
