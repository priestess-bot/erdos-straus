#!/usr/bin/env python3
"""Verify the owner-weighted target spectrum and Fourier-capacity controls."""

from __future__ import annotations

import argparse
import cmath
from math import gcd, isqrt, lcm


def factorint(value: int) -> dict[int, int]:
    """Return the prime factorization of a positive integer."""
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


def subgroup(generators: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    """Generate a finite multiplicative subgroup of units modulo modulus."""
    elements = {1 % modulus}
    changed = True
    while changed:
        changed = False
        for element in tuple(elements):
            for generator in generators:
                product = element * generator % modulus
                if product not in elements:
                    elements.add(product)
                    changed = True
    return tuple(sorted(elements))


def owner_weighted_spectrum(
    source_values: dict[int, int], target_value: int, modulus: int
) -> dict[str, object]:
    """Build eta_q, owner multiplicities, group support, and weighted coefficients."""
    target_factors = factorint(target_value)
    heights: dict[int, int] = {}
    owner_counts: dict[int, dict[int, tuple[int, ...]]] = {}
    for source_label, source_value in source_values.items():
        for prime, exponent in factorint(source_value).items():
            if prime == 2 or gcd(prime, modulus) != 1:
                continue
            common_height = min(exponent, target_factors.get(prime, 0))
            if common_height == 0:
                continue
            if common_height > heights.get(prime, 0):
                heights[prime] = common_height
            height_owners = owner_counts.setdefault(prime, {})
            for height in range(1, common_height + 1):
                old = set(height_owners.get(height, ()))
                old.add(source_label)
                height_owners[height] = tuple(sorted(old))

    generators = tuple(sorted(heights))
    group = subgroup(tuple(q % modulus for q in generators), modulus)
    weights = {1 % modulus: 1}
    for prime, exponent in sorted(heights.items()):
        choices = {1 % modulus: 1}
        for height in range(1, exponent + 1):
            residue = pow(prime, height, modulus)
            choices[residue] = (
                choices.get(residue, 0)
                + len(owner_counts[prime][height])
            )
        updated = {element: 0 for element in group}
        for left, left_weight in weights.items():
            for right, right_weight in choices.items():
                product = left * right % modulus
                updated[product] = updated.get(product, 0) + left_weight * right_weight
        weights = {element: weight for element, weight in updated.items() if weight}

    return {
        "heights": heights,
        "owner_counts": owner_counts,
        "group": group,
        "weights": weights,
        "total_weight": sum(weights.values()),
    }


def weighted_stabilizer(
    weights: dict[int, int], group: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    """Return the stabilizer of a finitely supported weighted function."""
    return tuple(
        element
        for element in group
        if all(
            weights.get(element * point % modulus, 0) == weights.get(point, 0)
            for point in group
        )
    )


def u16_coordinates(value: int) -> tuple[int, int]:
    """Coordinates for U(16)=<3> x <-1>, in the order (4,2)."""
    for first in range(4):
        for second in range(2):
            if (pow(3, first, 16) * pow(15, second, 16)) % 16 == value:
                return first, second
    raise ValueError(f"{value} is not a unit modulo 16")


def u16_character(value: int, first: int, second: int) -> complex:
    """Evaluate the (first, second) character of U(16)."""
    a, b = u16_coordinates(value)
    return (1j) ** (first * a) * ((-1) ** (second * b))


def u16_character_order(first: int, second: int) -> int:
    first_order = 1 if first == 0 else 4 // gcd(4, first)
    second_order = 1 if second == 0 else 2
    return lcm(first_order, second_order)


def type_ii_certificate(
    prime: int, target_layer: int, target_a: int, factor: int
) -> tuple[int, int, int]:
    """Return (K, B, C) for a target-layer Type II normal form."""
    modulus = 4 * target_layer
    if factor <= 1 or factor % modulus != modulus - 1:
        raise ValueError("factor is not a target congruence witness")
    target_value = prime + 4 * target_layer * target_a
    if target_value % factor:
        raise ValueError("factor does not divide the target denominator")
    K = (factor + 1) // modulus
    numerator = K * prime + target_a
    if numerator % factor:
        raise ValueError("normal-form numerator is not divisible")
    B = numerator // factor
    C = target_layer // target_a
    assert factor == 4 * target_a * C * K - 1
    assert B > target_a
    return K, B, C


def run_verification() -> dict[str, object]:
    # F-type gap: -1 lies in the generated source group but not in the finite spectrum.
    p_f = 409
    f_sources = {
        4: p_f + 4 * 8 * 4,
        8: p_f + 4 * 8 * 8,
    }
    f_target = p_f + 4 * 2 * 4
    f_profile = owner_weighted_spectrum(f_sources, f_target, 16)
    assert f_sources == {4: 537, 8: 665}
    assert f_target == 441
    assert f_profile["heights"] == {3: 1, 7: 1}
    assert f_profile["owner_counts"] == {3: {1: (4,)}, 7: {1: (8,)}}
    assert f_profile["group"] == (1, 3, 5, 7, 9, 11, 13, 15)
    assert f_profile["weights"] == {1: 1, 3: 1, 5: 1, 7: 1}
    assert f_profile["total_weight"] == 4
    assert 15 in f_profile["group"]
    assert f_profile["weights"].get(15, 0) == 0
    f_stabilizer = weighted_stabilizer(f_profile["weights"], f_profile["group"], 16)
    assert f_stabilizer == (1, 7)

    all_correlations: list[tuple[int, int, complex, complex]] = []
    for first in range(4):
        for second in range(2):
            coefficient = sum(
                weight * u16_character(point, first, second)
                for point, weight in f_profile["weights"].items()
            )
            target_correlation = (
                coefficient * u16_character(15, first, second).conjugate()
            )
            all_correlations.append((first, second, coefficient, target_correlation))

    quotient_correlations = [
        row
        for row in all_correlations
        if abs(u16_character(7, row[0], row[1]) - 1) < 1e-9
    ]
    assert len(quotient_correlations) == 4
    assert abs(sum(row[3] for row in quotient_correlations)) < 1e-9
    nontrivial = [row for row in quotient_correlations if row[:2] != (0, 0)]
    assert abs(sum(row[3] for row in nontrivial) + 4) < 1e-9
    best = min(
        nontrivial,
        key=lambda row: (
            -(-row[3].real),
            u16_character_order(row[0], row[1]),
            row[0],
            row[1],
        ),
    )
    assert best[:2] == (1, 1)
    assert best[2] == 2 + 2j
    assert abs(-best[3].real - 2) < 1e-9
    quotient_order = len(f_profile["group"]) // len(f_stabilizer)
    assert quotient_order == 4
    assert -best[3].real >= f_profile["total_weight"] / (quotient_order - 1)
    assert abs(
        best[2]
        - (1 + u16_character(3, 1, 1))
        * (1 + u16_character(7, 1, 1))
    ) < 1e-9

    # G-type separation with two owners for one repeated q.
    p_g = 57_399_241
    g_sources = {
        1: p_g + 4 * 41,
        41: p_g + 4 * 41 * 41,
    }
    g_target = p_g + 4
    g_profile = owner_weighted_spectrum(g_sources, g_target, 4)
    assert g_profile["heights"] == {5: 1}
    assert g_profile["owner_counts"] == {5: {1: (1, 41)}}
    assert g_profile["group"] == (1,)
    assert g_profile["weights"] == {1: 3}
    assert g_profile["total_weight"] == 3
    assert 3 not in g_profile["group"]
    for source_label in g_profile["owner_counts"][5][1]:
        source_value = 41 * source_label
        assert (source_value - 1) % 5 == 0

    # Direct target hit with an old-layer strict source-switch witness.
    p_hit = 5_113
    hit_sources = {3: p_hit + 24 * 3, 6: p_hit + 24 * 6}
    hit_target = p_hit + 4
    hit_profile = owner_weighted_spectrum(hit_sources, hit_target, 4)
    assert hit_profile["heights"] == {7: 1, 17: 1}
    assert hit_profile["owner_counts"] == {7: {1: (6,)}, 17: {1: (3,)}}
    assert hit_profile["group"] == (1, 3)
    assert hit_profile["weights"] == {1: 2, 3: 2}
    assert hit_profile["weights"].get(3, 0) > 0
    assert type_ii_certificate(p_hit, 1, 1, 7) == (2, 1_461, 1)
    assert type_ii_certificate(p_hit, 1, 1, 119) == (30, 1_289, 1)

    return {
        "f_gap": {
            "state": {"p": p_f, "D": 8, "target": [4, 2]},
            "heights": f_profile["heights"],
            "group": f_profile["group"],
            "weights": f_profile["weights"],
            "target": 15,
            "stabilizer": f_stabilizer,
            "canonical_character": {"coordinates": [1, 1], "real_deficit": 2},
            "status": "SOURCE_RESIDUE_FOURIER_GAP",
        },
        "g_separation": {
            "state": {"p": p_g, "D": 41, "target": [1, 1]},
            "heights": g_profile["heights"],
            "owner_counts": g_profile["owner_counts"],
            "weights": g_profile["weights"],
            "status": "G_SOURCE_SUPPORT_SEPARATION",
        },
        "hit": {
            "state": {"p": p_hit, "D": 6, "target": [1, 1]},
            "weights": hit_profile["weights"],
            "certificates": {
                7: type_ii_certificate(p_hit, 1, 1, 7),
                119: type_ii_certificate(p_hit, 1, 1, 119),
            },
            "status": "OWNER_WEIGHTED_TARGET_HIT",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    result = run_verification()
    print("verified owner-weighted target spectrum and Fourier-capacity controls")
    for branch in ("f_gap", "g_separation", "hit"):
        print(branch, result[branch]["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
