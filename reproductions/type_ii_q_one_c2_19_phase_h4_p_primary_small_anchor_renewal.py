#!/usr/bin/env python3
"""Verify the H4 p-primary small-anchor renewal map.

These are local H4 arithmetic controls, not asserted 19-phase H3 ancestors.
They replay the actual p-block and capacity-peeling word, then distinguish a
proper-overlap strict renewal, a proper-overlap top-capacity continuation, and
the full-overlap p-block boundary.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    peeled_part: int
    expected_h: int
    expected_z: int
    expected_d: int
    expected_bundle: int
    expected_delta: int
    expected_multiplier: int | None
    expected_capacity: int | None
    expected_a: int | None
    expected_outcome: str


FIXTURES = (
    Fixture(
        "proper_overlap_strict_renewal",
        prime=73,
        peeled_part=2_686,
        expected_h=2,
        expected_z=196_077,
        expected_d=21,
        expected_bundle=9_337,
        expected_delta=21,
        expected_multiplier=9_337,
        expected_capacity=52,
        expected_a=None,
        expected_outcome="p_free_strict_capacity",
    ),
    Fixture(
        "proper_overlap_top_capacity_a_one",
        prime=73,
        peeled_part=3_366,
        expected_h=2,
        expected_z=245_717,
        expected_d=1,
        expected_bundle=245_717,
        expected_delta=1,
        expected_multiplier=245_717,
        expected_capacity=72,
        expected_a=1,
        expected_outcome="p_free_top_capacity_a_one",
    ),
    Fixture(
        "full_overlap_p_block_boundary",
        prime=73,
        peeled_part=2_886,
        expected_h=74,
        expected_z=210_605,
        expected_d=1,
        expected_bundle=210_605,
        expected_delta=1,
        expected_multiplier=None,
        expected_capacity=None,
        expected_a=None,
        expected_outcome="full_overlap_p_block",
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


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def complete_excess(value: int, carrier: int) -> int:
    carrier_factors = factorization(carrier)
    bundle = 1
    for prime, exponent in factorization(value).items():
        if exponent > carrier_factors.get(prime, 0):
            bundle *= prime**exponent
    return bundle


def raw_step(r_value: int, selected: int, prime: int) -> int:
    other = r_value - selected
    if selected % prime:
        raise AssertionError("selected raw coordinate is not divisible by the chosen prime")
    next_selected = selected // prime
    numerator = other + r_value * (prime - 1)
    if numerator % prime:
        raise AssertionError("raw shift did not make the complementary coordinate integral")
    next_other = numerator // prime
    if not (
        next_selected + next_other == r_value
        and gcd(next_selected, next_other) == 1
        and next_other == r_value - next_selected
    ):
        raise AssertionError("raw transition lost the primitive bottom-node contract")
    return next_selected


def strip_to_capacity(r_value: int, carrier: int, selected: int) -> tuple[int, int]:
    steps = 0
    while True:
        excess_primes = [
            prime
            for prime, exponent in factorization(selected).items()
            if exponent > valuation(carrier, prime)
        ]
        if not excess_primes:
            return selected, steps
        selected = raw_step(r_value, selected, min(excess_primes))
        steps += 1


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    r4 = 1 + p * fixture.peeled_part
    k4 = (p * r4 + 1) // 4
    m4 = k4
    c4 = 1
    v = r4 - 1
    e = valuation(v, p)
    source = (p, r4 * (p - 1) - p, p - 1)
    raw_anchor = (
        source[0] // p,
        (source[1] + r4) // p,
        (source[2] + 1) // p,
    )

    selected = v
    for _ in range(e):
        selected = raw_step(r4, selected, p)
    p_peeled = selected
    h, _capacity_steps = strip_to_capacity(r4, k4, p_peeled)
    z = r4 - h
    d = gcd(z, k4)
    bundle = complete_excess(z, k4)
    delta = z // bundle
    bp = (p - 1) ** 2 // 4

    if not (
        is_prime(p)
        and p % 24 == 1
        and r4 % p == 1
        and r4 % 4 == 3
        and r4 > p**3 // 2
        and p * r4 + 1 == 4 * k4
        and k4 % 2 == 0
        and k4 == m4 * c4
        and 1 <= c4 <= p - 2
        and m4 > bp
        and k4 % p != 0
        and source[1] > 0
        and source[0] + source[1] == r4 * source[2]
        and gcd(source[0], source[1]) == 1
        and raw_anchor == (1, v, 1)
        and e >= 1
        and p_peeled == v // p**e
        and gcd(p_peeled, k4) == h
        and h == gcd(v, k4) == fixture.expected_h
        and h % 2 == 0
        and (p + 1) % h == 0
        and h <= p + 1
        and z == fixture.expected_z == r4 - h
        and gcd(h, z) == 1
        and d == fixture.expected_d
        and (p * h + 1) % d == 0
        and z > p * p + p + 1 >= d
        and bundle == fixture.expected_bundle
        and bundle > 1
        and delta == fixture.expected_delta
        and bundle * delta == z
        and d % delta == 0
        and gcd(bundle, delta) == 1
        and gcd(bundle, h * delta) == 1
        and k4 % (h * delta) == 0
    ):
        raise AssertionError(f"{fixture.name}: H4 small-anchor renewal changed")

    if h == p + 1:
        if not (
            bundle % p == 0
            and fixture.expected_multiplier is None
            and fixture.expected_capacity is None
            and fixture.expected_outcome == "full_overlap_p_block"
        ):
            raise AssertionError(f"{fixture.name}: full-overlap p-block boundary changed")
        outcome = "full_overlap_p_block"
        capacity = 0
    else:
        m_alt = lcm(m4, bundle)
        multiplier = m_alt // m4
        capacity = c4 * pow(multiplier, -1, p) % p
        if not (
            bundle % p != 0
            and multiplier == fixture.expected_multiplier
            and capacity == fixture.expected_capacity
            and 1 <= capacity <= p - 1
        ):
            raise AssertionError(f"{fixture.name}: p-free renewal target changed")
        if capacity <= p - 2:
            if fixture.expected_a is not None:
                raise AssertionError("strict fixture unexpectedly carries a d=1 a-label")
            outcome = "p_free_strict_capacity"
        else:
            n_alt = (4 * m_alt + 1) // p
            r_alt = (4 * m_alt * capacity - 1) // p
            alpha = (p + 1) // 2
            half_n_alt = (n_alt + 1) // 2
            shared = gcd(alpha, half_n_alt)
            a_alt = alpha // shared
            if not (
                capacity == p - 1
                and (4 * m_alt + 1) % p == 0
                and n_alt > 1
                and n_alt % 4 == 1
                and p * r_alt + 1 == 4 * m_alt * capacity
                and r_alt == (p - 1) * n_alt - 1
                and a_alt == fixture.expected_a
            ):
                raise AssertionError(f"{fixture.name}: d=1 top-capacity map changed")
            outcome = "p_free_top_capacity_a_one"

    if outcome != fixture.expected_outcome:
        raise AssertionError(f"{fixture.name}: renewal classification changed")
    return {
        "name": fixture.name,
        "h": h,
        "bundle": bundle,
        "capacity": capacity,
        "outcome": outcome,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "proper_overlap_strict_renewal",
            "h": 2,
            "bundle": 9_337,
            "capacity": 52,
            "outcome": "p_free_strict_capacity",
        },
        {
            "name": "proper_overlap_top_capacity_a_one",
            "h": 2,
            "bundle": 245_717,
            "capacity": 72,
            "outcome": "p_free_top_capacity_a_one",
        },
        {
            "name": "full_overlap_p_block_boundary",
            "h": 74,
            "bundle": 210_605,
            "capacity": 0,
            "outcome": "full_overlap_p_block",
        },
    ]:
        raise AssertionError("H4 p-primary small-anchor controls changed")
    print(
        "verified 3 H4 p-primary small-anchor renewals: "
        "proper strict, proper top-capacity a=1, and full-overlap p-block"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact H4 small-anchor controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
