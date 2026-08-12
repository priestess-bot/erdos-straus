#!/usr/bin/env python3
"""Verify the aligned m=24c-1 Type-I/Type-II strict-descent family."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import five_route_dispatch


def is_prime(value: int) -> bool:
    """Use trial division only for fixed family controls."""
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


def verify_aligned_family(*, c: int, q: int) -> dict[str, int]:
    """Build the Type-I terminal and Type-II two-tail descent at one c,q."""
    m = 24 * c - 1
    n = m * q - 8
    p = 24 * c * (n - 1) + 1
    x = 6 * c * n
    type_i_divisor = 2 * n
    type_ii_divisor = 2
    source_y = 2 * (3 * c * q - 1)
    source_z = 6 * c * n * (3 * c * q - 1)
    if not (
        c >= 1
        and q >= 1
        and p == (m + 1) * n - m
        and p % 24 == 1
        and (p - 1) % (m + 1) == 0
        and n == (p + m) // (m + 1)
        and x == (p + m) // 4
        and type_i_divisor == (p + m) // (12 * c)
        and x % type_i_divisor == 0
        and (p * x + type_i_divisor) % m == 0
        and x * x % type_ii_divisor == 0
        and (x + type_ii_divisor) % m == 0
        and (x + type_ii_divisor) // m == source_y
        and (x + x * x // type_ii_divisor) // m == source_z
    ):
        raise AssertionError("aligned gap-family certificate gates failed")
    assert_egyptian_identity(n, (x, source_y, source_z))
    assert_egyptian_identity(p, (x, p * source_y, p * source_z))
    return {
        "c": c,
        "q": q,
        "p": p,
        "n": n,
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
    """Verify the universal formulas and the R=3 G five-route-residual point."""
    c1 = verify_aligned_family(c=1, q=1)
    c2 = verify_aligned_family(c=2, q=3)
    c3 = verify_aligned_family(c=3, q=139)
    c4 = verify_aligned_family(c=4, q=2)
    primitive_steps = []
    for c in (1, 2, 3, 4):
        m = 24 * c - 1
        base = 24 * c * m - 216 * c + 1
        step = 24 * c * m
        if gcd(base, step) != 1:
            raise AssertionError("aligned family Dirichlet progression ceased to be primitive")
        primitive_steps.append({"c": c, "p_at_q_1": base, "step": step})
    if not (
        all(is_prime(record["p"]) for record in (c1, c2, c3, c4))
        and c1["p"] == 337
        and c2["p"] == 6337
        and c3
        == {
            "c": 3,
            "q": 139,
            "p": 709921,
            "n": 9861,
            "m": 71,
            "x": 177498,
            "type_i_d": 19722,
            "type_ii_d": 2,
            "source_y": 2500,
            "source_z": 221872500,
            "lifted_y": 1774802500,
            "lifted_z": 157511947072500,
        }
        and c4["p"] == 17377
        and all(is_prime(value) and value % 3 == 1 for value in (7, 13, 5851))
        and five_route_dispatch(p=c3["p"])["branch"] == "five_route_residual"
    ):
        raise AssertionError("aligned gap-family controls changed")
    return {
        "certificate_type": "aligned_gap_family_type_i_type_ii_strict_descent_v1",
        "scope": "One infinite strict-descent ray for every c; no universal G-state selector.",
        "controls": (c1, c2, c3, c4),
        "primitive_dirichlet_progressions": primitive_steps,
        "r3_g_five_route_residual_control": c3,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified aligned m=24c-1 Type-I/Type-II strict-descent family")


if __name__ == "__main__":
    main()
