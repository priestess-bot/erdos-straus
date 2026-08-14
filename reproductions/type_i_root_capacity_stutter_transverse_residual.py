#!/usr/bin/env python3
"""Verify the transverse quotient and coprimality map for root stutter arithmetic."""

from __future__ import annotations

import argparse
from math import gcd


def verify_case(p: int, r: int, u: int, d: int) -> None:
    h = 3 * u
    m0 = (p * p + p + 1) // 3
    c = (p * p - 1) // 2
    t = p * p * r - (p + 1) // 2
    z = 2 * p**3 * r - p * p - 2 * p * r - p + 1 - h
    m, m_remainder = divmod(d + h - 1, p)
    e, e_remainder = divmod(p * h + 1, d)
    v, v_remainder = divmod(m0, u)
    w, w_remainder = divmod(2 * r + 1, u)
    d_star = d // gcd(d, h * h - 1)

    if any((m_remainder, e_remainder, v_remainder, w_remainder)):
        raise AssertionError("fixed control did not define all integer stutter coordinates")
    if not (
        gcd(2 * r + 1, m0) == u
        and (p * p + p + 1) % h == 0
        and z % d == 0
        and (c * t) % d == 0
        and gcd(d, h) == 1
        and gcd(d, m0) == 1
        and d_star > 1
    ):
        raise AssertionError(f"root-stutter arithmetic gate failed for p={p}")
    if not (
        gcd(v, w) == 1
        and v % 2 == 1
        and w % 2 == 1
        and 2 * t == u * (p * p * w - 3 * v)
        and t % u == 0
    ):
        raise AssertionError(f"root quotient identity failed for p={p}")
    if t % d_star or (t // u) % d_star or (m + 2 * r) % d_star:
        raise AssertionError(f"transverse residual divisibility failed for p={p}")
    if 2 * t != p * p * (m + 2 * r) - (p + e) * d:
        raise AssertionError(f"stutter-to-T interface identity failed for p={p}")
    if gcd(d_star, p * m0 * (2 * r + 1) * (m - 1)) != 1:
        raise AssertionError(f"transverse residual coprimality failed for p={p}")


def verify() -> None:
    # These are arithmetic controls, not actual core-prime proper-root receipts.
    verify_case(54481, 2543533812, 4021, 696191)
    verify_case(361, 3601, 343, 55)
    verify_case(67, 1162, 31, 779)
    verify_case(283, 550, 367, 32)
    print("verified root-stutter transverse quotient and coprimality map")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
