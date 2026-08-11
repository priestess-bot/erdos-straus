#!/usr/bin/env python3
"""Verify the exact adaptive d=2r Type-I selector at gap 23."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_r11_gap7_gap11_joint_dispatch import dispatch as three_route_dispatch


AUTOMATIC_TYPE_II_RESIDUES = {7, 10, 11, 15, 17, 19, 20, 21, 22}


def is_prime(value: int) -> bool:
    """Use trial division only for fixed certificate controls."""
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


def positive_divisors(value: int) -> tuple[int, ...]:
    """Enumerate the complete divisor set of one fixed control parameter."""
    divisors = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        divisors.append(candidate)
        paired = value // candidate
        if paired != candidate:
            divisors.append(paired)
    return tuple(sorted(divisors))


def assert_egyptian_identity(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check a positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def upper_divisor_box(s: int) -> frozenset[int]:
    """Return U_23(s) = {s^2/r mod 23 : r divides s} exactly."""
    return frozenset((s * s // divisor) % 23 for divisor in positive_divisors(s))


def verify_adaptive_terminal(*, h: int, r: int) -> dict[str, int]:
    """Reconstruct one d=2r gap-23 Type-I terminal from the exact selector."""
    p = 24 * h + 1
    s = h + 1
    x = 6 * s
    if r <= 0 or s % r:
        raise AssertionError("selector factor is not a positive divisor of s")
    t = s // r
    divisor = 2 * r
    if not (
        p % 24 == 1
        and p % 23 != 0
        and r * t * t % 23 == 15
        and divisor <= x // 3
        and x % divisor == 0
        and x * x % divisor == 0
        and (p * x + divisor) % 23 == 0
        and 15 in upper_divisor_box(s)
    ):
        raise AssertionError("adaptive gap-23 Type-I selector failed")
    second_numerator = p * x + divisor
    third_numerator = p * (x + p * x * x // divisor)
    if second_numerator % 23 or third_numerator % 23:
        raise AssertionError("Type-I denominator reconstruction was not integral")
    terms = (x, second_numerator // 23, third_numerator // 23)
    assert_egyptian_identity(p, terms)
    return {
        "p": p,
        "h": h,
        "s": s,
        "r": r,
        "t": t,
        "x": x,
        "d": divisor,
        "y": terms[1],
        "z": terms[2],
    }


def select_adaptive_terminal(*, h: int) -> dict[str, int] | None:
    """Select the first certificate from the complete divisor box of s."""
    s = h + 1
    for r in positive_divisors(s):
        if r * (s // r) ** 2 % 23 == 15:
            return verify_adaptive_terminal(h=h, r=r)
    return None


def four_route_dispatch(*, p: int) -> dict[str, object]:
    """Append the direct gap-23 terminal to the established three-route order."""
    record = three_route_dispatch(p=p)
    if record["branch"] != "joint_residual":
        return {**record, "adaptive_gap23": None}
    adaptive = select_adaptive_terminal(h=record["h"])
    return {
        **record,
        "adaptive_gap23": adaptive,
        "branch": "gap23_adaptive_terminal" if adaptive is not None else "four_route_residual",
    }


def verify_cofactor_three_ray() -> tuple[dict[str, int], dict[str, int]]:
    """Check two controls of p=1201+1656a, including its new a=1 point."""
    records = []
    for a in (0, 1):
        r = 17 + 23 * a
        h = 50 + 69 * a
        record = verify_adaptive_terminal(h=h, r=r)
        if not (
            record["s"] == 3 * r
            and record["t"] == 3
            and record["p"] == 1201 + 1656 * a
            and record["d"] == 34 + 46 * a
        ):
            raise AssertionError("cofactor-three ray parameterization changed")
        records.append(record)
    if gcd(1201, 1656) != 1:
        raise AssertionError("cofactor-three Dirichlet ray ceased to be primitive")
    return tuple(records)


def build_result() -> dict[str, object]:
    """Verify symbolic gates and branch controls without a coverage scan."""
    p337 = verify_adaptive_terminal(h=14, r=15)
    p1201 = verify_adaptive_terminal(h=50, r=17)
    ray0, ray1 = verify_cofactor_three_ray()
    if not (
        is_prime(p337["p"])
        and is_prime(p1201["p"])
        and is_prime(ray1["p"])
        and p337["p"] == 337
        and p337["d"] == 30
        and p1201
        == {"p": 1201, "h": 50, "s": 51, "r": 17, "t": 3, "x": 306, "d": 34, "y": 15980, "z": 172727820}
        and ray1
        == {"p": 2857, "h": 119, "s": 120, "r": 40, "t": 3, "x": 720, "d": 80, "y": 89440, "z": 2299770720}
        and 17 not in positive_divisors(ray1["s"])
        and ray1["p"] % 23 not in AUTOMATIC_TYPE_II_RESIDUES
    ):
        raise AssertionError("adaptive gap-23 terminal controls changed")
    routes = {p: four_route_dispatch(p=p) for p in (313, 241, 337, 1201)}
    if not (
        routes[313]["branch"] == "r11_terminal"
        and routes[241]["branch"] == "gap7_strict_descent"
        and routes[337]["branch"] == "gap11_strict_descent"
        and routes[1201]["branch"] == "gap23_adaptive_terminal"
        and routes[1201]["adaptive_gap23"] == p1201
    ):
        raise AssertionError("four-route dispatch controls changed")
    return {
        "certificate_type": "gap23_adaptive_d_2r_type_i_terminal_selector_v1",
        "scope": "Exact divisor selector and one additional terminal branch; no universal coverage claim.",
        "p337_nonfixed_control": p337,
        "p1201_joint_residual_control": p1201,
        "cofactor_three_ray_controls": (ray0, ray1),
        "four_route_controls": routes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified adaptive gap-23 Type-I selector and four-route controls")


if __name__ == "__main__":
    main()
