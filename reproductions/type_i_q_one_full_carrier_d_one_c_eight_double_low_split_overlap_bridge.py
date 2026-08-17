#!/usr/bin/env python3
"""Verify the c=8 double-low split overlap bridge.

The checks are symbolic/fixed-constant only. They do not scan source
parameters, primes, factors of V, or terminal menus.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source
from type_i_q_one_full_carrier_d_one_c_eight_v_side_direct_m_one_capacity_map import (
    complete_excess,
)


# The q_star=103 CRT lower rows from the odd-carry-ray claim.
DEFECT_MINIMUM_PRIMES = (
    (1, 4_129),
    (11, 14_017),
    (41, 58_513),
    (149, 632_017),
    (451, 666_625),
    (1_639, 2_841_985),
    (6_109, 4_315_297),
    (67_199, 245_938_465),
)


def v2(value: int) -> int:
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def split_receipt(s: int, raw_prime: int) -> dict[str, int]:
    """Recompute the bridge on a stored actual high-q raw receipt."""
    data = source.source_data(s)
    p, K, M = data.prime, data.K, data.K // 8
    edge = source.v_side_raw_edge(data, raw_prime)
    a, b, layer = edge["destination"]
    q_a = complete_excess(a, K)
    q_b = complete_excess(b, K)
    t_a = lcm(M, q_a) // M
    t_b = lcm(M, q_b) // M
    defect = gcd(a, M)
    complement_overlap = gcd(b, M)
    epsilon = v2(b) - v2(M)
    epsilon = epsilon if 0 < epsilon <= 3 else 0
    overlap_weight = (1 << epsilon) * complement_overlap
    direct_capacity = (8 * pow(t_a, -1, p)) % p
    split_capacity = (8 * pow(t_a * t_b, -1, p)) % p

    if not (
        layer == 1
        and raw_prime > 2 * (p - 1)
        and t_a == a // defect
        and t_b == b // overlap_weight
        and gcd(defect, complement_overlap) == 1
        and (79 * direct_capacity + 32 * defect * raw_prime) % p == 0
        and (79 * t_b * split_capacity + 32 * defect * raw_prime) % p == 0
        and (
            (79 * direct_capacity - 32 * defect) * split_capacity
            - 4 * overlap_weight * direct_capacity * direct_capacity
        )
        % p
        == 0
    ):
        raise AssertionError("c=8 split-overlap bridge changed")

    return {
        "p": p,
        "defect": defect,
        "direct_capacity": direct_capacity,
        "split_capacity": split_capacity,
        "complement_overlap": complement_overlap,
        "epsilon": epsilon,
        "overlap_weight": overlap_weight,
    }


def small_capacity_bounds() -> tuple[tuple[int, int, int], ...]:
    """Certify |(79c-32D)C|<p on every q_star=103 defect row."""
    rows = []
    for defect, minimum_prime in DEFECT_MINIMUM_PRIMES:
        maximum = max(
            abs((79 * direct_capacity - 32 * defect) * split_capacity)
            for direct_capacity in range(1, 8)
            for split_capacity in range(1, 8)
        )
        if maximum >= minimum_prime:
            raise AssertionError("double-low quotient is no longer smaller than p")
        rows.append((defect, minimum_prime, maximum))
    return tuple(rows)


def zero_carry_menu() -> tuple[tuple[int, int, int, int], ...]:
    """Enumerate the fixed eight-by-seven-by-seven k=0 equation."""
    candidates = []
    for defect, _ in DEFECT_MINIMUM_PRIMES:
        for direct_capacity in range(1, 8):
            for split_capacity in range(1, 8):
                numerator = (79 * direct_capacity - 32 * defect) * split_capacity
                denominator = 4 * direct_capacity * direct_capacity
                if numerator > 0 and numerator % denominator == 0:
                    overlap_weight = numerator // denominator
                    if gcd(defect, overlap_weight) == 1:
                        candidates.append(
                            (defect, direct_capacity, split_capacity, overlap_weight)
                        )
    return tuple(candidates)


def verify() -> None:
    rows = small_capacity_bounds()
    if rows != (
        (1, 4_129, 3_647),
        (11, 14_017, 1_911),
        (41, 58_513, 8_631),
        (149, 632_017, 32_823),
        (451, 666_625, 100_471),
        (1_639, 2_841_985, 366_583),
        (6_109, 4_315_297, 1_367_863),
        (67_199, 245_938_465, 15_052_023),
    ):
        raise AssertionError("c=8 q_star=103 double-low threshold table changed")
    if zero_carry_menu() != ((1, 1, 4, 47),):
        raise AssertionError("c=8 double-low zero-carry menu changed")

    first = split_receipt(116, 578_581)
    second = split_receipt(3279, 5_963_047)
    if first != {
        "p": 5_569,
        "defect": 11,
        "direct_capacity": 4_202,
        "split_capacity": 5_291,
        "complement_overlap": 12,
        "epsilon": 0,
        "overlap_weight": 12,
    }:
        raise AssertionError("first c=8 split-overlap control changed")
    if second != {
        "p": 157_393,
        "defect": 1,
        "direct_capacity": 11_230,
        "split_capacity": 38_261,
        "complement_overlap": 3,
        "epsilon": 1,
        "overlap_weight": 6,
    }:
        raise AssertionError("second c=8 split-overlap control changed")
    print(
        "verified c=8 double-low split overlap bridge: "
        "eight bounded quotient rows, unique k=0 marker (D,c,C,u)=(1,1,4,47), "
        "and two actual high-q controls"
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
