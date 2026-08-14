#!/usr/bin/env python3
"""Verify fixed controls for the actual-root small-stutter exclusion."""

from __future__ import annotations

import argparse
from math import gcd


def factor(n: int) -> dict[int, int]:
    result: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def actual_root_receipt(p: int, r: int) -> dict[str, int]:
    g = (p + 1) // 2
    m0 = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, m0)
    h = 3 * u
    t_value = p * p * r - g
    a_value = g * t_value
    k_value = a_value * (p - 1)
    r_value = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    z_value = r_value - h
    capacity = factor(k_value)
    q_block = 1
    for q, exponent in factor(z_value).items():
        if exponent > capacity.get(q, 0):
            q_block *= q**exponent
    g_a = gcd(a_value, q_block)
    return {
        "p": p,
        "m0": m0,
        "u": u,
        "h": h,
        "K": k_value,
        "z": z_value,
        "D": (z_value // q_block) * g_a,
    }


def verify_actual_small_root_control() -> None:
    state = actual_root_receipt(73, 3)
    p, h, d_value = state["p"], state["h"], state["D"]
    p_cyclotomic = p * p + p + 1
    if not (
        p % 24 == 1
        and (state["m0"] % 6) == 1
        and (state["u"], h, d_value) == (1, 3, 220)
        and 2 <= h < p
        and h * h < 3 * p + 78
        and gcd(d_value, p_cyclotomic) == 1
        and state["z"] % state["K"] != 0
        and (d_value - (1 - h)) % p != 0
    ):
        raise AssertionError("actual small-root strict control changed")


def verify_m_one_needs_the_actual_root_gate() -> None:
    # This satisfies the linear m=1 stutter identities but is not a root receipt:
    # h is not 3u and D shares the cyclotomic factor 3 with P.
    p, h, m = 73, 71, 1
    d_value = m * p + 1 - h
    e_value = (p * h + 1) // d_value
    p_cyclotomic = p * p + p + 1
    if not (
        e_value * d_value == p * h + 1
        and d_value * (p + e_value) == p_cyclotomic
        and gcd(d_value, p_cyclotomic) == 3
        and p_cyclotomic % h != 0
    ):
        raise AssertionError("m=1 non-root boundary changed")


def verify_delta_six_boundary() -> None:
    c_value = 2
    for u in (1, 5, 7, 11):
        p = 3 * u * u - c_value
        h = 3 * u
        p_cyclotomic = p * p + p + 1
        quotient = (c_value * c_value - c_value + 1) // 3
        expanded = 3 * (3 * u**4 + (1 - 2 * c_value) * u * u + quotient)
        if not (
            p % 24 == 1
            and h * h - 3 * p == 6
            and p_cyclotomic == expanded
            and (p_cyclotomic % h == 0) == (quotient % u == 0)
        ):
            raise AssertionError("delta=6 defect identity changed")
    if 3 * 1 * 1 - c_value != 1:
        raise AssertionError("delta=6 prime contradiction changed")


def verify() -> None:
    verify_actual_small_root_control()
    verify_m_one_needs_the_actual_root_gate()
    verify_delta_six_boundary()
    print("verified actual-root small band and fixed defect-boundary controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
