#!/usr/bin/env python3
"""Verify QC1 endpoint-excess deflation valuation and residue boundaries."""

from __future__ import annotations

import argparse


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def deflation_control(prime: int, support: int, q: int, multiplier: int) -> dict[str, int]:
    if not (
        prime % 24 == 1
        and q < prime // 4
        and 4 * support % prime == prime - 1
        and multiplier % prime == 1
    ):
        raise AssertionError("outside endpoint-excess residue control")
    r = valuation(prime - 1, q)
    exponent = valuation(multiplier, q)
    if exponent <= r:
        raise AssertionError("control does not cross endpoint capacity")
    mu = 1 if exponent >= r + 2 else r + 1
    child_multiplier = multiplier // (q**mu)
    child_support = support * child_multiplier
    cofactor = (-pow(q, mu, prime)) % prime
    if not (
        multiplier % (q**exponent) == 0
        and child_multiplier > 1
        and child_support > support
        and 1 <= cofactor <= prime - 2
        and pow(q, mu, prime) != 1
    ):
        raise AssertionError("endpoint-excess deflation boundary changed")
    return {
        "prime": prime,
        "q": q,
        "r": r,
        "exponent": exponent,
        "mu": mu,
        "child_multiplier": child_multiplier,
        "cofactor": cofactor,
    }


def verify() -> None:
    controls = (
        deflation_control(97, 121, 7, 7 * 499),
        deflation_control(337, 421, 7, 7 * 7 * 619),
        deflation_control(3529, 4411, 7, 7 * 7 * 7 * 96281),
    )
    if tuple(item["mu"] for item in controls) != (1, 2, 3):
        raise AssertionError("endpoint-excess capacity-boundary cases changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified QC1 endpoint-excess deflation boundary")


if __name__ == "__main__":
    main()
