#!/usr/bin/env python3
"""Verify proper-root quotient-offset saturation for a fixed q-primary control."""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def verify() -> None:
    p, h, q, r = 1009, 111, 7, 351
    u = h // 3
    m_zero = (p * p + p + 1) // 3
    v = (p * p + p + 1) // h
    w = (2 * r + 1) // u
    t_value = p * p * r - (p + 1) // 2
    b = valuation(p - 1, q)
    t = valuation(t_value, q) - b
    offset_relation = p * p * (w + 9) - 3 * (v + 3)
    expected_relation = 2 * t_value // u + 9 * (p * p - 1)

    if not (
        is_prime(p)
        and p % 24 == 1
        and 2 <= h < p
        and h % 3 == 0
        and h != p
        and m_zero % u == 0
        and gcd(2 * r + 1, m_zero) == u
        and w * u == 2 * r + 1
        and v * h == p * p + p + 1
        and b == 1
        and t == 1
        and valuation(h + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(t_value, q) == b + t
        and valuation(v + 3, q) >= b
        and valuation(w + 9, q) >= b
        and offset_relation == expected_relation
        and valuation(offset_relation, q) == b
        and min(valuation(v + 3, q), valuation(w + 9, q)) == b
    ):
        raise AssertionError("proper-root q-primary offset saturation changed")
    print("verified transverse p-minus-one root-quotient offset saturation")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
