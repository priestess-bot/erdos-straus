#!/usr/bin/env python3
"""Verify the fixed-fiber affine q-primary phase-collapse lemma."""

from __future__ import annotations

import argparse
from math import gcd


P = 73
D = 1
A = 27
CARRIERS = (675, 2646, 10530)
N_VALUES = (37, 145, 577)


def phase_values(alpha: int, beta: int, q: int, exponent: int) -> tuple[int, ...]:
    modulus = q**exponent
    return tuple(sorted({(alpha * m + beta) % modulus for m in CARRIERS}))


def verify() -> None:
    if not (P % 24 == 1 and gcd(P, A) == 1 and 0 < D < P):
        raise AssertionError("fixed-fiber parameters changed")
    if len(CARRIERS) != len(N_VALUES):
        raise AssertionError("control row count changed")

    residue = (-pow((4 * D) % P, -1, P)) % P
    modulus = A * P
    if residue != 18 or modulus != 1971:
        raise AssertionError("fixed-fiber CRT residue changed")
    for m, n in zip(CARRIERS, N_VALUES):
        if m % A or m % P != residue:
            raise AssertionError("carrier CRT row changed")
        if P * n != 4 * D * m + 1:
            raise AssertionError("overflow determinant changed")
        if 4 * m - n <= P:
            raise AssertionError("overflow range changed")
    if len({m % modulus for m in CARRIERS}) != 1:
        raise AssertionError("full fixed-fiber residue did not collapse")

    q = 3
    full_depth = 3
    for exponent in range(1, full_depth + 1):
        if phase_values(1, 1, q, exponent) != (1,):
            raise AssertionError("affine phase did not collapse below Ap")
    if phase_values(1, 1, q, 4) != (1, 28, 55):
        raise AssertionError("first post-collapse phase split changed")

    required = (0, 1)
    actual_first_layer = phase_values(1, 0, q, 1)
    if actual_first_layer != (0,):
        raise AssertionError("carrier phase first layer changed")
    if set(required).issubset(actual_first_layer):
        raise AssertionError("collision fixture unexpectedly realized both labels")

    p_phase = phase_values(1, 0, P, 1)
    if p_phase != (18,):
        raise AssertionError("p-primary fixed-fiber phase changed")

    print(
        "verified fixed-fiber affine phase collapse: "
        "Ap=1971, q=3 depth=3, first split at q^4"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
