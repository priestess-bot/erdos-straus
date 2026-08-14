#!/usr/bin/env python3
"""Verify a composite root-divisor external-source Type I terminal."""

from __future__ import annotations

import argparse
from math import gcd


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization expects a positive integer")
    result: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def divisors(factors: dict[int, int]) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factors.items():
        previous = result
        result = []
        prime_power = 1
        for _ in range(exponent + 1):
            result.extend(value * prime_power for value in previous)
            prime_power *= prime
    return tuple(sorted(result))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def external_menu(p_value: int, modulus: int) -> dict[str, int | tuple[int, ...]]:
    if modulus <= 1 or modulus % 2 == 0:
        raise AssertionError("source modulus must be odd and nontrivial")
    rho = p_value % modulus
    i_value = modulus - rho
    if not (
        2 <= i_value <= modulus - 2
        and gcd(modulus, 4 * i_value) == 1
        and (p_value + i_value) % modulus == 0
    ):
        raise AssertionError("root-divisor source setup changed")
    quotient = (p_value + i_value) // modulus
    residue_modulus = 4 * i_value
    target_residue = (-p_value * pow(modulus, -1, residue_modulus)) % residue_modulus
    hits = tuple(
        value
        for value in divisors(factorization(quotient))
        if value % residue_modulus == target_residue
    )
    return {
        "rho": rho,
        "i": i_value,
        "quotient": quotient,
        "residue_modulus": residue_modulus,
        "target_residue": target_residue,
        "hits": hits,
    }


def verify() -> None:
    p_value, u_value, r_value = 177_433, 91, 45
    root_capacity = (p_value * p_value + p_value + 1) // 3
    prime_factors = factorization(u_value)
    menus = {modulus: external_menu(p_value, modulus) for modulus in (7, 13, 91)}
    composite = menus[91]
    t_value = 5
    i_value = int(composite["i"])
    gap = 91 * t_value
    x_value = (p_value + gap) // 4
    divisor = i_value * x_value
    source_quotient = (p_value + i_value) // gap
    y_value = x_value * source_quotient
    z_value = p_value * x_value * source_quotient // i_value

    if not (
        is_prime(p_value)
        and p_value % 24 == 1
        and factorization(root_capacity) == {7: 1, 13: 1, 19: 1, 6_069_529: 1}
        and prime_factors == {7: 1, 13: 1}
        and gcd(2 * r_value + 1, root_capacity) == u_value
        and 3 * u_value < p_value
        and menus[7]
        == {
            "rho": 4,
            "i": 3,
            "quotient": 25_348,
            "residue_modulus": 12,
            "target_residue": 5,
            "hits": (),
        }
        and menus[13]
        == {
            "rho": 9,
            "i": 4,
            "quotient": 13_649,
            "residue_modulus": 16,
            "target_residue": 3,
            "hits": (),
        }
        and composite
        == {
            "rho": 74,
            "i": 17,
            "quotient": 1_950,
            "residue_modulus": 68,
            "target_residue": 5,
            "hits": (5,),
        }
        and (gap, x_value, divisor, source_quotient)
        == (455, 44_472, 756_024, 390)
        and 3 <= gap <= p_value - 2
        and gap % 4 == 3
        and divisor % x_value == 0
        and x_value * x_value % divisor == 0
        and (p_value * x_value + divisor) % gap == 0
        and 4 * x_value * y_value * z_value
        == p_value * (y_value * z_value + x_value * z_value + x_value * y_value)
    ):
        raise AssertionError("composite root-divisor terminal changed")
    print("verified composite root-divisor external Type I terminal")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
