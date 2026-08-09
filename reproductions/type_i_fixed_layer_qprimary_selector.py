#!/usr/bin/env python3
"""Verify the fixed-layer q-primary representation/dual/capacity selector."""

from __future__ import annotations

from cmath import exp, pi
from itertools import product
from math import gcd


def box_vectors(budgets: tuple[int, ...]):
    return product(*(range(-budget, budget + 1) for budget in budgets))


def fixed_layer_stats(
    modulus: int,
    fixed_layer: set[int],
    generators: tuple[int, ...],
    budgets: tuple[int, ...],
    target: int,
    characters: tuple[int, ...],
) -> tuple[int, int, int, int]:
    pairs = []
    for fixed in fixed_layer:
        for vector in box_vectors(budgets):
            value = (fixed + sum(g * z for g, z in zip(generators, vector))) % modulus
            pairs.append((fixed, vector, value))

    annihilator = {
        value
        for value in range(modulus)
        if all((character * value) % modulus == 0 for character in characters)
    }
    exact = sum(value == target % modulus for _, _, value in pairs)
    filtered = sum(
        (value - target) % modulus in annihilator for _, _, value in pairs
    )
    volume = len(pairs)
    threshold = len(fixed_layer) * (2 ** len(generators))
    return exact, filtered, volume, threshold


def stabilizer(modulus: int, fixed_layer: set[int]) -> set[int]:
    return {
        shift
        for shift in range(modulus)
        if {(shift + value) % modulus for value in fixed_layer} == fixed_layer
    }


def character_order(modulus: int, character: int) -> int:
    return modulus // gcd(modulus, character)


def is_prime_power(value: int, prime: int) -> bool:
    if value == 1:
        return True
    while value % prime == 0:
        value //= prime
    return value == 1


def verify_q_primary(modulus: int, characters: tuple[int, ...], prime: int) -> None:
    assert 0 in characters
    assert all((a + b) % modulus in characters for a in characters for b in characters)
    assert all(is_prime_power(character_order(modulus, character), prime)
               for character in characters)


def fourier_sum(
    modulus: int,
    fixed_layer: set[int],
    generators: tuple[int, ...],
    budgets: tuple[int, ...],
    character: int,
) -> complex:
    total = 0j
    for fixed in fixed_layer:
        for vector in box_vectors(budgets):
            value = fixed + sum(g * z for g, z in zip(generators, vector))
            total += exp(2j * pi * character * value / modulus)
    return total


def choose_branch(
    modulus: int,
    fixed_layer: set[int],
    generators: tuple[int, ...],
    budgets: tuple[int, ...],
    target: int,
    characters: tuple[int, ...],
) -> dict[str, object]:
    exact, filtered, volume, threshold = fixed_layer_stats(
        modulus, fixed_layer, generators, budgets, target, characters
    )
    size = len(characters)
    if exact > threshold:
        branch = "NEIGHBOR_TERMINAL"
    elif filtered > threshold:
        branch = "Q_PRIMARY_QUOTIENT_SATURATED"
    elif volume > size * threshold:
        deficits = {
            character: -(
                exp(-2j * pi * character * target / modulus)
                * fourier_sum(modulus, fixed_layer, generators, budgets, character)
            ).real
            for character in characters
            if character != 0
        }
        character, deficit = max(deficits.items(), key=lambda item: (item[1], -item[0]))
        lower_bound = (volume - size * filtered) / (size - 1)
        branch = "Q_PRIMARY_FIXED_LAYER_FOURIER_DEFICIT"
        assert deficit + 1e-9 >= lower_bound
        return {
            "branch": branch,
            "exact": exact,
            "filtered": filtered,
            "volume": volume,
            "threshold": threshold,
            "character": character,
            "deficit": deficit,
            "lower_bound": lower_bound,
        }
    else:
        branch = "Q_PRIMARY_FIXED_LAYER_BOX_CAPACITY"
    return {
        "branch": branch,
        "exact": exact,
        "filtered": filtered,
        "volume": volume,
        "threshold": threshold,
    }


def verify() -> None:
    near = choose_branch(3, {0}, (1, 1), (2, 2), 0, (0, 1, 2))
    assert near["branch"] == "NEIGHBOR_TERMINAL"
    assert near["exact"] > near["threshold"]

    saturation = choose_branch(6, {0}, (1,), (3,), 1, (0, 3))
    assert saturation["branch"] == "Q_PRIMARY_QUOTIENT_SATURATED"
    assert saturation["exact"] <= saturation["threshold"] < saturation["filtered"]

    deficit = choose_branch(6, {0}, (1,), (2,), 1, (0, 3))
    assert deficit["branch"] == "Q_PRIMARY_FIXED_LAYER_FOURIER_DEFICIT"
    assert deficit["lower_bound"] == 1
    assert abs(deficit["deficit"] - 1) < 1e-9

    capacity = choose_branch(6, {0}, (1,), (1,), 1, (0, 3))
    assert capacity["branch"] == "Q_PRIMARY_FIXED_LAYER_BOX_CAPACITY"
    assert capacity["volume"] <= 2 * capacity["threshold"]

    modulus = 12
    fixed_layer = {0, 4, 8}
    stabilizer_set = stabilizer(modulus, fixed_layer)
    assert stabilizer_set == fixed_layer
    characters = (0, 3, 6, 9)
    verify_q_primary(modulus, characters, 2)
    assert all(
        all((character * shift) % modulus == 0 for shift in stabilizer_set)
        for character in characters
    )
    full = fourier_sum(modulus, fixed_layer, (1,), (1,), 3)
    quotient = fourier_sum(4, {0}, (1,), (1,), 3 % 4)
    assert abs(full - len(stabilizer_set) * quotient) < 1e-9
    full_stats = fixed_layer_stats(modulus, fixed_layer, (1,), (1,), 0, characters)
    quotient_stats = fixed_layer_stats(4, {0}, (1,), (1,), 0, (0, 1, 2, 3))
    assert full_stats[0] == quotient_stats[0]
    assert full_stats[1] == len(stabilizer_set) * quotient_stats[1]
    assert full_stats[2] == len(stabilizer_set) * quotient_stats[2]

    print("verified fixed-layer q-primary representation/dual/capacity selector")
    print({
        "near": near,
        "saturation": saturation,
        "deficit": deficit,
        "capacity": capacity,
        "stabilizer": {"P": sorted(stabilizer_set), "fourier_scale": len(stabilizer_set)},
    })


if __name__ == "__main__":
    verify()
