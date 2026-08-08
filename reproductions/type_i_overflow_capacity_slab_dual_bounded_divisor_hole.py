#!/usr/bin/env python3
"""Verify one exact factor-threshold row with no bounded-divisor exit."""

from __future__ import annotations

import argparse
from math import isqrt


P = 73
D = 13
N = 1461
M = 2051
A = 293


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def divisors(value: int) -> tuple[int, ...]:
    factors: list[int] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)

    result = [1]
    for factor in factors:
        result.extend(item * factor for item in tuple(result))
    return tuple(sorted(set(result)))


def verify() -> None:
    B = (P - 1) ** 2 // 4
    c = (P - 1) // 4
    b = M // A
    S = M * D
    r = M % P
    product = r * D
    s = (4 * product + 1) // P

    if not (is_prime(P) and P % 24 == 1 and P * N == 4 * M * D + 1):
        raise AssertionError("source determinant changed")
    if not (B < M < 2 * B and c <= A <= B and M % A == 0 and 4 * M - N > P):
        raise AssertionError("capacity/support/overflow gate changed")
    if not (1 < b <= D and D * b >= P and b == 7):
        raise AssertionError("factor-threshold residual gate changed")

    fixed_n_divisors = divisors(S)
    fixed_s_divisors = divisors(product)
    if fixed_n_divisors != (1, 7, 13, 91, 293, 2051, 3809, 26663):
        raise AssertionError("fixed-n factorization changed")
    if fixed_s_divisors != (1, 7, 13, 91) or not (r == 7 and s == 5):
        raise AssertionError("fixed-s factorization changed")

    fixed_n_candidates = tuple(
        L for L in fixed_n_divisors if A < L <= B and B // L < B // A
    )
    fixed_s_candidates = tuple(
        L
        for L in fixed_s_divisors
        if A < L <= B and 4 * L > s and B // L < B // A
    )
    if fixed_n_candidates or fixed_s_candidates:
        raise AssertionError("bounded-divisor hole closed unexpectedly")
    if not (D * b >= P and D > b and b < A):
        raise AssertionError("three-route residual gate changed")

    print("verified 1 focused dual bounded-divisor hole receipt")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
