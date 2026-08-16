#!/usr/bin/env python3
"""Verify the exact q_star=103 small-prime roughness criterion.

This is a three-control algebraic receipt. It does not scan core primes or
factor a target state.
"""

from __future__ import annotations

import argparse
import math

import type_ii_q_one_full_carrier_second_anchor_fixed_n_macro as macro


SMALL_PRIMES = (
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
)


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def q_star_is_103(s: int) -> bool:
    """Evaluate the finite exact criterion from the first-anchor excess blocks."""
    n = 6 * s - 1
    return (
        n % 103 == 0
        and n % 25 != 0
        and all(n % prime != 0 for prime in SMALL_PRIMES)
    )


def verify_control(prime: int, expected_q_star: int) -> None:
    """Replay a fixed actual macro and compare it with the roughness rule."""
    s = (prime - 1) // 48
    row = macro.even_macro(2 * s)
    actual = int(row["selected_carrier"]["q_star"])
    n, b = 6 * s - 1, 16 * s - 1
    if not (
        prime == 48 * s + 1
        and actual == expected_q_star
        and 8 * n - 3 * b == -5
        and math.gcd(n, s) == 1
        and math.gcd(n, b) in {1, 5}
        and (valuation(n, 5) <= 1 or valuation(b, 5) == 1)
        and (q_star_is_103(s) == (actual == 103))
    ):
        raise AssertionError("q_star=103 roughness control changed")


def verify() -> None:
    verify_control(4129, 103)
    verify_control(157393, 103)
    verify_control(340321, 7)
    if not (
        q_star_is_103(86)
        and q_star_is_103(3279)
        and not q_star_is_103(7090)
        and 7090 % 103 == 86
        and (6 * 7090 - 1) % 7 == 0
    ):
        raise AssertionError("q_star=103 necessary-versus-sufficient boundary changed")
    print(
        "verified q=1 even macro q_star=103 roughness criterion: "
        "s=86 and 3279 pass, while s=7090 is preempted by q_star=7"
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
