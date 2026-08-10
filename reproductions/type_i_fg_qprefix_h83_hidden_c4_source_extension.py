#!/usr/bin/env python3
"""Verify the hidden C4 sheet role and source-extension boundary for p=557281."""

from __future__ import annotations

import argparse
import math
from fractions import Fraction
from itertools import product


P = 557_281
SOURCE_MODULUS = 199
TARGET_MODULUS = 728
Q = 83
TARGET_D = 182


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors(value: int) -> tuple[int, ...]:
    result = [1]
    for prime, exponent in factorization(value).items():
        result = [entry * prime**power for entry in result for power in range(exponent + 1)]
    return tuple(sorted(result))


def multiplicative_order(value: int, modulus: int) -> int:
    assert math.gcd(value, modulus) == 1
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("multiplicative order not found")


def unit_group(modulus: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, modulus) if math.gcd(value, modulus) == 1)


def carmichael(value: int) -> int:
    component_exponents: list[int] = []
    for prime, exponent in factorization(value).items():
        if prime == 2 and exponent >= 3:
            component_exponents.append(2 ** (exponent - 2))
        else:
            component_exponents.append((prime - 1) * prime ** (exponent - 1))
    return math.lcm(*component_exponents)


def psi_four(value: int) -> int:
    """Quartic character represented in mu_4(13)={1,5,8,12}."""
    assert math.gcd(value, 13) == 1
    return pow(value % 13, 3, 13)


def eta_three(value: int) -> int:
    assert math.gcd(value, 13) == 1
    return pow(value % 13, 4, 13)


def chi_two(value: int) -> int:
    assert value % 2 == 1
    return 1 if value % 8 in (1, 7) else -1


def verify_relative_c4() -> dict[str, object]:
    order_three = multiplicative_order(3, TARGET_MODULUS)
    order_83 = multiplicative_order(Q, TARGET_MODULUS)
    three_group = {pow(3, exponent, TARGET_MODULUS) for exponent in range(order_three)}
    eighty_three_group = {
        pow(Q, exponent, TARGET_MODULUS) for exponent in range(order_83)
    }
    joint_group = {
        left * right % TARGET_MODULUS
        for left, right in product(three_group, eighty_three_group)
    }

    assert order_three == 6
    assert order_83 == 4
    assert three_group == {1, 3, 9, 27, 81, 243}
    assert eighty_three_group == {1, 83, 337, 307}
    assert pow(3, 3, TARGET_MODULUS) == 27
    assert pow(Q, 2, TARGET_MODULUS) == 337
    assert three_group & eighty_three_group == {1}
    assert len(joint_group) == 24

    mu_four = {1, 5, 8, 12}
    assert {psi_four(value) for value in unit_group(TARGET_MODULUS)} == mu_four
    assert psi_four(3) == 1
    assert psi_four(Q) == 8
    assert multiplicative_order(psi_four(Q), 13) == 4
    assert {value for value in joint_group if psi_four(value) == 1} == three_group

    relative_cosets = {
        frozenset(value * base % TARGET_MODULUS for base in three_group)
        for value in eighty_three_group
    }
    assert len(relative_cosets) == 4
    assert len({psi_four(next(iter(coset))) for coset in relative_cosets}) == 4

    return {
        "status": "P557_H83_RELATIVE_TRANSPORT_QUOTIENT_C4",
        "order_3_mod_728": order_three,
        "order_83_mod_728": order_83,
        "joint_group_order": len(joint_group),
        "relative_quotient_order": len(relative_cosets),
        "psi4_of_3": psi_four(3),
        "psi4_of_83": psi_four(Q),
    }


def verify_sheet_state() -> dict[str, object]:
    records = tuple(
        (exponent_three, exponent_83, pow(3, exponent_three) * pow(Q, exponent_83))
        for exponent_three, exponent_83 in product(range(4), range(3))
    )
    residues = tuple(value % TARGET_MODULUS for _, _, value in records)
    assert len(records) == 12
    assert len(set(residues)) == 12

    for exponent_three in range(4):
        fiber = [
            value
            for a_value, _, value in records
            if a_value == exponent_three
        ]
        assert len({eta_three(value) for value in fiber}) == 1
        assert tuple(psi_four(value) for value in fiber) == (1, 8, 12)

    assert chi_two(3) == -1
    assert chi_two(Q) == -1
    for exponent_three, exponent_83, value in records:
        base = pow(3, exponent_three)
        relative_chi_two = chi_two(value) * chi_two(base)
        psi_square = 1 if pow(psi_four(value), 2, 13) == 1 else -1
        assert relative_chi_two == (-1) ** exponent_83
        assert psi_square == relative_chi_two

    return {
        "status": (
            "P557_ARITHMETIC_SHEET_IDENTITY_NOT_RECOVERABLE_FROM_ETA_KEY"
        ),
        "record_count": len(records),
        "distinct_target_residue_count": len(set(residues)),
        "eta_fiber_size_per_base_record": 3,
        "quartic_sheet_phases": (1, 8, 12),
        "chi2_descends_to_relative_quotient": False,
        "physical_receipts_proved": False,
        "record_to_state_injectivity_assumed": False,
    }


