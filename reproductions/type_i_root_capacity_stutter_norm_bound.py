#!/usr/bin/env python3
"""Verify the positive-definite norm and square-root bound for root stutter."""

from __future__ import annotations

import argparse


def check_case(p: int, h: int, m: int, e: int) -> None:
    d = m * p + 1 - h
    a = e * m - h
    f_value = e * e * m * m - e * e * m + e * e + e * m - 2 * e + 1
    g_value = a * a - a * e + e * e + a - 2 * e + 1
    if d <= 0 or e * d != p * h + 1:
        raise AssertionError("stutter divisor identities failed")
    if not (2 <= h < p and a > 0 and p * a == e * (h - 1) + 1):
        raise AssertionError("proper-root stutter identities failed")
    if (p * p + p + 1) % h or f_value % h or g_value % h:
        raise AssertionError("cyclotomic divisibility failed")
    if f_value - g_value != h * (2 * e * m - e - h + 1):
        raise AssertionError("F/G change of variables changed")
    if 4 * g_value != (2 * a - e + 1) ** 2 + 3 * (e - 1) ** 2:
        raise AssertionError("positive-definite identity changed")
    if not (0 < g_value < e * e and a < e and e * e > h):
        raise AssertionError("norm bounds failed")
    if not (e * (m - 1) < h):
        raise AssertionError("linear menu bound failed")
    if not ((m - 1) ** 2 < h):
        raise AssertionError("square-root menu bound failed")


def verify() -> None:
    # Arithmetic controls; provenance is deliberately not asserted here.
    check_case(54481, 12063, 13, 944)
    check_case(25957, 9327, 3, 3532)
    print("verified root-stutter positive-definite norm and square-root bounds")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
