#!/usr/bin/env python3
"""Verify the c=8 low-gate complementary p-free and split interface.

This is a finite constant-factor check plus one exact raw-source control. It
does not scan primes, c=8 parameters, endpoints, or certificate menus.
"""

from __future__ import annotations

import argparse
from math import gcd, lcm

import type_i_q_one_full_carrier_d_one_c_eight_universal_source_non_p_separation as source
from type_i_q_one_full_carrier_d_one_c_eight_v_side_direct_m_one_capacity_map import (
    complete_excess,
)


def divisors(value: int) -> list[int]:
    result = [1]
    factor = 2
    remaining = value
    while factor * factor <= remaining:
        if remaining % factor:
            factor += 1
            continue
        power = 1
        while remaining % factor == 0:
            remaining //= factor
            power *= factor
        result = [
            item * factor_power
            for item in result
            for factor_power in _powers(power, factor)
        ]
        factor += 1
    if remaining > 1:
        result = [
            item * remaining_power
            for item in result
            for remaining_power in (1, remaining)
        ]
    return sorted(result)


def _powers(power: int, factor: int) -> tuple[int, ...]:
    values = [1]
    value = 1
    while value != power:
        value *= factor
        values.append(value)
    return tuple(values)


def prime_divisors(value: int) -> list[int]:
    """Return the distinct prime divisors of a small positive integer."""
    value = abs(value)
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor += 1 if divisor == 2 else 2
            continue
        result.append(divisor)
        while value % divisor == 0:
            value //= divisor
    if value > 1:
        result.append(value)
    return result


def low_gate_p_candidates() -> list[tuple[int, int, int, int, int]]:
    """Factor only the 56 fixed integers 32*h-79*c, never the parameter ray."""
    candidates = []
    for h in divisors(source.SHARED_SUPPORT):
        for capacity in range(1, 8):
            difference = 32 * h - 79 * capacity
            for p in prime_divisors(difference):
                if p < 4_129 or p % 48 != 1:
                    continue
                s = (p - 1) // 48
                candidates.append((h, capacity, p, s, s % 103))
    return candidates


def two_side_control() -> dict[str, int]:
    """Replay the existing terminal-preempted raw control through both colors."""
    data = source.source_data(3279)
    q = 5_963_047
    p, R, K, V = data.prime, data.R, data.K, data.V
    support = K // 8
    edge = source.v_side_raw_edge(data, q)
    a, b, layer = edge["destination"]
    q_a = complete_excess(a, K)
    q_b = complete_excess(b, K)
    beta_a, beta_b = a // q_a, b // q_b
    t_a = lcm(support, q_a) // support
    t_b = lcm(support, q_b) // support
    total_multiplier = lcm(support, q_a, q_b) // support
    capacity_a = (8 * pow(t_a, -1, p)) % p
    capacity_split = (8 * pow(total_multiplier, -1, p)) % p
    h = gcd(a, support)
    if not (
        p == 157_393
        and q > 2 * (p - 1)
        and edge["gcd_reduction"] == 1
        and layer == 1
        and a + b == R
        and gcd(a, b) == 1
        and q * a == V
        and a % p != 0
        and b % p != 0
        and q_a > 1
        and q_b > 1
        and gcd(q_a, q_b) == 1
        and K % (beta_a * beta_b) == 0
        and q_a % p != 0
        and q_b % p != 0
        and t_a == a // h
        and total_multiplier == t_a * t_b
        and (79 * capacity_a + 32 * h * q) % p == 0
        and (79 * t_b * capacity_split + 32 * h * q) % p == 0
    ):
        raise AssertionError("c=8 complementary split control changed")
    return {
        "q_a": q_a,
        "q_b": q_b,
        "t_a": t_a,
        "t_b": t_b,
        "total_multiplier": total_multiplier,
        "capacity_a": capacity_a,
        "capacity_split": capacity_split,
    }


def verify() -> None:
    if divisors(source.SHARED_SUPPORT) != [1, 11, 41, 149, 451, 1639, 6109, 67199]:
        raise AssertionError("shared-support divisor menu changed")
    if low_gate_p_candidates() != [(1639, 1, 52_369, 1091, 61)]:
        raise AssertionError("low-gate p-primary exclusion certificate changed")
    if any(s_mod_103 == 86 for _, _, _, _, s_mod_103 in low_gate_p_candidates()):
        raise AssertionError("a c=8 q_star=103 low gate can carry p on the complement")
    receipt = two_side_control()
    if receipt != {
        "q_a": 3_113_076_331_159_817,
        "q_b": 19_138_464_436_332_689,
        "t_a": 3_113_076_331_159_817,
        "t_b": 19_138_464_436_332_689,
        "total_multiplier": 59_579_500_651_491_202_538_305_440_357_913,
        "capacity_a": 11_230,
        "capacity_split": 38_261,
    }:
        raise AssertionError("stored two-sided c=8 control changed")
    print(
        "verified c=8 low-gate complementary p-free exclusion: "
        "only p=52369 candidate has s=1091 not 86 mod 103"
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
