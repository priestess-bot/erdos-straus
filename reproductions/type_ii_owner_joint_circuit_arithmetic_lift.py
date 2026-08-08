#!/usr/bin/env python3
"""Verify the owner joint-circuit arithmetic lift trichotomy."""

from __future__ import annotations

import argparse
from itertools import product
from math import prod


def lattice_contains(
    vector: tuple[int, ...], generators: tuple[tuple[int, ...], ...], bound: int = 4
) -> bool:
    """Exact for the small bounded controls used here."""
    if not generators:
        return all(value == 0 for value in vector)
    for coefficients in product(range(-bound, bound + 1), repeat=len(generators)):
        candidate = tuple(
            sum(coefficient * generator[index] for coefficient, generator in zip(coefficients, generators))
            for index in range(len(vector))
        )
        if candidate == vector:
            return True
    return False


def classify_circuit(
    coefficients: tuple[int, ...],
    relation_generators: tuple[tuple[int, ...], ...],
    factors: tuple[int, ...],
    *,
    p: int,
    d: int,
    d_prime: int,
    a: int,
) -> dict[str, object]:
    """Apply SNF, power-closure, then the Type II normal-form test."""
    if not lattice_contains(coefficients, relation_generators):
        return {
            "status": "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED",
            "reason": "SNF_RELATION_NOT_LIFTABLE",
        }
    if d_prime % a or d_prime // a != d_prime / a:
        return {
            "status": "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED",
            "reason": "RANGE_OR_DIVISOR_GATE",
        }
    target_factor = p + 4 * a * d_prime
    powers = tuple(factor**coefficient for factor, coefficient in zip(factors, coefficients))
    if any(target_factor % power for power in powers if power > 1):
        return {
            "status": "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED",
            "reason": "POWER_CLOSED_SOURCE_CONTRACT_EMPTY",
        }
    factor_product = prod(powers)
    modulus = 4 * d_prime
    if factor_product % modulus == modulus - 1:
        k_prime = (factor_product + 1) // modulus
        c_prime = d_prime // a
        numerator = k_prime * p + a
        if numerator % factor_product:
            return {
                "status": "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED",
                "reason": "NORMAL_FORM_INTEGRALITY",
            }
        b_prime = numerator // factor_product
        return {
            "status": "CIRCUIT_TYPE_II_SHORT_CERTIFICATE",
            "k": k_prime,
            "b": b_prime,
            "c": c_prime,
            "factor_product": factor_product,
        }
    return {
        "status": "CIRCUIT_SOURCE_RELATION_FOURIER",
        "factor_product": factor_product,
        "modulus": modulus,
    }


def run_verification() -> dict[str, object]:
    direct = classify_circuit(
        (1, 1),
        ((1, 1),),
        (17, 7),
        p=5113,
        d=6,
        d_prime=1,
        a=1,
    )
    assert direct["status"] == "CIRCUIT_TYPE_II_SHORT_CERTIFICATE"
    assert direct["k"] == 30
    assert direct["b"] == 1289

    fourier = classify_circuit(
        (1, 2),
        ((1, 2),),
        (5, 7),
        p=241,
        d=1,
        d_prime=1,
        a=1,
    )
    assert fourier["status"] == "CIRCUIT_SOURCE_RELATION_FOURIER"
    assert fourier["factor_product"] == 245

    obstructed = classify_circuit(
        (1, 1),
        ((2, 0), (0, 2)),
        (5, 7),
        p=241,
        d=1,
        d_prime=1,
        a=1,
    )
    assert obstructed["status"] == "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED"

    power_obstructed = classify_circuit(
        (1, 2),
        ((1, 2),),
        (5, 7),
        p=97,
        d=6,
        d_prime=1,
        a=1,
    )
    assert power_obstructed["status"] == "CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED"
    assert power_obstructed["reason"] == "POWER_CLOSED_SOURCE_CONTRACT_EMPTY"

    return {
        "direct": direct,
        "fourier": fourier,
        "obstructed": obstructed,
        "power_obstructed": power_obstructed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner joint-circuit arithmetic lift trichotomy")
    for key, value in result.items():
        print(key, value["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
