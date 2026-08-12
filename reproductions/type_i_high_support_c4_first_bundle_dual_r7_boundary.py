#!/usr/bin/env python3
"""Verify the C=4 first-bundle dual R=7 boundary and p=1801 pressure point."""

from __future__ import annotations

import argparse

import sympy

import type_i_bottom_sink_scc_complete_excess_bundle as bottom
from type_i_high_support_c4_g_stutter_boundary import (
    c4_plus_boundary,
    canonical_stutter,
)


def g_separator(*, R: int, K: int) -> bool:
    """Check the finite Jacobi separator used for a named G chart."""
    values = [bottom.jacobi_symbol(q, R) for q in bottom.factorization(K)]
    return all(value == 1 for value in values) and bottom.jacobi_symbol(-1, R) == -1


def first_bundle_duals(prime: int) -> dict[str, int]:
    """Build the determinant duals of the first C=4 stutter target."""
    boundary = c4_plus_boundary(prime)
    stutter = canonical_stutter(boundary)
    M = stutter["M"]
    R_M = stutter["target_R"]
    K_M = stutter["target_K"]
    d = prime - 4
    n = 4 * M - R_M
    r = M % prime
    s = (4 * r * d + 1) // prime
    R_d = 4 * d - s
    R_r = 4 * r - s
    K_d = d * (prime - r)
    K_r = r * (prime - d)
    if not (
        0 < r < prime
        and (4 * r * d + 1) % prime == 0
        and prime * n == 4 * M * d + 1
        and bottom.canonical_chart(prime, d) == (R_d, K_d)
        and bottom.canonical_chart(prime, r) == (R_r, K_r)
        and R_d > prime
        and R_r < prime
        and M > K_r
    ):
        raise AssertionError("C=4 first-bundle dual formulas failed")
    expected_r = (7 * prime + 1) // 16
    expected_s = (7 * prime - 27) // 4
    if not (
        r == expected_r
        and s == expected_s
        and R_d == (9 * prime - 37) // 4
        and R_r == 7
        and K_r == (7 * prime + 1) // 4
    ):
        raise AssertionError("C=4 dual closed form changed")
    return {
        "p": prime,
        "M": M,
        "R_M": R_M,
        "K_M": K_M,
        "n": n,
        "d": d,
        "r": r,
        "s": s,
        "R_d": R_d,
        "K_d": K_d,
        "R_r": R_r,
        "K_r": K_r,
    }


def verify_p1801_pressure() -> None:
    """Check the restricted C4 route at the explicit core prime p=1801."""
    prime = 1_801
    if not sympy.isprime(prime) or prime % 24 != 1:
        raise AssertionError("p=1801 is not a core prime")
    boundary = c4_plus_boundary(prime)
    stutter = canonical_stutter(boundary)
    duals = first_bundle_duals(prime)
    if boundary != {
        "p": 1801,
        "B": 810000,
        "R": 7207,
        "A": 811238,
        "K": 3244952,
    }:
        raise AssertionError("p=1801 C=4 source chart changed")
    if stutter != {
        "Q": 3603,
        "beta": 2,
        "residual": 2,
        "M": 2922890514,
        "target_R": 25966823,
        "target_K": 11691562056,
        "source_cofactor": 4,
        "target_cofactor": 4,
    }:
        raise AssertionError("p=1801 C=4 first bundle changed")
    if duals != {
        "p": 1801,
        "M": 2922890514,
        "R_M": 25966823,
        "K_M": 11691562056,
        "n": 11665595233,
        "d": 1797,
        "r": 788,
        "s": 3145,
        "R_d": 4043,
        "K_d": 1820361,
        "R_r": 7,
        "K_r": 3152,
    }:
        raise AssertionError("p=1801 dual receipt changed")

    charts = (
        ("H0", boundary["R"], boundary["K"]),
        ("H1", stutter["target_R"], stutter["target_K"]),
        ("R7", duals["R_r"], duals["K_r"]),
    )
    for name, R, K in charts:
        if not g_separator(R=R, K=K):
            raise AssertionError(f"{name} ceased to be a Jacobi G chart")
    if bottom.factorization(boundary["K"]) != {2: 3, 43: 1, 9433: 1}:
        raise AssertionError("p=1801 H0 factorization changed")
    if bottom.factorization(stutter["target_K"]) != {
        2: 3,
        3: 1,
        43: 1,
        1201: 1,
        9433: 1,
    }:
        raise AssertionError("p=1801 H1 factorization changed")
    if bottom.factorization(duals["K_r"]) != {2: 4, 197: 1}:
        raise AssertionError("p=1801 R=7 factorization changed")

    x7 = (prime + 7) // 4
    x7_factors = bottom.factorization(x7)
    if x7_factors != {2: 2, 113: 1} or any(
        factor % 7 not in {1, 2, 4} for factor in x7_factors
    ):
        raise AssertionError("p=1801 gap-7 factor-pair status changed")


def verify() -> None:
    for prime in (73, 313, 409, 601, 1801, 2137):
        if prime % 48 != 25:
            raise AssertionError("closed-form control left the C=4 branch")
        first_bundle_duals(prime)
    verify_p1801_pressure()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()
    print("verified C=4 first-bundle dual R=7 boundary and p=1801 pressure point")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
