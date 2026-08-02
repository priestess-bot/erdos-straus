#!/usr/bin/env python3
"""Exact cyclic-quotient Fourier profiles for fixed-layer certificates.

The profile keeps the finite-group arithmetic exact.  Fourier energies are
stored as a group-ring autocorrelation together with the character index;
this avoids treating an algebraic root-of-unity value as a floating-point
number.  The module deliberately does not choose a maximal nontrivial
character: the missing-target Fourier lemma supplies existence, while a
separate algebraic backend may order characters when that is justified.
"""

from __future__ import annotations

import math
from typing import Iterable, Sequence


def multiply_sets(left: set[int], right: set[int], modulus: int) -> set[int]:
    return {(a * b) % modulus for a in left for b in right}


def generated_subgroup(generators: Iterable[int], modulus: int) -> set[int]:
    subgroup = {1}
    generators = {value % modulus for value in generators}
    if any(math.gcd(value, modulus) != 1 for value in generators):
        raise AssertionError("quotient generators must be units")
    changed = True
    while changed:
        changed = False
        expanded = multiply_sets(subgroup, generators | {1}, modulus)
        if not expanded <= subgroup:
            subgroup |= expanded
            changed = True
    return subgroup


def stabilizer(group: set[int], subset: set[int], modulus: int) -> set[int]:
    if not subset or not subset <= group:
        raise AssertionError("fixed layer must be a nonempty subset of the group")
    return {
        candidate
        for candidate in group
        if {(candidate * value) % modulus for value in subset} == subset
    }


def coset_partition(
    group: set[int], stabilizer_set: set[int], modulus: int
) -> tuple[dict[int, int], list[frozenset[int]], list[int]]:
    if not stabilizer_set or 1 not in stabilizer_set:
        raise AssertionError("stabilizer must contain the identity")
    index: dict[int, int] = {}
    cosets: list[frozenset[int]] = []
    representatives: list[int] = []
    for value in sorted(group):
        if value in index:
            continue
        coset = frozenset((value * h) % modulus for h in stabilizer_set)
        if not coset <= group or len(coset) != len(stabilizer_set):
            raise AssertionError("stabilizer does not define a quotient partition")
        coset_index = len(cosets)
        cosets.append(coset)
        representatives.append(value)
        for member in coset:
            if member in index:
                raise AssertionError("quotient cosets overlap")
            index[member] = coset_index
    if set(index) != group:
        raise AssertionError("quotient partition does not cover the group")
    return index, cosets, representatives


def quotient_multiplication(
    index: dict[int, int],
    representatives: Sequence[int],
    left: int,
    right: int,
    modulus: int,
) -> int:
    return index[(representatives[left] * representatives[right]) % modulus]


def quotient_order_of(
    index: dict[int, int],
    representatives: Sequence[int],
    value: int,
    modulus: int,
) -> int:
    identity = index[1]
    current = identity
    generator = index[value]
    for exponent in range(1, len(representatives) + 1):
        current = quotient_multiplication(
            index, representatives, current, generator, modulus
        )
        if current == identity:
            return exponent
    raise AssertionError("quotient order exceeded quotient size")


def _modular_power(value: int, exponent: int, modulus: int) -> int:
    value %= modulus
    if exponent >= 0:
        return pow(value, exponent, modulus)
    return pow(pow(value, -1, modulus), -exponent, modulus)


