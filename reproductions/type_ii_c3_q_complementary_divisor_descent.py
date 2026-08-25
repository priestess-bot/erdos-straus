#!/usr/bin/env python3
"""Verify the c=3 q-complementary-divisor Type II terminal construction.

For p = 24h + 1 and a divisor r | q = 2h + 1 with r = 7 (mod 11),
the verifier constructs both the direct Type II certificate for 4/p and the
strict two-tail descent certificate for 4/q.  It is intentionally local:
it does not scan primes, modify selector state, or claim coverage outside the
declared input tuple.
"""

from __future__ import annotations

import argparse
from math import isqrt


def is_prime(value: int) -> bool:
    """Small deterministic primality check for fixed verifier controls."""
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


def assert_egyptian_identity(numerator: int, denominator: int, terms: tuple[int, int, int]) -> None:
    """Check numerator / denominator equals the three displayed unit fractions."""
    first, second, third = terms
    if min(first, second, third) <= 0:
        raise AssertionError("unit-fraction denominator was nonpositive")
    if numerator * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("Egyptian-fraction identity failed")


def verify_q_complementary_divisor_descent(*, p: int, h: int, r: int) -> dict[str, object]:
    """Construct and replay the Type II terminal and its strict descent."""
    if p != 24 * h + 1 or not is_prime(p) or p % 24 != 1:
        raise AssertionError("input is not a core prime p = 24h + 1")

    q = 2 * h + 1
    if q <= 0 or q % r or r % 11 != 7:
        raise AssertionError("r is not an eligible q divisor")

    d = q // r
    c_numerator = 3 * r + 1
    if c_numerator % 11:
        raise AssertionError("r = 7 (mod 11) did not produce an integer c")
    c = c_numerator // 11
    x = 3 * q

    if p != 12 * q - 11 or x != (p + 11) // 4:
        raise AssertionError("fixed-gap Type II chart changed")
    if x + d != 11 * c * d or x * x % d:
        raise AssertionError("Type II divisibility conditions failed")

    terminal = (x, p * c * d, 3 * p * c * q)
    descent = (x, c * d, 3 * c * q)
    assert_egyptian_identity(4, p, terminal)
    assert_egyptian_identity(4, q, descent)
    if q >= p:
        raise AssertionError("descent target was not strict")

    return {
        "p": p,
        "h": h,
        "q": q,
        "r": r,
        "d": d,
        "c": c,
        "type_ii_parameters": {"m": 11, "x": x},
        "terminal_denominators": list(terminal),
        "descent_target": q,
        "descent_denominators": list(descent),
        "strict_descent": q < p,
    }


CONTROLS = (
    {
        "name": "r7_original_c3_branch",
        "p": 73,
        "h": 3,
        "r": 7,
        "terminal": (21, 146, 3066),
        "descent": (21, 2, 42),
    },
    {
        "name": "r29_complementary_factor_ray",
        "p": 5209,
        "h": 217,
        "r": 29,
        "terminal": (1305, 625080, 54381960),
        "descent": (1305, 120, 10440),
    },
)


def build_result() -> dict[str, object]:
    """Replay the two fixed theorem controls without a coverage scan."""
    controls: list[dict[str, object]] = []
    for control in CONTROLS:
        receipt = verify_q_complementary_divisor_descent(
            p=int(control["p"]),
            h=int(control["h"]),
            r=int(control["r"]),
        )
        if tuple(receipt["terminal_denominators"]) != control["terminal"]:
            raise AssertionError(f"{control['name']}: terminal formula changed")
        if tuple(receipt["descent_denominators"]) != control["descent"]:
            raise AssertionError(f"{control['name']}: descent formula changed")
        controls.append({"name": control["name"], "receipt": receipt})

    return {
        "certificate_type": "c3_q_complementary_divisor_type_ii_v1",
        "scope": (
            "Two fixed constructive controls only. This is a terminal-first "
            "certificate/descent verifier, not a factor search or coverage claim."
        ),
        "controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified c=3 q-complementary-divisor controls: r=7,29")
        return
    print(result)


if __name__ == "__main__":
    main()
