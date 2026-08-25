#!/usr/bin/env python3
"""Verify the q=1 C=9 R=23 fixed-tail terminal subray."""

from __future__ import annotations

import argparse


def terminal_ray(prime: int) -> dict[str, int]:
    if prime % 11_088 != 1_033:
        raise AssertionError("prime is outside the R=23 fixed-tail terminal ray")
    if prime % 24 != 1:
        raise AssertionError("prime is outside the core residue class")
    j = (prime - 25) // 1_008
    K = (23 * prime + 1) // 4
    e = K // 22
    a = (K + e) // 23
    b = (K + K * K // e) // 23
    if not (
        prime == 1_008 * j + 25
        and j % 11 == 1
        and 23 * prime + 1 == 4 * K
        and K % 22 == 0
        and e % 23 == (-K) % 23
        and K * K % e == 0
        and (K + e) % 23 == 0
        and (K + K * K // e) % 23 == 0
        and (a, b) == (e, K)
        and 4 * a * b * prime * K
        == prime * (b * prime * K + a * prime * K + a * b)
    ):
        raise AssertionError("R=23 fixed-tail terminal identity changed")
    return {"prime": prime, "j": j, "K": K, "e": e, "a": a, "b": b, "third": prime * K}


def verify() -> None:
    control = terminal_ray(1_033)
    if control != {
        "prime": 1033,
        "j": 1,
        "K": 5940,
        "e": 270,
        "a": 270,
        "b": 5940,
        "third": 6136020,
    }:
        raise AssertionError("R=23 terminal control changed")
    try:
        terminal_ray(3_049)
    except AssertionError:
        return
    raise AssertionError("off-ray C=9 control was accepted")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified q=1 C=9 R=23 fixed-tail terminal ray")


if __name__ == "__main__":
    main()