def _factorization(value: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append((value, 1))
    return factors


def q_primary_phase_projection(
    *,
    character_index: int,
    quotient_order: int,
    coordinate: int,
    prime: int,
) -> dict[str, int | bool | str]:
    """Project a character phase to the q-primary part of its order.

    If d is the character order and q**h || d, a reduced phase numerator u in
    Z/dZ is sent to (d/q**h) * u in Z/q**hZ.  This is a well-defined additive
    homomorphism.  When q does not divide d, every such homomorphism is
    trivial, which is recorded rather than silently treated as a carrier.
    """
    if prime <= 1 or any(prime % divisor == 0 for divisor in range(2, math.isqrt(prime) + 1)):
        raise AssertionError("q-primary projection requires a prime")
    if quotient_order <= 0 or not 0 <= character_index < quotient_order:
        raise AssertionError("invalid character index")
    gcd_index = math.gcd(quotient_order, character_index)
    character_order = quotient_order // gcd_index
    if character_order == 1:
        raise AssertionError("the trivial character has no nontrivial phase projection")
    q_exponent = next(
        (exponent for factor, exponent in _factorization(character_order) if factor == prime),
        0,
    )
    if q_exponent == 0:
        return {
            "available": False,
            "reason": "q_not_dividing_character_order",
            "character_order": character_order,
            "q": prime,
            "q_exponent": 0,
            "reduced_phase_numerator": 0,
            "projected_phase_numerator": 0,
        }
    reduced_numerator = (character_index // gcd_index * coordinate) % character_order
    q_modulus = prime**q_exponent
    projected_numerator = (character_order // q_modulus * reduced_numerator) % q_modulus
    return {
        "available": True,
        "reason": "q_primary_character_order_projection",
        "character_order": character_order,
        "q": prime,
        "q_exponent": q_exponent,
        "q_modulus": q_modulus,
        "reduced_phase_numerator": reduced_numerator,
        "projected_phase_numerator": projected_numerator,
    }


def _residual_values(
    residual_blocks: Sequence[tuple[int, int]], modulus: int
) -> list[int]:
    values = [1]
    for prime, exponent in residual_blocks:
        if exponent < 0 or math.gcd(prime, modulus) != 1:
            raise AssertionError("residual blocks must be unit prime powers")
        old = values
        values = [
            (value * _modular_power(prime, power, modulus)) % modulus
            for value in old
            for power in range(-exponent, exponent + 1)
        ]
    return values


def _raw_counts(
    group: set[int],
    fixed_layer: set[int],
    residual_values: Sequence[int],
    modulus: int,
) -> dict[int, int]:
    counts = {value: 0 for value in group}
    for fixed in fixed_layer:
        for residual in residual_values:
            value = (fixed * residual) % modulus
            if value not in counts:
                raise AssertionError("residual block left the generated subgroup")
            counts[value] += 1
    return counts


def _cyclic_coordinates(
    index: dict[int, int],
    representatives: Sequence[int],
    modulus: int,
) -> tuple[int, dict[int, int]]:
    quotient_order = len(representatives)
    generator = next(
        value
        for value in sorted(index)
        if quotient_order_of(index, representatives, value, modulus) == quotient_order
    )
    generator_index = index[generator]
    coordinates: dict[int, int] = {}
    current = index[1]
    for coordinate in range(quotient_order):
        if current in coordinates:
            raise AssertionError("cyclic quotient coordinates are not unique")
        coordinates[current] = coordinate
        current = quotient_multiplication(
            index, representatives, current, generator_index, modulus
        )
    if len(coordinates) != quotient_order:
        raise AssertionError("quotient generator did not span the quotient")
    return generator, coordinates


def cyclic_quotient_fourier_profile(
    *,
    modulus: int,
    group: set[int],
    fixed_layer: set[int],
    residual_blocks: Sequence[tuple[int, int]],
    target: int,
) -> dict[str, object]:
    """Build an exact Fourier profile when the stabilizer quotient is cyclic.

    The returned `coefficient_vector` is the exact quotient representation
    count vector.  `autocorrelation` is an exact element of the group ring
    Z[C_m]; at character k its evaluation is |A(k)|^2.  Consequently the
    profile can be replayed without complex arithmetic or root-of-unity
    approximations.
    """
    if modulus <= 1 or not group or any(math.gcd(value, modulus) != 1 for value in group):
        raise AssertionError("group must be a nonempty unit subgroup")
    target %= modulus
    if target not in group:
        raise AssertionError("Fourier target must lie in the generated subgroup")
    if 1 not in group:
        raise AssertionError("generated subgroup must contain identity")
    if multiply_sets(group, group, modulus) != group:
        raise AssertionError("group input is not closed under multiplication")
    if not fixed_layer <= group or 1 not in fixed_layer:
        raise AssertionError("fixed layer must be a subset containing identity")

    stabilizer_set = stabilizer(group, fixed_layer, modulus)
    if not stabilizer_set <= fixed_layer:
        raise AssertionError("fixed-layer stabilizer must be contained in the layer")
    index, cosets, representatives = coset_partition(group, stabilizer_set, modulus)
    quotient_order = len(cosets)
    quotient_identity = index[1]

    quotient_fixed_layer = sorted({index[value] for value in fixed_layer})
    quotient_stabilizer = {
        candidate
        for candidate in range(quotient_order)
        if {
            quotient_multiplication(index, representatives, candidate, value, modulus)
            for value in quotient_fixed_layer
        }
        == set(quotient_fixed_layer)
    }
    if quotient_stabilizer != {quotient_identity}:
        raise AssertionError("stabilizer quotient retained a nontrivial period")

    generator, coordinates = _cyclic_coordinates(index, representatives, modulus)
    residual_values = _residual_values(residual_blocks, modulus)
    raw = _raw_counts(group, fixed_layer, residual_values, modulus)

    coefficient_vector = [0] * quotient_order
    for fixed_index in quotient_fixed_layer:
        for residual in residual_values:
            residual_index = index[residual]
            value = quotient_multiplication(
                index, representatives, fixed_index, residual_index, modulus
            )
            coefficient_vector[coordinates[value]] += 1

    for value in group:
        if raw[value] != coefficient_vector[coordinates[index[value]]]:
            raise AssertionError("raw and quotient representation counts disagree")

    target_coordinate = coordinates[index[target]]
    target_count = coefficient_vector[target_coordinate]
    total = sum(coefficient_vector)
    sum_of_squares = sum(value * value for value in coefficient_vector)
    autocorrelation = [
        sum(
            coefficient_vector[position]
            * coefficient_vector[(position - shift) % quotient_order]
            for position in range(quotient_order)
        )
        for shift in range(quotient_order)
    ]
    if autocorrelation[0] != sum_of_squares:
        raise AssertionError("autocorrelation zero shift changed")
    if sum(autocorrelation) != total * total:
        raise AssertionError("autocorrelation total changed")
    parseval_nontrivial = quotient_order * sum_of_squares - total * total
    if parseval_nontrivial != quotient_order * autocorrelation[0] - total * total:
        raise AssertionError("Parseval ledger changed")

    phase_signatures = []
    residual_coordinates = [coordinates[index[prime % modulus]] for prime, _ in residual_blocks]
    for character_index in range(1, quotient_order):
        character_order = quotient_order // math.gcd(quotient_order, character_index)
        reduced_index = character_index // math.gcd(quotient_order, character_index)
        reduced_phase_numerators = [
            (reduced_index * coordinate) % character_order
            for coordinate in residual_coordinates
        ]
        q_primary_projections = {
            str(prime): [
                int(
                    q_primary_phase_projection(
                        character_index=character_index,
                        quotient_order=quotient_order,
                        coordinate=coordinate,
                        prime=prime,
                    )["projected_phase_numerator"]
                )
                for coordinate in residual_coordinates
            ]
            for prime, _ in _factorization(character_order)
        }
        phase_signatures.append(
            {
                "character_index": character_index,
                "character_order": character_order,
                "reduced_phase_numerators": reduced_phase_numerators,
                "residual_phase_numerators": [
                    (character_index * coordinate) % quotient_order
                    for coordinate in residual_coordinates
                ],
                "q_primary_prime_divisors": sorted(
                    int(prime) for prime, _ in _factorization(character_order)
                ),
                "q_primary_projections": q_primary_projections,
            }
        )

    return {
        "group_order": len(group),
        "fixed_layer_size": len(fixed_layer),
        "stabilizer_order": len(stabilizer_set),
        "quotient_order": quotient_order,
        "quotient_is_cyclic": True,
        "quotient_generator": generator,
        "quotient_fixed_layer": quotient_fixed_layer,
        "quotient_identity": quotient_identity,
        "residual_blocks": [
            {"prime": prime, "exponent": exponent}
            for prime, exponent in residual_blocks
        ],
        "residual_coordinates": residual_coordinates,
        "target": target,
        "target_coordinate": target_coordinate,
        "coefficient_vector": coefficient_vector,
        "target_count": target_count,
        "total_representation_count": total,
        "autocorrelation": autocorrelation,
        "parseval_nontrivial_energy": parseval_nontrivial,
        "threshold_amplitude_fraction": [total, quotient_order - 1],
        "threshold_amplitude_squared_fraction": [
            total * total,
            (quotient_order - 1) * (quotient_order - 1),
        ],
        "missing_target_fourier_witness_exists": (
            target_count == 0 and total > 0 and quotient_order > 1
        ),
        "character_profile": phase_signatures,
        "energy_expression": {
            "basis": "Z[C_m]",
            "meaning": "evaluate sum_d autocorrelation[d] * zeta_m^(k*d)",
            "autocorrelation": autocorrelation,
        },
        "canonical_profile_policy": (
            "full_character_index_order; algebraic amplitude ordering is deferred"
        ),
        "q_primary_projection_rule": (
            "for character order d, map reduced phase u in Z/dZ to "
            "(d/q**h)*u mod q**h when q**h || d; q not dividing d is trivial"
        ),
        "qadic_phase_bridge": {
            "status": "conditional_contract_only",
            "phase_source": "character_profile",
            "required_inputs": [
                "explicit_affine_phase_map",
                "q_adic_height",
                "nested_congruence_check",
                "label_repetition_bound",
            ],
            "carrier_mapping_status": "unproved",
        },
        "carrier_mapping_status": "unproved",
    }
