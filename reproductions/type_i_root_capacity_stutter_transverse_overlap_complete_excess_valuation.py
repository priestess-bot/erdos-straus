#!/usr/bin/env python3
"""Verify q-primary complete-excess alternatives for transverse overlaps."""

from __future__ import annotations

import argparse
from math import gcd


def valuation(value: int, prime: int) -> int:
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


def canonical_primary(
    branch: str, q: int, b: int, tau: int, zeta: int
) -> tuple[int, int, int]:
    c = q**b
    t_value = q**tau
    a = (q**b if branch == "plus" else 1) * t_value
    k = c * t_value
    z = q**zeta
    q_block = z if zeta > valuation(k, q) else 1
    beta = z // q_block
    e = q_block // gcd(a, q_block)
    d = beta * gcd(a, q_block)
    if e * d != z or k % d:
        raise AssertionError("canonical q-primary normalization failed")
    return valuation(d, q), valuation(e, q), valuation(k, q)


def verify_plus_nonexcess() -> None:
    q, b, t, tau, zeta = 5, 2, 1, 3, 3
    d_value, e_value, k_value = canonical_primary("plus", q, b, tau, zeta)
    if not (d_value == b + t and e_value == 0 and zeta <= k_value and tau >= t):
        raise AssertionError("p+1 non-excess alternative failed")


def verify_plus_excess() -> None:
    q, b, t, tau, zeta = 5, 1, 2, 2, 5
    d_value, e_value, k_value = canonical_primary("plus", q, b, tau, zeta)
    if not (
        d_value == b + t
        and tau == t
        and zeta > b + t
        and b + t == k_value
        and e_value == zeta - b - t
    ):
        raise AssertionError("p+1 complete-excess alternative failed")


def verify_minus_nonexcess() -> None:
    q, b, t, tau, zeta = 5, 1, 1, 3, 2
    d_value, e_value, k_value = canonical_primary("minus", q, b, tau, zeta)
    if not (d_value == b + t and e_value == 0 and zeta <= k_value and tau >= t):
        raise AssertionError("p-1 non-excess alternative failed")


def verify_minus_excess() -> None:
    q, b, t, tau, zeta = 5, 1, 1, 2, 5
    d_value, e_value, k_value = canonical_primary("minus", q, b, tau, zeta)
    if not (
        d_value == b + t
        and tau == b + t
        and zeta > 2 * b + t
        and 2 * b + t == k_value
        and e_value == zeta - b - t > b
    ):
        raise AssertionError("p-1 complete-excess alternative failed")


def verify_t_high_residue_locks() -> None:
    q = 5
    plus_p, plus_r = 169, 10
    plus_t = plus_p * plus_p * plus_r - (plus_p + 1) // 2
    minus_p, minus_r = 121, 21
    minus_t = minus_p * minus_p * minus_r - (minus_p + 1) // 2
    if not (
        plus_p % 24 == minus_p % 24 == 1
        and valuation(plus_p + 1, q) == valuation(plus_r, q) == 1
        and valuation(plus_t, q) == 2
        and valuation(minus_p - 1, q) == valuation(minus_r - 1, q) == 1
        and valuation(minus_t, q) == 2
    ):
        raise AssertionError("T-high residue lock failed")


def verify() -> None:
    # These are q-primary normalization and residue controls, not root receipts.
    verify_plus_nonexcess()
    verify_plus_excess()
    verify_minus_nonexcess()
    verify_minus_excess()
    verify_t_high_residue_locks()
    print("verified transverse overlap complete-excess valuation classification")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
