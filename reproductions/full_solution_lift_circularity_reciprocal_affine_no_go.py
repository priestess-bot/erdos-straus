#!/usr/bin/env python3
"""Verify focused controls for reciprocal-affine lift rigidity."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import math


def normalized_denominators(source_denominator: int, solution: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value // math.gcd(source_denominator, value) for value in solution)


def binary_outputs(prime: int, normalized: tuple[int, ...]):
    for choices in product((1, prime), repeat=len(normalized)):
        yield tuple(value * choice for value, choice in zip(normalized, choices))


def reciprocal_sum(values: tuple[int, ...]) -> Fraction:
    return sum((Fraction(1, value) for value in values), start=Fraction(0))


def verify() -> None:
    for prime in (73, 241, 2521):
        even_n = prime - 1
        even_solution = (even_n // 2, even_n, even_n)
        assert reciprocal_sum(even_solution) == Fraction(4, even_n)
        normalized = normalized_denominators(even_n, even_solution)
        assert normalized == (1, 1, 1)
        assert all(
            reciprocal_sum(output) != Fraction(4, prime)
            for output in binary_outputs(prime, normalized)
        )

        divisible_three_n = 3 * ((prime - 1) // 3)
        divisible_three_solution = (
            divisible_three_n // 3,
            2 * divisible_three_n,
            2 * divisible_three_n,
        )
        assert reciprocal_sum(divisible_three_solution) == Fraction(4, divisible_three_n)
        normalized = normalized_denominators(divisible_three_n, divisible_three_solution)
        assert normalized == (1, 2, 2)
        assert all(
            reciprocal_sum(output) != Fraction(4, prime)
            for output in binary_outputs(prime, normalized)
        )

    # A direct arithmetic control for the divisibility collapse in (8)--(9).
    prime, n, a = 73, 33, 15
    g = math.gcd(n, a)
    n_reduced, h = n // g, a // g
    candidates = []
    for k in range(-20, 21):
        reduced_factor = n_reduced + k * h
        if reduced_factor > 0 and prime * h % reduced_factor == 0:
            candidates.append((k, reduced_factor, prime * h // reduced_factor))
    assert candidates == [(-2, 1, 365)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified reciprocal-affine lift rigidity controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
