#!/usr/bin/env python3
"""Verify the p=241 R=3/R=7 empty-fiber counterexample and Type-II rescue."""

from __future__ import annotations

import argparse


def residue_fiber(k_factors: tuple[tuple[int, int], ...], modulus: int) -> set[int]:
    residues = {1}
    for prime, exponent in k_factors:
        powers = {pow(prime, power, modulus) for power in range(-exponent, exponent + 1)}
        residues = {(left * right) % modulus for left in residues for right in powers}
    return residues


def run_verification() -> dict[str, object]:
    prime = 241
    r3 = residue_fiber(((181, 1),), 3)
    r7 = residue_fiber(((2, 1), (211, 1)), 7)
    assert r3 == {1}
    assert r7 == {1, 2, 4}
    assert (-1) % 3 not in r3
    assert (-1) % 7 not in r7

    a, c, k, b, h = 1, 1, 2, 69, 7
    assert h == 4 * a * c * k - 1
    assert (prime + 4 * a * a * c) % h == 0
    assert (k * prime + a) % h == 0
    assert b == (k * prime + a) // h
    assert b > a

    return {
        "p": prime,
        "R3_fiber": sorted(r3),
        "R7_fiber": sorted(r7),
        "type_ii": {"A": a, "C": c, "K": k, "B": b, "h": h},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified R=3/R=7 chart-fan counterexample")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
