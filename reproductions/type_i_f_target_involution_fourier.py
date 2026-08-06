#!/usr/bin/env python3
"""Verify target-odd Fourier energy and direct q-primary phase collapse."""

from __future__ import annotations

import argparse
from math import gcd

try:
    from fixed_layer_quotient_fourier import (
        cyclic_quotient_fourier_profile,
        generated_subgroup,
    )
except ModuleNotFoundError:
    from reproductions.fixed_layer_quotient_fourier import (
        cyclic_quotient_fourier_profile,
        generated_subgroup,
    )


SixRoot = tuple[int, int]


def six_root_power(exponent: int) -> SixRoot:
    """Return zeta_6**exponent in the integral basis (1, zeta_6)."""
    return {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 1),
        3: (-1, 0),
        4: (0, -1),
        5: (1, -1),
    }[exponent % 6]


def six_root_norm_squared(value: SixRoot) -> int:
    """Compute the exact norm in Q(zeta_6)."""
    first, second = value
    return first * first + first * second + second * second


def six_root_fourier_norm(coefficients: list[int], character_index: int) -> int:
    """Evaluate a C6 character exactly when its root has order dividing six."""
    first = 0
    second = 0
    for coordinate, count in enumerate(coefficients):
        root_first, root_second = six_root_power(character_index * coordinate)
        first += count * root_first
        second += count * root_second
    return six_root_norm_squared((first, second))


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value) for positive integers used in the fixed controls."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> dict[int, int]:
    """Factor the two fixed control integers by trial division."""
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = 1
    return factors


def centered_residues(factors: dict[int, int], modulus: int) -> set[int]:
    """Build the centered finite exponent layer for one fixed factor block."""
    residues = {1}
    for prime, bound in factors.items():
        residues = {
            residue * pow(prime, exponent, modulus) % modulus
            for residue in residues
            for exponent in range(-bound, bound + 1)
        }
    return residues


