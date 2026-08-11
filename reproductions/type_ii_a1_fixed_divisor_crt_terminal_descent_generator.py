#!/usr/bin/env python3
"""Verify the A=1 fixed-divisor CRT Type-II terminal/descent generator."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def linear_solution(coefficient: int, target: int, modulus: int) -> tuple[int, int] | None:
    """Return r, q for coefficient*h == target (mod modulus), or None."""
    divisor = gcd(coefficient, modulus)
    if target % divisor:
        return None
    reduced_modulus = modulus // divisor
    if reduced_modulus == 1:
        return 0, 1
    residue = (target // divisor) * pow(coefficient // divisor, -1, reduced_modulus)
    return residue % reduced_modulus, reduced_modulus


def merge(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int] | None:
    """Merge two residue classes with generalized CRT."""
    left_residue, left_modulus = left
    right_residue, right_modulus = right
    divisor = gcd(left_modulus, right_modulus)
    difference = right_residue - left_residue
    if difference % divisor:
        return None
    reduced_right = right_modulus // divisor
    modulus = left_modulus * reduced_right
    if reduced_right == 1:
        return left_residue % modulus, modulus
    step = (difference // divisor) * pow(left_modulus // divisor, -1, reduced_right)
    return (left_residue + left_modulus * (step % reduced_right)) % modulus, modulus


def ray(m: int, d: int) -> tuple[int, int, int] | None:
    assert m >= 3 and m % 4 == 3 and d > 0 and gcd(m, d) == 1
    a = (m + 1) // 4
    constraints = (
        linear_solution(6, 0, a),
        linear_solution(6, -a, d),
        linear_solution(6, -a - d, m),
    )
    state = (0, 1)
    for constraint in constraints:
        if constraint is None:
            return None
        state = merge(state, constraint)
        if state is None:
            return None
    residue, modulus = state
    return residue, modulus, a


def certificate(h: int, m: int, d: int) -> tuple[int, int, int, int, int]:
    data = ray(m, d)
    assert data is not None
    residue, modulus, a = data
    assert h % modulus == residue
    p = 24 * h + 1
    x = (p + m) // 4
    assert a != 0 and x == 6 * h + a and (p - 1) % (m + 1) == 0
    assert x % d == 0 and (x + d) % m == 0
    B = x // d
    K = (B + 1) // m
    n = (p + m) // (m + 1)
    assert (B + 1) % m == 0 and n == x // a and n < p
    return p, x, B, K, n


def verify_identity(h: int, m: int, d: int, expected: tuple[int, int, int, int, int]) -> None:
    p, x, B, K, n = certificate(h, m, d)
    assert (p, x, B, K, n) == expected
    source = (d * B, d * K, d * B * K)
    target = (source[0], p * source[1], p * source[2])
    assert Fraction(4, n) == sum((Fraction(1, value) for value in source), Fraction())
    assert Fraction(4, p) == sum((Fraction(1, value) for value in target), Fraction())


def verify() -> None:
    assert ray(11, 2) is None

    gap_11 = ray(11, 15)
    assert gap_11 == (52, 55, 3)
    assert gcd(24 * gap_11[0] + 1, 24 * gap_11[1]) == 1
    verify_identity(217, 11, 15, (5209, 1305, 87, 8, 435))
    assert is_prime(5209)

    gap_59 = ray(59, 21)
    assert gap_59 == (820, 2065, 15)
    assert gcd(24 * gap_59[0] + 1, 24 * gap_59[1]) == 1
    verify_identity(4950, 59, 21, (118801, 29715, 1415, 24, 1981))
    assert is_prime(118801)

    print("verified A=1 fixed-divisor CRT terminal/descent generator")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused controls")
    args = parser.parse_args()
    if args.verify:
        verify()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
