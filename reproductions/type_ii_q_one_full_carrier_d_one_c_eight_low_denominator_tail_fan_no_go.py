#!/usr/bin/env python3
"""Verify the c=8 low-denominator p-1 Type-II tail no-go.

The check replays only fixed constant-divisor consequences of the Type-II
condition. It does not scan primes, gaps, denominators, or prior targets.
"""

from __future__ import annotations

import argparse


def divisors_from_prime_powers(powers: tuple[tuple[int, int], ...]) -> list[int]:
    """Build a fixed finite divisor menu from a supplied prime-power factorization."""
    values = [1]
    for prime, exponent in powers:
        values = [
            value * prime_power
            for value in values
            for prime_power in (prime**power for power in range(exponent + 1))
        ]
    return sorted(values)


def tail_shape(s: int, r: int) -> dict[str, int]:
    """Return one p-1 indexed Type-II tail shape and its intended source."""
    prime = 48 * s + 1
    gap = (prime - 1) // r - 1
    x = (prime + gap) // 4
    source = (prime + gap) // (gap + 1)
    if not (
        s >= 1
        and (prime - 1) % r == 0
        and 4 * x == prime + gap
        and gap % 4 == 3
        and 3 <= gap <= prime - 2
        and (prime - 1) % (gap + 1) == 0
        and source == r + 1
        and source < prime
    ):
        raise AssertionError("p-1 indexed low-denominator tail shape changed")
    return {"p": prime, "m": gap, "x": x, "source": source}


def r_two_no_go_constants() -> list[int]:
    """Return d | 324 with d == -1 (mod 6); the menu must be empty."""
    return [
        divisor
        for divisor in divisors_from_prime_powers(((2, 2), (3, 4)))
        if divisor % 6 == 5
    ]


def r_three_no_go_constants() -> list[int]:
    """Return u | 128 with u == -1 (mod 8); the menu must be empty."""
    return [
        divisor
        for divisor in divisors_from_prime_powers(((2, 7),))
        if divisor % 8 == 7
    ]


def r_four_necessary_candidates() -> list[tuple[int, int]]:
    """Return d | 100, d == 7 (mod 9), with its forced s=(d+2)/9."""
    return [
        (divisor, (divisor + 2) // 9)
        for divisor in divisors_from_prime_powers(((2, 2), (5, 2)))
        if divisor % 9 == 7
    ]


def r_six_necessary_candidates() -> dict[str, list[int]]:
    """Return the two fixed menus forced by the k=2 and k=3 cases."""
    k_two = [
        divisor + 1
        for divisor in divisors_from_prime_powers(((2, 1), (7, 2)))
    ]
    k_three = [
        (divisor + 3) // 10
        for divisor in divisors_from_prime_powers(((2, 2), (3, 2), (7, 2)))
        if divisor % 10 == 7
    ]
    return {"k_two_s": k_two, "k_three_s": k_three}


def r_eight_no_go_constants() -> tuple[list[int], list[int]]:
    """Return the k=3 and k=4 constant menus, both of which must be empty."""
    k_three = [
        divisor
        for divisor in divisors_from_prime_powers(((3, 6),))
        if divisor % 3 == 2
    ]
    k_four = [
        divisor
        for divisor in divisors_from_prime_powers(((2, 4),))
        if divisor % 21 == 17
    ]
    return k_three, k_four


def verify() -> None:
    expected_shapes = {
        2: {"p": 4_129, "m": 2_063, "x": 1_548, "source": 3},
        3: {"p": 4_129, "m": 1_375, "x": 1_376, "source": 4},
        4: {"p": 4_129, "m": 1_031, "x": 1_290, "source": 5},
        6: {"p": 4_129, "m": 687, "x": 1_204, "source": 7},
        8: {"p": 4_129, "m": 515, "x": 1_161, "source": 9},
    }
    if {r: tail_shape(86, r) for r in expected_shapes} != expected_shapes:
        raise AssertionError("c=8 low-denominator tail shapes changed")
    if r_two_no_go_constants() != []:
        raise AssertionError("r=2 constant obstruction changed")
    if r_three_no_go_constants() != []:
        raise AssertionError("r=3 constant obstruction changed")
    if r_four_necessary_candidates() != [(25, 3)]:
        raise AssertionError("r=4 constant obstruction changed")
    r_six = r_six_necessary_candidates()
    if r_six != {
        "k_two_s": [2, 3, 8, 15, 50, 99],
        "k_three_s": [1, 15],
    }:
        raise AssertionError("r=6 constant obstruction changed")
    if [s for s in r_six["k_two_s"] if s >= 86] != [99]:
        raise AssertionError("r=6 high-s candidate reduction changed")
    if 48 * 99 + 1 != 7 * 679:
        raise AssertionError("r=6 high-s composite control changed")
    if r_eight_no_go_constants() != ([], []):
        raise AssertionError("r=8 constant obstruction changed")
    print(
        "verified c=8 low-denominator p-1 Type-II tail no-go: "
        "r=2,3,4,6 fail for s>=86, and even-s r=8 also fails"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
