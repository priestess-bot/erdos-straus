#!/usr/bin/env python3
"""Verify the algebraic two-ray reduction for q_star=103 c8 sources."""

from __future__ import annotations

import argparse


def ray_from_u(u: int) -> dict[str, int]:
    if u % 7 not in {1, 6}:
        raise AssertionError("u is outside the two surviving residue classes")
    s = 86 + 103 * u
    p = 48 * s + 1
    six_s_minus_one = 6 * s - 1
    if u % 7 == 1:
        v = (u - 1) // 7
        expected_s = 189 + 721 * v
        expected_p = 9073 + 34608 * v
        expected_tail = 103 * (42 * v + 11)
        branch = 1
    else:
        v = (u - 6) // 7
        expected_s = 704 + 721 * v
        expected_p = 33793 + 34608 * v
        expected_tail = 103 * (42 * v + 41)
        branch = 6
    if not (
        u >= 1
        and s == expected_s
        and p == expected_p
        and six_s_minus_one == expected_tail
        and six_s_minus_one % 7 != 0
    ):
        raise AssertionError("c8 two-ray reduction identity changed")
    return {
        "u_mod_7": branch,
        "v": v,
        "s": s,
        "p": p,
        "six_s_minus_one": six_s_minus_one,
    }


def verify() -> None:
    first = ray_from_u(1)
    second = ray_from_u(6)
    if first != {
        "u_mod_7": 1,
        "v": 0,
        "s": 189,
        "p": 9073,
        "six_s_minus_one": 1133,
    }:
        raise AssertionError("first c8 ray control changed")
    if second != {
        "u_mod_7": 6,
        "v": 0,
        "s": 704,
        "p": 33793,
        "six_s_minus_one": 4223,
    }:
        raise AssertionError("second c8 ray control changed")
    try:
        ray_from_u(5)
    except AssertionError:
        return
    raise AssertionError("gap-7/roughness excluded class was accepted")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified c8 q_star=103 terminal-prefix two-ray reduction")


if __name__ == "__main__":
    main()
