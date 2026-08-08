#!/usr/bin/env python3
"""Verify two exact factor-threshold rows with no bounded-divisor exit."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


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

    verify_clean_slab_hole()
    print("verified 2 focused dual bounded-divisor hole receipts")


def verify_clean_slab_hole() -> None:
    p = 673
    parent_R = 527
    parent_K = 88_668
    A_parent = 821
    Q = 263
    alpha = 2
    beta = 1
    B = (p - 1) ** 2 // 4
    c = (p - 1) // 4

    if not (
        is_prime(p)
        and p % 24 == 1
        and 4 * parent_K == p * parent_R + 1
        and 3 <= parent_R <= p - 2
        and parent_R % 4 == 3
        and A_parent <= parent_K <= B
    ):
        raise AssertionError("clean-slab parent chart changed")
    if not (parent_K % A_parent == 0 and parent_K // A_parent == 108):
        raise AssertionError("clean-slab parent support changed")
    if not (
        is_prime(Q)
        and parent_K % Q != 0
        and Q * alpha + beta == parent_R
        and gcd(Q * alpha, beta) == 1
        and alpha * beta == 2
        and parent_K % (alpha * beta) == 0
    ):
        raise AssertionError("clean-slab source contract changed")

    M_parent = A_parent * Q
    R = (-pow(p, -1, 4 * M_parent)) % (4 * M_parent)
    K = (p * R + 1) // 4
    C = K // M_parent
    d = p - C
    n = 4 * M_parent - R
    if not (B < M_parent < 2 * B and c <= A_parent <= B and R > p):
        raise AssertionError("clean-slab capacity overflow gate changed")
    if not (K % M_parent == 0 and C == 26 and d == 647 and n == 830_325):
        raise AssertionError("clean-slab rechart changed")
    if not (p * n == 4 * M_parent * d + 1 and M_parent // A_parent == Q <= d):
        raise AssertionError("clean-slab determinant residual changed")

    fixed_n_divisors = divisors(M_parent * d)
    r = M_parent % p
    product = r * d
    s = (4 * product + 1) // p
    fixed_s_divisors = divisors(product)
    if fixed_n_divisors != (1, 263, 647, 821, 170161, 215923, 531187, 139702181):
        raise AssertionError("clean-slab fixed-n factorization changed")
    if fixed_s_divisors != (1, 563, 647, 364261) or not (r == 563 and s == 2165):
        raise AssertionError("clean-slab fixed-s factorization changed")
    fixed_n_candidates = tuple(
        L for L in fixed_n_divisors if A_parent < L <= B and B // L < B // A_parent
    )
    fixed_s_candidates = tuple(
        L
        for L in fixed_s_divisors
        if A_parent < L <= B and 4 * L > s and B // L < B // A_parent
    )
    if fixed_n_candidates or fixed_s_candidates:
        raise AssertionError("clean-slab bounded-divisor hole closed unexpectedly")

    gap = 7
    x = 170
    divisor = 5
    y = 16_345
    z = 374_006_290
    if not (
        4 * x == p + gap
        and gap % 4 == 3
        and x * x % divisor == 0
        and (p * x + divisor) // gap == y
        and (p * x + divisor) % gap == 0
        and Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
    ):
        raise AssertionError("terminal-first control changed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
