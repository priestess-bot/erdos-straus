#!/usr/bin/env python3
"""Verify focused clean-q raw bridge controls for H4 a=1 top capacity.

Both fixtures are local H4 arithmetic specializations, not asserted 19-phase
H3 predecessors.  The second uses q=11**2 to replay a composite carrier as
two legal prime raw edges.  No prime-range or denominator scan is performed.
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
    expected_raw_selected: tuple[int, ...]
    expected_x: int
    expected_y: int
    expected_q_x: int
    expected_q_y: int
    expected_multiplier: int
    expected_capacity: int
    expected_p_primary_gate: int


FIXTURES = (
    Fixture(
        "prime_q37_atomic_split_strict",
        prime=73,
        peeled_part=3_366,
        expected_q=37,
        expected_raw_selected=(6_641,),
        expected_x=239_078,
        expected_y=6_641,
        expected_q_x=119_539,
        expected_q_y=6_641,
        expected_multiplier=793_858_499,
        expected_capacity=24,
        expected_p_primary_gate=37,
    ),
    Fixture(
        "composite_q121_atomic_split_strict",
        prime=241,
        peeled_part=29_886,
        expected_q=121,
        expected_raw_selected=(654_775, 59_525),
        expected_x=7_143_002,
        expected_y=59_525,
        expected_q_x=3_571_501,
        expected_q_y=59_525,
        expected_multiplier=212_593_597_025,
        expected_capacity=80,
        expected_p_primary_gate=121,
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
    """Return the maximal complete-excess block without factoring value."""
    if value <= 0:
        raise ValueError("complete excess requires a positive coordinate")
    common = gcd(value, carrier)
    exposed = value // common
    return gcd(value, pow(exposed, value.bit_length(), value))


def raw_q_word(residual: int, carrier: int, selected: int, q: int) -> tuple[int, tuple[int, ...]]:
    """Replay the canonical prime-factor raw word that divides selected by q."""
    raw_selected: list[int] = []
    for prime, exponent in factorization(q).items():
        if not is_prime(prime):
            raise AssertionError("raw word factorization lost primality")
        for _ in range(exponent):
            if valuation(selected, prime) <= valuation(carrier, prime):
                raise AssertionError("q factor is not a legal complete-excess raw edge")
            selected //= prime
            other = residual - selected
            if gcd(selected, other) != 1:
                raise AssertionError("raw q word lost primitive bottom-node status")
            raw_selected.append(selected)
    return selected, tuple(raw_selected)


def audit(fixture: Fixture) -> dict[str, int | str]:
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
    c_alt = pow((4 * m_alt) % p, -1, p)
    n_alt = (4 * m_alt + 1) // p
    a_alt = w // gcd(w, (n_alt + 1) // 2)

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
        and q_block % q == 0
        and gcd(q, k4) == 1
        and q_block % p != 0
        and c_alt == p - 1
        and (4 * m_alt + 1) % p == 0
        and a_alt == 1
    ):
        raise AssertionError(f"{fixture.name}: H4 q-carrier entry changed")

    y, raw_selected = raw_q_word(r4, k4, z, q)
    x = r4 - y
    q_x = complete_excess(x, k4)
    q_y = complete_excess(y, k4)
    beta_x = x // q_x
    beta_y = y // q_y
    p_primary_gate = p + 1 - q
    target_support = lcm(m4, q_x, q_y)
    multiplier = target_support // m4
    target_capacity = pow((4 * target_support) % p, -1, p)

    if not (
        y == z // q
        and x + y == r4
        and gcd(x, y) == 1
        and raw_selected == fixture.expected_raw_selected
        and x == fixture.expected_x
        and y == fixture.expected_y
        and q_x == fixture.expected_q_x > 1
        and q_y == fixture.expected_q_y > 1
        and p_primary_gate == fixture.expected_p_primary_gate
        and h != p_primary_gate
        and (x % p == 0) == (h == p_primary_gate)
        and y % p != 0
        and x % p != 0
        and x == q_x * beta_x
        and y == q_y * beta_y
        and gcd(q_x, beta_x) == 1
        and gcd(q_y, beta_y) == 1
        and k4 % (beta_x * beta_y) == 0
        and (q_x * q_y) % p != 0
        and k4 % (y * beta_x) != 0
        and k4 % (x * beta_y) != 0
        and multiplier == fixture.expected_multiplier
        and target_capacity == fixture.expected_capacity
        and target_capacity <= p - 2
        and target_capacity == c4 * pow(multiplier, -1, p) % p
    ):
        raise AssertionError(f"{fixture.name}: q raw bridge split dispatch changed")

    return {
        "name": fixture.name,
        "q": q,
        "raw_steps": len(raw_selected),
        "capacity": target_capacity,
        "p_primary": False,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    if receipts != [
        {
            "name": "prime_q37_atomic_split_strict",
            "q": 37,
            "raw_steps": 1,
            "capacity": 24,
            "p_primary": False,
        },
        {
            "name": "composite_q121_atomic_split_strict",
            "q": 121,
            "raw_steps": 2,
            "capacity": 80,
            "p_primary": False,
        },
    ]:
        raise AssertionError("H4 q-carrier raw bridge controls changed")
    print("verified 2 H4 clean-q raw bridges: q=37 and q=11^2")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact q-bridge controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
