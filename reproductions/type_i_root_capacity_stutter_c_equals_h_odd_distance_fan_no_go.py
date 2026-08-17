#!/usr/bin/env python3
"""Verify exact constants in the c=h odd-distance proper-root no-go."""

from __future__ import annotations

import argparse
from fractions import Fraction


def verify() -> None:
    upper_coefficient = Fraction(1, 49) + Fraction(1, 56) + Fraction(1, 64)
    if upper_coefficient != Fraction(169, 3_136):
        raise AssertionError("the fan upper-bound coefficient changed")
    if not upper_coefficient < Fraction(1, 9):
        raise AssertionError("the fan upper bound no longer contradicts one ninth")

    hard_wall_squared_coefficient = Fraction(8, 513)
    if not hard_wall_squared_coefficient > Fraction(1, 81):
        raise AssertionError("the cubic hard-root lower bound weakened past one ninth")

    # A relaxed arithmetic control satisfies the named fan and root congruence,
    # but deliberately fails the hard-root wall.  It checks that the proof uses
    # the actual hard-root input rather than claiming a bare congruence no-go.
    p_value, h_value, delta, ray = 25, 3, 1, 7
    if not (
        p_value - h_value == delta * (1 + h_value * ray)
        and delta * ray % 4 == 3
        and (p_value * p_value + p_value + 1) % h_value == 0
        and 513 * h_value**6 <= 8 * p_value**4
    ):
        raise AssertionError("the relaxed boundary control changed")

    print("verified c=h odd-distance fan no-go constants and hard-wall boundary")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
