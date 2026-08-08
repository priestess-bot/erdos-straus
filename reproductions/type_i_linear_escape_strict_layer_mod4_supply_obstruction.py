#!/usr/bin/env python3
"""Verify the strict-layer mod-4 supply obstruction at p=57399241, D=41."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt


def factorint(value: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer by trial division."""
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def divisors(value: int) -> tuple[int, ...]:
    """Return positive divisors in increasing order."""
    lower: list[int] = []
    upper: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        lower.append(divisor)
        if divisor * divisor != value:
            upper.append(value // divisor)
    return tuple(lower + list(reversed(upper)))


def is_squarefree(value: int) -> bool:
    return all(exponent == 1 for exponent in factorint(value).values())


def standard_sources(prime: int, layer: int) -> tuple[int, ...]:
    return tuple(
        a
        for a in divisors(layer)
        if is_squarefree(layer // a) and 4 * a * layer < prime
    )


def legendre_symbol(value: int, prime: int) -> int:
    residue = value % prime
    if residue == 0:
        return 0
    return -1 if pow(residue, (prime - 1) // 2, prime) == prime - 1 else 1


def multiplicative_order(value: int, modulus: int) -> int:
    if gcd(value, modulus) != 1:
        raise ValueError("value must be a unit")
    current = value % modulus
    order = 1
    while current != 1:
        current = current * value % modulus
        order += 1
    return order


def source_supply_envelope(prime: int, layer: int, target_layer: int, target_a: int) -> tuple[
    tuple[int, ...], int
]:
    """Return the canonical source support and shared-height upper envelope."""
    target = prime + 4 * target_layer * target_a
    contributions: dict[int, int] = {}
    target_factors = factorint(target)
    for source_a in standard_sources(prime, layer):
        source_factors = factorint(prime + 4 * layer * source_a)
        for q in source_factors.keys() & target_factors.keys():
            contributions[q] = contributions.get(q, 0) + min(
                source_factors[q], target_factors[q]
            )
    heights = {
        q: min(target_factors[q], contribution)
        for q, contribution in contributions.items()
    }
    envelope = 1
    for q, exponent in heights.items():
        envelope *= q**exponent
    return tuple(sorted(heights)), envelope


def run_verification() -> dict[str, object]:
    prime = 57_399_241
    modulus = 59
    layer = 41
    target_layer, target_a = 1, 1

    assert standard_sources(prime, layer) == (1, 41)
    assert divisors(layer) == (1, 41)

    source_values = {
        1: prime + 4 * layer,
        41: prime + 4 * layer * 41,
    }
    target_value = prime + 4
    assert source_values == {1: 57_399_405, 41: 57_405_965}
    assert target_value == 57_399_245
    assert factorint(source_values[1]) == {3: 1, 5: 1, 7: 1, 546_661: 1}
    assert factorint(source_values[41]) == {5: 1, 2_861: 1, 4_013: 1}
    assert factorint(target_value) == {5: 1, 11_479_849: 1}
    assert tuple(gcd(value, target_value) for value in source_values.values()) == (5, 5)

    supply, envelope = source_supply_envelope(
        prime, layer, target_layer, target_a
    )
    assert supply == (5,)
    assert envelope == 5
    assert all(q % 4 == 1 for q in supply)
    strict_candidates = [
        h
        for h in divisors(envelope)
        if h > 1 and h % (4 * target_layer) == -1 % (4 * target_layer)
    ]
    assert strict_candidates == []

    fixed_layer_primes = tuple(sorted(set().union(*(factorint(n) for n in source_values.values()))))
    assert fixed_layer_primes == (3, 5, 7, 2_861, 4_013, 546_661)
    assert all(legendre_symbol(q, modulus) == 1 for q in fixed_layer_primes)

    u_odd = 15
    escape_representative = 2_693
    assert multiplicative_order(u_odd, modulus) == 29
    assert multiplicative_order(escape_representative, modulus) == 58
    assert legendre_symbol(u_odd, modulus) == 1
    assert legendre_symbol(escape_representative, modulus) == -1

    x = 14_349_815
    y = 43_350_973_295_260
    z = 11_446_239_633_292_287_329_236
    assert Fraction(4, prime) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

    return {
        "arithmetic": (
            "Every standard D=41 source factor shared with the only strict lower "
            "fiber (1,1) divides 5, so no h can be -1 modulo 4."
        ),
        "state": {"p": prime, "R": modulus, "D": layer},
        "strict_lower_target": {"D_prime": target_layer, "A": target_a},
        "source_values": source_values,
        "target_value": target_value,
        "supply_primes": list(supply),
        "shared_height_envelope": envelope,
        "strict_switch_candidates": strict_candidates,
        "fixed_layer_quadratic_residue_primes": list(fixed_layer_primes),
        "block_subgroup_order": 29,
        "escape_direction_order": 58,
        "conclusion": "D41_C2_RECURSIVE_SOURCE_OBSTRUCTED",
        "terminal_first_control": {"x": x, "y": y, "z": z},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified strict-layer mod-4 supply obstruction and D41 C2 control")
    print(result["conclusion"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
