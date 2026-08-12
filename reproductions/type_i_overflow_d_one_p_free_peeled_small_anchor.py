#!/usr/bin/env python3
"""Verify fixed d=1 p-free-failure small-anchor receipts.

This focused verifier uses five fixed states. It does not scan primes,
denominators, selector history, or complete raw Reach graphs.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_exponent: int
    expected_x_capacity: int
    expected_small_anchor: int
    expected_next_capacity: int
    expected_bundle: int
    expected_target_capacity: int | None
    expected_valuation_correction: int


FIXTURES = (
    Fixture(
        "p73_n217_e1_small_anchor_capacity_exit",
        73,
        217,
        1,
        1,
        2,
        3,
        5_207,
        3,
        1,
    ),
    Fixture(
        "p73_n1020794549_e1_countdown_endpoint_capacity_exit",
        73,
        1_020_794_549,
        1,
        1,
        2,
        21,
        3_499_867_025,
        21,
        1,
    ),
    Fixture(
        "p73_n26497_e2_nontrivial_x_capacity",
        73,
        26_497,
        2,
        5,
        2,
        3,
        635_927,
        3,
        1,
    ),
    Fixture(
        "p73_n10729_a_one_repeated_p_boundary",
        73,
        10_729,
        1,
        1,
        74,
        3,
        257_471,
        None,
        1,
    ),
    Fixture(
        "p97_n10765_nontrivial_valuation_correction",
        97,
        10_765,
        1,
        1,
        14,
        9,
        1_033_425,
        45,
        3,
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


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    bundle = 1
    for prime, exponent in factorization(value).items():
        if exponent > valuation(capacity, prime):
            bundle *= prime**exponent
    return bundle, value // bundle


def raw_divide_side(selected: int, residual: int, prime: int) -> tuple[int, int]:
    if selected % prime:
        raise AssertionError("selected raw side is not divisible by its edge prime")
    next_selected = selected // prime
    next_other = residual - next_selected
    if gcd(next_selected, next_other) != 1:
        raise AssertionError("unexpected gcd reduction in a bottom raw edge")
    return next_selected, next_other


def audit(fixture: Fixture) -> dict[str, int | str | None]:
    p = fixture.prime
    n = fixture.denominator
    A = (p * n - 1) // 4
    R = (p - 1) * n - 1
    K = A * (p - 1)
    B = (p - 1) ** 2 // 4
    alpha = (p + 1) // 2
    v = (n + 1) // 2
    g = gcd(alpha, v)
    a = alpha // g
    b = v // g
    E = (p - 1) * b - a
    exponent = valuation(E, p)
    p_power = p**exponent
    u = E // p_power

    selected = R - 1
    other = 1
    for _ in range(exponent):
        if valuation(selected, p) <= valuation(K, p):
            raise AssertionError(f"{fixture.name}: p raw capacity edge disappeared")
        selected, other = raw_divide_side(selected, R, p)

    y = selected
    x = other
    x_capacity = gcd(x, K)
    x_capacity_bound = gcd(x, abs(p_power - p - 1))
    y_capacity = gcd(y, K)

    peel_quotient = y // y_capacity
    for prime, exponent_to_remove in factorization(peel_quotient).items():
        for _ in range(exponent_to_remove):
            if valuation(selected, prime) <= valuation(K, prime):
                raise AssertionError(f"{fixture.name}: capacity peel stopped early")
            selected, other = raw_divide_side(selected, R, prime)

    h = selected
    z = other
    D = gcd(z, K)
    bundle, beta = complete_excess(z, K)
    multiplier = bundle // gcd(A, bundle)
    exterior = z // D
    valuation_correction = multiplier // exterior
    expected_correction = 1
    for prime in factorization(exterior):
        expected_correction *= prime ** valuation(p - 1, prime)
    reduced_capacity = D // valuation_correction
    target_capacity: int | None = None

    if bundle % p:
        target_capacity = (-pow(multiplier, -1, p)) % p
        target_support = lcm(A, bundle)
        target_K = target_support * target_capacity
        target_R = (4 * target_K - 1) // p
        if not (
            target_support == A * multiplier
            and target_support > A > B
            and 1 <= target_capacity <= p - 2
            and p * target_R + 1 == 4 * target_K
            and (0, target_capacity) < (0, p - 1)
        ):
            raise AssertionError(f"{fixture.name}: strict canonical exit changed")
    elif not (a == 1 and h == p + 1 and multiplier % p == 0):
        raise AssertionError(f"{fixture.name}: repeated p boundary changed")

    if not (
        is_prime(p)
        and p % 24 == 1
        and n > 1
        and n % 4 == 1
        and p * R + 1 == 4 * K
        and gcd(a, b) == 1
        and b % p == (-a) % p
        and E == p_power * u
        and u % p != 0
        and exponent == fixture.expected_exponent
        and valuation(R - 1, p) == exponent
        and y == (R - 1) // p_power == 2 * g * u
        and x == R - y == 1 + (p_power - 1) * y
        and y_capacity == 2 * g
        and x_capacity == x_capacity_bound == fixture.expected_x_capacity
        and h == fixture.expected_small_anchor
        and z == R - 2 * g
        and gcd(h, z) == 1
        and h <= p + 1
        and D == gcd(z, 2 * g * p + 1)
        and D == fixture.expected_next_capacity
        and D <= p * p + p + 1
        and z > D
        and h * D != 0
        and K % (h * D) == 0
        and bundle == fixture.expected_bundle
        and bundle > 1
        and beta == z // bundle
        and D % beta == 0
        and K % (h * beta) == 0
        and (bundle % p != 0) == (a > 1)
        and multiplier == exterior * valuation_correction
        and valuation_correction == expected_correction
        and D % valuation_correction == 0
        and (2 * g * p + 1) % reduced_capacity == 0
        and valuation_correction == fixture.expected_valuation_correction
        and (a == 1 or multiplier % p != 1)
        and target_capacity == fixture.expected_target_capacity
    ):
        raise AssertionError(f"{fixture.name}: small-anchor receipt changed")

    return {
        "name": fixture.name,
        "exponent": exponent,
        "x_capacity": x_capacity,
        "small_anchor": h,
        "next_capacity": D,
        "bundle": bundle,
        "target_capacity": target_capacity,
        "valuation_correction": valuation_correction,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    strict_exits = sum(receipt["target_capacity"] is not None for receipt in receipts)
    repeated_p_boundaries = len(receipts) - strict_exits
    nontrivial_corrections = sum(
        receipt["valuation_correction"] != 1 for receipt in receipts
    )
    if (strict_exits, repeated_p_boundaries, nontrivial_corrections) != (4, 1, 1):
        raise AssertionError("fixed small-anchor classifications changed")
    print(
        "verified 5 actual p-primary/small-anchor paths, 4 strict capacity exits, "
        "1 nontrivial e=2 competing capacity, 1 nontrivial valuation correction, "
        "and 1 exact a=1 repeated-p boundary"
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
