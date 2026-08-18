#!/usr/bin/env python3
"""Verify controls for the proper-root common-divisor alignment lemma.

The proof is the valuation argument in the matching claim. These exact
controls protect the cyclotomic identity and keep an abstract stutter tuple
without root provenance from being mistaken for a counterexample.
"""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factor(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def stutter_data(p: int, h: int, m: int, e: int) -> dict[str, int]:
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b
    if norm % h:
        raise AssertionError("control lost h-divisibility of the Eisenstein norm")
    return {
        "p": p,
        "h": h,
        "m": m,
        "e": e,
        "a": a,
        "b": b,
        "norm": norm,
        "k": norm // h,
    }


def verify_alignment(data: dict[str, int]) -> None:
    p, h, e, a, b, norm, k = (
        data[key] for key in ("p", "h", "e", "a", "b", "norm", "k")
    )
    if p * a != e * (h - 1) + 1:
        raise AssertionError("stutter linear identity changed")
    cyclotomic = p * p + p + 1
    if cyclotomic % h:
        raise AssertionError("control lost the cyclotomic root condition")

    bracket = e * e * h + e * (a - 2 * b) + k
    if a * a * cyclotomic != h * bracket:
        raise AssertionError("cyclotomic common-divisor identity changed")
    if bracket % (a * a):
        raise AssertionError("cyclotomic quotient was not integral")

    common = gcd(a, b)
    if (h + k) % common or norm % (common * common):
        raise AssertionError("common-divisor prerequisites changed")
    if gcd(h, k) % common:
        raise AssertionError("common divisor escaped gcd(h, k)")
    for prime, exponent in factor(common).items():
        if exponent > min(valuation(h, prime), valuation(k, prime)):
            raise AssertionError("valuation alignment changed")


def verify_cyclotomic_controls() -> None:
    shared = stutter_data(25_957, 9_327, 3, 3_532)
    verify_alignment(shared)
    if (shared["k"], gcd(shared["a"], shared["b"])) != (1_029, 3):
        raise AssertionError("shared-factor control changed")

    primitive = stutter_data(54_481, 12_063, 13, 944)
    verify_alignment(primitive)
    if (primitive["k"], gcd(primitive["a"], primitive["b"])) != (61, 1):
        raise AssertionError("quotient-only control changed")


def verify_missing_cyclotomic_boundary() -> None:
    clue = stutter_data(20_065_847_377, 138_378_387, 6_768, 20_446)
    p, h, e, a, b, k = (
        clue[key] for key in ("p", "h", "e", "a", "b", "k")
    )
    cyclotomic = p * p + p + 1
    bracket = e * e * h + e * (a - 2 * b) + k
    common = gcd(a, b)
    if not (
        cyclotomic % h == 39_277_161
        and a * a * cyclotomic == h * bracket
        and bracket % (a * a) == 5_643
        and common == 141
        and gcd(h, k) == 3
        and (h + k) % common == 3
    ):
        raise AssertionError("missing-cyclotomic boundary changed")


def verify() -> None:
    verify_cyclotomic_controls()
    verify_missing_cyclotomic_boundary()
    print("verified proper-root common-divisor alignment controls")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
