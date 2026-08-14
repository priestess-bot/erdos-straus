#!/usr/bin/env python3
"""Verify the necessary integer-curve constraints for a root stutter gate."""

from __future__ import annotations

import argparse
from math import gcd


def curve_values(p: int, h: int, m: int, e: int) -> dict[str, int]:
    d = m * p + 1 - h
    a = e * m - h
    f = e * e * m * m - e * e * m + e * e + e * m - 2 * e + 1
    return {"D": d, "a": a, "F": f}


def verify_tuple(p: int, h: int, m: int, e: int, *, core_congruence: bool) -> None:
    values = curve_values(p, h, m, e)
    d, a, f = values["D"], values["a"], values["F"]
    if d <= 0 or a <= 0:
        raise AssertionError("stutter parameters must give positive D and a")
    if e * d != p * h + 1:
        raise AssertionError("eD=ph+1 identity changed")
    if p * a != e * (h - 1) + 1:
        raise AssertionError("p(em-h)=e(h-1)+1 identity changed")
    if d * a != m + h * (h - 1):
        raise AssertionError("D(em-h)=m+h(h-1) identity changed")
    if m * e * e - e + 1 != a * (p + e):
        raise AssertionError("exact p+e quotient identity changed")
    if (p * p + p + 1) % h != 0 or f % h != 0:
        raise AssertionError("cyclotomic curve condition changed")
    if gcd(e, h) != 1:
        raise AssertionError("gcd(e,h)=1 consequence changed")
    if ((e - 1) ** 2) % gcd(h, m) != 0:
        raise AssertionError("gcd(h,m)|(e-1)^2 consequence changed")
    if core_congruence and p % 24 != 1:
        raise AssertionError("core congruence control changed")


def verify() -> None:
    # Core-congruence control; p is deliberately composite, so this is not an actual receipt.
    verify_tuple(361, 1029, 3, 6754, core_congruence=True)
    # Prime control outside the core residue class; it is also only an arithmetic candidate.
    verify_tuple(67, 93, 13, 8, core_congruence=False)

    # A one-unit perturbation must fail the exact eD relation.
    p, h, m, e = 361, 1029, 3, 6755
    if e * (m * p + 1 - h) == p * h + 1:
        raise AssertionError("negative perturbation unexpectedly remained a stutter tuple")
    print("verified root-stutter integer curve controls and negative perturbation")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
