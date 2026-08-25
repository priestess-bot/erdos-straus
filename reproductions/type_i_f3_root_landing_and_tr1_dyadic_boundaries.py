#!/usr/bin/env python3
"""Replay static controls for two F3 arithmetic boundary theorems.

The controls validate integer identities only.  They are not persistent-source
receipts and do not claim E1, admission, or a terminal-first miss.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def complete_excess(value: int, capacity: int) -> int:
    capacity_factors = factorization(capacity)
    result = 1
    for prime, exponent in factorization(value).items():
        if exponent > capacity_factors.get(prime, 0):
            result *= prime**exponent
    return result


def root_atomic_countercontrol() -> dict[str, int]:
    prime = 73
    root_support = 590_150
    support = 638
    capacity = 24
    carrier = support * capacity
    residual = (4 * carrier - 1) // prime
    left, right = 25, 814
    q_left, q_right = 25, 37
    if not (
        4 * carrier == prime * residual + 1
        and left + right == residual
        and gcd(left, right) == 1
        and right == q_right * 22
        and carrier % 22 == 0
        and complete_excess(left, carrier) == q_left
        and complete_excess(right, carrier) == q_right
        and lcm(support, q_left, q_right) == root_support
        and pow(4 * root_support, -1, prime) == prime - 1
        and support <= (prime - 1) ** 2 // 4
    ):
        raise AssertionError("static atomic root-landing countercontrol changed")
    return {
        "p": prime,
        "A_star": root_support,
        "a": support,
        "c": capacity,
        "K": carrier,
        "R": residual,
        "Q_x": q_left,
        "Q_y": q_right,
    }


def dyadic_local_control() -> dict[str, int]:
    prime, height, divisor, m, quotient = 283, 1_101, 32, 4, 9_737
    shared = gcd(divisor, height * height - 1)
    d_star = divisor // shared
    if not (
        prime * height + 1 == divisor * quotient
        and shared == 8
        and d_star == 4
        and valuation(divisor, 2) == 5
        and valuation(height * height - 1, 2) == 3
        and m % 2 == 0
    ):
        raise AssertionError("local dyadic control changed")
    return {
        "p": prime,
        "h": height,
        "D": divisor,
        "m": m,
        "e": quotient,
        "D_star": d_star,
    }


def atomic_companion_residue_control() -> dict[str, int]:
    prime, height, multiplier = 73, 3, 367
    opposite_side = (height + 1) // 2
    if not (
        multiplier % prime == 2
        and multiplier % prime == opposite_side
        and multiplier % prime != 1
    ):
        raise AssertionError("atomic companion residue control changed")
    return {"p": prime, "h_mod_p": height, "F_y": multiplier, "y_mod_p": opposite_side}


def verify() -> None:
    root_atomic_countercontrol()
    dyadic_local_control()
    atomic_companion_residue_control()
    print("verified static root-landing and local TR1 dyadic boundary controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
