#!/usr/bin/env python3
"""Verify that a local transverse relay does not force the p-1 source fan."""

from __future__ import annotations

import argparse
from math import gcd, isqrt

from type_i_root_capacity_stutter_transverse_overlap_receipt_relay import (
    relay_values,
    valuation,
)


def divisors(value: int) -> list[int]:
    result: list[int] = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate:
            continue
        result.append(candidate)
        if candidate * candidate != value:
            result.append(value // candidate)
    return sorted(result)


def p_minus_one_fan_rows(p: int) -> tuple[tuple[int, int, int, int, int, int, tuple[int, ...]], ...]:
    rows = []
    for divisor in divisors(p - 1):
        if divisor % 4 != 1:
            continue
        source_quotient = (p - 1) // divisor
        tail_modulus = source_quotient - 1
        coefficient = (p - divisor) // 4
        carrier = coefficient * source_quotient
        tail_hits = tuple(
            factor
            for factor in divisors(carrier * carrier)
            if factor <= carrier and (carrier + factor) % tail_modulus == 0
        )
        rows.append(
            (
                divisor,
                source_quotient,
                tail_modulus,
                coefficient,
                carrier,
                len(divisors(carrier * carrier)),
                tail_hits,
            )
        )
    return tuple(rows)


def verify_local_relay() -> None:
    p, q, r, multiplier, divisor = 241, 5, 16, 3375, 25
    values = relay_values(p, r, multiplier, divisor)
    b = valuation(p - 1, q)
    t = valuation(divisor, q) - b
    reduced_divisor = divisor // gcd(divisor, values["h"] * values["h"] - 1)
    zeta = valuation(values["z"], q)
    if not (
        p % 24 == 1
        and values["h"] > p
        and b == t == 1
        and valuation(values["T"], q) == b + t
        and valuation(reduced_divisor, q) == t
        and (values["m"] + 2) % q == 0
        and values["h"] % q == -1 % q
        and valuation(multiplier, q) > b
        and zeta > valuation(values["K"], q) == 2 * b + t
        and valuation(values["e"], q) == b
        and valuation(values["a"], q) == 0
        and valuation(values["s"] + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(values["B1"], q) == 0
        and valuation(values["E1"] + 1, q) == b
        and values["N"] % q == 3 % q
        and valuation(values["N"], q) == 0
    ):
        raise AssertionError("fixed local p-minus-one relay control changed")


def verify_p_minus_one_fan_miss() -> None:
    rows = p_minus_one_fan_rows(241)
    expected = (
        (1, 240, 239, 60, 14400, 325, ()),
        (5, 48, 47, 59, 2832, 81, ()),
    )
    if rows != expected:
        raise AssertionError("p-minus-one source fan boundary changed")


def verify() -> None:
    verify_local_relay()
    verify_p_minus_one_fan_miss()
    print("verified transverse relay p-minus-one source-tail boundary")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
