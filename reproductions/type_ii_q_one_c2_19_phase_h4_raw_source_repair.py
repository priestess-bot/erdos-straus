#!/usr/bin/env python3
"""Verify the H4 R == 0 (mod p) least-coprime source repair.

The fixtures are local H4 chart controls, not asserted q=1 19-phase H3
ancestors.  They isolate the arithmetic used by the same-anchor replacement:
one reaches a direct strict H5 capacity and one reaches H5 top capacity before
its d=1 row immediately takes a strict exit.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    multiplier: int
    capacity: int
    expected_source_prime: int
    expected_bundle: int
    expected_c5: int
    expected_h5_exit: int | None


FIXTURES = (
    Fixture(
        "zero_residue_direct_capacity_exit",
        prime=73,
        multiplier=7,
        capacity=1,
        expected_source_prime=11,
        expected_bundle=255,
        expected_c5=71,
        expected_h5_exit=None,
    ),
    Fixture(
        "zero_residue_top_capacity_then_d_one_exit",
        prime=73,
        multiplier=295,
        capacity=1,
        expected_source_prime=7,
        expected_bundle=291,
        expected_c5=72,
        expected_h5_exit=61,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


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


def complete_excess(value: int, carrier: int) -> int:
    carrier_factors = factorization(carrier)
    bundle = 1
    for prime, exponent in factorization(value).items():
        if exponent > carrier_factors.get(prime, 0):
            bundle *= prime**exponent
    return bundle


def least_coprime_prime(forbidden: int) -> int:
    candidate = 2
    while True:
        if is_prime(candidate) and forbidden % candidate:
            return candidate
        candidate += 1


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    r4 = p * fixture.multiplier
    k4 = (p * r4 + 1) // 4
    c4 = fixture.capacity
    m4 = k4 // c4
    v = r4 - 1
    bundle = complete_excess(v, k4)
    beta = v // bundle
    q_star = least_coprime_prime(r4 * k4 * v)
    source = (q_star, r4 * (q_star - 1) - q_star, q_star - 1)
    raw_anchor = (
        source[0] // q_star,
        (source[1] + r4) // q_star,
        (source[2] + 1) // q_star,
    )
    m5 = lcm(m4, bundle)
    l5 = m5 // m4
    c5 = c4 * pow(l5, -1, p) % p
    bp = (p - 1) ** 2 // 4

    if not (
        is_prime(p)
        and p % 24 == 1
        and r4 % p == 0
        and r4 % 4 == 3
        and p * r4 + 1 == 4 * k4
        and k4 % 2 == 0
        and k4 == m4 * c4
        and 1 <= c4 <= p - 2
        and m4 > bp
        and k4 % p != 0
        and v > p + 1
        and gcd(v, k4) <= p + 1 < v
        and bundle > 1
        and bundle * beta == v
        and bundle % p != 0
        and q_star == fixture.expected_source_prime
        and is_prime(q_star)
        and q_star != p
        and (r4 * k4 * v) % q_star != 0
        and source[1] > 0
        and source[0] + source[1] == r4 * source[2]
        and gcd(source[0], source[1]) == 1
        and k4 % q_star != 0
        and source[2] % q_star == q_star - 1
        and raw_anchor == (1, v, 1)
        and gcd(*raw_anchor[:2]) == 1
        and bundle % q_star != 0
        and m5 == lcm(m4, bundle)
        and c5 == fixture.expected_c5
    ):
        raise AssertionError(f"{fixture.name}: H4 same-anchor repair changed")

    if c5 <= p - 2:
        if fixture.expected_h5_exit is not None:
            raise AssertionError("direct capacity fixture unexpectedly needs H5 suffix")
        outcome = "direct_strict_capacity"
    else:
        n5 = (4 * m5 + 1) // p
        r5 = (4 * m5 * c5 - 1) // p
        alpha = (p + 1) // 2
        half_n5 = (n5 + 1) // 2
        shared = gcd(alpha, half_n5)
        a = alpha // shared
        b = half_n5 // shared
        e = (p - 1) * b - a
        strict_capacity = (-pow(e, -1, p)) % p
        if not (
            c5 == p - 1
            and n5 > 1
            and n5 % 4 == 1
            and p * r5 + 1 == 4 * m5 * c5
            and r5 == (p - 1) * n5 - 1
            and gcd(a, b) == 1
            and a == 1
            and b % p not in {0, (-a) % p, (-a - 1) % p}
            and e % p not in {0, 1}
            and strict_capacity == fixture.expected_h5_exit
            and 1 <= strict_capacity <= p - 2
        ):
            raise AssertionError(f"{fixture.name}: H5 top-capacity suffix changed")
        outcome = f"top_capacity_then_strict_{strict_capacity}"

    return {
        "name": fixture.name,
        "q_star": q_star,
        "bundle": bundle,
        "c5": c5,
        "outcome": outcome,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "zero_residue_direct_capacity_exit",
            "q_star": 11,
            "bundle": 255,
            "c5": 71,
            "outcome": "direct_strict_capacity",
        },
        {
            "name": "zero_residue_top_capacity_then_d_one_exit",
            "q_star": 7,
            "bundle": 291,
            "c5": 72,
            "outcome": "top_capacity_then_strict_61",
        },
    ]:
        raise AssertionError("H4 zero-residue repair controls changed")
    print(
        "verified 2 H4 R=0 (mod p) same-anchor source repairs: "
        "one direct strict capacity and one H5 top-capacity strict suffix"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact H4 source-repair controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
