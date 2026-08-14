#!/usr/bin/env python3
"""Verify fixed controls for the strict-root canonical even-source gate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

from short_certificate import (
    GapCertificate,
    positive_divisors_from_spf,
    positive_divisors_square_product_from_spf,
    smallest_prime_factors,
    verify_certificate,
)
from type_i_root_capacity_general_endpoint_divisor_gate import chart


def canonical_even_complement(p: int, cofactor: int) -> tuple[int, int]:
    """Return the even source n and its odd complementary distance."""
    if not 1 <= cofactor <= p - 2:
        raise ValueError("strict cofactor is outside its canonical range")
    source = cofactor if cofactor % 2 == 0 else p - cofactor
    distance = p - source
    if not (2 <= source < p and source % 2 == 0 and distance % 2 == 1):
        raise AssertionError("canonical complement parity changed")
    return source, distance


def retained_standard_tail_factors(p: int, source: int) -> list[int]:
    """List exactly the sorted-tail factors for 4/p = 1/source + 1/u + 1/v."""
    remainder = 4 * source - p
    product = p * source
    if remainder <= 0:
        return []
    if gcd(remainder, product) != 1:
        raise AssertionError("standard-tail residual unexpectedly lost coprimality")
    spf = smallest_prime_factors(p)
    return [
        factor
        for factor in positive_divisors_square_product_from_spf(p, source, spf)
        if factor <= product and (product + factor) % remainder == 0
    ]


def compatible_odd_distance_rays(
    p: int, source: int, distance: int
) -> list[tuple[int, int, int]]:
    """Return the first arithmetic gate of the complete odd-distance fan."""
    spf = smallest_prime_factors(p)
    rays: list[tuple[int, int, int]] = []
    for shift in positive_divisors_from_spf(source, spf):
        quotient = source // shift
        if quotient <= 1 or (quotient - 1) % distance:
            continue
        multiplier = (quotient - 1) // distance
        if (shift * multiplier + 1) % 4 == 0:
            rays.append((shift, quotient, multiplier))
    return rays


def verify_standard_tail_positive_control() -> None:
    p, source, factor = 21_169, 12_198, 342
    remainder = 4 * source - p
    product = p * source
    factors = retained_standard_tail_factors(p, source)
    if factor not in factors:
        raise AssertionError("fixed high-half factor left the exact gate")
    companion = product * product // factor
    first = (product + factor) // remainder
    second = (product + companion) // remainder
    source_solution = (source // 2, source, source)
    target_solution = (source, first, second)
    certificate = GapCertificate(p, "I", 16_223, first, factor, source, second)
    if not (
        source > p // 2
        and factor <= product
        and product * product % factor == 0
        and (product + factor) % remainder == 0
        and (product + companion) % remainder == 0
        and Fraction(4, source)
        == sum((Fraction(1, value) for value in source_solution), Fraction())
        and Fraction(4, p)
        == sum((Fraction(1, value) for value in target_solution), Fraction())
        and verify_certificate(certificate)
    ):
        raise AssertionError("high-half standard-tail construction changed")


def verify_actual_root_control(
    p: int, root_parameter: int, expected_cofactor: int, expected_high_half: bool
) -> None:
    receipt = chart(p, root_parameter)
    cofactor = (-pow(receipt["E"], -1, p)) % p
    source, distance = canonical_even_complement(p, cofactor)
    remainder = 4 * source - p
    product = p * source
    tail_factors = retained_standard_tail_factors(p, source)
    rays = compatible_odd_distance_rays(p, source, distance)

    if not (
        receipt["u"] < receipt["M"]
        and receipt["Q"] > 1
        and 1 <= cofactor == expected_cofactor <= p - 2
        and (receipt["E"] * cofactor + 1) % p == 0
        and Fraction(4, source)
        == Fraction(1, source // 2) + Fraction(1, source) + Fraction(1, source)
        and (source > p // 2) == expected_high_half
        and not tail_factors
        and not rays
    ):
        raise AssertionError("actual strict-root complement gate changed")

    if expected_high_half:
        if not (
            source == 298
            and distance == 15
            and remainder == 879
            and product == 93_274
            and (-product) % remainder == 779
        ):
            raise AssertionError("high-half hard-root control changed")
    else:
        if not (
            4 * source > p
            and 2 * source < p
            and source == 36
            and distance == 37
            and remainder == 71
            and product == 2_628
            and (-product) % remainder == 70
            and source <= distance
        ):
            raise AssertionError("middle-band strict-root control changed")


def verify() -> None:
    verify_standard_tail_positive_control()
    verify_actual_root_control(73, 3, 37, False)
    verify_actual_root_control(313, 271, 298, True)
    print(
        "verified the canonical even-complement trichotomy, one high-half "
        "marked lift, and two actual strict-root selector boundaries"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
