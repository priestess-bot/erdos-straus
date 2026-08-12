#!/usr/bin/env python3
"""Verify fixed d=1 p-block peeling provenance obstructions."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_exponent: int
    expected_reduced_multiplier: int


FIXTURES = (
    Fixture("p73_n217_initial_p_free_failure", 73, 217, 1, 107),
    Fixture(
        "p73_n1020794549_countdown_p_free_failure",
        73,
        1_020_794_549,
        1,
        503_405_531,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    n = fixture.denominator
    A = (p * n - 1) // 4
    R = (p - 1) * n - 1
    K = A * (p - 1)
    alpha = (p + 1) // 2
    v = (n + 1) // 2
    g = gcd(alpha, v)
    a = alpha // g
    b = v // g
    E = (p - 1) * b - a
    exponent = valuation(E, p)
    p_power = p**exponent
    E0 = E // p_power
    M = A * E
    M0 = A * E0
    y = R - 1
    x = 1

    for _ in range(exponent):
        if y % p or gcd(x, y) != 1:
            raise AssertionError(f"{fixture.name}: p-peeling source changed")
        y_next = y // p
        x_next = R - y_next
        if not (
            x_next == (x + R * (p - 1)) // p
            and x_next + y_next == R
            and gcd(x_next, y_next) == 1
        ):
            raise AssertionError(f"{fixture.name}: raw p-peeling edge changed")
        x, y = x_next, y_next

    c0 = (-pow(E0, -1, p)) % p
    K0 = M0 * c0
    R0 = (4 * K0 - 1) // p
    divisor_remainder = (p * y + 1) % x

    if not (
        is_prime(p)
        and p % 24 == 1
        and n > 1
        and n % 4 == 1
        and b % p == (-a) % p
        and E % p == 0
        and exponent == fixture.expected_exponent
        and exponent == valuation(R - 1, p)
        and E0 == fixture.expected_reduced_multiplier
        and M % p == 0
        and M0 % p != 0
        and y == (R - 1) // p_power
        and x == R - y == 1 + (p_power - 1) * y
        and K % x != 0
        and divisor_remainder != 0
        and 1 <= c0 < p
        and (4 * K0 - 1) % p == 0
        and 1 <= R0 < 4 * M0
        and K0 % M0 == 0
    ):
        raise AssertionError(f"{fixture.name}: p-block obstruction changed")

    return {
        "name": fixture.name,
        "exponent": exponent,
        "reduced_multiplier": E0,
        "peeled_x": x,
        "peeled_y": y,
        "arithmetic_capacity": c0,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if len(receipts) != 2 or any(r["exponent"] != 1 for r in receipts):
        raise AssertionError("fixed p-block controls changed")
    print(
        "verified 2 actual p-block peeling paths, 2 p-free arithmetic recharts, "
        "and 2 strict complete-excess provenance failures"
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
