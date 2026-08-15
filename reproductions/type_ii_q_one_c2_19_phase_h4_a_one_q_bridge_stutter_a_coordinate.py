#!/usr/bin/env python3
"""Verify static d=1 controls for the H4 q-bridge stutter transduction.

These fixtures check the exact integer normal form derived from a hypothetical
H4 q-bridge arithmetic stutter.  They do not assert an actual 19-phase H4
predecessor, endpoint, atomic adapter, or persistent edge.  No range scan is
performed.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    base_b: int
    q: int
    excess_s: int
    expected_a: int
    expected_target_class: str
    expected_b_target: int | None
    expected_ordinary_capacity: int | None
    expected_regeneration_terminal: str | None = None


FIXTURES = (
    Fixture(
        "p73_same_support_s_zero",
        73,
        1,
        37,
        0,
        1,
        "support_stutter",
        1,
        None,
    ),
    Fixture(
        "p73_a_greater_than_one_handoff",
        73,
        1,
        37,
        1,
        37,
        "a_greater_than_one",
        None,
        None,
    ),
    Fixture(
        "p73_a_one_raw_p_source_cell",
        73,
        1,
        37,
        37,
        1,
        "raw_p_source",
        73,
        None,
    ),
    Fixture(
        "p73_a_one_p_free_cell",
        73,
        1,
        37,
        74,
        1,
        "p_free_failure",
        145,
        None,
    ),
    Fixture(
        "p73_a_one_regeneration_cell",
        73,
        1,
        37,
        111,
        1,
        "regeneration",
        217,
        None,
        "strict",
    ),
    Fixture(
        "p73_a_one_regeneration_p_free_return_cell",
        73,
        1,
        37,
        10_915,
        1,
        "regeneration",
        21_241,
        None,
        "p_free_return",
    ),
    Fixture(
        "p73_a_one_direct_strict_cell",
        73,
        1,
        37,
        148,
        1,
        "strict",
        289,
        36,
    ),
    Fixture(
        "p241_composite_q0_direct_strict_cell",
        241,
        1,
        121,
        484,
        1,
        "strict",
        961,
        120,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def ordinary_target_class(prime: int, b_target: int) -> str:
    residue = b_target % prime
    if residue == 0:
        return "raw_p_source"
    if residue == prime - 1:
        return "p_free_failure"
    if residue == prime - 2:
        return "regeneration"
    return "strict"


def audit(fixture: Fixture) -> dict[str, int | str]:
    p = fixture.prime
    b = fixture.base_b
    q = fixture.q
    s = fixture.excess_s
    w = (p + 1) // 2
    n = (p + 1) * b - 1
    support = (p * n - 1) // 4
    gamma = gcd(q, b + 1)
    q0 = q // gamma
    excess = q + p * s
    m = support // q
    target_support = m * excess
    target_n = n + 4 * m * s
    target_a = w // gcd(w, (target_n + 1) // 2)
    target_capacity = pow((4 * target_support) % p, -1, p)

    if not (
        is_prime(p)
        and p % 24 == 1
        and b > 0
        and b % 2 == 1
        and 1 < q < p
        and w % q == 0
        and n > 1
        and n % 4 == 1
        and support == w * ((p * b - 1) // 2)
        and support % q == 0
        and excess == q + p * s
        and target_support == (p * target_n - 1) // 4
        and target_n % 4 == 1
        and target_capacity == p - 1
        and target_a == q0 // gcd(q0, s) == fixture.expected_a
    ):
        raise AssertionError(f"{fixture.name}: q-bridge target normal form changed")

    if s == 0:
        if not (
            target_support == support
            and target_n == n
            and target_a == 1
            and fixture.expected_target_class == "support_stutter"
            and fixture.expected_b_target == b
        ):
            raise AssertionError(f"{fixture.name}: same-support checkpoint changed")
        return {
            "name": fixture.name,
            "q0": q0,
            "a": target_a,
            "target_class": "support_stutter",
        }

    if s % q0:
        if not (
            target_a > 1
            and fixture.expected_target_class == "a_greater_than_one"
            and fixture.expected_b_target is None
        ):
            raise AssertionError(f"{fixture.name}: a-greater-than-one split changed")
        return {
            "name": fixture.name,
            "q0": q0,
            "a": target_a,
            "target_class": "a_greater_than_one",
        }

    t = s // q0
    quotient = (p * b - 1) // gamma
    b_target = b + quotient * t
    multiplier = (p - 1) * b_target - 1
    target_class = ordinary_target_class(p, b_target)
    ordinary_capacity: int | None = None
    regeneration_terminal: str | None = None

    if target_class == "strict":
        ordinary_capacity = (-pow(multiplier, -1, p)) % p
    elif target_class == "raw_p_source":
        target_g = gcd(w, (target_n + 1) // 2)
        repair_capacity = (2 * target_g) % p
        if target_g != w or repair_capacity != 1:
            raise AssertionError(f"{fixture.name}: a=1 raw-p-source repair changed")
    elif target_class == "regeneration":
        residual = multiplier - 1
        valuation = 0
        while residual % p == 0:
            residual //= p
            valuation += 1
        terminal_digit = residual % p
        regeneration_terminal = (
            "p_free_return"
            if terminal_digit == p - 1
            else "raw_p_source"
            if terminal_digit == p - 2
            else "strict"
        )

    exceptional_t = {
        "raw_p_source": (gamma * b) % p,
        "p_free_failure": (gamma * (b + 1)) % p,
        "regeneration": (gamma * (b + 2)) % p,
    }

    if not (
        target_a == 1
        and q0 * (gamma + p * t) == excess
        and target_n == (p + 1) * b_target - 1
        and quotient * gamma == p * b - 1
        and b_target % p == (b - pow(gamma, -1, p) * t) % p
        and target_class == fixture.expected_target_class
        and b_target == fixture.expected_b_target
        and ordinary_capacity == fixture.expected_ordinary_capacity
        and regeneration_terminal == fixture.expected_regeneration_terminal
        and (target_class != "regeneration" or valuation >= 1)
        and (target_class not in exceptional_t or t % p == exceptional_t[target_class])
        and (
            target_class != "strict"
            or (
                t % p not in set(exceptional_t.values())
                and multiplier % p not in {0, 1, p - 1}
                and ordinary_capacity is not None
                and 1 <= ordinary_capacity <= p - 2
            )
        )
    ):
        raise AssertionError(f"{fixture.name}: a=1 residual dispatch changed")

    return {
        "name": fixture.name,
        "q0": q0,
        "a": target_a,
        "target_class": target_class,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    expected = [
        {"name": "p73_same_support_s_zero", "q0": 37, "a": 1, "target_class": "support_stutter"},
        {"name": "p73_a_greater_than_one_handoff", "q0": 37, "a": 37, "target_class": "a_greater_than_one"},
        {"name": "p73_a_one_raw_p_source_cell", "q0": 37, "a": 1, "target_class": "raw_p_source"},
        {"name": "p73_a_one_p_free_cell", "q0": 37, "a": 1, "target_class": "p_free_failure"},
        {"name": "p73_a_one_regeneration_cell", "q0": 37, "a": 1, "target_class": "regeneration"},
        {"name": "p73_a_one_regeneration_p_free_return_cell", "q0": 37, "a": 1, "target_class": "regeneration"},
        {"name": "p73_a_one_direct_strict_cell", "q0": 37, "a": 1, "target_class": "strict"},
        {"name": "p241_composite_q0_direct_strict_cell", "q0": 121, "a": 1, "target_class": "strict"},
    ]
    if receipts != expected:
        raise AssertionError("q-bridge a-coordinate controls changed")
    print("verified 8 static q-bridge stutter a-coordinate controls")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run exact static controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
