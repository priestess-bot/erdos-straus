#!/usr/bin/env python3
"""Verify one local H4 q0=1 double clean-q raw bridge control.

The fixture is a local H4 arithmetic specialization, not an asserted
19-phase H3 predecessor or a registered persistent macro.  It checks the
q0=1 forced q**2 carrier, two legal raw q words, the p-free second endpoint,
and its exact q**2 capacity formula.  No prime-range or denominator scan is
performed.
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
    expected_q: int
    expected_b: int
    expected_raw_first: tuple[int, ...]
    expected_raw_second: tuple[int, ...]
    expected_x_first: int
    expected_y_first: int
    expected_x_second: int
    expected_y_second: int
    expected_q_x_first: int
    expected_q_y_first: int
    expected_q_x_second: int
    expected_q_y_second: int
    expected_capacity_first: int
    expected_capacity_second: int


FIXTURE = Fixture(
    name="p73_q0_one_double_q_strict",
    prime=73,
    peeled_part=12_246,
    expected_q=37,
    expected_b=10_799_471_865,
    expected_raw_first=(24_161,),
    expected_raw_second=(653,),
    expected_x_first=869_798,
    expected_y_first=24_161,
    expected_x_second=893_306,
    expected_y_second=653,
    expected_q_x_first=434_899,
    expected_q_y_first=24_161,
    expected_q_x_second=446_653,
    expected_q_y_second=653,
    expected_capacity_first=24,
    expected_capacity_second=51,
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
    """Return the maximal complete-excess block without factoring value."""
    common = gcd(value, carrier)
    exposed = value // common
    return gcd(value, pow(exposed, value.bit_length(), value))


def raw_q_word(residual: int, carrier: int, selected: int, q: int) -> tuple[int, tuple[int, ...]]:
    """Replay the canonical raw word which removes one full q from selected."""
    raw_selected: list[int] = []
    for prime, exponent in factorization(q).items():
        for _ in range(exponent):
            if valuation(selected, prime) <= valuation(carrier, prime):
                raise AssertionError("q factor is not a legal complete-excess raw edge")
            selected //= prime
            if gcd(selected, residual - selected) != 1:
                raise AssertionError("raw q word lost primitive endpoint status")
            raw_selected.append(selected)
    return selected, tuple(raw_selected)


def audit(fixture: Fixture) -> dict[str, int | str | bool]:
    p = fixture.prime
    r4 = 1 + p * fixture.peeled_part
    k4 = (p * r4 + 1) // 4
    m4 = k4
    c4 = 1
    h = gcd(r4 - 1, k4)
    z = r4 - h
    w = (p + 1) // 2
    d4 = gcd(w, m4)
    q = w // d4
    q_block = complete_excess(z, k4)
    m_alt = lcm(m4, q_block)
    l0 = m_alt // m4
    c_alt = pow((4 * m_alt) % p, -1, p)
    n_alt = (4 * m_alt + 1) // p
    b = (n_alt + 1) // (p + 1)
    gamma = gcd(q, b + 1)
    q0 = q // gamma
    t = (p * b - 1) // 2

    if not (
        is_prime(p)
        and p % 24 == 1
        and r4 % p == 1
        and r4 % 4 == 3
        and 2 * r4 > p**3
        and p * r4 + 1 == 4 * k4
        and m4 > (p - 1) ** 2 // 4
        and k4 == m4 * c4
        and 1 <= c4 <= p - 2
        and h == 2
        and h < p + 1
        and (p + 1) % h == 0
        and gcd(h, z) == 1
        and q == fixture.expected_q > 1
        and gcd(q, k4) == 1
        and q_block == z
        and k4 % (z // q_block) == 0
        and q_block % (q * q) == 0
        and q_block % p != 0
        and c_alt == p - 1
        and n_alt > 1
        and n_alt % 4 == 1
        and b % 2 == 1
        and m_alt == w * t
        and t % q == 0
        and l0 % (q * q) == 0
        and gamma == q
        and q0 == 1
        and b == fixture.expected_b
    ):
        raise AssertionError(f"{fixture.name}: q0=1 double-carrier entry changed")

    y_first, raw_first = raw_q_word(r4, k4, z, q)
    x_first = r4 - y_first
    y_second, raw_second = raw_q_word(r4, k4, y_first, q)
    x_second = r4 - y_second
    q_x_first = complete_excess(x_first, k4)
    q_y_first = complete_excess(y_first, k4)
    q_x_second = complete_excess(x_second, k4)
    q_y_second = complete_excess(y_second, k4)
    e_first = q_x_first // gcd(m4, q_x_first)
    e_second = q_x_second // gcd(m4, q_x_second)
    support_first = lcm(m4, q_x_first, q_y_first)
    support_second = lcm(m4, q_x_second, q_y_second)
    l_first = support_first // m4
    l_second = support_second // m4
    capacity_first = pow((4 * support_first) % p, -1, p)
    capacity_second = pow((4 * support_second) % p, -1, p)

    e = h // 2
    p_primary_numerator = q * q + h - 1
    noncore_p = 5
    noncore_q = 3
    noncore_d = 1
    noncore_e = 1

    if not (
        raw_first == fixture.expected_raw_first
        and raw_second == fixture.expected_raw_second
        and x_first == fixture.expected_x_first
        and y_first == fixture.expected_y_first == z // q
        and x_second == fixture.expected_x_second
        and y_second == fixture.expected_y_second == z // (q * q)
        and gcd(x_first, y_first) == gcd(x_second, y_second) == 1
        and q_x_first == fixture.expected_q_x_first
        and q_y_first == fixture.expected_q_y_first == q_block // q
        and q_x_second == fixture.expected_q_x_second
        and q_y_second == fixture.expected_q_y_second == q_block // (q * q)
        and p % q != 0
        and all(value % p for value in (x_first, y_first, x_second, y_second))
        and q_y_second % p != 0
        and q_x_second % p != 0
        and l_first == l0 // q * e_first
        and l_second == l0 // (q * q) * e_second
        and capacity_first == fixture.expected_capacity_first
        and capacity_second == fixture.expected_capacity_second
        and capacity_first == (-q * pow(e_first, -1, p)) % p
        and capacity_second == (-q * q * pow(e_second, -1, p)) % p
        and e_second % p != (q * q) % p
        and 1 <= capacity_second <= p - 2
        and p_primary_numerator % p != 0
        and noncore_p == 2 * noncore_q * noncore_d - 1
        and (noncore_q * noncore_q + 2 * noncore_e - 1) % noncore_p == 0
        and noncore_p % 24 != 1
        and e == 1
        and e <= d4
        and d4 % e == 0
    ):
        raise AssertionError(f"{fixture.name}: double q bridge map changed")

    return {
        "name": fixture.name,
        "q0": q0,
        "raw_steps": len(raw_first) + len(raw_second),
        "second_capacity": capacity_second,
        "second_p_primary": False,
        "second_stutter": False,
    }


def verify() -> None:
    receipt = audit(FIXTURE)
    expected = {
        "name": "p73_q0_one_double_q_strict",
        "q0": 1,
        "raw_steps": 2,
        "second_capacity": 51,
        "second_p_primary": False,
        "second_stutter": False,
    }
    if receipt != expected:
        raise AssertionError("q0=1 double-q bridge control changed")
    print("verified one q0=1 H4 double-q bridge: p-free second endpoint and strict q^2 capacity")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused double-q control")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
