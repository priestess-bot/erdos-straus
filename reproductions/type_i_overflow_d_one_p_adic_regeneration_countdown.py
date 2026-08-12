#!/usr/bin/env python3
"""Verify fixed d=1 complete-excess p-adic countdown receipts.

This is a focused integer verifier. It checks six fixed normal forms and does
not search primes, denominators, selector history, or persisted state graphs.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    denominator: int
    expected_events: tuple[str, ...]
    expected_final_denominator: int


FIXTURES = (
    Fixture("p73_n5_low_support_capacity_exit", 73, 5, ("capacity:42",), 5),
    Fixture("p73_n73_high_support_capacity_exit", 73, 73, ("capacity:37",), 73),
    Fixture(
        "p73_n69_low_support_regeneration_then_capacity",
        73,
        69,
        ("regeneration:1->0", "capacity:4"),
        171_293,
    ),
    Fixture(
        "p73_n5033_two_regenerations_then_capacity",
        73,
        5_033,
        ("regeneration:2->1", "regeneration:1->0", "capacity:46"),
        29_936_985_425_892_356_393,
    ),
    Fixture(
        "p73_n5325_regeneration_to_p_free_failure",
        73,
        5_325,
        ("regeneration:1->0", "p_free_failure"),
        1_020_794_549,
    ),
    Fixture(
        "p73_n16129_regeneration_to_raw_failure",
        73,
        16_129,
        ("regeneration:1->0", "raw_failure"),
        9_365_182_993,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def valuation(value: int, prime: int) -> int:
    if value <= 0:
        raise AssertionError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def normal_form(prime: int, denominator: int) -> dict[str, int | bool]:
    alpha = (prime + 1) // 2
    v = (denominator + 1) // 2
    g = gcd(alpha, v)
    a = alpha // g
    b = v // g
    multiplier = (prime - 1) * b - a
    support = (prime * denominator - 1) // 4
    residual = (prime - 1) * denominator - 1
    capacity_bound = (prime - 1) ** 2 // 4
    raw_source_ok = b % prime != 0
    p_free_bundle_ok = multiplier % prime != 0

    if not (
        is_prime(prime)
        and prime % 24 == 1
        and denominator > 1
        and denominator % 4 == 1
        and gcd(a, b) == 1
        and gcd(alpha, prime - 1) == 1
        and prime * denominator == 4 * support + 1
        and prime * residual + 1 == 4 * support * (prime - 1)
        and multiplier
        == (((prime - 1) * denominator - 2) // 2) // g
        and multiplier > 1
        and multiplier % prime == (-a - b) % prime
        and raw_source_ok == (residual % prime != 0)
        and raw_source_ok == (b % prime != 0)
        and p_free_bundle_ok == (((residual - 1) // 2) % prime != 0)
        and p_free_bundle_ok == (b % prime != (-a) % prime)
    ):
        raise AssertionError("d=1 normalized form changed")

    return {
        "alpha": alpha,
        "g": g,
        "a": a,
        "b": b,
        "E": multiplier,
        "A": support,
        "R": residual,
        "B": capacity_bound,
        "raw": raw_source_ok,
        "p_free": p_free_bundle_ok,
        "eta": valuation(multiplier - 1, prime),
    }


def audit(fixture: Fixture) -> tuple[tuple[str, ...], int]:
    p = fixture.prime
    n = fixture.denominator
    events: list[str] = []

    for _ in range(8):
        state = normal_form(p, n)
        a = int(state["a"])
        b = int(state["b"])
        E = int(state["E"])
        A = int(state["A"])
        B = int(state["B"])
        eta = int(state["eta"])

        raw_residue = b % p == 0
        p_free_residue = b % p == (-a) % p
        regeneration_residue = b % p == (-a - 1) % p
        if sum((raw_residue, p_free_residue, regeneration_residue)) > 1:
            raise AssertionError(f"{fixture.name}: special residues overlap")

        if not state["raw"]:
            if not raw_residue or not state["p_free"] or eta != 0:
                raise AssertionError(f"{fixture.name}: raw gate classification changed")
            events.append("raw_failure")
            break

        if not state["p_free"]:
            if not p_free_residue or eta != 0:
                raise AssertionError(f"{fixture.name}: p-free gate classification changed")
            events.append("p_free_failure")
            break

        carrier = A * E
        capacity = (-pow(E, -1, p)) % p
        target_K = carrier * capacity
        target_R = (4 * target_K - 1) // p
        rank_before = (B // A, p - 1, eta)

        if not (
            carrier > p * p > B
            and 1 <= capacity < p
            and (4 * target_K - 1) % p == 0
            and 1 <= target_R < 4 * carrier
            and p * target_R + 1 == 4 * target_K
            and (capacity == p - 1) == (E % p == 1)
            and regeneration_residue == (E % p == 1)
        ):
            raise AssertionError(f"{fixture.name}: canonical capacity changed")

        if capacity != p - 1:
            rank_after = (B // carrier, capacity, 0)
            if not (capacity <= p - 2 and rank_after < rank_before):
                raise AssertionError(f"{fixture.name}: capacity exit is not strict")
            events.append(f"capacity:{capacity}")
            break

        s = (E - 1) // p
        next_n = E * n - s
        next_state = normal_form(p, next_n)
        b_prime = b * E - a * s
        unit = p + (p - 1) * (p * b - a)
        next_eta = int(next_state["eta"])
        rank_after = (B // carrier, p - 1, next_eta)

        if not (
            state["raw"]
            and state["p_free"]
            and next_n == (4 * carrier + 1) // p
            and int(next_state["A"]) == carrier
            and int(next_state["R"]) == target_R
            and int(next_state["g"]) == int(state["g"])
            and int(next_state["a"]) == a
            and int(next_state["b"]) == b_prime
            and gcd(a, b_prime) == 1
            and int(next_state["E"]) - 1 == s * unit
            and unit % p == a % p
            and next_eta == eta - 1
            and rank_after < rank_before
        ):
            raise AssertionError(f"{fixture.name}: regeneration countdown changed")

        events.append(f"regeneration:{eta}->{next_eta}")
        n = next_n
    else:
        raise AssertionError(f"{fixture.name}: focused chain did not terminate")

    result = tuple(events), n
    expected = fixture.expected_events, fixture.expected_final_denominator
    if result != expected:
        raise AssertionError(f"{fixture.name}: expected {expected}, got {result}")
    return result


def verify() -> None:
    results = [audit(fixture) for fixture in FIXTURES]
    events = [event for chain, _ in results for event in chain]
    regenerations = sum(event.startswith("regeneration:") for event in events)
    capacity_exits = sum(event.startswith("capacity:") for event in events)
    raw_failures = events.count("raw_failure")
    p_free_failures = events.count("p_free_failure")
    if (regenerations, capacity_exits, raw_failures, p_free_failures) != (5, 4, 1, 1):
        raise AssertionError("focused countdown classification changed")
    print(
        "verified 5 exact p-adic regeneration steps, 4 strict capacity exits, "
        "and 2 sharp terminal gate boundaries across 6 fixed d=1 receipts"
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
