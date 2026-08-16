#!/usr/bin/env python3
"""Verify high-q shared-defect rigidity for the c=8 source.

The check evaluates four fixed source parameters and one stored raw receipt.
It does not scan parameters, prime factors, endpoints, or certificate menus.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source


SHARED_RESIDUES = ((11, 6), (41, 30), (149, 55))


def defect_from_residues(s: int) -> int:
    """Return the exact shared defect specified by the three fixed residue rows."""
    result = 1
    for prime, residue in SHARED_RESIDUES:
        if s % prime == residue:
            result *= prime
    return result


def source_defect(s: int) -> int:
    """Recompute D_s from the source normal form and its fixed residue formula."""
    data = source.source_data(s)
    support = data.K // 8
    defect = gcd(data.V, support)
    if not (
        data.V % 2 == 1
        and defect == gcd(data.V, data.K)
        and defect == defect_from_residues(s)
        and source.SHARED_SUPPORT % defect == 0
    ):
        raise AssertionError("c=8 source defect formula changed")
    return defect


def low_gate_residues(prime: int, defect: int) -> tuple[int, ...]:
    """Return the seven fixed low-capacity q residues for one source defect."""
    inverse = pow(32 * defect, -1, prime)
    residues = tuple((-79 * capacity * inverse) % prime for capacity in range(1, 8))
    if len(set(residues)) != 7:
        raise AssertionError("low-gate residues unexpectedly collided")
    return residues


def nontrivial_high_q_control() -> dict[str, int]:
    """Replay a fixed D_s=11 raw edge and its endpoint support separation."""
    data = source.source_data(116)
    q = 578_581
    edge = source.v_side_raw_edge(data, q)
    a, b, layer = edge["destination"]
    support = data.K // 8
    defect = source_defect(data.s)
    h = gcd(a, support)
    g_b = gcd(b, support)
    multiplier = a // h
    capacity = (8 * pow(multiplier, -1, data.prime)) % data.prime
    if not (
        source.is_prime(data.prime)
        and data.prime % 24 == 1
        and data.prime == 5_569
        and q > 2 * (data.prime - 1)
        and edge["gcd_reduction"] == 1
        and layer == 1
        and a + b == data.R
        and gcd(a, b) == 1
        and q * a == data.V
        and gcd(q, support) == 1
        and defect == 11
        and h == defect
        and gcd(defect, g_b) == 1
        and g_b == 12
        and multiplier == 4_569_010_345
        and capacity == 4_202
        and (79 * capacity + 32 * defect * q) % data.prime == 0
        and q % data.prime not in low_gate_residues(data.prime, defect)
    ):
        raise AssertionError("nontrivial c=8 high-q defect control changed")
    return {
        "defect": defect,
        "h": h,
        "g_b": g_b,
        "capacity": capacity,
    }


def verify() -> None:
    expected_defects = {86: 1, 112: 41, 116: 11, 353: 149, 358: 451}
    if {s: source_defect(s) for s in expected_defects} != expected_defects:
        raise AssertionError("fixed c=8 shared-defect controls changed")
    if nontrivial_high_q_control() != {
        "defect": 11,
        "h": 11,
        "g_b": 12,
        "capacity": 4_202,
    }:
        raise AssertionError("stored high-q defect receipt changed")
    print(
        "verified c=8 high-q shared-defect rigidity: "
        "h=D_s, D_s is disjoint from the complementary overlap, and each source has seven low gates"
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
