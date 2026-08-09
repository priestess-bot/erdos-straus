#!/usr/bin/env python3
"""Focused direct checks for finite source dual profiles in owner windows."""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd


def owner_prefix(p: int, modulus: int) -> int:
    value = (-p * pow(4, -1, modulus)) % modulus
    assert 0 < value < modulus
    return value


def owner_window(p: int, q: int, layer: int) -> tuple[int, int, tuple[int, ...]]:
    modulus = q**layer
    prefix = owner_prefix(p, modulus)
    bound = (p - 1) // 4
    maximum_index = (bound - prefix) // modulus
    labels = tuple(
        prefix + modulus * index
        for index in range(maximum_index + 1)
    ) if maximum_index >= 0 else ()
    assert all(0 < 4 * value < p for value in labels)
    assert all((p + 4 * value) % modulus == 0 for value in labels)
    return prefix, maximum_index, labels


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def canonical_vertex(owner: int) -> tuple[int, int, int]:
    """Return (D, A, C) with owner=A*D=A^2*C and C squarefree."""
    a_value = 1
    c_value = 1
    for prime, exponent in factorization(owner).items():
        a_value *= prime ** (exponent // 2)
        if exponent % 2:
            c_value *= prime
    d_value = a_value * c_value
    assert owner == a_value * d_value == a_value * a_value * c_value
    assert all(exponent == 1 for exponent in factorization(c_value).values())
    return d_value, a_value, c_value


def affine_ideal_distance(offset: int, period: int) -> int:
    period = abs(period)
    if period == 0:
        return abs(offset)
    residue = offset % period
    return min(residue, period - residue)


def direct_rank_one_box_profiles(
    coordinates: tuple[int, ...],
    q: int,
    role_value: int,
    maximum_index: int,
) -> tuple[tuple[tuple[int, ...], int, int], ...]:
    """Enumerate the finite owner box, then solve its exact rank-one equations."""
    assert coordinates and coordinates[0] == 0
    profiles: list[tuple[tuple[int, ...], int, int]] = []
    for indices in product(range(maximum_index + 1), repeat=len(coordinates)):
        translation = indices[0]
        candidate: int | None = None
        consistent = True
        for coordinate, index in zip(coordinates[1:], indices[1:]):
            difference = index - translation
            if coordinate == 0:
                if difference:
                    consistent = False
                    break
                continue
            if difference % coordinate:
                consistent = False
                break
            current = difference // coordinate
            if candidate is None:
                candidate = current
            elif candidate != current:
                consistent = False
                break
        if not consistent:
            continue
        if candidate is None:
            candidate = role_value % q
        if candidate % q != role_value % q:
            continue
        if any(
            translation + coordinate * candidate != index
            for coordinate, index in zip(coordinates, indices)
        ):
            continue
        profiles.append((tuple(indices), candidate, translation))
    return tuple(profiles)


def deep_indices(p: int, q: int, layer: int, maximum_index: int) -> tuple[int, ...]:
    modulus = q**layer
    prefix = owner_prefix(p, modulus)
    deeper_prefix = owner_prefix(p, modulus * q)
    digit = (deeper_prefix - prefix) // modulus
    assert 0 <= digit < q
    return tuple(
        index for index in range(maximum_index + 1)
        if index % q == digit
    )


def verify_positive_boundary_profile() -> dict[str, object]:
    p, q, layer = 97, 3, 1
    prefix, maximum_index, labels = owner_window(p, q, layer)
    assert (prefix, maximum_index, labels) == (
        2,
        7,
        (2, 5, 8, 11, 14, 17, 20, 23),
    )

    profiles = direct_rank_one_box_profiles((0, 7), q, 1, maximum_index)
    assert profiles == (((0, 7), 1, 0),)
    indices, normalized_dual, translation = profiles[0]
    ambient_coefficient = q**layer * normalized_dual
    source_labels = tuple(prefix + q**layer * index for index in indices)
    assert ambient_coefficient == 3
    assert source_labels == (2, 23)
    assert all(
        prefix + q**layer * translation + ambient_coefficient * coordinate == label
        for coordinate, label in zip((0, 7), source_labels)
    )
    assert (indices[1] - indices[0]) % q == 1
    assert tuple(valuation(p + 4 * value, q) for value in source_labels) == (1, 3)
    assert tuple(canonical_vertex(value) for value in source_labels) == (
        (2, 1, 2),
        (23, 1, 23),
    )

    deeper = deep_indices(p, q, layer, maximum_index)
    unused = tuple(index for index in deeper if index not in indices)
    assert deeper == (1, 4, 7) and unused == (1, 4)
    local_deep_label = prefix + q**layer * unused[0]
    assert local_deep_label == 5
    assert valuation(p + 4 * local_deep_label, q) == 2
    assert canonical_vertex(local_deep_label) == (5, 1, 5)

    # The local deep label is not a common-base next-layer target for this edge.
    step = (source_labels[1] - source_labels[0]) // q**layer
    common_base = gcd(source_labels[0], step)
    assert step == 7 and common_base == 1
    assert (common_base * common_base) % local_deep_label != 0

    return {
        "owner_indices": indices,
        "source_labels": source_labels,
        "source_heights": (1, 3),
        "unused_local_deep_indices": unused,
        "local_deep_label": local_deep_label,
        "common_base_next_layer_toggle_ready": False,
    }


def verify_strict_range_obstruction() -> dict[str, object]:
    p, q, layer = 97, 3, 1
    _, maximum_index, _ = owner_window(p, q, layer)
    profiles = direct_rank_one_box_profiles((0, 8), q, 1, maximum_index)
    assert profiles == ()

    # This is a complete finite-box check: every possible index difference lies in [-7, 7].
    differences = {
        right - left
        for left in range(maximum_index + 1)
        for right in range(maximum_index + 1)
    }
    assert differences == set(range(-7, 8))
    assert all(
        difference % 8 != 0 or (difference // 8) % q != 1
        for difference in differences
    )
    assert affine_ideal_distance(8, 8 * q) == 8
    assert 8 > maximum_index

    return {
        "coordinates": (0, 8),
        "maximum_index": maximum_index,
        "admissible_profiles": 0,
        "minimum_oscillation": 8,
    }


def verify_local_deep_index_exhaustion() -> dict[str, object]:
    p, q, layer = 97, 11, 1
    prefix, maximum_index, labels = owner_window(p, q, layer)
    assert (prefix, maximum_index, labels) == (6, 1, (6, 17))
    profiles = direct_rank_one_box_profiles((0, 1), q, 1, maximum_index)
    assert profiles == (((0, 1), 1, 0),)
    indices = profiles[0][0]
    assert tuple(valuation(p + 4 * value, q) for value in labels) == (2, 1)
    assert tuple(canonical_vertex(value) for value in labels) == (
        (6, 1, 6),
        (17, 1, 17),
    )

    deeper = deep_indices(p, q, layer, maximum_index)
    assert owner_prefix(p, q**2) == 6
    assert deeper == (0,)
    assert set(deeper).issubset(indices)

    return {
        "owner_indices": indices,
        "source_labels": labels,
        "deep_indices": deeper,
        "unused_local_deep_indices": (),
        "local_exhaustion_implies_global_obstruction": False,
        "global_occurrence_status": "UNDECIDED",
    }


def verify_two_point_distance_family() -> dict[str, object]:
    p, q, layer = 97, 3, 1
    _, maximum_index, _ = owner_window(p, q, layer)
    direct = {}
    closed_form = {}
    for separation in range(1, 13):
        direct[separation] = bool(
            direct_rank_one_box_profiles((0, separation), q, 1, maximum_index)
        )
        # Y=1+3Z, hence the difference ideal is separation+3*separation*Z.
        distance = affine_ideal_distance(separation, separation * q)
        closed_form[separation] = distance <= maximum_index
    assert direct == closed_form
    assert tuple(key for key, value in direct.items() if value) == tuple(range(1, 8))
    singleton = direct_rank_one_box_profiles((0,), q, 1, maximum_index)
    assert len(singleton) == maximum_index + 1
    return {
        "checked_separations": len(direct),
        "admitted": tuple(key for key, value in direct.items() if value),
    }


def verify() -> None:
    positive = verify_positive_boundary_profile()
    range_no_go = verify_strict_range_obstruction()
    deep_exhaustion = verify_local_deep_index_exhaustion()
    family = verify_two_point_distance_family()
    print("verified: affine dual-profile boundary", positive)
    print("verified: strict owner-window range obstruction", range_no_go)
    print("verified: local unused deep-index exhaustion", deep_exhaustion)
    print("verified: two-point affine-ideal distance family", family)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
