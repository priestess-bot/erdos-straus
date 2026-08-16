#!/usr/bin/env python3
"""Verify two intrinsic m=1 carry obstructions for the q=1 c=8 target.

The script uses exact gcd and modular-power complete-excess normalization.
It does not search primes, factor a target, or claim source/path provenance.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction as c8


@dataclass(frozen=True)
class StructuredNode:
    name: str
    small: int
    large: int
    excess_block: int
    multiplier: int
    next_capacity: int


def complete_excess(value: int, capacity: int) -> int:
    """Return the maximal complete-excess block without factorization."""
    shared = math.gcd(value, capacity)
    reduced = value // shared
    return math.gcd(value, pow(reduced, value.bit_length(), value))


def p_adic_part(value: int, prime: int) -> int:
    """Return the exact prime-primary part of value."""
    part = 1
    while value % prime == 0:
        value //= prime
        part *= prime
    return part


def canonical_capacity(prime: int, multiplier: int) -> int:
    if math.gcd(prime, multiplier) != 1:
        raise AssertionError("structured multiplier is not p-free")
    return (8 * pow(multiplier, -1, prime)) % prime


def structured_nodes(s: int) -> tuple[StructuredNode, StructuredNode]:
    """Recompute both c=8 macro-factor nodes and their forced carries."""
    target = c8.c_eight_target(s)
    p, L, E, M, K, R = (
        target.prime,
        176 * s + 5,
        3168 * s * s + 24 * s - 1,
        target.M,
        target.K,
        target.R,
    )
    n = 132 * s + 1
    H = 1584 * s * s + 12 * s - 1
    F = 139392 * s * s + 1980 * s - 59

    small_e, large_e = E, R - E
    q_e = complete_excess(large_e, K)
    multiplier_e = math.lcm(M, q_e) // M
    c_e = canonical_capacity(p, multiplier_e)
    s_59 = p_adic_part(s, 59)

    small_l, large_l = 3 * L, R - 3 * L
    q_l = complete_excess(large_l, K)
    multiplier_l = math.lcm(M, q_l) // M
    c_l = canonical_capacity(p, multiplier_l)
    expected_l = 16 * n * H if s % 2 else n * H

    if not (
        s >= 86
        and p == 48 * s + 1
        and p * R + 1 == 4 * K
        and K == 8 * M
        and large_e == 24 * s * F
        and large_l == 16 * n * H
        and R > 2 * small_e > 0
        and R > 2 * small_l > 0
        and K % small_e == 0
        and K % small_l == 0
        and math.gcd(small_e, large_e) == 1
        and math.gcd(small_l, large_l) == 1
        and F % s == (-59) % s
        and -4 * F + (3168 * s - 45) * L == 11
        and -(168 * s + 4) * F + (7392 * s + 225) * E == 11
        and F % 11 == 7
        and math.gcd(F, 72 * L * E) == 1
        and math.gcd(F, s) == math.gcd(59, s)
        and q_e == s_59 * F
        and math.gcd(M, q_e) == s_59
        and multiplier_e == F
        and 4 * F == 242 * p * p - 319 * p - 159
        and (159 * c_e + 32) % p == 0
        and c_e > 8
        and 3 * L - 4 * n == 11
        and 24 * s * n - E == 1
        and -16 * H + (144 * s - 3) * L == 1
        and -2 * H + E == 1
        and math.gcd(n * H, M) == 1
        and q_l == expected_l
        and multiplier_l == expected_l
        and 64 * n * H == p * (278784 * s * s - 1584 * s - 127) + 63
        and (
            (63 * c_l - 32) % p == 0
            if s % 2
            else (63 * c_l - 512) % p == 0
        )
        and c_l > 8
    ):
        raise AssertionError("c=8 structured-node carry normal form changed")

    return (
        StructuredNode("E", small_e, large_e, q_e, multiplier_e, c_e),
        StructuredNode("3L", small_l, large_l, q_l, multiplier_l, c_l),
    )


def actual_c_eight_control() -> None:
    """Replay the stored prime c=8 macro control without using it as a counterexample."""
    c8.actual_c_eight_control()
    node_e, node_l = structured_nodes(3279)
    if not (
        node_e.multiplier == 1498727113033
        and node_e.next_capacity == 99979
        and node_l.multiplier == 117943862947424624
        and node_l.next_capacity == 144902
    ):
        raise AssertionError("stored prime c=8 structured-node control changed")


def parity_controls() -> None:
    """Replay one odd and one even algebraic c=8-shape control."""
    odd_e, odd_l = structured_nodes(189)
    even_e, even_l = structured_nodes(704)
    if not (
        odd_e.next_capacity == 1997
        and odd_l.next_capacity == 4465
        and even_e.next_capacity == 22741
        and even_l.next_capacity == 21464
    ):
        raise AssertionError("c=8 structured-node parity controls changed")


def verify() -> None:
    actual_c_eight_control()
    parity_controls()
    print(
        "verified q=1 zero-k c=8 structured-node carry obstruction: "
        "E and 3L multipliers both have next capacity above 8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
