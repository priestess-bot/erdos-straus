#!/usr/bin/env python3
"""Verify complete d=2r family misses at focused core controls."""

from __future__ import annotations

import argparse
from math import isqrt

from type_i_24c_minus_one_adaptive_divisor_terminal_family import seven_route_dispatch


def is_prime(value: int) -> bool:
    """Use trial division only for the named controls."""
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


def factor(value: int) -> tuple[tuple[int, int], ...]:
    """Factor one fixed control integer by trial division."""
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return tuple(factors)


def positive_divisors(value: int) -> tuple[int, ...]:
    """Return the complete positive divisor set of a control integer."""
    divisors = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        divisors.append(candidate)
        paired = value // candidate
        if paired != candidate:
            divisors.append(paired)
    return tuple(sorted(divisors))


def all_d2r_hits(*, p: int) -> tuple[dict[str, int], ...]:
    """Exhaust the full legal (c,r) family, not a bounded c/t sub-menu."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime")
    h = (p - 1) // 24
    hits = []
    for c in range(1, h + 1):
        modulus = 24 * c - 1
        s = h + c
        for r in positive_divisors(s):
            t = s // r
            divisor = 2 * r
            x = 6 * s
            if (p * x + divisor) % modulus == 0:
                if not (x * x % divisor == 0 and divisor <= x // 3):
                    raise AssertionError("recorded d=2r witness was not legal")
                hits.append({"c": c, "m": modulus, "s": s, "r": r, "t": t, "d": divisor})
    return tuple(hits)


def build_result() -> dict[str, object]:
    """Check the complete family at double-G controls without a range audit."""
    p73_hits = all_d2r_hits(p=73)
    p241_hits = all_d2r_hits(p=241)
    p2521_hits = all_d2r_hits(p=2521)
    p118801_hits = all_d2r_hits(p=118801)
    N3 = (3 * 2521 + 1) // 4
    X = (2521 + 3) // 4
    if not (
        p73_hits == ()
        and p241_hits == ()
        and p2521_hits == ()
        and p118801_hits == ({"c": 3526, "m": 84623, "s": 8476, "r": 26, "t": 326, "d": 52},)
        and factor(N3) == ((31, 1), (61, 1))
        and factor(X) == ((631, 1),)
        and all(prime % 3 == 1 for prime, _ in factor(N3) + factor(X))
        and seven_route_dispatch(p=2521)["branch"] == "seven_route_residual"
    ):
        raise AssertionError("complete d=2r family boundary controls changed")
    return {
        "certificate_type": "complete_d2r_adaptive_type_i_family_boundary_v1",
        "scope": "Exact only for the named primes; no claim about the full core-prime population.",
        "p73_non_g_miss": p73_hits,
        "p241_double_g_miss": p241_hits,
        "p2521_double_g_seven_route_residual_miss": p2521_hits,
        "p118801_double_g_hit": p118801_hits,
        "p2521_r3_data": {"N3": N3, "N3_factors": factor(N3), "X": X, "X_factors": factor(X)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified complete d=2r adaptive family boundary controls")


if __name__ == "__main__":
    main()
