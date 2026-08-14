#!/usr/bin/env python3
"""Verify oriented proper-root quotient valuations in a fixed q-primary control."""

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
    p, h, q, r = 8641, 39, 5, 266
    u = h // 3
    root_capacity = (p * p + p + 1) // 3
    v = (p * p + p + 1) // h
    w = (2 * r + 1) // u
    t_value = p * p * r - (p + 1) // 2
    b = valuation(p - 1, q)
    t = valuation(t_value, q) - b
    q_power = q**b
    p_unit = (p - 1) // q_power
    h_unit = (h + 1) // q_power
    r_unit = (r - 1) // q_power
    receipt_unit = h_unit - p_unit + q_power * p_unit * h_unit
    t_unit = (
        2 * r_unit
        + 3 * p_unit
        + q_power * (2 * p_unit * p_unit + 4 * p_unit * r_unit)
        + 2 * q_power * q_power * p_unit * p_unit * r_unit
    )

    if not (
        is_prime(p)
        and p % 24 == 1
        and 2 <= h < p
        and h % 3 == 0
        and root_capacity % u == 0
        and gcd(2 * r + 1, root_capacity) == u
        and b == t == 1
        and valuation(h + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(p * h + 1, q) == 2 * b + t
        and p * h + 1 == q_power * receipt_unit
        and receipt_unit % q == 0
        and valuation(t_value, q) == b + t
        and 2 * t_value == q_power * t_unit
        and t_unit % q == 0
        and h * ((v + 3) // q_power)
        == 3 * (p_unit + h_unit) + q_power * p_unit * p_unit
        and u * ((w + 9) // q_power) == 2 * r_unit + 3 * h_unit
        and valuation(v + 3, q) == b
        and valuation(w + 9, q) >= b + 1
    ):
        raise AssertionError("oriented root-quotient q-primary control changed")
    print("verified transverse p-minus-one root-quotient orientation")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
