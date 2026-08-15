#!/usr/bin/env python3
"""Verify H4 p-free p-block provenance obstructions.

The fixtures are local H4 chart controls rather than asserted 19-phase H3
ancestors.  They check the two possible p-adic depths used in the proof and
show why the p-free carrier after deleting p^e has no clean E1 receipt.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    p_power: int
    p_free_part: int
    expected_bundle: int
    expected_q0: int
    expected_beta: int
    expected_x: int
    expected_m0: int
    expected_c0: int


FIXTURES = (
    Fixture(
        "one_p_block",
        prime=73,
        p_power=1,
        p_free_part=6,
        expected_bundle=219,
        expected_q0=3,
        expected_beta=2,
        expected_x=433,
        expected_m0=24_036,
        expected_c0=49,
    ),
    Fixture(
        "two_p_blocks",
        prime=73,
        p_power=2,
        p_free_part=6,
        expected_bundle=15_987,
        expected_q0=3,
        expected_beta=2,
        expected_x=31_969,
        expected_m0=1_750_632,
        expected_c0=49,
    ),
)


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization requires a positive integer")
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


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def complete_excess(value: int, carrier: int) -> int:
    carrier_factors = factorization(carrier)
    bundle = 1
    for prime, exponent in factorization(value).items():
        if exponent > carrier_factors.get(prime, 0):
            bundle *= prime**exponent
    return bundle


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    e = fixture.p_power
    y = fixture.p_free_part
    r4 = 1 + p**e * y
    k4 = (p * r4 + 1) // 4
    m4 = k4
    c4 = 1
    v = r4 - 1
    bundle = complete_excess(v, k4)
    q0 = bundle // p**e
    beta = v // bundle
    m0 = lcm(m4, q0)
    c0 = pow((4 * m0) % p, -1, p)

    selected = v
    other = 1
    for remaining in range(e, 0, -1):
        if selected % p:
            raise AssertionError("p-primary raw path ended too early")
        next_selected = selected // p
        next_other = (other + r4 * (p - 1)) // p
        if not (
            other + selected == r4
            and (other + r4 * (p - 1)) % p == 0
            and next_other == r4 - next_selected
            and gcd(next_selected, next_other) == 1
            and valuation(selected, p) == remaining
        ):
            raise AssertionError("p-primary raw peeling changed")
        selected, other = next_selected, next_other

    x = other
    if not (
        is_prime(p)
        and p % 24 == 1
        and r4 % p == 1
        and r4 % 4 == 3
        and p * r4 + 1 == 4 * k4
        and k4 % 2 == 0
        and k4 == m4 * c4
        and k4 % p != 0
        and valuation(v, p) == e
        and bundle == fixture.expected_bundle
        and q0 == fixture.expected_q0
        and beta == fixture.expected_beta
        and bundle == p**e * q0
        and q0 % p != 0
        and gcd(bundle, beta) == 1
        and k4 % beta == 0
        and beta <= p + 1
        and selected == y == q0 * beta
        and x == fixture.expected_x == r4 - y
        and x == 1 + (p**e - 1) * y
        and gcd(x, y) == 1
        and k4 % x != 0
        and k4 % (x * beta) != 0
        and m0 == fixture.expected_m0
        and m0 % p != 0
        and c0 == fixture.expected_c0
        and (4 * m0 * c0 - 1) % p == 0
    ):
        raise AssertionError(f"{fixture.name}: H4 p-block provenance obstruction changed")

    return {
        "name": fixture.name,
        "e": e,
        "q0": q0,
        "beta": beta,
        "x": x,
        "c0": c0,
        "outcome": "p_free_chart_has_no_clean_E1",
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "one_p_block",
            "e": 1,
            "q0": 3,
            "beta": 2,
            "x": 433,
            "c0": 49,
            "outcome": "p_free_chart_has_no_clean_E1",
        },
        {
            "name": "two_p_blocks",
            "e": 2,
            "q0": 3,
            "beta": 2,
            "x": 31_969,
            "c0": 49,
            "outcome": "p_free_chart_has_no_clean_E1",
        },
    ]:
        raise AssertionError("H4 p-free p-block controls changed")
    print(
        "verified 2 H4 R=1 (mod p) p-block peelings: "
        "the p-free arithmetic charts both fail the clean E1 condition"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact H4 p-block controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
