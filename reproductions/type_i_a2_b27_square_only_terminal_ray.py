#!/usr/bin/env python3
"""Verify the square-only (A,B)=(2,27) Type-I terminal family."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import seven_route_dispatch
from type_i_complete_divisor_layer_normal_form import direct_hits


def is_prime(value: int) -> bool:
    """Use trial division only for the two named ray controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def certificate(*, p: int, c: int) -> dict[str, int] | None:
    """Construct this family on one gap, or return None outside its selector."""
    if not (is_prime(p) and p % 24 == 1):
        raise ValueError("p must be a core prime")
    h = (p - 1) // 24
    if not 1 <= c <= h:
        raise ValueError("c is outside the natural gap range")
    m = 24 * c - 1
    s = h + c
    if s % 9 or (27 * p + 2) % m:
        return None
    C = s // 9
    x = 54 * C
    d = 4 * C
    y = (p * x + d) // m
    z = p * (x + p * x * x // d) // m
    if not (
        x == (p + m) // 4
        and x * x % d == 0
        and x % d != 0
        and (p * x + d) % m == 0
        and gcd(2 * C, m) == 1
        and 4 * x * y * z == p * (x * y + x * z + y * z)
    ):
        raise AssertionError("Type-I reconstruction failed")
    g = gcd(d, x)
    A, B, recovered_C = d // g, x // g, g // (d // g)
    if (A, B, recovered_C) != (2, 27, C):
        raise AssertionError("wrong coprime normal form")
    return {
        "p": p,
        "c": c,
        "m": m,
        "s": s,
        "C": C,
        "x": x,
        "d": d,
        "A": A,
        "B": B,
        "y": y,
        "z": z,
    }


def factor_selector(*, p: int) -> tuple[dict[str, int], ...]:
    """Recover this entire family from eligible divisors of 27p+2."""
    if not (is_prime(p) and p % 24 == 1):
        raise ValueError("p must be a core prime")
    target = 27 * p + 2
    records = []
    for trial in range(1, isqrt(target) + 1):
        if target % trial:
            continue
        for m in {trial, target // trial}:
            if not (23 <= m <= p - 2 and (p + m) % 216 == 0):
                continue
            c = (m + 1) // 24
            record = certificate(p=p, c=c)
            if record is None or record["m"] != m:
                raise AssertionError("factor selector and gap selector disagree")
            records.append(record)
    return tuple(sorted(records, key=lambda item: item["m"]))


def full_square_hits(*, p: int) -> tuple[dict[str, int], ...]:
    """Exhaust all gap certificates d|x^2 for the small named control only."""
    h = (p - 1) // 24
    records = []
    for c in range(1, h + 1):
        m = 24 * c - 1
        x = 6 * (h + c)
        for trial in range(1, isqrt(x * x) + 1):
            if (x * x) % trial:
                continue
            for d in {trial, x * x // trial}:
                if (p * x + d) % m == 0:
                    records.append({"c": c, "m": m, "x": x, "d": d})
    return tuple(sorted(records, key=lambda item: (item["c"], item["d"])))


def ray_prime(a: int) -> int:
    """Return the fixed-m=1583 specialization p=2521+341928a."""
    if a < 0:
        raise ValueError("a must be nonnegative")
    return 2521 + 341928 * a


def verify() -> None:
    first = certificate(p=2521, c=66)
    later = certificate(p=ray_prime(6), c=66)
    assert first == {
        "p": 2521,
        "c": 66,
        "m": 1583,
        "s": 171,
        "C": 19,
        "x": 1026,
        "d": 76,
        "A": 2,
        "B": 27,
        "y": 1634,
        "z": 55610739,
    }
    assert later == {
        "p": 2054089,
        "c": 66,
        "m": 1583,
        "s": 85653,
        "C": 9517,
        "x": 513918,
        "d": 38068,
        "A": 2,
        "B": 27,
        "y": 666856190,
        "z": 18492056520222285,
    }
    assert is_prime(2521) and is_prime(ray_prime(6))
    assert gcd(2521, 341928) == 1
    assert certificate(p=2521, c=1) is None
    assert factor_selector(p=2521) == (first,)
    assert factor_selector(p=ray_prime(6)) == (later,)
    assert direct_hits(p=2521) == ()
    assert seven_route_dispatch(p=2521)["branch"] == "seven_route_residual"
    assert full_square_hits(p=2521) == (
        {"c": 1, "m": 23, "x": 636, "d": 848},
        {"c": 66, "m": 1583, "x": 1026, "d": 76},
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    print("verified the square-only (A,B)=(2,27) Type-I terminal ray")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
