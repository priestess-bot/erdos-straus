#!/usr/bin/env python3
"""Verify the fixed-layer stabilizer quotient and its Fourier obstruction."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

try:
    from fixed_layer_quotient_fourier import cyclic_quotient_fourier_profile
except ModuleNotFoundError:
    from reproductions.fixed_layer_quotient_fourier import cyclic_quotient_fourier_profile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-fixed-layer-stabilizer-fourier-results.json"
)


# For the focused receipt H/P is cyclic of order six.  Writing zeta_6 in the
# integral basis {1, zeta_6}, with zeta_6^2 = zeta_6 - 1, keeps the Fourier
# norm exact instead of relying on a floating-point phase comparison.
SixRoot = tuple[int, int]


def six_root_power(exponent: int) -> SixRoot:
    return {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 1),
        3: (-1, 0),
        4: (0, -1),
        5: (1, -1),
    }[exponent % 6]


def six_root_add(left: SixRoot, right: SixRoot) -> SixRoot:
    return left[0] + right[0], left[1] + right[1]


def six_root_multiply(left: SixRoot, right: SixRoot) -> SixRoot:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c + b * d


def six_root_norm_squared(value: SixRoot) -> int:
    a, b = value
    return a * a + a * b + b * b


def six_root_sum(exponents: list[int]) -> SixRoot:
    result: SixRoot = (0, 0)
    for exponent in exponents:
        result = six_root_add(result, six_root_power(exponent))
    return result


def factorization(value: int) -> dict[int, int]:
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


def units(modulus: int) -> set[int]:
    return {value for value in range(1, modulus) if math.gcd(value, modulus) == 1}


def multiply_sets(left: set[int], right: set[int], modulus: int) -> set[int]:
    return {(a * b) % modulus for a in left for b in right}


def divisor_residues(factors: dict[int, int], modulus: int) -> set[int]:
    result = {1}
    for prime, exponent in factors.items():
        result = multiply_sets(
            result,
            {pow(prime, power, modulus) for power in range(exponent + 1)},
            modulus,
        )
    return result


def generated_subgroup(generators: set[int], modulus: int) -> set[int]:
    subgroup = {1}
    changed = True
    while changed:
        changed = False
        expanded = multiply_sets(subgroup, generators | {1}, modulus)
        if not expanded <= subgroup:
            subgroup |= expanded
            changed = True
    return subgroup


def stabilizer(group: set[int], subset: set[int], modulus: int) -> set[int]:
    return {
        candidate
        for candidate in group
        if {(candidate * value) % modulus for value in subset} == subset
    }


def coset_partition(
    group: set[int], stabilizer_set: set[int], modulus: int
) -> tuple[dict[int, int], list[frozenset[int]], list[int]]:
    index: dict[int, int] = {}
    cosets: list[frozenset[int]] = []
    representatives: list[int] = []
    for value in sorted(group):
        if value in index:
            continue
        coset = frozenset((value * h) % modulus for h in stabilizer_set)
        coset_index = len(cosets)
        cosets.append(coset)
        representatives.append(value)
        for member in coset:
            index[member] = coset_index
    return index, cosets, representatives


def quotient_multiplication(
    index: dict[int, int], representatives: list[int], left: int, right: int, modulus: int
) -> int:
    return index[(representatives[left] * representatives[right]) % modulus]


def order_in_quotient(
    index: dict[int, int], representatives: list[int], value: int, modulus: int
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


def count_raw(
    group: set[int], fixed_layer: set[int], q: int, nu: int, modulus: int
) -> dict[int, int]:
    counts = {value: 0 for value in group}
    for fixed in fixed_layer:
        for exponent in range(-nu, nu + 1):
            value = (fixed * pow(q, exponent, modulus)) % modulus
            counts[value] += 1
    return counts


def quotient_counts(
    fixed_indices: set[int], q: int, nu: int, index: dict[int, int],
    representatives: list[int], modulus: int
) -> dict[int, int]:
    counts = {value: 0 for value in range(len(representatives))}
    identity = index[1]
    for fixed in fixed_indices:
        for exponent in range(-nu, nu + 1):
            power = pow(q, exponent, modulus)
            power_index = index[power]
            value = quotient_multiplication(
                index, representatives, fixed, power_index, modulus
            )
            counts[value] += 1
    if counts[identity] < 0:
        raise AssertionError("unreachable quotient count guard")
    return counts


def verify_case() -> dict[str, object]:
    prime, modulus, fixed_integer = 193, 63, 608
    K = (prime * modulus + 1) // 4
    if K != 3040 or K != fixed_integer * 5:
        raise AssertionError("arithmetic fixed-layer case changed")
    K_factors = factorization(K)
    fixed_factors = factorization(fixed_integer)
    residual_prime, residual_exponent = 5, K_factors[5]
    H = generated_subgroup(set(K_factors), modulus)
    unit_group = units(modulus)
    if H != unit_group:
        raise AssertionError("prime support did not generate the unit group")
    J = divisor_residues(fixed_factors, modulus)
    if not J <= H or 1 not in J:
        raise AssertionError("fixed layer left the generated subgroup")
    P = stabilizer(H, J, modulus)
    if not P <= J:
        raise AssertionError("fixed-layer stabilizer is not contained in J")
    index, cosets, representatives = coset_partition(H, P, modulus)
    fixed_indices = {index[value] for value in J}
    quotient_stabilizer = {
        candidate
        for candidate in range(len(cosets))
        if {
            quotient_multiplication(index, representatives, candidate, value, modulus)
            for value in fixed_indices
        }
        == fixed_indices
    }
    if quotient_stabilizer != {index[1]}:
        raise AssertionError("quotient fixed layer retained a nontrivial stabilizer")

    raw = count_raw(H, J, residual_prime, residual_exponent, modulus)
    quotient = quotient_counts(
        fixed_indices,
        residual_prime,
        residual_exponent,
        index,
        representatives,
        modulus,
    )
    for value in H:
        if raw[value] != quotient[index[value]]:
            raise AssertionError("raw/quotient representation count mismatch")
    target = (-1) % modulus
    if raw[target] != 0 or quotient[index[target]] != 0:
        raise AssertionError("focused state unexpectedly hit the target")

    quotient_order = len(cosets)
    generator = next(
        value
        for value in sorted(H)
        if order_in_quotient(index, representatives, value, modulus) == quotient_order
    )
    generator_index = index[generator]
    quotient_coordinates: dict[int, int] = {}
    current = index[1]
    for coordinate in range(quotient_order):
        if current in quotient_coordinates:
            raise AssertionError("quotient generator coordinates are not unique")
        quotient_coordinates[current] = coordinate
        current = quotient_multiplication(
            index, representatives, current, generator_index, modulus
        )
    if len(quotient_coordinates) != quotient_order:
        raise AssertionError("quotient generator did not span H/P")

    q_coordinate = quotient_coordinates[index[residual_prime]]
    J_coordinates = sorted(quotient_coordinates[value] for value in fixed_indices)
    target_coordinate = quotient_coordinates[index[target]]
    box_size = 2 * residual_exponent + 1
    amplitudes: list[dict[str, object]] = []
    for character_index in range(1, quotient_order):
        fixed_sum = six_root_sum(
            [character_index * coordinate for coordinate in J_coordinates]
        )
        dirichlet_sum = six_root_sum(
            [
                character_index * q_coordinate * exponent
                for exponent in range(-residual_exponent, residual_exponent + 1)
            ]
        )
        fourier_value = six_root_multiply(fixed_sum, dirichlet_sum)
        amplitude_squared = six_root_norm_squared(fourier_value)
        amplitudes.append(
            {
                "character_index": character_index,
                "algebraic_value_basis_1_zeta6": list(fourier_value),
                "amplitude_squared": amplitude_squared,
                "amplitude": math.sqrt(amplitude_squared),
            }
        )
    threshold_quotient = len(fixed_indices) * box_size / (quotient_order - 1)
    max_amplitude_squared = max(int(row["amplitude_squared"]) for row in amplitudes)
    max_amplitude = math.sqrt(max_amplitude_squared)
    if max_amplitude + 1e-9 < threshold_quotient:
        raise AssertionError("quotient Fourier lower bound failed")
    if max_amplitude_squared != 12:
        raise AssertionError("focused quotient Fourier amplitude changed")
    threshold_lifted = len(J) * box_size / (quotient_order - 1)
    if len(P) * max_amplitude + 1e-9 < threshold_lifted:
        raise AssertionError("lifted Fourier lower bound failed")
    chosen = min(
        (
            row
            for row in amplitudes
            if int(row["amplitude_squared"]) == max_amplitude_squared
        ),
        key=lambda row: int(row["character_index"]),
    )
    if chosen["character_index"] != 1:
        raise AssertionError("canonical focused Fourier character changed")

    character_order = quotient_order // math.gcd(
        quotient_order, int(chosen["character_index"])
    )
    if character_order != quotient_order:
        raise AssertionError("focused character is not primitive in the quotient")

    character_index = int(chosen["character_index"])
    phase_numerator = (character_index * q_coordinate) % quotient_order
    phase_distance = min(phase_numerator, quotient_order - phase_numerator)
    if phase_distance == 0:
        raise AssertionError("selected character is trivial on the residual block")
    phase_debt_fraction = Fraction(
        min(quotient_order * quotient_order,
            residual_exponent * residual_exponent * phase_distance * phase_distance),
        quotient_order * quotient_order,
    )
    finite_order_debt_fraction = Fraction(
        min(character_order * character_order,
            residual_exponent * residual_exponent),
        character_order * character_order,
    )

    generic_spectrum = cyclic_quotient_fourier_profile(
        modulus=modulus,
        group=H,
        fixed_layer=J,
        residual_blocks=[(residual_prime, residual_exponent)],
        target=target,
    )
    if generic_spectrum["quotient_order"] != quotient_order:
        raise AssertionError("generic quotient profile order changed")
    if generic_spectrum["target_count"] != raw[target]:
        raise AssertionError("generic quotient target count changed")
    if not generic_spectrum["missing_target_fourier_witness_exists"]:
        raise AssertionError("generic missing-target Fourier witness disappeared")
    first_phase = generic_spectrum["character_profile"][0]
    if first_phase["q_primary_projections"].get("3") != [2]:
        raise AssertionError("focused q-primary Fourier projection changed")
    if "5" in first_phase["q_primary_projections"]:
        raise AssertionError("q not dividing the character order was projected")

    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "fixed_integer": fixed_integer,
        "fixed_layer_factors": sorted(fixed_factors.items()),
        "residual_block": {"prime": residual_prime, "exponent": residual_exponent},
        "H": sorted(H),
        "J": sorted(J),
        "P": sorted(P),
        "quotient_order": quotient_order,
        "quotient_fixed_layer": sorted(fixed_indices),
        "quotient_stabilizer": sorted(quotient_stabilizer),
        "target": target,
        "target_quotient_coordinate": target_coordinate,
        "raw_target_count": raw[target],
        "quotient_target_count": quotient[index[target]],
        "quotient_generator": generator,
        "quotient_generator_order": quotient_order,
        "quotient_fixed_coordinates": J_coordinates,
        "quotient_residual_coordinate": q_coordinate,
        "quotient_fourier_threshold": threshold_quotient,
        "quotient_fourier_threshold_fraction": [
            len(fixed_indices) * box_size,
            quotient_order - 1,
        ],
        "lifted_fourier_threshold": threshold_lifted,
        "lifted_fourier_threshold_fraction": [len(J) * box_size, quotient_order - 1],
        "maximum_quotient_fourier_amplitude_squared": max_amplitude_squared,
        "maximum_quotient_fourier_amplitude": max_amplitude,
        "selected_character_phase_distance_fraction": [phase_distance, quotient_order],
        "phase_debt_fraction": [phase_debt_fraction.numerator, phase_debt_fraction.denominator],
        "finite_order_debt_fraction": [
            finite_order_debt_fraction.numerator,
            finite_order_debt_fraction.denominator,
        ],
        "carrier_mapping_status": "unproved",
        "selected_character": chosen,
        "generic_spectrum_profile": generic_spectrum,
        "typed_certificate": {
            "certificate_type": "fixed_layer_quotient_fourier",
            "selector_status": "analysis_evidence",
            "state_class": "F",
            "phase": "DUAL_CERTIFICATE",
            "quotient_order": quotient_order,
            "stabilizer_order": len(P),
            "character_order": character_order,
            "amplitude_squared": max_amplitude_squared,
            "threshold_fraction": [
                len(fixed_indices) * box_size,
                quotient_order - 1,
            ],
            "lifted_threshold_fraction": [len(J) * box_size, quotient_order - 1],
            "finite_order_debt_fraction": [
                finite_order_debt_fraction.numerator,
                finite_order_debt_fraction.denominator,
            ],
            "carrier_mapping_status": "unproved",
            "recursive_edge_eligible": False,
        },
        "classification": "fixed_layer_stabilizer_quotient_fourier_miss",
    }


def verify_companion_case() -> dict[str, object]:
    """Exercise the generic profile on a cyclic quotient of a different order."""
    prime, modulus, K = 97, 27, 655
    if (prime * modulus + 1) // 4 != K:
        raise AssertionError("companion arithmetic case changed")
    group = generated_subgroup({5, 131}, modulus)
    fixed_layer = {1, 5}
    profile = cyclic_quotient_fourier_profile(
        modulus=modulus,
        group=group,
        fixed_layer=fixed_layer,
        residual_blocks=[(131, 1)],
        target=-1,
    )
    if profile["quotient_order"] != 18 or profile["stabilizer_order"] != 1:
        raise AssertionError("companion quotient shape changed")
    if profile["target_count"] != 0:
        raise AssertionError("companion target unexpectedly hit")
    if not profile["missing_target_fourier_witness_exists"]:
        raise AssertionError("companion Fourier witness disappeared")
    if profile["character_profile"][0]["q_primary_projections"].get("3") != [4]:
        raise AssertionError("companion q-primary Fourier projection changed")
    return {
        "prime": prime,
        "R": modulus,
        "K": K,
        "fixed_layer": sorted(fixed_layer),
        "classification": "cyclic_quotient_fourier_profile_companion",
        "profile": profile,
    }


def build_results() -> dict[str, object]:
    return {
        "schema_version": 1,
        "arithmetic": (
            "Exact fixed-layer stabilizer quotient, representation-count identity, "
            "and quotient Fourier lower-bound check for one core state."
        ),
        "scope_note": (
            "Focused algebraic receipt only; the quotient theorem is general, while this "
            "case does not establish a cross-state capacity contradiction."
        ),
        "receipt": verify_case(),
        "generic_companion": verify_companion_case(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_results(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.verify:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("stored focused result does not match regenerated output")
        print("verified", args.output)
        return
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
