#!/usr/bin/env python3
"""Verify the dyadic target-factor gate for U(4D)."""

from __future__ import annotations

import argparse
from math import gcd, lcm


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    candidate = 2
    while candidate * candidate <= value:
        while value % candidate == 0:
            factors[candidate] = factors.get(candidate, 0) + 1
            value //= candidate
        candidate += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("2-adic valuation is undefined at zero")
    value = abs(value)
    depth = 0
    while value % 2 == 0:
        value //= 2
        depth += 1
    return depth


def prime_power_carmichael(prime: int, exponent: int) -> int:
    if prime == 2 and exponent >= 3:
        return 1 << (exponent - 2)
    return (prime - 1) * (prime ** (exponent - 1))


def carmichael(value: int) -> int:
    result = 1
    for prime, exponent in factorization(value).items():
        result = lcm(result, prime_power_carmichael(prime, exponent))
    return result


def dyadic_unit_exponent(D_prime: int) -> int:
    """Return v_2(lambda(4 D_prime)) from the factorization of D_prime."""
    if D_prime < 1:
        raise ValueError("D' must be positive")
    exponent = max(1, v2(D_prime) if D_prime % 2 == 0 else 0)
    for prime in factorization(D_prime):
        if prime != 2:
            exponent = max(exponent, v2(prime - 1))
    return exponent


def unit_group_exponent(value: int) -> int:
    result = 1
    for unit in range(1, value):
        if gcd(unit, value) != 1:
            continue
        current = 1
        for order in range(1, carmichael(value) + 1):
            current = (current * unit) % value
            if current == 1:
                result = lcm(result, order)
                break
        else:
            raise AssertionError("unit order exceeded Carmichael bound")
    return result


def dyadic_target_gate(D_prime: int, dyadic_depth: int) -> bool:
    """Pure C_(2^b) target gate, including -1 -> the top involution."""
    if dyadic_depth < 0:
        raise ValueError("target depth must be nonnegative")
    return dyadic_depth == 0 or dyadic_depth <= dyadic_unit_exponent(D_prime)


def verify() -> None:
    for D_prime in range(1, 41):
        actual = v2(unit_group_exponent(4 * D_prime))
        expected = dyadic_unit_exponent(D_prime)
        if actual != expected:
            raise AssertionError(
                f"dyadic exponent mismatch for D'={D_prime}: {actual} != {expected}"
            )

    controls = {
        (1, 1): True,
        (1, 2): False,
        (3, 2): False,
        (5, 2): True,
        (5, 3): False,
        (15, 2): True,
        (4, 2): True,
        (8, 3): True,
    }
    for (D_prime, depth), expected in controls.items():
        actual = dyadic_target_gate(D_prime, depth)
        if actual != expected:
            raise AssertionError(
                f"gate mismatch for D'={D_prime}, b={depth}: {actual} != {expected}"
            )

    if dyadic_unit_exponent(1) != v2(carmichael(4)):
        raise AssertionError("U(4) exponent control failed")
    if dyadic_unit_exponent(5) != v2(carmichael(20)):
        raise AssertionError("U(20) exponent control failed")

    print("verified dyadic U(4D') target-factor gate")
    print(
        {
            "D_prime_1": {
                "v2_lambda": dyadic_unit_exponent(1),
                "C2": dyadic_target_gate(1, 1),
                "C4": dyadic_target_gate(1, 2),
            },
            "D_prime_5": {
                "v2_lambda": dyadic_unit_exponent(5),
                "C4": dyadic_target_gate(5, 2),
                "C8": dyadic_target_gate(5, 3),
            },
            "formula": "max(1, v2(D'), max_{q odd | D'} v2(q-1))",
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()

