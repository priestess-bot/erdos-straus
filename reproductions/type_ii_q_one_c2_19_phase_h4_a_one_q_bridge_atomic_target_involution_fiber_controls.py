#!/usr/bin/env python3
"""Verify direct F certificates for two H4 atomic-target control charts.

The two inputs are local H4 arithmetic fixtures, not asserted persistent
19-phase predecessors.  The verifier reconstructs each atomic target,
checks a complete supplied factorization, exhausts only its small centered
box, and verifies one unbounded one-generator witness for -1 modulo R.
It intentionally does not search the generated subgroup or register an edge.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, lcm, prod

import type_i_high_r_chart_two_anchor as fiber
from type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge import (
    FIXTURES,
    complete_excess,
    raw_q_word,
)


@dataclass(frozen=True)
class Control:
    fixture_name: str
    factors: tuple[tuple[int, int], ...]
    involution_prime: int
    involution_exponent: int
    expected_target_R: int
    expected_target_K: int
    expected_target_support: int
    expected_capacity: int
    expected_box_cardinality: int


CONTROLS = (
    Control(
        fixture_name="prime_q37_atomic_split_strict",
        factors=(
            (2, 5),
            (3, 1),
            (7, 1),
            (29, 1),
            (229, 1),
            (17_077, 1),
            (1_121_093, 1),
        ),
        involution_prime=29,
        involution_exponent=571_589_117_469_993,
        expected_target_R=4_681_587_057_373_319,
        expected_target_K=85_438_963_797_063_072,
        expected_target_support=3_559_956_824_877_628,
        expected_capacity=24,
        expected_box_cardinality=8_019,
    ),
    Control(
        fixture_name="composite_q121_atomic_split_strict",
        factors=(
            (2, 6),
            (5, 3),
            (89, 1),
            (229, 1),
            (2_381, 1),
            (5_323, 1),
            (3_571_501, 1),
        ),
        involution_prime=5_323,
        involution_exponent=2_744_808_672_054_466_815,
        expected_target_R=122_496_889_878_545_062_639,
        expected_target_K=7_380_437_615_182_340_024_000,
        expected_target_support=92_255_470_189_779_250_300,
        expected_capacity=80,
        expected_box_cardinality=22_113,
    ),
)


def complete_factor_product(factors: tuple[tuple[int, int], ...]) -> int:
    if tuple(sorted(factors)) != factors:
        raise AssertionError("support factorization must be sorted")
    if any(exponent <= 0 or not fiber.is_prime(prime) for prime, exponent in factors):
        raise AssertionError("support factorization lost a positive prime factor")
    return prod(prime**exponent for prime, exponent in factors)


def reconstruct_target(fixture: object) -> tuple[int, int, int, int]:
    prime = int(getattr(fixture, "prime"))
    peeled_part = int(getattr(fixture, "peeled_part"))
    R4 = 1 + prime * peeled_part
    K4 = (prime * R4 + 1) // 4
    height = gcd(R4 - 1, K4)
    q = (prime + 1) // (2 * gcd((prime + 1) // 2, K4))
    endpoint_y, _raw_word = raw_q_word(R4, K4, R4 - height, q)
    endpoint_x = R4 - endpoint_y
    Q_x = complete_excess(endpoint_x, K4)
    Q_y = complete_excess(endpoint_y, K4)
    support = lcm(K4, Q_x, Q_y)
    capacity = pow((4 * support) % prime, -1, prime)
    K = support * capacity
    R = (4 * K - 1) // prime
    if not (
        prime * R + 1 == 4 * K
        and R % 4 == 3
        and support % K4 == 0
        and support % Q_x == 0
        and support % Q_y == 0
        and Q_x > 1
        and Q_y > 1
    ):
        raise AssertionError("atomic target reconstruction changed")
    return R, K, support, capacity


def audit(control: Control) -> dict[str, int | str | bool]:
    fixture = next(
        fixture for fixture in FIXTURES if getattr(fixture, "name") == control.fixture_name
    )
    prime = int(getattr(fixture, "prime"))
    R, K, support, capacity = reconstruct_target(fixture)
    factor_product = complete_factor_product(control.factors)
    index = next(
        index
        for index, (factor, _exponent) in enumerate(control.factors)
        if factor == control.involution_prime
    )
    witness = tuple(
        control.involution_exponent if coordinate == index else 0
        for coordinate in range(len(control.factors))
    )
    profile = fiber.provided_unbounded_residue_witness(R, list(control.factors), witness)

    if not (
        R == control.expected_target_R
        and K == control.expected_target_K
        and support == control.expected_target_support
        and capacity == control.expected_capacity
        and factor_product == K
        and gcd(K, R) == 1
        and pow(control.involution_prime, control.involution_exponent, R) == R - 1
        and profile["classification"] == "F"
        and profile["witness_policy"] == "provided_unbounded_modular"
        and profile["finite_box_hit"] is False
        and profile["finite_box_cardinality"] == control.expected_box_cardinality
        and profile["witness_residue"] == R - 1
        and profile["canonical_fourier_eligible"] is False
    ):
        raise AssertionError(f"{control.fixture_name}: direct F certificate changed")

    return {
        "fixture": control.fixture_name,
        "p": prime,
        "target_R": R,
        "classification": str(profile["classification"]),
        "involution_prime": control.involution_prime,
        "involution_exponent": control.involution_exponent,
        "box_cardinality": control.expected_box_cardinality,
        "canonical_fourier_eligible": bool(profile["canonical_fourier_eligible"]),
    }


def verify() -> None:
    receipts = [audit(control) for control in CONTROLS]
    expected = [
        {
            "fixture": "prime_q37_atomic_split_strict",
            "p": 73,
            "target_R": 4_681_587_057_373_319,
            "classification": "F",
            "involution_prime": 29,
            "involution_exponent": 571_589_117_469_993,
            "box_cardinality": 8_019,
            "canonical_fourier_eligible": False,
        },
        {
            "fixture": "composite_q121_atomic_split_strict",
            "p": 241,
            "target_R": 122_496_889_878_545_062_639,
            "classification": "F",
            "involution_prime": 5_323,
            "involution_exponent": 2_744_808_672_054_466_815,
            "box_cardinality": 22_113,
            "canonical_fourier_eligible": False,
        },
    ]
    if receipts != expected:
        raise AssertionError("H4 atomic target F receipts changed")
    print("verified 2 H4 atomic target F classifications without subgroup BFS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact controls")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
