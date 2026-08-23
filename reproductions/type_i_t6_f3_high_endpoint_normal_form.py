#!/usr/bin/env python3
"""Focused checks for the F3 high-endpoint normal form."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_root_capacity_general_endpoint_divisor_gate import chart


def check_strict_actual_control() -> None:
    receipt = chart(313, 271)
    p = receipt["p"]
    h = receipt["h"]
    c = receipt["D"] * pow(h - 1, -1, p) % p
    support = receipt["A"] * receipt["E"]
    target_capacity = support * c
    target_remainder = (4 * target_capacity - 1) // p
    bound = (p - 1) ** 2 // 4
    if not (
        receipt["u"] < receipt["M"]
        and h > p
        and receipt["z"] % receipt["K"] != 0
        and receipt["D"] == 8
        and c == 298 < p - 1
        and receipt["E"] * receipt["D"] == receipt["z"]
        and receipt["K"] % receipt["D"] == 0
        and (p * h + 1) % receipt["D"] == 0
        and support > bound
        and target_remainder > p
        and target_capacity // support == c
        and (0, c) < (0, p - 1)
    ):
        raise AssertionError("strict high actual normal form changed")


def check_high_stutter_shadow() -> None:
    # Deliberately outside the core-prime domain: arithmetic shadow only.
    p, r, shadow_d = 67, 25_311, 779
    M = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, M)
    h = 3 * u
    delta = h - p - 1
    m = (shadow_d + delta) // p + 1
    e = (p * h + 1) // shadow_d
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b
    L = a * m
    s = m - a
    divisor_form = L * L + L * s + s * s
    if not (
        p % 24 != 1
        and h > p
        and M % u == 0
        and 0 < u < M
        and shadow_d == (m - 1) * p - delta
        and (m, e, a) == (13, 8, 11)
        and a > e > 0
        and p * a == e * (h - 1) + 1
        and (p * h + 1) % shadow_d == 0
        and (p * p + p + 1) % h == 0
        and norm % h == 0
        and m >= 3
        and (a + 3 * u) % m == 0
        and L * p == 9 * u * u + 3 * (a - 1) * u + s
        and divisor_form % u == 0
    ):
        raise AssertionError("high stutter shadow normal form changed")


def check_high_stutter_symbolic_identities() -> None:
    controls = (
        # p, h, D, m, e; all are deliberately non-core shadows.
        (67, 93, 779, 13, 8),
        (283, 1_101, 32, 4, 9_737),
        (2_383, 37_623, 506, 16, 177_185),
        (3_607, 8_337, 13_306, 6, 2_260),
    )
    for p, h, D, m, e in controls:
        a = e * m - h
        b = e - 1
        norm = a * a - a * b + b * b
        u = h // 3
        L = a * m
        s = m - a
        if not (
            p % 24 != 1
            and h > p
            and D == m * p + 1 - h
            and e * D == p * h + 1
            and a > e > 0
            and p * a == e * (h - 1) + 1
            and (p * p + p + 1) % h == 0
            and norm % h == 0
            and m >= 3
            and m % 3 != 2
            and (a + 3 * u) % m == 0
            and L * p == 9 * u * u + 3 * (a - 1) * u + s
            and (L * L + L * s + s * s) % u == 0
        ):
            raise AssertionError("high stutter symbolic-control family changed")


def verify() -> None:
    check_strict_actual_control()
    check_high_stutter_shadow()
    check_high_stutter_symbolic_identities()
    print("verified high-endpoint strict overflow form and high stutter identities")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
