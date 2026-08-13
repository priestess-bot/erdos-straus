#!/usr/bin/env python3
"""Audit the proper-root stutter gate and the withdrawn low-end argument."""

from __future__ import annotations

import argparse
from math import gcd


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    cap = factor(capacity)
    q_block = 1
    for q, exponent in factor(value).items():
        if exponent > cap.get(q, 0):
            q_block *= q**exponent
    return q_block, value // q_block


def receipt(prime: int, r: int) -> dict[str, int]:
    m0 = (prime * prime + prime + 1) // 3
    u = gcd(2 * r + 1, m0)
    h = 3 * u
    g = (prime + 1) // 2
    t_value = prime * prime * r - g
    a_value = g * t_value
    k_value = a_value * (prime - 1)
    r_value = 2 * prime**3 * r - prime * prime - 2 * prime * r - prime + 1
    z_value = r_value - h
    q_block, beta = complete_excess(z_value, k_value)
    g_a = gcd(a_value, q_block)
    e_value = q_block // g_a
    d_value = beta * g_a
    return {
        "p": prime,
        "r": r,
        "m0": m0,
        "u": u,
        "h": h,
        "A": a_value,
        "K": k_value,
        "R": r_value,
        "z": z_value,
        "E": e_value,
        "D": d_value,
    }


def verify_receipt(data: dict[str, int]) -> None:
    p, h, m0, d = data["p"], data["h"], data["m0"], data["D"]
    z, k = data["z"], data["K"]
    if not (
        data["u"] < m0
        and k % h == 0
        and k % d == 0
        and z % d == 0
        and gcd(h, z) == 1
        and (p * h + 1) % d == 0
    ):
        raise AssertionError("fixed root receipt no longer satisfies actual hypotheses")

    c = (d * pow(h - 1, -1, p)) % p
    if not 1 <= c <= p - 1:
        raise AssertionError("canonical cofactor range changed")


def verify_withdrawn_argument(p: int, h: int, m: int) -> None:
    """Exhibit why the former subtraction step is not a valid implication."""
    if not (0 < h < p and m >= 1):
        raise AssertionError("invalid symbolic test parameters")
    d = m * p + 1 - h
    if d <= 0:
        raise AssertionError("the hypothetical divisor must be positive")
    if (p * h + 1) + p * d != m * p * p + p + 1:
        raise AssertionError("first divisibility identity changed")
    cyclotomic_multiple = m * (p * p + p + 1)
    if cyclotomic_multiple % d == 0:
        raise AssertionError("control accidentally validates the withdrawn implication")
    if (m * p * p + p + 1) % d != 0:
        raise AssertionError("stutter divisibility control changed")


def verify_core_stutter_control() -> None:
    """Keep a core-congruence stutter candidate separate from actual receipts."""
    p, h, m, e = 361, 1029, 3, 6754
    d = m * p + 1 - h
    n = p * p + p + 1
    if not (
        p % 24 == 1
        and n % h == 0
        and d == 55
        and e * d == p * h + 1
        and d % p == (1 - h) % p
    ):
        raise AssertionError("core abstract stutter control changed")


def verify() -> None:
    verify_receipt(receipt(73, 3))
    verify_receipt(receipt(457, 3))
    verify_withdrawn_argument(5, 3, 2)
    verify_core_stutter_control()
    print("verified actual root gates, the withdrawn proof boundary, and a core abstract gate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
