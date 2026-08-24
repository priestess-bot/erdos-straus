#!/usr/bin/env python3
"""Focused checks for the high-endpoint stutter divisor gates."""

from __future__ import annotations

import argparse
from math import gcd


def gate_values(p: int, r: int, h: int, D: int, m: int) -> dict[str, int]:
    M = (p * p + p + 1) // 3
    u = gcd(2 * r + 1, M)
    v = M // u
    omega = (2 * r + 1) // u
    delta = h - p - 1
    n = m - 1
    root_gate = delta**3 + n * delta**2 + n * n * delta + v * n**3
    capacity_gate = (delta * delta - n * n) * (
        omega * delta * delta - 3 * v * n * n
    )
    return {
        "M": M,
        "u": u,
        "v": v,
        "omega": omega,
        "delta": delta,
        "n": n,
        "root_gate": root_gate,
        "capacity_gate": capacity_gate,
    }


def check_noncore_complete_shadow() -> None:
    row = gate_values(67, 25_311, 93, 779, 13)
    if not (
        row["u"] == 31
        and row["v"] == 49
        and row["omega"] == 1_633
        and row["delta"] == 25
        and row["n"] == 12
        and row["root_gate"] % 779 == 0
        and row["capacity_gate"] % 779 == 0
    ):
        raise AssertionError("noncore complete high shadow changed")


def check_capacity_gate_rejects_curve_shadows() -> None:
    controls = (
        (283, 183, 1_101, 32, 4),
        (2_383, 6_270, 37_623, 506, 16),
        (3_607, 1_389, 8_337, 13_306, 6),
    )
    for p, r, h, D, m in controls:
        row = gate_values(p, r, h, D, m)
        if not (row["root_gate"] % D == 0 and row["capacity_gate"] % D != 0):
            raise AssertionError("capacity gate no longer rejects high curve shadow")


def verify() -> None:
    check_noncore_complete_shadow()
    check_capacity_gate_rejects_curve_shadows()
    print("verified high stutter root-quotient and capacity divisor gates")


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
