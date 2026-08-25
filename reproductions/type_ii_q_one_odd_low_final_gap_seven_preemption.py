#!/usr/bin/env python3
"""Verify the odd q=1 low-final congruence split and gap-7 preemption."""

from __future__ import annotations

import argparse
from fractions import Fraction


def macro_j(prime: int) -> int:
    values = [j for j in range(1, 14) if (j * prime - 3) % 14 == 0]
    if len(values) != 1:
        raise AssertionError("odd macro quotient parameter is not unique")
    return values[0]


def low_final_class(prime: int) -> int | None:
    """Return the unique low-final residue class, or None for a high final."""
    if prime % 48 != 25:
        raise AssertionError("this verifier is restricted to odd t")
    j = macro_j(prime)
    low = j >= 10
    residue = prime % 336
    if low != (residue in {25, 265}):
        raise AssertionError("odd low-final CRT classification changed")
    return residue if low else None


def gap_seven_terminal(prime: int) -> tuple[int, int, int]:
    if prime % 336 != 265:
        raise AssertionError("gap-7 d=2 preemption has the wrong congruence class")
    x = (prime + 7) // 4
    d = 2
    y = prime * (x + d) // 7
    z = prime * (x + x * x // d) // 7
    if not (
        4 * x == prime + 7
        and x % 2 == 0
        and x % 7 == 5
        and d <= x
        and (x + d) % 7 == 0
        and (x + x * x // d) % 7 == 0
        and sum((Fraction(1, value) for value in (x, y, z)), Fraction())
        == Fraction(4, prime)
    ):
        raise AssertionError("gap-7 d=2 terminal changed")
    return x, y, z


def verify() -> None:
    # These four rows cover both odd-low CRT classes and two high-final rows.
    expected = {
        73: (None, 1),
        601: (265, 11),
        1033: (25, 13),
        2521: (None, 3),
    }
    for prime, (expected_low, expected_j) in expected.items():
        if macro_j(prime) != expected_j or low_final_class(prime) != expected_low:
            raise AssertionError(f"odd low-final row changed for p={prime}")
    if gap_seven_terminal(601) != (152, 13_222, 1_004_872):
        raise AssertionError("p=601 gap-7 terminal control changed")
    print("verified q=1 odd low-final CRT split and gap-7 d=2 preemption")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
