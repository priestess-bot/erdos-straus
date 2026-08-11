#!/usr/bin/env python3
"""Verify the neutral-carrier no-go for weighted Jacobi box overflow."""

from __future__ import annotations

import argparse
from itertools import product

import sympy

import short_certificate
from type_ii_p_minus_one_jacobi_odd_kernel_affine_box import (
    direct_target,
    state_data,
)
from type_ii_p_minus_one_jacobi_source_localization import derive_state


PRIME = 67_369


def physical_overflow_weight(
    factors: dict[int, int], vector: tuple[int, ...]
) -> int:
    weight = 1
    for (prime_factor, exponent), coordinate in zip(
        factors.items(), vector, strict=True
    ):
        weight *= prime_factor ** max(abs(coordinate) - exponent, 0)
    return weight


def target_hits_below_weight(
    data: dict, maximum_weight: int
) -> list[tuple[int, ...]]:
    ranges = []
    for prime_factor, exponent in data["factors"].items():
        extra = 0
        power = prime_factor
        while power <= maximum_weight:
            extra += 1
            power *= prime_factor
        ranges.append(range(-exponent - extra, exponent + extra + 1))

    return sorted(
        vector
        for vector in product(*ranges)
        if physical_overflow_weight(data["factors"], vector) <= maximum_weight
        and direct_target(data, vector)
    )


def unit_shell_hits(data: dict) -> list[tuple[int, ...]]:
    factors = tuple(data["factors"])
    exponents = tuple(data["factors"].values())
    hits: set[tuple[int, ...]] = set()
    for active, exponent in enumerate(exponents):
        for sign in (-1, 1):
            overflow_value = sign * (exponent + 1)
            ranges = tuple(
                (overflow_value,)
                if index == active
                else range(-other_exponent, other_exponent + 1)
                for index, other_exponent in enumerate(exponents)
            )
            for vector in product(*ranges):
                if direct_target(data, vector):
                    hits.add(vector)

    for vector in hits:
        overflow = sum(
            max(abs(coordinate) - data["factors"][prime_factor], 0)
            for prime_factor, coordinate in zip(factors, vector, strict=True)
        )
        if overflow != 1:
            raise AssertionError("unit shell contains a non-unit overflow")
    return sorted(hits)


def overflow_support(
    factors: dict[int, int], vector: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        prime_factor
        for (prime_factor, exponent), coordinate in zip(
            factors.items(), vector, strict=True
        )
        if abs(coordinate) > exponent
    )


def ratio_pair(
    factors: dict[int, int], vector: tuple[int, ...]
) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for prime_factor, coordinate in zip(factors, vector, strict=True):
        if coordinate > 0:
            numerator *= prime_factor**coordinate
        elif coordinate < 0:
            denominator *= prime_factor ** (-coordinate)
    return numerator, denominator


def legal_shared_gaps(prime: int, numerator: int, denominator: int) -> list[int]:
    return [
        int(gap)
        for gap in sympy.divisors(numerator + denominator)
        if gap % 4 == 3 and 3 <= gap <= prime - 2
    ]


def direct_signed_box_hits(prime: int, cofactor: int) -> list[tuple[int, ...]]:
    state = derive_state(prime, cofactor)
    factors = {
        int(prime_factor): int(exponent)
        for prime_factor, exponent in sympy.factorint(
            state.first_denominator
        ).items()
    }
    hits = []
    for vector in product(
        *(range(-exponent, exponent + 1) for exponent in factors.values())
    ):
        residue = 1
        for prime_factor, coordinate in zip(factors, vector, strict=True):
            residue = residue * pow(prime_factor, coordinate, state.modulus)
            residue %= state.modulus
        if residue == state.modulus - 1:
            hits.append(vector)
    return hits


def certificates_at_gap(
    gap: int, spf: list[int]
) -> tuple[
    short_certificate.GapCertificate | None,
    short_certificate.GapCertificate | None,
]:
    return (
        short_certificate.type_i_residue_certificate(PRIME, gap, spf),
        short_certificate.type_ii_residue_certificate(PRIME, gap, spf),
    )


