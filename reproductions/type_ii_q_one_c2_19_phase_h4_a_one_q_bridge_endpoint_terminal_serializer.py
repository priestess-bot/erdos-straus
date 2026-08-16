#!/usr/bin/env python3
"""Verify the direct Type I serializer for a full-excess raw sink.

The fixture is a local arithmetic sink control, not an asserted H4 predecessor.
It performs no prime-range or denominator scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


FIXTURE = {
    "prime": 73,
    "residue": 23,
    "left": 2,
    "right": 21,
    "expected_denominators": (20, 210, 30_660),
}


def serialize_full_excess_sink(
    prime: int, residue: int, carrier: int, left: int, right: int
) -> tuple[int, int, int]:
    """Return the orientation-independent direct terminal certificate."""
    if (
        prime <= 0
        or residue <= 0
        or carrier <= 0
        or left <= 0
        or right <= 0
        or left + right != residue
        or gcd(left, right) != 1
        or carrier % (left * right)
        or 4 * carrier != prime * residue + 1
    ):
        raise ValueError("input is not a primitive full-excess sink")
    return tuple(sorted((carrier // right, carrier // left, prime * carrier)))


def verify() -> None:
    prime = int(FIXTURE["prime"])
    residue = int(FIXTURE["residue"])
    left = int(FIXTURE["left"])
    right = int(FIXTURE["right"])
    carrier = (prime * residue + 1) // 4
    denominators = serialize_full_excess_sink(prime, residue, carrier, left, right)

    if not (
        prime % 24 == 1
        and carrier == 420
        and denominators == FIXTURE["expected_denominators"]
        and sum((Fraction(1, value) for value in denominators), Fraction())
        == Fraction(4, prime)
        and sum(value % prime == 0 for value in denominators) == 1
    ):
        raise AssertionError("full-excess sink terminal serializer changed")
    print("verified full-excess Type I terminal serializer: p=73, R=23")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact sink control")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
