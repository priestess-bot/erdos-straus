#!/usr/bin/env python3
"""Verify top-capacity H5-to-d=1 handoff and its exact suffix classes.

The fixtures are abstract high-support d=1 top-capacity rows.  They check the
integer handoff used by an H5 receipt; they do not assert that a fixture is an
actual q=1 19-phase H5 witness or replay a global selector history.
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


FIXTURES = (
    Fixture("p73_a_one_direct_strict", 73, 73, ("strict:37",)),
    Fixture("p73_raw_source_repair", 73, 145, ("raw_repair:2",)),
    Fixture("p73_a_gt_one_p_free_handoff", 73, 217, ("p_free_a_gt_one",)),
    Fixture("p73_a_one_p_free_residual", 73, 10_729, ("a_one_p_free_residual",)),
    Fixture("p73_regeneration_to_strict", 73, 361, ("regen:1->0", "strict:30")),
    Fixture(
        "p73_regeneration_to_a_gt_one_p_free",
        73,
        5_325,
        ("regen:1->0", "p_free_a_gt_one"),
    ),
    Fixture("p73_regeneration_to_raw_repair", 73, 16_129, ("regen:1->0", "raw_repair:2")),
    Fixture("p73_a_one_regeneration_to_strict", 73, 5_253, ("regen:1->0", "strict:37")),
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


def top_capacity_row(prime: int, denominator: int) -> dict[str, int | bool]:
    """Rebuild a c=p-1 H5 candidate as a complete-product d=1 row."""
    if not (is_prime(prime) and prime % 24 == 1 and denominator > 1 and denominator % 4 == 1):
        raise AssertionError("input is not a core d=1 candidate")

    support = (prime * denominator - 1) // 4
    capacity_bound = (prime - 1) ** 2 // 4
    capacity = prime - 1
    residual = (prime - 1) * denominator - 1
    K = support * capacity
    alpha = (prime + 1) // 2
    v = (denominator + 1) // 2
    g = gcd(alpha, v)
    a = alpha // g
    b = v // g
    multiplier = (prime - 1) * b - a
    eta = valuation(multiplier - 1, prime)
    omega = ((multiplier - 1) // (prime**eta)) % prime
    raw_failure = b % prime == 0
    p_free_failure = b % prime == (-a) % prime
    regeneration = b % prime == (-a - 1) % prime
    strict = not (raw_failure or p_free_failure or regeneration)
    top_support_saturation = support % alpha == 0

    if not (
        prime * denominator == 4 * support + 1
        and 4 * support % prime == prime - 1
        and prime * residual + 1 == 4 * K
        and support > capacity_bound
        and denominator == (4 * support + 1) // prime
        and denominator % 4 == 1
        and gcd(a, b) == 1
        and multiplier > 1
        and multiplier % prime == (-a - b) % prime
        and raw_failure == (denominator % prime == prime - 1)
        and raw_failure == (residual % prime == 0)
        and p_free_failure == (denominator % prime == prime - 2)
        and p_free_failure == (residual % prime == 1)
        and regeneration == (multiplier % prime == 1)
        and sum((raw_failure, p_free_failure, regeneration)) <= 1
        and strict == (multiplier % prime not in {0, 1} and not raw_failure)
        and (a == 1) == top_support_saturation
    ):
        raise AssertionError("top-capacity d=1 normal form changed")

    return {
        "A": support,
        "B": capacity_bound,
        "R": residual,
        "K": K,
        "alpha": alpha,
        "g": g,
        "a": a,
        "b": b,
        "E": multiplier,
        "eta": eta,
        "omega": omega,
        "raw": raw_failure,
        "p_free": p_free_failure,
        "regen": regeneration,
        "strict": strict,
        "a_one_support_saturation": top_support_saturation,
    }


def trace_suffix(fixture: Fixture) -> tuple[tuple[str, ...], dict[str, int | bool]]:
    """Follow only the arithmetic d=1 suffix until its first non-regeneration row."""
    p = fixture.prime
    n = fixture.denominator
    initial = top_capacity_row(p, n)
    initial_a = int(initial["a"])
    initial_g = int(initial["g"])
    initial_eta = int(initial["eta"])
    initial_omega = int(initial["omega"])
    events: list[str] = []

    for _ in range(initial_eta + 2):
        state = top_capacity_row(p, n)
        a = int(state["a"])
        g = int(state["g"])
        E = int(state["E"])
        eta = int(state["eta"])

        if state["raw"]:
            repaired_capacity = (2 * g) % p
            if not (a == initial_a and g == initial_g and 1 <= repaired_capacity <= p - 2):
                raise AssertionError("least-coprime raw repair changed")
            events.append(f"raw_repair:{repaired_capacity}")
            break

        if state["p_free"]:
            if a > 1:
                events.append("p_free_a_gt_one")
            else:
                if initial_omega != p - 1:
                    raise AssertionError("a=1 p-free digit classification changed")
                events.append("a_one_p_free_residual")
            break

        target_capacity = (-pow(E, -1, p)) % p
        if target_capacity != p - 1:
            if not (state["strict"] and 1 <= target_capacity <= p - 2):
                raise AssertionError("strict d=1 capacity classification changed")
            events.append(f"strict:{target_capacity}")
            break

        if not state["regen"]:
            raise AssertionError("top capacity did not classify as regeneration")
        next_n = E * n - (E - 1) // p
        next_state = top_capacity_row(p, next_n)
        if not (
            int(next_state["A"]) == int(state["A"]) * E
            and int(next_state["a"]) == a
            and int(next_state["g"]) == g
            and int(next_state["eta"]) == eta - 1
            and int(next_state["E"]) - 1
            == ((E - 1) // p) * (p + (p - 1) * (p * int(state["b"]) - a))
        ):
            raise AssertionError("d=1 regeneration handoff changed")
        events.append(f"regen:{eta}->{eta - 1}")
        n = next_n
    else:
        raise AssertionError("focused d=1 suffix did not terminate")

    if initial_a == 1:
        residual = events[-1] == "a_one_p_free_residual"
        if residual != (initial_omega == p - 1):
            raise AssertionError("a=1 residual is not exactly omega=-1")
    elif events[-1] == "a_one_p_free_residual":
        raise AssertionError("a>1 entered the a=1 residual")

    result = tuple(events)
    if result != fixture.expected_events:
        raise AssertionError(f"{fixture.name}: expected {fixture.expected_events}, got {result}")
    return result, initial


def verify() -> None:
    traces = [trace_suffix(fixture) for fixture in FIXTURES]
    events = [event for trace, _ in traces for event in trace]
    regenerations = sum(event.startswith("regen:") for event in events)
    strict_exits = sum(event.startswith("strict:") for event in events)
    raw_repairs = sum(event.startswith("raw_repair:") for event in events)
    a_gt_one_handoffs = events.count("p_free_a_gt_one")
    a_one_residuals = events.count("a_one_p_free_residual")
    if (regenerations, strict_exits, raw_repairs, a_gt_one_handoffs, a_one_residuals) != (4, 3, 2, 2, 1):
        raise AssertionError("top-capacity handoff summary changed")
    print(
        "verified 8 high-support top-capacity d=1 handoffs: 4 regeneration steps, "
        "3 strict exits, 2 raw-source repairs, 2 a>1 p-free handoffs, and "
        "the unique a=1 p-free residual class"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run fixed top-capacity receipts")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