def target_q_primary_phase(
    *, quotient_order: int, character_index: int, target_coordinate: int, prime: int
) -> tuple[int, int]:
    """Return (q-exponent, direct target phase) for one cyclic character."""
    character_order = quotient_order // gcd(quotient_order, character_index)
    exponent = valuation(character_order, prime)
    if exponent == 0:
        raise AssertionError("requested prime does not divide the character order")
    q_modulus = prime**exponent
    reduced_index = character_index // gcd(quotient_order, character_index)
    phase_mod_order = (reduced_index * target_coordinate) % character_order
    phase = (character_order // q_modulus * phase_mod_order) % q_modulus
    if (2 * phase) % q_modulus:
        raise AssertionError("direct target phase is not an involution phase")
    return exponent, phase


def verify_target_odd_energy(
    profile: dict[str, object], expected_coefficients: list[int]
) -> dict[str, int]:
    """Check the target-odd Parseval identity entirely in integer arithmetic."""
    quotient_order = int(profile["quotient_order"])
    coefficients = [int(value) for value in profile["coefficient_vector"]]
    autocorrelation = [int(value) for value in profile["autocorrelation"]]
    target_coordinate = int(profile["target_coordinate"])
    if quotient_order % 2 or target_coordinate != quotient_order // 2:
        raise AssertionError("target did not remain the nontrivial involution")
    if coefficients != expected_coefficients or coefficients[target_coordinate] != 0:
        raise AssertionError("focused target-odd coefficient vector changed")
    if coefficients[0] < 1:
        raise AssertionError("zero residual representation disappeared")

    target_odd_indices = [index for index in range(quotient_order) if index % 2]
    if not target_odd_indices:
        raise AssertionError("cyclic involution has no target-odd characters")
    if any(
        valuation(quotient_order // gcd(quotient_order, index), 2)
        != valuation(quotient_order, 2)
        for index in target_odd_indices
    ):
        raise AssertionError("target-odd character lost full two-adic order")

    energy = quotient_order * (autocorrelation[0] - autocorrelation[target_coordinate]) // 2
    difference_square_sum = sum(
        (coefficients[index] - coefficients[(index + target_coordinate) % quotient_order]) ** 2
        for index in range(quotient_order)
    )
    if quotient_order * difference_square_sum % 4:
        raise AssertionError("target-odd energy ceased to be integral")
    if energy != quotient_order * difference_square_sum // 4:
        raise AssertionError("target-odd energy identity changed")
    if energy < quotient_order * coefficients[0] * coefficients[0] // 2:
        raise AssertionError("target-odd energy lower bound changed")
    return {
        "quotient_order": quotient_order,
        "target_coordinate": target_coordinate,
        "target_odd_energy": energy,
        "C_identity": autocorrelation[0],
        "C_target": autocorrelation[target_coordinate],
    }


def verify_c6_control() -> dict[str, object]:
    """Check the centered C6 F control without creating a result artifact."""
    prime, modulus, K = 193, 63, 3040
    if 4 * K != prime * modulus + 1 or factorization(K) != {2: 5, 5: 1, 19: 1}:
        raise AssertionError("C6 Type I control changed")
    group = generated_subgroup({2, 5, 19}, modulus)
    fixed_layer = centered_residues({2: 5, 19: 1}, modulus)
    profile = cyclic_quotient_fourier_profile(
        modulus=modulus,
        group=group,
        fixed_layer=fixed_layer,
        residual_blocks=[(5, 1)],
        target=-1,
    )
    energy = verify_target_odd_energy(profile, [3, 2, 1, 0, 1, 2])
    if energy != {
        "quotient_order": 6,
        "target_coordinate": 3,
        "target_odd_energy": 33,
        "C_identity": 19,
        "C_target": 8,
    }:
        raise AssertionError("C6 target-odd energy control changed")
    if [six_root_fourier_norm([3, 2, 1, 0, 1, 2], index) for index in (1, 3, 5)] != [16, 1, 16]:
        raise AssertionError("C6 target-odd Fourier norms changed")
    q_three = target_q_primary_phase(
        quotient_order=6, character_index=1, target_coordinate=3, prime=3
    )
    q_two = target_q_primary_phase(
        quotient_order=6, character_index=1, target_coordinate=3, prime=2
    )
    if q_three != (1, 0) or q_two != (1, 1):
        raise AssertionError("C6 direct q-primary target phases changed")
    return {"prime": prime, "R": modulus, "K": K, "energy": energy}


def verify_c18_control() -> dict[str, object]:
    """Check a second cyclic order and its direct target q-primary phases."""
    prime, modulus, K = 97, 27, 655
    if 4 * K != prime * modulus + 1:
        raise AssertionError("C18 Type I control changed")
    group = generated_subgroup({5, 131}, modulus)
    profile = cyclic_quotient_fourier_profile(
        modulus=modulus,
        group=group,
        fixed_layer={1, 5},
        residual_blocks=[(131, 1)],
        target=-1,
    )
    coefficients = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
    energy = verify_target_odd_energy(profile, coefficients)
    if energy != {
        "quotient_order": 18,
        "target_coordinate": 9,
        "target_odd_energy": 36,
        "C_identity": 6,
        "C_target": 2,
    }:
        raise AssertionError("C18 target-odd energy control changed")
    # k=3,15 have order six, so their C18 values use the exact C6 backend.
    if [six_root_fourier_norm(coefficients, index // 3) for index in (3, 15)] != [12, 12]:
        raise AssertionError("C18 order-six target-odd norms changed")
    q_three = target_q_primary_phase(
        quotient_order=18, character_index=3, target_coordinate=9, prime=3
    )
    q_two = target_q_primary_phase(
        quotient_order=18, character_index=3, target_coordinate=9, prime=2
    )
    if q_three != (1, 0) or q_two != (1, 1):
        raise AssertionError("C18 direct q-primary target phases changed")
    return {"prime": prime, "R": modulus, "K": K, "energy": energy}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify_c6_control()
    verify_c18_control()
    if args.verify:
        print("verified F target-involution Fourier controls")


if __name__ == "__main__":
    main()