def verify_source_obstruction() -> dict[str, object]:
    assert multiplicative_order(3, SOURCE_MODULUS) == 198
    source_units = unit_group(SOURCE_MODULUS)
    assert len(source_units) == 198

    hom_generator_images = tuple(value for value in range(4) if 198 * value % 4 == 0)
    assert hom_generator_images == (0, 2)
    assert tuple(value % 2 for value in hom_generator_images) == (0, 0)
    assert 4 not in divisors(198)

    source_logs = (106, 138, 189, 165)
    assert pow(3, source_logs[0], SOURCE_MODULUS) == 2
    assert source_logs[0] % 2 == 0
    assert source_logs[2] % 2 == 1
    assert source_logs[3] % 2 == 1
    target_relative_c2_phase = 1 if pow(psi_four(Q), 2, 13) == 12 else 0
    assert target_relative_c2_phase == 1
    assert source_logs[0] % 2 != target_relative_c2_phase

    # An image equal to 83 would violate the exponent relation directly.
    assert pow(Q, 198, TARGET_MODULUS) == 337
    assert pow(Q, 198, TARGET_MODULUS) != 1
    assert 198 * 1 % 4 == 2

    return {
        "status": (
            "P557_WHOLE_SOURCE_RELATION_HOMOMORPHIC_C4_ADAPTER_NO_GO"
        ),
        "source_group_order_and_exponent": 198,
        "source_c4_hom_generator_images": hom_generator_images,
        "source_c2_character_lifts_through_c4": False,
        "factor2_named_edge_c2_phase": source_logs[0] % 2,
        "target_83_relative_c2_phase": target_relative_c2_phase,
        "named_edge_status": "P557_CURRENT_FACTOR2_EDGE_C2_SHEET_ADAPTER_NO_GO",
        "partial_relation_preserving_status": (
            "P557_ORIGINAL_STATE_RELATION_PRESERVING_C4_"
            "ADAPTER_INCLUDING_B1_NO_GO"
        ),
        "primitive_sheet_relation_target_value": 198 * 1 % 4,
        "set_theoretic_partial_physical_adapter_proved": False,
    }


def verify_abstract_extension() -> dict[str, object]:
    # C_396 contains C_198 as <t^2>; t -> 1 mod 4 realizes a relative
    # primitive phase at index 2, while its restriction to C_198 has order 2.
    relative_extension_order = 396
    relative_embedding_phases = {2 * exponent % 4 for exponent in range(198)}
    assert relative_extension_order // 198 == 2
    assert relative_extension_order % 4 == 0
    assert relative_embedding_phases == {0, 2}
    assert 1 not in relative_embedding_phases

    images = {
        (pow(3, exponent, TARGET_MODULUS) * pow(Q, cargo, TARGET_MODULUS))
        % TARGET_MODULUS
        for exponent, cargo in product(range(198), range(4))
    }
    kernel = tuple(
        (exponent, cargo)
        for exponent, cargo in product(range(198), range(4))
        if pow(3, exponent, TARGET_MODULUS) * pow(Q, cargo, TARGET_MODULUS)
        % TARGET_MODULUS
        == 1
    )
    labelled_prefix = {
        pow(3, exponent, TARGET_MODULUS) * pow(Q, cargo, TARGET_MODULUS)
        % TARGET_MODULUS
        for exponent, cargo in product(range(4), range(3))
    }

    assert len(images) == 24
    assert len(kernel) == 33
    assert all(cargo == 0 and exponent % 6 == 0 for exponent, cargo in kernel)
    assert len(labelled_prefix) == 12
    assert (198 * 4) // len(images) == len(kernel)
    assert (198 * 4) % 24 == 0
    assert all((198 * index) % 24 != 0 for index in (1, 2, 3))

    return {
        "status": "P557_ABSTRACT_C4_LABELLED_STATE_EXTENSION_REALIZED",
        "relative_c4_extension_minimum_index": 2,
        "relative_index_two_restriction_image": tuple(sorted(relative_embedding_phases)),
        "external_trivial_coordinate_or_full_joint_minimum_index": 4,
        "joint_image_order": len(images),
        "kernel_order": len(kernel),
        "labelled_prefix_image_count": len(labelled_prefix),
        "physical_source_receipt_proved": False,
    }


def verify_role_guided_terminal() -> dict[str, object]:
    proper_divisors = tuple(value for value in divisors(TARGET_D) if value < TARGET_D)
    c4_capable = tuple(
        value for value in proper_divisors if carmichael(4 * value) % 4 == 0
    )
    assert proper_divisors == (1, 2, 7, 13, 14, 26, 91)
    assert c4_capable == (13, 26, 91)

    d_value = 13
    a_value = 1
    c_value = 13
    h_value = 103
    k_value = (h_value + 1) // (4 * d_value)
    target_numerator = P + 4 * a_value * d_value
    assert k_value == 2
    assert target_numerator == 557_333 == 7 * 103 * 773
    assert target_numerator % h_value == 0
    assert h_value % (4 * d_value) == 4 * d_value - 1
    b_value = (k_value * P + a_value) // h_value
    assert b_value == 10_821
    assert h_value * b_value == k_value * P + a_value
    assert b_value > a_value

    denominators = (
        b_value * d_value,
        P * d_value * k_value,
        P * b_value * c_value * k_value,
    )
    assert denominators == (140_673, 14_489_306, 156_788_780_226)
    assert sum((Fraction(1, value) for value in denominators), Fraction()) == Fraction(4, P)

    return {
        "status": "P557_ROLE_GUIDED_D13_TYPEII_TERMINAL",
        "c4_capable_proper_divisors": c4_capable,
        "A_C_K_h_B": (a_value, c_value, k_value, h_value, b_value),
        "denominators": denominators,
    }


def verify() -> None:
    relative = verify_relative_c4()
    sheets = verify_sheet_state()
    source = verify_source_obstruction()
    extension = verify_abstract_extension()
    terminal = verify_role_guided_terminal()
    print("PASS: FG_QPREFIX_H83_HIDDEN_C4_SOURCE_EXTENSION")
    print(relative)
    print(sheets)
    print(source)
    print(extension)
    print(terminal)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
