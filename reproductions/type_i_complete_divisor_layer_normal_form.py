#!/usr/bin/env python3
"""Verify the exact d|x Type-I normal form within the 24c-1 gap family."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_gap23_adaptive_divisor_terminal_selector import four_route_dispatch
from type_i_24c_minus_one_adaptive_divisor_terminal_family import seven_route_dispatch


def is_prime(value: int) -> bool:
    """Use trial division only for named control parameters."""
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
    """Return a complete positive divisor box for one control integer."""
    divisors = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        divisors.append(candidate)
        paired = value // candidate
        if paired != candidate:
            divisors.append(paired)
    return tuple(sorted(divisors))


def direct_hits(*, p: int) -> tuple[dict[str, int], ...]:
    """Exhaust all gap m=24c-1 Type-I certificates with d dividing x."""
    h = (p - 1) // 24
    records = []
    for c in range(1, h + 1):
        m = 24 * c - 1
        x = 6 * (h + c)
        for d in positive_divisors(x):
            if (p * x + d) % m == 0:
                records.append({"c": c, "m": m, "x": x, "d": d})
    return tuple(records)


def normal_form_hits(*, p: int) -> tuple[dict[str, int], ...]:
    """Reconstruct exactly the same layer using lambda=gcd(d,6)."""
    h = (p - 1) // 24
    records = []
    for c in range(1, h + 1):
        m = 24 * c - 1
        s = h + c
        for r in positive_divisors(s):
            t = s // r
            for lam in (1, 2, 3, 6):
                if gcd(r, 6 // lam) != 1:
                    continue
                if (6 * p * t + lam) % m:
                    continue
                d = lam * r
                x = 6 * s
                if not (x % d == 0 and (p * x + d) % m == 0):
                    raise AssertionError("normal-form witness was not a direct Type-I hit")
                records.append({"c": c, "m": m, "x": x, "d": d})
    return tuple(records)


def verify_direct_certificate(*, p: int, c: int, d: int) -> dict[str, int]:
    """Recover and verify one Type-I identity from a normal-form record."""
    h = (p - 1) // 24
    m = 24 * c - 1
    x = 6 * (h + c)
    y = (p * x + d) // m
    z = p * (x + p * x * x // d) // m
    if not (
        x % d == 0
        and x * x % d == 0
        and (p * x + d) % m == 0
        and p * (x + p * x * x // d) % m == 0
        and 4 * x * y * z == p * (x * y + x * z + y * z)
    ):
        raise AssertionError("direct Type-I reconstruction failed")
    lam = gcd(d, 6)
    r = d // lam
    t = x // (6 * r)
    if not (
        lam in {1, 2, 3, 6}
        and gcd(r, 6 // lam) == 1
        and (6 * p * t + lam) % m == 0
    ):
        raise AssertionError("certificate did not recover the canonical normal form")
    return {"p": p, "c": c, "m": m, "x": x, "d": d, "lam": lam, "r": r, "t": t, "y": y, "z": z}


def build_result() -> dict[str, object]:
    """Check exact layer equality, a strict extension control, and a core miss."""
    p2137_direct = direct_hits(p=2137)
    p2137_normal = normal_form_hits(p=2137)
    p2521_direct = direct_hits(p=2521)
    p2521_normal = normal_form_hits(p=2521)
    p118801_direct = direct_hits(p=118801)
    p118801_normal = normal_form_hits(p=118801)
    p2137_certificate = verify_direct_certificate(p=2137, c=1, d=45)
    if not (
        is_prime(2137)
        and p2137_direct == p2137_normal
        and p2137_direct == ({"c": 1, "m": 23, "x": 540, "d": 45}, {"c": 4, "m": 95, "x": 558, "d": 279})
        and p2137_certificate
        == {"p": 2137, "c": 1, "m": 23, "x": 540, "d": 45, "lam": 3, "r": 15, "t": 6, "y": 50175, "z": 1286687700}
        and p2521_direct == p2521_normal == ()
        and p118801_direct == p118801_normal
        and p118801_direct
        == (
            {"c": 8, "m": 191, "x": 29748, "d": 29748},
            {"c": 13, "m": 311, "x": 29778, "d": 29778},
            {"c": 82, "m": 1967, "x": 30192, "d": 444},
            {"c": 3526, "m": 84623, "x": 50856, "d": 52},
        )
        and four_route_dispatch(p=2137)["branch"] == "four_route_residual"
        and seven_route_dispatch(p=2521)["branch"] == "seven_route_residual"
    ):
        raise AssertionError("complete d|x normal-form controls changed")
    return {
        "certificate_type": "complete_d_divides_x_type_i_normal_form_v1",
        "scope": "Exact only for the d|x Type-I layer; d|x^2 but d not dividing x is excluded.",
        "p2137_strict_extension_control": p2137_certificate,
        "p2521_double_g_seven_route_residual_miss": p2521_direct,
        "p118801_complete_layer_controls": p118801_direct,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified complete d|x Type-I normal form controls")


if __name__ == "__main__":
    main()
