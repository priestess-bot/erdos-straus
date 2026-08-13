#!/usr/bin/env python3
"""Verify fixed controls for the root-capacity/external-terminal coupling."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def menu(p: int, q: int) -> tuple[int, int, int, int, list[int]]:
    rho = p % q
    i = q - rho
    if not (q % 3 == 1 and (rho * rho + rho + 1) % q == 0):
        raise AssertionError("capacity prime lost its cyclotomic order")
    if not (2 <= i <= q - 2 and gcd(q, 4 * i) == 1):
        raise AssertionError("minimal external source is outside its exact range")
    N = (p + i) // q
    tau = (-p * pow(q, -1, 4 * i)) % (4 * i)
    hits = [t for t in divisors(N) if t % (4 * i) == tau]
    return rho, i, N, tau, hits


def certificate(p: int, q: int, t: int) -> tuple[int, int, int, int]:
    rho, i, N, tau, hits = menu(p, q)
    if t not in hits:
        raise AssertionError("requested divisor is not in the exact terminal menu")
    m = q * t
    x = (p + m) // 4
    d = i * x
    B = (p + i) // m
    if not (
        N % t == 0
        and t % (4 * i) == tau
        and (p + i) % m == 0
        and (p + m) % (4 * i) == 0
        and 3 <= m <= p - 2
        and m % 4 == 3
        and x * x % d == 0
        and (p * x + d) % m == 0
        and rho == q - i
    ):
        raise AssertionError("external-source Type I certificate changed")
    if Fraction(1, x) + Fraction(1, x * B) + Fraction(i, p * x * B) != Fraction(4, p):
        raise AssertionError("reconstructed unit-fraction identity changed")
    return m, x, d, B


def verify() -> None:
    # The primitive CRT class with q=7, rho=2, i=5 and its first three primes.
    for p in (2473, 3313, 4153):
        if not (is_prime(p) and p % 840 == 793 and p % 24 == 1):
            raise AssertionError("fixed Dirichlet-class control changed")
        M = (p * p + p + 1) // 3
        r = 3
        if gcd(2 * r + 1, M) != 7:
            raise AssertionError("root capacity coupling changed")
        certificate(p, 7, 1)

    if certificate(2473, 7, 1) != (7, 620, 3100, 354):
        raise AssertionError("gap-7 explicit control changed")
    if certificate(2137, 7, 9) != (63, 550, 2750, 34):
        raise AssertionError("nontrivial divisor-menu hit changed")

    p = 457
    rho, i, N, tau, hits = menu(p, 7)
    M = (p * p + p + 1) // 3
    if not (
        (rho, i, N, tau, hits) == (2, 5, 66, 9, [])
        and M == 69_769
        and gcd(7, M) == 7
        and gcd(2 * 3 + 1, M) == 7
    ):
        raise AssertionError("empty-menu negative control changed")

    x = (p + 7) // 4
    residues = {d % 7 for d in divisors(x * x)}
    if not (
        x == 116
        and residues == {1, 2, 4}
        and (-p * x) % 7 == 6
        and (-x) % 7 == 3
    ):
        raise AssertionError("gap-7 Type I/II negative control changed")

    print(
        "verified the exact q-coupled divisor menu, two positive certificates, "
        "one primitive CRT class, and one empty-menu Type I/II control"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
