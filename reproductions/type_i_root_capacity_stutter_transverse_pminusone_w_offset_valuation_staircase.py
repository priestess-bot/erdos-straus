#!/usr/bin/env python3
"""Verify fixed q-primary controls for the p-minus-one w+9 valuation staircase."""

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


def verify_control(
    p: int,
    h: int,
    q: int,
    r: int,
    b: int,
    t: int,
    expected_w_valuation: int,
    *,
    proper_root: bool,
) -> None:
    u = h // 3
    root_capacity = (p * p + p + 1) // 3
    t_value = p * p * r - (p + 1) // 2
    if (
        not is_prime(p)
        or p % 24 != 1
        or not is_prime(q)
        or q in (2, 3)
        or not (2 <= h < p and h % 3 == 0)
        or u <= 0
        or (2 * r + 1) % u
        or u % q == 0
    ):
        raise AssertionError("control did not satisfy its core q-primary input")

    root_conditions = root_capacity % u == 0 and gcd(2 * r + 1, root_capacity) == u
    if root_conditions != proper_root:
        raise AssertionError("control root provenance label changed")

    w = (2 * r + 1) // u
    w_valuation = valuation(w + 9, q)
    if not (
        valuation(p - 1, q) == b
        and valuation(h + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(p * h + 1, q) == 2 * b + t
        and valuation(t_value, q) == b + t
        and p * p * u * (w + 9)
        == 2 * t_value + (p - 1) ** 2 + 3 * p * (p * h + 1)
        and w_valuation == expected_w_valuation
    ):
        raise AssertionError("w+9 valuation staircase input changed")

    if t < b:
        if w_valuation != b + t:
            raise AssertionError("t<b staircase branch changed")
    elif t > b:
        if w_valuation != 2 * b:
            raise AssertionError("t>b staircase branch changed")
    else:
        resonance = (
            2 * (t_value // q ** (2 * b)) + ((p - 1) // q**b) ** 2
        ) % q
        if w_valuation < 2 * b or (w_valuation > 2 * b) != (resonance == 0):
            raise AssertionError("t=b resonance gate changed")


def verify() -> None:
    # The second and last controls have full proper-root input; all four exercise
    # only the valuation algebra, not a complete actual stutter receipt.
    verify_control(7057, 2253, 7, 254213, 2, 1, 3, proper_root=False)
    verify_control(8641, 39, 5, 266, 1, 1, 2, proper_root=True)
    verify_control(2017, 1623, 7, 183128, 1, 1, 3, proper_root=False)
    verify_control(74161, 7059, 5, 224711, 1, 2, 2, proper_root=True)
    print("verified transverse p-minus-one w+9 valuation staircase")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