def verify_weighted_minimum(
    cofactor: int,
    generator: int,
    expected_negative: int,
    expected_hits: list[tuple[int, ...]],
) -> dict:
    data = state_data(PRIME, cofactor, generator)
    hits = target_hits_below_weight(data, 3)
    if hits != expected_hits:
        raise AssertionError(
            f"weighted minimum changed for q={cofactor}: {hits}"
        )
    if any(physical_overflow_weight(data["factors"], vector) != 3 for vector in hits):
        raise AssertionError("the declared minimum does not have physical weight 3")
    if set(hits) != {hits[0], tuple(-value for value in hits[0])}:
        raise AssertionError("weighted minimum is not one antipodal orbit")
    if data["negative"] != (expected_negative,):
        raise AssertionError("negative-source control changed")
    for vector in hits:
        if overflow_support(data["factors"], vector) != (3,):
            raise AssertionError("weighted overflow left the carrier prime 3")
        if data["beta"][3] != 0 or cofactor % 3:
            raise AssertionError("overflow prime 3 is not a neutral q-carrier")
        negative_index = tuple(data["factors"]).index(expected_negative)
        if abs(vector[negative_index]) > data["factors"][expected_negative]:
            raise AssertionError("negative source unexpectedly overflowed")
    return data


def verify() -> None:
    spf = short_certificate.smallest_prime_factors((PRIME + 200) // 4 + 2)

    data_q21 = verify_weighted_minimum(
        21,
        2,
        73,
        [(-2, 1, 0, -1), (2, -1, 0, 1)],
    )
    data_q42 = verify_weighted_minimum(
        42,
        5,
        67,
        [(-2, 3, -1, 1), (2, -3, 1, -1)],
    )

    q21_ratio = ratio_pair(data_q21["factors"], (-2, 1, 0, -1))
    if q21_ratio != (7, 657) or sum(q21_ratio) != 664:
        raise AssertionError("q=21 minimum relation changed")
    if legal_shared_gaps(PRIME, *q21_ratio) != [83]:
        raise AssertionError("q=21 shared-gap list changed")
    if certificates_at_gap(83, spf) != (None, None):
        raise AssertionError("q=21 minimum unexpectedly acquired a terminal")

    q42_ratio = ratio_pair(data_q42["factors"], (-2, 3, -1, 1))
    if q42_ratio != (1809, 28) or sum(q42_ratio) != 1837:
        raise AssertionError("q=42 weighted minimum relation changed")
    if legal_shared_gaps(PRIME, *q42_ratio) != [11, 167]:
        raise AssertionError("q=42 weighted shared-gap list changed")
    if any(certificates_at_gap(gap, spf) != (None, None) for gap in (11, 167)):
        raise AssertionError("q=42 weighted minimum unexpectedly acquired a terminal")

    expected_unit_q42 = [
        (-2, 1, 2, 1),
        (-2, 3, -1, 1),
        (2, -3, 1, -1),
        (2, -1, -2, -1),
    ]
    if unit_shell_hits(data_q42) != expected_unit_q42:
        raise AssertionError("q=42 unweighted unit shell changed")
    positive_ratio = ratio_pair(data_q42["factors"], (-2, 1, 2, 1))
    if positive_ratio != (9849, 4) or sum(positive_ratio) != 9853:
        raise AssertionError("q=42 positive-control relation changed")
    if legal_shared_gaps(PRIME, *positive_ratio) != [59, 167]:
        raise AssertionError("q=42 positive-control gaps changed")
    type_i_59, type_ii_59 = certificates_at_gap(59, spf)
    if type_i_59 is None or type_ii_59 is not None:
        raise AssertionError("gap-59 Type I positive control changed")
    if (
        type_i_59.divisor,
        type_i_59.x,
        type_i_59.y,
        type_i_59.z,
    ) != (151_713, 16_857, 19_250_694, 144_100_000_454):
        raise AssertionError("gap-59 Type I reconstruction changed")

    for deflated_q, gap in ((7, 27), (14, 55)):
        if direct_signed_box_hits(PRIME, deflated_q):
            raise AssertionError(
                f"carrier deflation q={deflated_q} acquired a Type II hit"
            )
        if certificates_at_gap(gap, spf) != (None, None):
            raise AssertionError(
                f"carrier deflation gap={gap} acquired a terminal"
            )

    type_i_31, type_ii_31 = certificates_at_gap(31, spf)
    if type_i_31 is None or type_ii_31 is not None:
        raise AssertionError("external gap-31 terminal changed")
    if (
        type_i_31.divisor,
        type_i_31.x,
        type_i_31.y,
        type_i_31.z,
    ) != (421_250, 16_850, 36_631_900, 98_714_178_844):
        raise AssertionError("gap-31 Type I reconstruction changed")

    print(
        "PASS: "
        "TYPE_II_P_MINUS_ONE_JACOBI_WEIGHTED_MINIMUM_OVERFLOW_NEUTRAL_CARRIER_NO_GO"
    )
    print("p67369_q21=W3_carrier3_gap83_empty_q_to_7_empty")
    print("p67369_q42=W3_carrier3_gaps11_167_empty_q_to_14_empty")
    print("q42_unweighted_other_orbit=gap59_TypeI_positive_control")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
