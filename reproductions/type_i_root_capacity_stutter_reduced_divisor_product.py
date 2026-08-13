#!/usr/bin/env python3
"""Verify the reduced-divisor product constraint for root stutter arithmetic."""

from __future__ import annotations

import argparse
from math import gcd


def factor_split(p: int, r: int, h: int, d: int) -> dict[str, int]:
    c = (p * p - 1) // 2
    t = p * p * r - (p + 1) // 2
    z = 2 * p**3 * r - p * p - 2 * p * r - p + 1 - h
    m, remainder = divmod(d + h - 1, p)
    if remainder:
        raise AssertionError("stutter divisor did not define an integer m")
    h2 = h * h - 1
    d_star = d // gcd(d, h2)
    s_value = h * h - h - 2 * r
    j_value = (
        2 * h * h * r
        - h * m
        - 4 * h * r
        - m**3
        - 2 * m * m * r
        - m * m
        + m
        + 2 * r
    )
    h1 = h * h - h + m
    h2_factor = h * h - 2 * h - m * m - m + 1
    return {
        "C": c,
        "T": t,
        "z": z,
        "m": m,
        "D_star": d_star,
        "S": s_value,
        "J": j_value,
        "H1": h1,
        "H2": h2_factor,
    }


def verify_case(p: int, r: int, u: int, d: int) -> None:
    h = 3 * u
    values = factor_split(p, r, h, d)
    c = values["C"]
    t = values["T"]
    z = values["z"]
    m = values["m"]
    d_star = values["D_star"]
    if not (
        (p * p + p + 1) % h == 0
        and (2 * r + 1) % u == 0
        and (p * h + 1) % d == 0
        and d % p == (1 - h) % p
        and z % d == 0
        and (c * t) % d == 0
        and d_star > 0
    ):
        raise AssertionError(f"stutter arithmetic gate failed for p={p}, r={r}")
    if any(values[key] % d_star for key in ("T", "S", "J")):
        raise AssertionError(f"reduced divisor does not divide all required terms for p={p}")
    if (
        values["J"]
        + ((h - 1) * (h - 1) - m * m) * values["S"]
        != values["H1"] * values["H2"]
    ):
        raise AssertionError("resultant-product identity changed")
    if values["H1"] * values["H2"] % d_star:
        raise AssertionError("reduced divisor product consequence changed")


def verify() -> None:
    # These are arithmetic controls, not claims of actual core-prime provenance.
    verify_case(361, 3601, 343, 55)
    verify_case(67, 1162, 31, 779)
    verify_case(283, 550, 367, 32)
    print("verified root-stutter reduced-divisor and product identities")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
