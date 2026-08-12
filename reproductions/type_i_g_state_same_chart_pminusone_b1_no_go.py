#!/usr/bin/env python3
"""Verify the G-state obstruction to a same-chart p-1, B=1 bridge."""

from __future__ import annotations

import argparse
from math import gcd

import type_i_bottom_sink_scc_complete_excess_bundle as bottom


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in factors.items():
        values = [value * prime**power for value in values for power in range(exponent + 1)]
    return sorted(values)


def same_chart_b1_candidates(prime: int, R: int) -> list[int]:
    K, remainder = divmod(prime * R + 1, 4)
    if remainder or K <= 0:
        raise AssertionError("invalid chart")
    return [
        C
        for C in divisors_from_factorization(bottom.factorization(K))
        if (4 * C + 1) % R == 0
    ]


def verify_control(prime: int, R: int) -> dict[str, object]:
    if not bottom.is_prime(prime) or prime % 24 != 1:
        raise AssertionError("control is not a core prime")
    if R % 4 != 3 or R < 3 or R > prime - 2:
        raise AssertionError("invalid legal chart modulus")
    K, remainder = divmod(prime * R + 1, 4)
    if remainder or gcd(K, R) != 1:
        raise AssertionError("chart identity or coprimality failed")
    factors = bottom.factorization(K)
    if any(bottom.jacobi_symbol(q, R) != 1 for q in factors):
        raise AssertionError("control is not Jacobi G")
    if bottom.jacobi_symbol(-1, R) != -1:
        raise AssertionError("control lacks the negative target phase")
    if bottom.jacobi_symbol(4, R) != 1:
        raise AssertionError("quadratic character did not fix the square 4")
    candidates = same_chart_b1_candidates(prime, R)
    if candidates:
        raise AssertionError(f"unexpected same-chart B=1 candidates: {candidates}")
    return {
        "p": prime,
        "R": R,
        "K": K,
        "K_factors": factors,
        "required_C_residue": (-pow(4, -1, R)) % R,
        "candidates": candidates,
    }


def verify() -> None:
    controls = (
        (73, 7),
        (1009, 7),
        (1801, 7),
        (241, 3),
    )
    receipts = [verify_control(prime, R) for prime, R in controls]
    if receipts[2]["K_factors"] != {2: 4, 197: 1}:
        raise AssertionError("p=1801 factorization receipt changed")
    if receipts[2]["required_C_residue"] != 5:
        raise AssertionError("R=7 residue changed")
    if receipts[3]["K_factors"] != {181: 1}:
        raise AssertionError("p=241 factorization receipt changed")
    if receipts[3]["required_C_residue"] != 2:
        raise AssertionError("R=3 residue changed")
    print("verified G same-chart p-1 B=1 no-go controls")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
