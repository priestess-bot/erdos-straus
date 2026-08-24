#!/usr/bin/env python3
"""Focused symbolic checks for the high-endpoint k=1 Pell residual."""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def parameters(d: int, x: int, y: int) -> dict[str, int]:
    Q = x * x - x * y + y * y
    e = d * x * x
    a = d * x * y - 1
    m = d * Q - 1
    h = d * d * x * x * Q - d * x * (x + y) + 1
    numerator = d**3 * x**4 * Q - d * d * x**3 * (x + y) + 1
    if numerator % a:
        raise AssertionError("Pell parameters did not produce integral p")
    p = numerator // a
    D = m * p + 1 - h
    return {
        "Q": Q,
        "e": e,
        "a": a,
        "m": m,
        "h": h,
        "p": p,
        "D_shadow": D,
    }


def check_noncore_shadow() -> None:
    row = parameters(2, 2, 3)
    if not (
        row
        == {
            "Q": 7,
            "e": 8,
            "a": 11,
            "m": 13,
            "h": 93,
            "p": 67,
            "D_shadow": 779,
        }
        and row["p"] % 24 != 1
        and row["h"] > row["p"]
        and row["D_shadow"] * row["e"] == row["p"] * row["h"] + 1
    ):
        raise AssertionError("noncore high Pell shadow changed")


def check_core_curve_shadow_terminal_preemption() -> None:
    row = parameters(11, 101, 1_020)
    p = row["p"]
    h = row["h"]
    x_gap = (p + 3) // 4
    terminal_factor = 8_363
    if not (
        p == 115_815_206_209
        and is_prime(p)
        and p % 24 == 1
        and h == 1_169_617_882_071
        and h > p
        and row["D_shadow"] == 1_207_185_892_628_946_440
        and row["D_shadow"] * row["e"] == p * h + 1
        and x_gap % terminal_factor == 0
        and terminal_factor % 3 == 2
    ):
        raise AssertionError("core high Pell curve shadow changed")


def verify_symbolic_parameterization() -> None:
    for d, x, y in ((2, 2, 3), (2, 13, 21), (11, 101, 1_020)):
        row = parameters(d, x, y)
        c_numerator = y * y + x * y - x * x
        if not (
            gcd(x, y) == 1
            and y > x
            and d % 3 == 2
            and x % 3 != 0
            and y % 3 == 0
            and c_numerator == row["a"]
            and row["a"] > row["e"]
            and row["m"] % 3 == 1
            and row["h"] % 3 == 0
            and (row["p"] * row["p"] + row["p"] + 1) % row["h"] == 0
        ):
            raise AssertionError("high k=1 Pell parameterization changed")


def verify() -> None:
    verify_symbolic_parameterization()
    check_noncore_shadow()
    check_core_curve_shadow_terminal_preemption()
    print("verified high k=1 Pell residual parameterization and boundary controls")


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
