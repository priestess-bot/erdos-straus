#!/usr/bin/env python3
"""Replay the exact R=3 D-contact completion dichotomy controls."""

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
            return value == divisor
        divisor = 3 if divisor == 2 else divisor + 2
    return True


def factor_certificate(prime: int, A: int, B: int, C: int, K: int, m: int) -> dict[str, int]:
    h = 4 * A * C * K - 1
    D = 2 * prime - 3
    T = 8 * A * A * C + 3
    L = 3 * K + 2 * A
    g = gcd(h, D)
    p_plus_four = prime + 4
    n_three = (3 * prime + 1) // 4
    if not (
        is_prime(prime)
        and prime % 24 == 1
        and prime == h * m - 4 * A * A * C
        and B == K * m - A
        and m % 4 == 3
        and 3 <= m <= prime - 2
        and all(q % 4 == 1 for q in factor(p_plus_four))
        and all(q % 3 == 1 for q in factor(n_three))
    ):
        raise AssertionError("normal form identity changed")
    if not (g > 1 and g < h):
        raise AssertionError("control is not a genuine mixed contact")
    s, r, t, ell = h // g, D // g, T // g, L // g
    if not (
        h % g == 0
        and D % g == 0
        and T % g == 0
        and L % g == 0
        and r + t == 2 * s * m
        and t == 4 * A * C * ell - 3 * s
        and 2 * s * B == K * r + ell
        and B >= A
        and gcd(A, B) == 1
    ):
        raise AssertionError("quotient completion identities changed")
    x = A * B * C
    d = A * A * C
    y = prime * (x + d) // m
    z = prime * (x + x * x // d) // m
    if (
        d > x
        or (x + d) % m
        or (x + x * x // d) % m
        or sum((Fraction(1, q) for q in (x, y, z)), Fraction()) != Fraction(4, prime)
    ):
        raise AssertionError("reconstructed Type-II certificate changed")
    return {"p": prime, "h": h, "D": D, "g": g, "s": s, "r": r, "t": t, "ell": ell, "B": B}


def verify_prime_d_empty() -> None:
    prime = 2_521
    if len(factor(2 * prime - 3)) != 1:
        raise AssertionError("prime-D control changed")


def verify_partial_contact() -> None:
    prime, A, C, K = 118_801, 1, 46, 17
    h, D = 4 * A * C * K - 1, 2 * prime - 3
    T, L = 8 * A * A * C + 3, 3 * K + 2 * A
    g = gcd(h, D)
    s, r, ell = h // g, D // g, L // g
    if not (
        g == 53
        and T == 371
        and L == 53
        and T % g == 0
        and L % g == 0
        and (K * r + ell) % (2 * s) != 0
    ):
        raise AssertionError("partial D-contact completion control changed")


def verify_partial_progression() -> None:
    """Check the fixed-q partial-contact progression and its cofactor gate."""
    h, T, L = 3_127, 371, 53
    q = 53
    controls = (1, 17, 26, 37, 43, 47, 66, 92, 93, 112)
    for index in controls:
        prime = 505 + 1_272 * index
        denominator = 2 * prime - 3
        if not (
            prime % 24 == 1
            and denominator == 53 * (19 + 48 * index)
            and h % q == 0
            and T % q == 0
            and L % q == 0
            and denominator % q == 0
            and (prime + 184) % q == 0
            and (prime + 184) % 59 != 0
            and is_prime(prime)
            and all(factor_prime % 4 == 1 for factor_prime in factor(prime + 4))
            and all(factor_prime % 3 == 1 for factor_prime in factor((3 * prime + 1) // 4))
        ):
            raise AssertionError("partial-contact progression control changed")
    exceptional_index = 56
    exceptional_prime = 505 + 1_272 * exceptional_index
    if (exceptional_prime + 184) % 59 != 0:
        raise AssertionError("cofactor congruence class changed")


def verify_composite_terminal_progression() -> None:
    """Check an infinite-prime arithmetic family of genuine mixed terminals."""
    h, T, L = 55, 115, 5
    for index in (0, 3, 5, 7, 11):
        prime = 769 + 1_320 * index
        m = 15 + 24 * index
        B = 14 + 24 * index
        D = 2 * prime - 3
        g = gcd(h, D)
        s, r, tq, ell = h // g, D // g, T // g, L // g
        if not (
            is_prime(prime)
            and prime % 24 == 1
            and g == 5
            and r == 307 + 528 * index
            and tq == 23
            and ell == 1
            and r + tq == 2 * s * m
            and 2 * s * B == r + ell
            and B == m - 1
        ):
            raise AssertionError("composite-D terminal progression changed")


def factor(value: int) -> tuple[int, ...]:
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return tuple(result)


def verify() -> None:
    verify_prime_d_empty()
    verify_partial_contact()
    verify_partial_progression()
    verify_composite_terminal_progression()
    controls = (
        (769, 1, 14, 14, 1, 15),
        (21_937, 1, 2_771, 2, 12, 231),
        (20_809, 1, 1_308, 4, 11, 119),
    )
    for row in controls:
        factor_certificate(*row)
    partial = (2 * 118_801 - 3)
    if factor(partial) != (53, 4483):
        raise AssertionError("partial D control changed")
    print("verified D-prime EMPTY stratum, composite completion controls, and certificate reconstruction")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
