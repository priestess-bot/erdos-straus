#!/usr/bin/env python3
"""Verify fixed overlap valuation controls for transverse root-stutter residuals."""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def shared_values(p: int, h: int, m: int, d: int, q: int) -> tuple[int, int, int, int]:
    if not (
        p % 24 == 1
        and h % 3 == 0
        and q % 2 == 1
        and q != 3
        and d == m * p + 1 - h
        and (p * h + 1) % d == 0
        and (d + h - 1) % p == 0
    ):
        raise AssertionError("fixed control did not satisfy the stutter divisor gate")
    d_star = d // gcd(d, h * h - 1)
    c = (p * p - 1) // 2
    d_t = d // gcd(d, c)
    if gcd(d_star, h) != 1 or d_star % q or d_t % q:
        raise AssertionError("fixed control did not retain q in both residuals")
    return d_star, d_t, valuation(d, q), valuation(h * h - 1, q)


def verify_p_plus_one_overlap() -> None:
    p, h, m, d, q = 1489, 1341, 135, 199675, 5
    d_star, d_t, d_value, h_value = shared_values(p, h, m, d, q)
    base = valuation(m, q)
    if not (
        m % q == 0
        and p % q == -1 % q
        and h % q == 1
        and base == valuation(p + 1, q) == valuation(h - 1, q)
        and d_value > base
        and h_value == base
        and valuation(d_star, q) == valuation(d_t, q) == d_value - base
    ):
        raise AssertionError("p+1 overlap valuation alignment failed")


def verify_p_minus_one_overlap() -> None:
    p, h, m, d, q = 165361, 2109, 3, 493975, 5
    d_star, d_t, d_value, h_value = shared_values(p, h, m, d, q)
    base = valuation(m + 2, q)
    if not (
        (m + 2) % q == 0
        and p % q == 1
        and h % q == -1 % q
        and base == valuation(p - 1, q) == valuation(h + 1, q)
        and d_value > base
        and h_value == base
        and valuation(d_star, q) == valuation(d_t, q) == d_value - base
    ):
        raise AssertionError("p-1 overlap valuation alignment failed")


def verify() -> None:
    # Both controls are abstract stutter arithmetic, not actual root receipts.
    verify_p_plus_one_overlap()
    verify_p_minus_one_overlap()
    print("verified transverse overlap valuation alignment")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
