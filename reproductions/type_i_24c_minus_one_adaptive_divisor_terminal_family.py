#!/usr/bin/env python3
"""Verify the adaptive d=2r Type-I selector for gaps m=24c-1."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_gap23_adaptive_divisor_terminal_selector import (
    assert_egyptian_identity,
    four_route_dispatch,
    positive_divisors,
)


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


def selector_target(modulus: int) -> int:
    """Return tau_m=-72^{-1} modulo a legal m=24c-1 gap."""
    if modulus < 3 or modulus % 24 != 23:
        raise AssertionError("selector modulus is not of the form 24c-1")
    return -pow(72, -1, modulus) % modulus


def upper_divisor_box(*, s: int, modulus: int) -> frozenset[int]:
    """Return U_m(s)={s^2/r mod m:r divides s} exactly."""
    return frozenset((s * s // divisor) % modulus for divisor in positive_divisors(s))


def verify_family_terminal(*, h: int, c: int, r: int) -> dict[str, int]:
    """Reconstruct one m=24c-1 Type-I terminal from its exact selector."""
    p = 24 * h + 1
    modulus = 24 * c - 1
    s = h + c
    x = 6 * s
    if not (1 <= c <= h and r > 0 and s % r == 0):
        raise AssertionError("gap or selector factor is not legal")
    t = s // r
    divisor = 2 * r
    target = selector_target(modulus)
    if not (
        gcd(s, modulus) == 1
        and r * t * t % modulus == target
        and target in upper_divisor_box(s=s, modulus=modulus)
        and divisor <= x // 3
        and x % divisor == 0
        and x * x % divisor == 0
        and (p * x + divisor) % modulus == 0
    ):
        raise AssertionError("adaptive 24c-1 Type-I selector failed")
    second_numerator = p * x + divisor
    third_numerator = p * (x + p * x * x // divisor)
    if second_numerator % modulus or third_numerator % modulus:
        raise AssertionError("Type-I denominator reconstruction was not integral")
    terms = (x, second_numerator // modulus, third_numerator // modulus)
    assert_egyptian_identity(p, terms)
    return {
        "p": p,
        "h": h,
        "c": c,
        "m": modulus,
        "s": s,
        "r": r,
        "t": t,
        "x": x,
        "d": divisor,
        "y": terms[1],
        "z": terms[2],
    }


def select_family_terminal(*, h: int, c: int) -> dict[str, int] | None:
    """Select the first certificate from the complete divisor box at one gap."""
    modulus = 24 * c - 1
    s = h + c
    target = selector_target(modulus)
    for r in positive_divisors(s):
        if r * (s // r) ** 2 % modulus == target:
            return verify_family_terminal(h=h, c=c, r=r)
    return None


def five_route_dispatch(*, p: int) -> dict[str, object]:
    """Append the c=2, gap-47 terminal to the established four-route order."""
    record = four_route_dispatch(p=p)
    if record["branch"] != "four_route_residual":
        return {**record, "adaptive_gap47": None}
    adaptive = select_family_terminal(h=record["h"], c=2)
    return {
        **record,
        "adaptive_gap47": adaptive,
        "branch": "gap47_adaptive_terminal" if adaptive is not None else "five_route_residual",
    }


def verify_gap47_ray() -> tuple[dict[str, int], dict[str, int]]:
    """Check the base and four-route-residual controls on p=313+1128a."""
    records = []
    for a in (0, 3):
        h = 13 + 47 * a
        s = h + 2
        record = verify_family_terminal(h=h, c=2, r=s)
        if not (
            record["p"] == 313 + 1128 * a
            and record["s"] == 15 + 47 * a
            and record["d"] == 30 + 94 * a
            and record["t"] == 1
        ):
            raise AssertionError("gap-47 Dirichlet ray parameterization changed")
        records.append(record)
    if gcd(313, 1128) != 1:
        raise AssertionError("gap-47 Dirichlet ray ceased to be primitive")
    return tuple(records)


def build_result() -> dict[str, object]:
    """Verify generic m=23/47 gates and focused five-route controls."""
    m23 = verify_family_terminal(h=50, c=1, r=17)
    m47 = verify_family_terminal(h=154, c=2, r=156)
    ray0, ray3 = verify_gap47_ray()
    if not (
        selector_target(23) == 15
        and selector_target(47) == 15
        and is_prime(m23["p"])
        and is_prime(m47["p"])
        and m23["p"] == 1201
        and m23["m"] == 23
        and m47
        == {
            "p": 3697,
            "h": 154,
            "c": 2,
            "m": 47,
            "s": 156,
            "r": 156,
            "t": 1,
            "x": 936,
            "d": 312,
            "y": 73632,
            "z": 816652512,
        }
        and ray0["p"] == 313
        and ray3 == m47
    ):
        raise AssertionError("adaptive 24c-1 terminal controls changed")
    routes = {p: five_route_dispatch(p=p) for p in (313, 241, 337, 1201, 3697)}
    if not (
        routes[313]["branch"] == "r11_terminal"
        and routes[241]["branch"] == "gap7_strict_descent"
        and routes[337]["branch"] == "gap11_strict_descent"
        and routes[1201]["branch"] == "gap23_adaptive_terminal"
        and routes[3697]["branch"] == "gap47_adaptive_terminal"
        and routes[3697]["adaptive_gap47"] == m47
    ):
        raise AssertionError("five-route dispatch controls changed")
    return {
        "certificate_type": "gap_24c_minus_one_adaptive_d_2r_type_i_selector_v1",
        "scope": "Exact terminal selectors at all legal 24c-1 gaps; no universal coverage claim.",
        "gap23_control": m23,
        "gap47_four_route_residual_control": m47,
        "gap47_ray_controls": (ray0, ray3),
        "five_route_controls": routes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified adaptive 24c-1 Type-I selector and five-route controls")


if __name__ == "__main__":
    main()
