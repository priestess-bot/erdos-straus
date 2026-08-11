#!/usr/bin/env python3
"""Verify the R=11 adaptive-divisor Type I terminal family.

The verifier checks one symbolic construction and three fixed controls.  It
does not scan primes or claim coverage outside the stated divisor condition.
"""

from __future__ import annotations

import argparse
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    """Use trial division only for the three fixed control primes."""
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
    """Check one positive three-unit-fraction identity exactly."""
    first, second, third = terms
    if min(terms) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_adaptive_divisor_terminal(*, p: int, divisor: int) -> dict[str, int]:
    """Construct the terminal from one actual 8 mod 11 divisor."""
    if not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime")
    h = (p - 1) // 24
    numerator = 22 * h + 1
    if divisor <= 0 or numerator % divisor or divisor % 11 != 8:
        raise AssertionError("adaptive R=11 divisor condition failed")
    companion = numerator // divisor
    K = 3 * numerator
    factor = 3 * companion + 1
    if (divisor * companion) % 11 != 1 or factor % 11:
        raise AssertionError("mod-11 integrality gate failed")

    u = divisor * factor // 11
    v = 3 * divisor * companion * factor // 11
    terminal = (u, v, p * K)
    if not (
        K == (11 * p + 1) // 4
        and 11 * p + 1 == 4 * K
        and K % divisor == 0
        and divisor % 11 == (-K) % 11
        and 11 * u - K == divisor
        and 11 * v - K == K * K // divisor
        and (11 * u - K) * (11 * v - K) == K * K
        and u < v < p * K
    ):
        raise AssertionError("R=11 fixed-tail factorization changed")
    assert_egyptian_identity(p, terminal)
    return {
        "p": p,
        "h": h,
        "r": divisor,
        "s": companion,
        "K": K,
        "u": u,
        "v": v,
        "third_denominator": p * K,
    }


def verify_dirichlet_ray(*, divisor: int) -> dict[str, int]:
    """Check the primitive progression attached to one allowed divisor."""
    if divisor <= 1 or divisor % 2 == 0 or divisor % 11 != 8 or gcd(divisor, 22) != 1:
        raise AssertionError("ray divisor must be an odd 8 mod 11 unit")
    h0 = (-pow(22, -1, divisor)) % divisor
    p0 = 24 * h0 + 1
    step = 24 * divisor
    if not (0 < h0 < divisor and (22 * h0 + 1) % divisor == 0 and gcd(p0, step) == 1):
        raise AssertionError("Dirichlet progression ceased to be primitive")
    return {"r": divisor, "h0": h0, "p0": p0, "step": step}


CONTROLS = (
    (313, 41),
    (601, 19),
    (1993, 63),
)


def build_result() -> dict[str, object]:
    """Return terminal and progression receipts without a coverage scan."""
    terminals = [verify_adaptive_divisor_terminal(p=p, divisor=r) for p, r in CONTROLS]
    rays = [verify_dirichlet_ray(divisor=r) for r in (19, 41, 63)]
    if terminals[0]["third_denominator"] != 269493:
        raise AssertionError("p=313 control changed")
    if terminals[1]["third_denominator"] != 993453:
        raise AssertionError("p=601 control changed")
    if terminals[2]["third_denominator"] != 10923633:
        raise AssertionError("p=1993 control changed")
    return {
        "certificate_type": "r11_adaptive_8_mod_11_divisor_terminal_v1",
        "scope": (
            "Every core prime whose 22h+1 has a divisor congruent to 8 modulo 11; "
            "the terminal is direct and does not assert global coverage."
        ),
        "terminal_controls": terminals,
        "primitive_dirichlet_rays": rays,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified R=11 adaptive-divisor Type I terminal controls")


if __name__ == "__main__":
    main()
