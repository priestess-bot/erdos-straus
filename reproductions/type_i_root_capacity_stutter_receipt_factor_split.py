#!/usr/bin/env python3
"""Verify the root endpoint D factor split on fixed integer controls."""

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
    capacity_factors = factor(capacity)
    q_block = 1
    for q, exponent in factor(value).items():
        if exponent > capacity_factors.get(q, 0):
            q_block *= q**exponent
    return q_block, value // q_block


def chart(p: int, r: int) -> dict[str, int]:
    g = (p + 1) // 2
    m0 = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, m0)
    h = 3 * u
    t_value = p * p * r - g
    a_value = g * t_value
    k_value = a_value * (p - 1)
    r_value = 2 * p**3 * r - p * p - 2 * p * r - p + 1
    z_value = r_value - h
    q_block, beta = complete_excess(z_value, k_value)
    g_a = gcd(a_value, q_block)
    e_value = q_block // g_a
    d_value = beta * g_a
    c_value = (p * p - 1) // 2
    d_c = gcd(d_value, c_value)
    d_t = d_value // d_c
    return {
        "p": p,
        "r": r,
        "m0": m0,
        "u": u,
        "h": h,
        "T": t_value,
        "A": a_value,
        "K": k_value,
        "R": r_value,
        "z": z_value,
        "Q": q_block,
        "E": e_value,
        "D": d_value,
        "C": c_value,
        "D_C": d_c,
        "D_T": d_t,
    }


def verify_case(p: int, r: int) -> None:
    s = chart(p, r)
    h = s["h"]
    d_value = s["D"]
    z_value = s["z"]
    m0 = s["m0"]
    d_c = s["D_C"]
    d_t = s["D_T"]
    if not (
        s["K"] % (h * d_value) == 0
        and gcd(h, z_value) == 1
        and (p * h + 1) % d_value == 0
        and gcd(d_value, m0) == 1
        and (h * h - 1) % d_c == 0
        and (h * h - h - 2 * r) % d_t == 0
        and ((h * h - 1) * (h * h - h - 2 * r)) % d_value == 0
    ):
        raise AssertionError(f"factor split failed for p={p}, r={r}")

    # A cyclotomic prime occurring in z has zero K-capacity and is wholly in E.
    for q in factor(m0):
        if z_value % q == 0:
            z_exponent = factor(z_value).get(q, 0)
            if s["K"] % q == 0 or d_value % q == 0:
                raise AssertionError(f"cyclotomic allocation failed for q={q}")
            if s["E"] % (q**z_exponent) != 0:
                raise AssertionError(f"cyclotomic E allocation failed for q={q}")


def verify() -> None:
    # Proper root, saturated root, and nontrivial T-part controls.
    for p, r in ((313, 271), (73, 900), (73, 3), (241, 3)):
        verify_case(p, r)
    s = chart(313, 271)
    if (s["u"], s["h"], s["D"], s["D_C"], s["D_T"]) != (181, 543, 8, 8, 1):
        raise AssertionError("proper-root control changed")
    s = chart(73, 3)
    if s["D_T"] != 55:
        raise AssertionError("nontrivial T-part control changed")
    print("verified four fixed root receipts and the cyclotomic D/E split")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
