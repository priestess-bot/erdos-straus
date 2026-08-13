#!/usr/bin/env python3
"""Verify the Eisenstein-prime support restriction for root stutter norms."""

from __future__ import annotations

import argparse

import sympy


def check_case(p: int, h: int, m: int, e: int) -> None:
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b
    if not (h % 2 == 1 and 2 <= h < p):
        raise AssertionError("control is outside the proper-root parity box")
    if (p * p + p + 1) % h:
        raise AssertionError("h does not divide the cyclotomic factor")
    if p * a != h * (b + 1) - b:
        raise AssertionError("stutter linear identity changed")
    if norm % h:
        raise AssertionError("h does not divide the Eisenstein norm")
    factors = sympy.factorint(norm)
    bad = [q for q in factors if q != 3 and q % 3 != 1]
    if bad:
        raise AssertionError(f"forbidden norm-prime classes: {bad}")
    quotient = norm // h
    quotient_factors = sympy.factorint(quotient)
    bad_quotient = [q for q in quotient_factors if q != 3 and q % 3 != 1]
    if bad_quotient:
        raise AssertionError(f"forbidden quotient-prime classes: {bad_quotient}")

    # For a non-degenerate h-prime q, the capacity-source residue is forced by pa=-b mod q.
    for q in sympy.factorint(h):
        if a % q:
            if (p * a + b) % q:
                raise AssertionError("h-prime source residue relation changed")
            i = q - (p % q)
            if not (0 < i < q and (p + i) % q == 0):
                raise AssertionError("capacity-source residue was not reconstructed")


def verify() -> None:
    # These are arithmetic controls for the stutter curve, not provenance claims.
    check_case(25957, 9327, 3, 3532)
    check_case(54481, 12063, 13, 944)
    print("verified Eisenstein support restriction for root-stutter norms")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
