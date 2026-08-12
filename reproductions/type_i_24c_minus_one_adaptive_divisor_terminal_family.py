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


def diagonal_n_bridge(*, h: int, c: int) -> dict[str, int | bool]:
    """Verify that the r=s selector is equivalent to m dividing (3p+1)/4."""
    p = 24 * h + 1
    modulus = 24 * c - 1
    s = h + c
    x = 6 * s
    N = (3 * p + 1) // 4
    if not (1 <= c <= h and gcd(8 * s, modulus) == 1):
        raise AssertionError("diagonal bridge parameters were not legal")
    terminal_gate = (p * x + 2 * s) % modulus == 0
    divisor_gate = N % modulus == 0
    if not (
        p * x + 2 * s == 8 * s * N
        and terminal_gate == divisor_gate
        and (72 * s + 1 - 3 * modulus) == 4 * N
    ):
        raise AssertionError("diagonal N-divisor bridge failed")
    return {"p": p, "h": h, "c": c, "m": modulus, "s": s, "N": N, "hit": terminal_gate}


def t3_affine_bridge(*, h: int, c: int) -> dict[str, int | bool]:
    """Verify that t=3 is equivalent to m dividing 9p+1."""
    p = 24 * h + 1
    modulus = 24 * c - 1
    s = h + c
    x = 6 * s
    if not (1 <= c <= h and s % 3 == 0):
        raise AssertionError("t=3 bridge parameters were not legal")
    r = s // 3
    divisor = 2 * r
    factor = 2 * s // 3
    terminal_gate = (p * x + divisor) % modulus == 0
    affine_gate = (9 * p + 1) % modulus == 0
    if not (
        gcd(factor, modulus) == 1
        and p * x + divisor == factor * (9 * p + 1)
        and terminal_gate == affine_gate
    ):
        raise AssertionError("t=3 affine bridge failed")
    return {
        "p": p,
        "h": h,
        "c": c,
        "m": modulus,
        "s": s,
        "r": r,
        "d": divisor,
        "hit": terminal_gate,
    }


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
    diagonal_p337 = diagonal_n_bridge(h=14, c=1)
    diagonal_p3697 = diagonal_n_bridge(h=154, c=2)
    off_diagonal_p1201 = diagonal_n_bridge(h=50, c=1)
    t3_p1201 = t3_affine_bridge(h=50, c=1)
    t3_p364417 = t3_affine_bridge(h=15184, c=2)
    r3_g_control_divisors = positive_divisors(181)
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
        and diagonal_p337 == {"p": 337, "h": 14, "c": 1, "m": 23, "s": 15, "N": 253, "hit": True}
        and diagonal_p3697 == {"p": 3697, "h": 154, "c": 2, "m": 47, "s": 156, "N": 2773, "hit": True}
        and off_diagonal_p1201 == {"p": 1201, "h": 50, "c": 1, "m": 23, "s": 51, "N": 901, "hit": False}
        and t3_p1201 == {"p": 1201, "h": 50, "c": 1, "m": 23, "s": 51, "r": 17, "d": 34, "hit": True}
        and t3_p364417
        == {"p": 364417, "h": 15184, "c": 2, "m": 47, "s": 15186, "r": 5062, "d": 10124, "hit": True}
        and is_prime(273313)
        and 273313 % 3 == 1
        and four_route_dispatch(p=364417)["branch"] == "four_route_residual"
        and all(divisor % 3 == 1 for divisor in r3_g_control_divisors)
        and not any(divisor % 24 == 23 for divisor in r3_g_control_divisors)
    ):
        raise AssertionError("adaptive 24c-1 terminal controls changed")
    routes = {p: five_route_dispatch(p=p) for p in (313, 241, 337, 1201, 3697, 364417)}
    if not (
        routes[313]["branch"] == "r11_terminal"
        and routes[241]["branch"] == "gap7_strict_descent"
        and routes[337]["branch"] == "gap11_strict_descent"
        and routes[1201]["branch"] == "gap23_adaptive_terminal"
        and routes[3697]["branch"] == "gap47_adaptive_terminal"
        and routes[3697]["adaptive_gap47"] == m47
        and routes[364417]["branch"] == "gap47_adaptive_terminal"
        and routes[364417]["adaptive_gap47"]["r"] == 5062
        and routes[364417]["adaptive_gap47"]["t"] == 3
    ):
        raise AssertionError("five-route dispatch controls changed")
    return {
        "certificate_type": "gap_24c_minus_one_adaptive_d_2r_type_i_selector_v1",
        "scope": "Exact terminal selectors at all legal 24c-1 gaps; no universal coverage claim.",
        "gap23_control": m23,
        "gap47_four_route_residual_control": m47,
        "gap47_ray_controls": (ray0, ray3),
        "diagonal_n_divisor_bridge_controls": (diagonal_p337, diagonal_p3697, off_diagonal_p1201),
        "t3_affine_bridge_controls": (t3_p1201, t3_p364417),
        "t3_r3_g_control": {"p": 364417, "N3": 273313, "N3_factors": ((273313, 1),)},
        "r3_g_diagonal_boundary_control": {"p": 241, "N": 181, "divisors": r3_g_control_divisors},
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
