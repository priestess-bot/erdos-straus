#!/usr/bin/env python3
"""Verify fixed arithmetic controls for the H4 q0 p-free re-entry capacity map.

These are formal capacity-map controls only.  They do not assert that a listed
tuple has an actual 19-phase H4 predecessor, nor do they validate a typed or
atomic payload.
"""

from __future__ import annotations

import argparse
from math import gcd


P = 73
Q = 37
GAMMA = 1
Q0 = 37
D = 1
M4 = 4
L0 = 333
C4 = 32
N = 73
W = 37


def capacity(multiplier: int) -> int:
    return (-L0 * pow(multiplier, -1, P)) % P


def top_data(factor: int, e_zeta: int) -> tuple[int, int, int, int]:
    multiplier = factor * e_zeta
    sigma, remainder = divmod(multiplier - L0, P)
    if remainder:
        raise AssertionError("fixture is not a top-capacity control")
    n_re = N + 4 * M4 * sigma
    a_re = W // gcd(W, (n_re + 1) // 2)
    return multiplier, sigma, n_re, a_re


def verify_capacity_map() -> None:
    if C4 * pow(L0, -1, P) % P != P - 1:
        raise AssertionError("base H4 top-capacity congruence changed")

    # A p-free non-top re-entry has strictly smaller canonical capacity.
    strict_factor = GAMMA + P * 2
    strict_capacity = capacity(strict_factor)
    if strict_factor != 147 or strict_capacity != 32 or strict_capacity >= P - 1:
        raise AssertionError("strict p-free re-entry control changed")

    # The same p-free multiplier has a top-capacity target with a>1.
    high_multiplier, high_sigma, high_n, high_a = top_data(strict_factor, 41)
    if (high_multiplier, high_sigma, high_n, high_a, capacity(high_multiplier)) != (
        6027,
        78,
        1321,
        37,
        72,
    ):
        raise AssertionError("a>1 re-entry top-capacity control changed")

    # A top q-lock can remain arithmetically possible, so it must be retained.
    lock_t = 1
    lock_factor = GAMMA + P * lock_t
    lock_multiplier, lock_sigma, lock_n, lock_a = top_data(lock_factor, 41)
    if (lock_multiplier, lock_sigma, lock_n, lock_a, capacity(lock_multiplier)) != (
        3034,
        37,
        665,
        1,
        72,
    ):
        raise AssertionError("q-lock top-capacity control changed")
    if lock_sigma % Q != 0 or (lock_factor * 41) % Q != 0:
        raise AssertionError("q-lock equivalence control changed")


def verify_unitary_lock_signature() -> None:
    """Check the rho=q endpoint allocation in the retained q-lock control."""
    t = 1
    factor = GAMMA + P * t
    xi = factor * D
    rho = gcd(Q, xi)
    if rho != Q or gcd(rho, Q // rho) != 1:
        raise AssertionError("q-lock unitary allocation changed")
    if (t - GAMMA) % rho != 0:
        raise AssertionError("rho-side q-lock congruence changed")
    if Q // rho != 1:
        raise AssertionError("fixture no longer represents the rho=q branch")


def verify() -> None:
    verify_capacity_map()
    verify_unitary_lock_signature()
    print(
        "verified q0 p-free re-entry capacity map: "
        "strict, a>1 top-capacity, and retained unitary q-lock controls"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
