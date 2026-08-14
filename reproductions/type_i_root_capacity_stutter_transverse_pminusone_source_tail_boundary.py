#!/usr/bin/env python3
"""Verify that a local transverse relay does not force the p-1 source fan."""

from __future__ import annotations

import argparse
from math import gcd

from type_i_root_capacity_stutter_transverse_overlap_receipt_relay import (
    relay_values,
    valuation,
)


def factorization(value: int) -> dict[int, int]:
    result: dict[int, int] = {}
    candidate = 2
    while candidate * candidate <= value:
        while value % candidate == 0:
            result[candidate] = result.get(candidate, 0) + 1
            value //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def divisors_from_factorization(factors: dict[int, int]) -> list[int]:
    result = [1]
    for prime, exponent in factors.items():
        next_result = []
        prime_power = 1
        for _ in range(exponent + 1):
            next_result.extend(divisor * prime_power for divisor in result)
            prime_power *= prime
        result = next_result
    return sorted(result)


def divisors(value: int) -> list[int]:
    return divisors_from_factorization(factorization(value))


def is_prime(value: int) -> bool:
    return value > 1 and len(factorization(value)) == 1 and factorization(value).get(value) == 1


def p_minus_one_fan_rows(p: int) -> tuple[tuple[int, int, int, int, int, int, tuple[int, ...]], ...]:
    rows = []
    for divisor in divisors(p - 1):
        if divisor % 4 != 1:
            continue
        source_quotient = (p - 1) // divisor
        tail_modulus = source_quotient - 1
        coefficient = (p - divisor) // 4
        carrier = coefficient * source_quotient
        carrier_square_divisors = divisors_from_factorization(
            {prime: 2 * exponent for prime, exponent in factorization(carrier).items()}
        )
        tail_hits = tuple(
            factor
            for factor in carrier_square_divisors
            if factor <= carrier and (carrier + factor) % tail_modulus == 0
        )
        rows.append(
            (
                divisor,
                source_quotient,
                tail_modulus,
                coefficient,
                carrier,
                len(carrier_square_divisors),
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


def verify_oriented_root_input_tail_miss() -> None:
    p, h, q, r = 8641, 39, 5, 266
    u = h // 3
    root_capacity = (p * p + p + 1) // 3
    v = (p * p + p + 1) // h
    w = (2 * r + 1) // u
    t_value = p * p * r - (p + 1) // 2
    b = valuation(p - 1, q)
    t = valuation(t_value, q) - b
    rows = p_minus_one_fan_rows(p)
    expected = (
        (1, 8640, 8639, 2160, 18662400, 1365, ()),
        (5, 1728, 1727, 2159, 3730752, 819, ()),
        (9, 960, 959, 2158, 2071680, 1215, ()),
        (45, 192, 191, 2149, 412608, 351, ()),
    )
    if not (
        is_prime(p)
        and p % 24 == 1
        and 2 <= h < p
        and h % 3 == 0
        and root_capacity % u == 0
        and gcd(2 * r + 1, root_capacity) == u
        and b == t == 1
        and valuation(h + 1, q) == b
        and valuation(r - 1, q) == b
        and valuation(p * h + 1, q) == 2 * b + t
        and valuation(t_value, q) == b + t
        and valuation(v + 3, q) == b
        and p * p * u * (w + 9)
        == 2 * t_value + (p - 1) ** 2 + 3 * p * (p * h + 1)
        and valuation(w + 9, q) == 2 * b
        and rows == expected
    ):
        raise AssertionError("oriented root input did not retain the source-tail boundary")


def verify() -> None:
    verify_local_relay()
    verify_p_minus_one_fan_miss()
    verify_oriented_root_input_tail_miss()
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
