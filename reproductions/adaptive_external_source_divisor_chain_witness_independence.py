#!/usr/bin/env python3
"""Verify exact external-source denominator-chain gcd and witness no-reuse."""

from __future__ import annotations

import argparse
from math import gcd


def divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate for candidate in range(1, value + 1) if value % candidate == 0
    )


def source_denominator(p: int, k: int) -> int:
    assert p % 24 == 1 and (p - 1) % (4 * k) == 0
    q = 4 * k - 1
    numerator = q * p + 1
    assert numerator % (q + 1) == 0
    return numerator // (q + 1)


def witnesses(p: int, k: int) -> tuple[int, ...]:
    q = 4 * k - 1
    return tuple(
        factor
        for factor in divisors(source_denominator(p, k))
        if factor > 1 and factor % q == q - 1
    )


def verify_gcd_formula(p: int, k: int, ell: int) -> None:
    h = (p - 1) // 4
    assert h % k == h % ell == 0 and ell % k == 0 and k < ell
    n_k = source_denominator(p, k)
    n_l = source_denominator(p, ell)
    scale = ell // k
    assert gcd(n_k, n_l) == gcd(n_k, scale - 1)
    assert set(witnesses(p, k)).isdisjoint(witnesses(p, ell))


def verify() -> None:
    assert source_denominator(193, 1) == 145
    assert source_denominator(193, 2) == 169
    assert witnesses(193, 1) == (5, 29)
    assert witnesses(193, 2) == (13,)
    verify_gcd_formula(193, 1, 2)

    assert source_denominator(73, 2) == 64
    assert source_denominator(73, 6) == 70
    assert gcd(64, 70) == 2 == gcd(64, 6 // 2 - 1)
    assert witnesses(73, 2) == witnesses(73, 6) == ()
    assert 2 < 4 * 6 - 2
    verify_gcd_formula(73, 2, 6)

    print("verified adaptive external-source divisor-chain witness independence")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
