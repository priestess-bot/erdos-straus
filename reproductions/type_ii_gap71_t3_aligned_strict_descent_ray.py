#!/usr/bin/env python3
"""Verify the gap-71 t=3 Type-I/Type-II terminal and strict-descent ray."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import five_route_dispatch


def is_prime(value: int) -> bool:
    """Use trial division only for the fixed R=3 G control."""
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


def verify_ray(*, a: int) -> dict[str, int]:
    """Reconstruct both terminal types and the strict two-tail descent."""
    p = 4465 + 5112 * a
    n = 63 + 71 * a
    u = 8 + 9 * a
    m = 71
    x = 18 * n
    type_i_divisor = (p + m) // 36
    type_ii_divisor = 2
    source_y = 2 * u
    source_z = 18 * n * u
    if not (
        p == 72 * n - m
        and p % 24 == 1
        and (p - 1) % (m + 1) == 0
        and n == (p + m) // (m + 1)
        and x == (p + m) // 4
        and (p * x + type_i_divisor) % m == 0
        and x * x % type_i_divisor == 0
        and x * x % type_ii_divisor == 0
        and (x + type_ii_divisor) % m == 0
        and (x + type_ii_divisor) // m == source_y
        and (x + x * x // type_ii_divisor) // m == source_z
    ):
        raise AssertionError("gap-71 t=3 ray certificate gates failed")
    assert_egyptian_identity(n, (x, source_y, source_z))
    assert_egyptian_identity(p, (x, p * source_y, p * source_z))
    return {
        "p": p,
        "n": n,
        "u": u,
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
    """Verify symbolic identities and the R=3 G five-route-residual control."""
    control = verify_ray(a=138)
    if not (
        gcd(4465, 5112) == 1
        and is_prime(control["p"])
        and control
        == {
            "p": 709921,
            "n": 9861,
            "u": 1250,
            "m": 71,
            "x": 177498,
            "type_i_d": 19722,
            "type_ii_d": 2,
            "source_y": 2500,
            "source_z": 221872500,
            "lifted_y": 1774802500,
            "lifted_z": 157511947072500,
        }
        and all(is_prime(value) and value % 3 == 1 for value in (7, 13, 5851))
        and five_route_dispatch(p=control["p"])["branch"] == "five_route_residual"
    ):
        raise AssertionError("gap-71 t=3 aligned descent control changed")
    return {
        "certificate_type": "gap71_t3_type_i_type_ii_aligned_strict_descent_ray_v1",
        "scope": "An infinite strict-descent ray, not a universal G-state selector.",
        "r3_g_five_route_residual_control": control,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified gap-71 t=3 aligned Type-I/Type-II strict-descent ray")


if __name__ == "__main__":
    main()
