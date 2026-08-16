#!/usr/bin/env python3
"""Verify the direct m=1 V-side capacity map for the c=8 source.

This is an exact one-control receipt. It does not scan source factors,
parameters, or target states.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source


def complete_excess(value: int, capacity: int) -> int:
    """Return the full excess block using the existing factor-free normalization."""
    shared = gcd(value, capacity)
    reduced = value // shared
    return gcd(value, pow(reduced, value.bit_length(), value))


def direct_m_one_capacity(s: int, prime: int) -> dict[str, int]:
    """Build the source endpoint and its a-side complete-excess capacity map."""
    data = source.source_data(s)
    p, R, K, V = data.prime, data.R, data.K, data.V
    M = K // 8
    edge = source.v_side_raw_edge(data, prime)
    a, b, layer = edge["destination"]
    h = gcd(a, M)
    Q = complete_excess(a, K)
    multiplier = lcm(M, Q) // M
    capacity = (8 * pow(multiplier, -1, p)) % p
    low_residues = {
        (-79 * candidate * pow(32 * h, -1, p)) % p
        for candidate in range(1, 8)
    }
    if not (
        p == 48 * s + 1
        and K == 8 * M
        and p * R + 1 == 4 * K
        and prime > 2 * (p - 1)
        and edge["gcd_reduction"] == 1
        and layer == 1
        and a == V // prime
        and b == R - a
        and 0 < a < b
        and source.SHARED_SUPPORT % h == 0
        and Q > 1
        and multiplier == a // h
        and gcd(multiplier, p) == 1
        and 1 <= capacity < p
        and (79 * capacity + 32 * h * prime) % p == 0
        and ((capacity < 8) == (prime % p in low_residues))
    ):
        raise AssertionError("c=8 direct m=1 V-side capacity map changed")
    return {
        "q": prime,
        "a": a,
        "h": h,
        "Q": Q,
        "multiplier": multiplier,
        "capacity": capacity,
        "low_residue_count": len(low_residues),
    }


def verify() -> None:
    source.control_receipt()
    receipt = direct_m_one_capacity(3279, 5_963_047)
    if receipt != {
        "q": 5_963_047,
        "a": 3_113_076_331_159_817,
        "h": 1,
        "Q": 3_113_076_331_159_817,
        "multiplier": 3_113_076_331_159_817,
        "capacity": 11_230,
        "low_residue_count": 7,
    }:
        raise AssertionError("stored c=8 direct m=1 capacity control changed")
    print(
        "verified q=1 zero-k c=8 direct V-side m=1 capacity map: "
        "h divides 67199 and q=5963047 gives c=11230"
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
