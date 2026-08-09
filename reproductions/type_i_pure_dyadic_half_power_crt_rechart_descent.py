#!/usr/bin/env python3
"""Verify the pure-dyadic half-power CRT split and strict rechart controls."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

from type_i_core_jacobi_punctured_kernel_primary_selector import (
    analyze_core,
    factorint,
    jacobi,
    multiplicative_order,
    vector_image,
)


def is_power_of_two(value: int) -> bool:
    return value >= 1 and value & (value - 1) == 0


def exponent_map(
    factors: tuple[tuple[int, int], ...], vector: tuple[int, ...]
) -> dict[int, int]:
    return {
        prime: exponent
        for (prime, _), exponent in zip(factors, vector, strict=True)
        if exponent
    }


def orient_below_one(exponents: dict[int, int]) -> dict[int, int]:
    value = Fraction(1)
    for prime, exponent in exponents.items():
        value *= Fraction(prime**max(exponent, 0), prime**max(-exponent, 0))
    if value > 1:
        return {prime: -exponent for prime, exponent in exponents.items()}
    assert value < 1
    return exponents


def within_centered_box(exponents: dict[int, int], K: int) -> bool:
    budgets = dict(factorint(K))
    return all(abs(exponent) <= budgets.get(prime, 0) for prime, exponent in exponents.items())


def within_dyadic_box(exponents: dict[int, int], K: int) -> bool:
    budgets = dict(factorint(K))
    for prime, exponent in exponents.items():
        budget = budgets.get(prime, 0)
        lower = -budget - 1 if prime == 2 else -budget
        if not lower <= exponent <= budget:
            return False
    return True


def overflow_from_dyadic_box(exponents: dict[int, int], K: int) -> dict[int, int]:
    budgets = dict(factorint(K))
    overflow: dict[int, int] = {}
    for prime, exponent in exponents.items():
        budget = budgets.get(prime, 0)
        lower = -budget - 1 if prime == 2 else -budget
        excess = max(lower - exponent, exponent - budget, 0)
        if excess:
            overflow[prime] = excess
    return overflow


def classify_chart(modulus: int, K: int) -> str:
    factors = factorint(K)
    vectors: list[tuple[int, ...]] = [()]
    for _, budget in factors:
        vectors = [
            prefix + (entry,)
            for prefix in vectors
            for entry in range(-budget, budget + 1)
        ]
    if any(vector_image(modulus, factors, vector) == modulus - 1 for vector in vectors):
        return "hit"

    subgroup = {1 % modulus}
    frontier = [1 % modulus]
    generators = [prime % modulus for prime, _ in factors]
    while frontier:
        value = frontier.pop()
        for generator in generators:
            successor = value * generator % modulus
            if successor not in subgroup:
                subgroup.add(successor)
                frontier.append(successor)
    return "F" if modulus - 1 in subgroup else "G"


def half_power_split(
    prime: int,
    modulus: int,
    K: int,
    vector: tuple[int, ...],
) -> dict[str, object]:
    assert prime % 24 == 1 and modulus % 4 == 3
    assert 4 * K == prime * modulus + 1
    factors = factorint(K)
    assert len(vector) == len(factors)

    source_phase = vector_image(modulus, factors, vector)
    phase_order = multiplicative_order(source_phase, modulus)
    assert phase_order >= 2 and is_power_of_two(phase_order)
    half_multiplier = phase_order // 2
    half_vector = tuple(half_multiplier * entry for entry in vector)
    full_relation = tuple(phase_order * entry for entry in vector)
    half_phase = vector_image(modulus, factors, half_vector)

    assert vector_image(modulus, factors, full_relation) == 1
    assert half_phase * half_phase % modulus == 1
    assert half_phase not in (1, modulus - 1)

    plus_modulus = gcd(modulus, half_phase - 1)
    minus_modulus = gcd(modulus, half_phase + 1)
    assert plus_modulus > 1 and minus_modulus > 1
    assert gcd(plus_modulus, minus_modulus) == 1
    assert plus_modulus * minus_modulus == modulus

    candidates = [value for value in (plus_modulus, minus_modulus) if value % 4 == 3]
    assert len(candidates) == 1
    target_modulus = candidates[0]
    complement = modulus // target_modulus
    assert complement % 4 == 1 and 1 < target_modulus < modulus

    target_K = (prime * target_modulus + 1) // 4
    support_bound = (complement - 1) // 4
    assert K == complement * target_K - support_bound
    common_support = gcd(K, target_K)
    assert common_support == gcd(target_K, support_bound)

    sign = 1 if half_phase % target_modulus == 1 else -1
    assert half_phase % target_modulus == sign % target_modulus
    assert half_phase % complement == (-sign) % complement

    half_exponents = exponent_map(factors, half_vector)
    relation_exponents = orient_below_one(dict(half_exponents))
    target_admitted = sign == -1 and within_centered_box(half_exponents, target_K)
    relation_admitted = sign == 1 and within_dyadic_box(relation_exponents, target_K)

    terminal: dict[str, object] | None = None
    if target_admitted:
        value = Fraction(target_K)
        for q, exponent in orient_below_one(dict(half_exponents)).items():
            value *= Fraction(q**max(exponent, 0), q**max(-exponent, 0))
        assert value.denominator == 1
        divisor = value.numerator
        assert 0 < divisor < target_K
        assert target_K * target_K % divisor == 0
        assert divisor % target_modulus == (-target_K) % target_modulus
        terminal = {"kind": "type_I_target", "divisor": divisor}
    elif relation_admitted:
        value = Fraction(target_K)
        for q, exponent in relation_exponents.items():
            value *= Fraction(q**max(exponent, 0), q**max(-exponent, 0))
        assert value.denominator == 1
        U = value.numerator
        E = 4 * U
        predecessor = (4 * target_K - E) // target_modulus
        assert 0 < U < target_K
        assert E % target_modulus == 1
        assert predecessor % 2 == 0 and 0 < predecessor < prime
        terminal = {
            "kind": "dyadic_relation",
            "E": E,
            "predecessor": predecessor,
        }

    d1_terminal: tuple[int, int, int] | None = None
    if (prime + 4) % target_modulus == 0:
        x = (prime + target_modulus) // 4
        y = prime * (x + 1) // target_modulus
        z = prime * x * (x + 1) // target_modulus
        assert Fraction(4, prime) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        d1_terminal = (x, y, z)

    return {
        "source_factors": factors,
        "phase_order": phase_order,
        "half_vector": half_vector,
        "full_relation": full_relation,
        "full_relation_overflow": overflow_from_dyadic_box(
            exponent_map(factors, full_relation), K
        ),
        "half_phase": half_phase,
        "plus_modulus": plus_modulus,
        "minus_modulus": minus_modulus,
        "target_modulus": target_modulus,
        "complement": complement,
        "target_K": target_K,
        "support_bound": support_bound,
        "common_support": common_support,
        "sign": sign,
        "target_admitted": target_admitted,
        "relation_admitted": relation_admitted,
        "terminal": terminal,
        "d1_terminal": d1_terminal,
        "target_class": classify_chart(target_modulus, target_K),
    }


def verify_core_control(
    prime: int,
    modulus: int,
    K: int,
    vector: tuple[int, ...],
) -> dict[str, object]:
    data = analyze_core(prime, modulus, K)
    assert not data["target_hits"] and not data["collisions"]
    record = next(row for row in data["negative_records"] if row[0] == vector)
    _, image, normalized = record
    assert jacobi(image, modulus) == -1
    assert multiplicative_order(image, modulus) == multiplicative_order(normalized, modulus)
    assert is_power_of_two(multiplicative_order(normalized, modulus))
    return half_power_split(prime, modulus, K, vector)


def verify() -> None:
    p73_terminal = verify_core_control(73, 63, 1150, (0, 1, -1))
    assert p73_terminal["phase_order"] == 2
    assert p73_terminal["half_phase"] == 55
    assert (p73_terminal["plus_modulus"], p73_terminal["minus_modulus"]) == (9, 7)
    assert p73_terminal["target_modulus"] == 7
    assert p73_terminal["target_K"] == 128
    assert p73_terminal["common_support"] == 2
    assert p73_terminal["sign"] == -1
    assert not p73_terminal["target_admitted"]
    assert p73_terminal["d1_terminal"] == (20, 219, 4380)

    p73_obstruction = verify_core_control(73, 95, 1734, (1, 0, -1))
    assert p73_obstruction["phase_order"] == 2
    assert p73_obstruction["half_phase"] == 56
    assert (p73_obstruction["plus_modulus"], p73_obstruction["minus_modulus"]) == (5, 19)
    assert p73_obstruction["target_modulus"] == 19
    assert p73_obstruction["target_K"] == 347
    assert p73_obstruction["common_support"] == 1
    assert p73_obstruction["sign"] == -1
    assert not p73_obstruction["target_admitted"]
    assert p73_obstruction["d1_terminal"] is None
    assert p73_obstruction["target_class"] == "G"

    p97_obstruction = verify_core_control(97, 55, 1334, (0, 1, 0))
    assert p97_obstruction["phase_order"] == 4
    assert p97_obstruction["half_phase"] == 34
    assert (p97_obstruction["plus_modulus"], p97_obstruction["minus_modulus"]) == (11, 5)
    assert p97_obstruction["target_modulus"] == 11
    assert p97_obstruction["target_K"] == 267
    assert p97_obstruction["common_support"] == 1
    assert p97_obstruction["sign"] == 1
    assert not p97_obstruction["relation_admitted"]
    assert p97_obstruction["d1_terminal"] is None
    assert p97_obstruction["target_class"] == "G"

    admitted_kernel = half_power_split(337, 255, 21484, (1, 0, 0))
    assert admitted_kernel["phase_order"] == 8
    assert admitted_kernel["half_phase"] == 16
    assert admitted_kernel["target_modulus"] == 15
    assert admitted_kernel["target_K"] == 1264
    assert admitted_kernel["sign"] == 1
    assert admitted_kernel["relation_admitted"]
    assert admitted_kernel["terminal"] == {
        "kind": "dyadic_relation",
        "E": 316,
        "predecessor": 316,
    }

    print("verified pure-dyadic half-power CRT rechart descent")
    print("p73_R63", "split=9x7", "D1_typeII=(20,219,4380)")
    print("p73_R95", "target_sign", "support_gcd=1", "edge=95->19", "target=G")
    print("p97_R55", "kernel_sign", "support_gcd=1", "edge=55->11", "target=G")
    print("p337_R255", "kernel_admitted", "edge=255->15", "even_terminal=(316,316)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
