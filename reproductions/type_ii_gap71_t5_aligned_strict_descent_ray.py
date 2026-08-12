#!/usr/bin/env python3
"""Verify the gap-71 t=5 Type-I/Type-II terminal and strict-descent ray."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import six_route_dispatch


def is_prime(value: int) -> bool:
    """Use trial division only for the two fixed ray controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check a positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_ray(*, b: int) -> dict[str, int]:
    """Reconstruct both terminal types and the strict two-tail descent."""
    p = 19009 + 25560 * b
    n = 265 + 355 * b
    L = 53 + 71 * b
    m = 71
    x = 90 * L
    type_i_divisor = (p + m) // 60
    type_ii_divisor = 1620
    source_y = 90 * (b + 1)
    source_z = 5 * L * (b + 1)
    if not (
        p == 72 * n - m
        and n == 5 * L
        and p % 24 == 1
        and (p - 1) % (m + 1) == 0
        and n == (p + m) // (m + 1)
        and x == (p + m) // 4
        and (p * x + type_i_divisor) % m == 0
        and x * x % type_i_divisor == 0
        and type_ii_divisor <= x
        and x * x % type_ii_divisor == 0
        and (x + type_ii_divisor) % m == 0
        and (x + type_ii_divisor) // m == source_y
        and (x + x * x // type_ii_divisor) // m == source_z
    ):
        raise AssertionError("gap-71 ray certificate gates failed")
    assert_egyptian_identity(n, (x, source_y, source_z))
    assert_egyptian_identity(p, (x, p * source_y, p * source_z))
    return {
        "p": p,
        "n": n,
        "L": L,
        "m": m,
        "x": x,
        "type_i_d": type_i_divisor,
        "type_ii_d": type_ii_divisor,
        "source_y": source_y,
        "source_z": source_z,
        "lifted_y": p * source_y,
        "lifted_z": p * source_z,
    }


def build_result() -> dict[str, object]:
    """Verify symbolic identities and the R=3 G six-route-residual control."""
    base = verify_ray(b=0)
    control = verify_ray(b=20)
    if not (
        gcd(19009, 25560) == 1
        and is_prime(base["p"])
        and is_prime(control["p"])
        and base["p"] == 19009
        and base["n"] == 265
        and control
        == {
            "p": 530209,
            "n": 7365,
            "L": 1473,
            "m": 71,
            "x": 132570,
            "type_i_d": 8838,
            "type_ii_d": 1620,
            "source_y": 1890,
            "source_z": 154665,
            "lifted_y": 1002095010,
            "lifted_z": 82004774985,
        }
        and all(is_prime(value) and value % 3 == 1 for value in (13, 181))
        and six_route_dispatch(p=control["p"])["branch"] == "six_route_residual"
    ):
        raise AssertionError("gap-71 aligned descent controls changed")
    return {
        "certificate_type": "gap71_t5_type_i_type_ii_aligned_strict_descent_ray_v1",
        "scope": "An infinite strict-descent ray, not a universal G-state selector.",
        "base_control": base,
        "r3_g_six_route_residual_control": control,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified gap-71 t=5 aligned Type-I/Type-II strict-descent ray")


if __name__ == "__main__":
    main()
