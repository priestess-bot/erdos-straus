#!/usr/bin/env python3
"""Verify the endpoint envelope, large-prime allocation, and p=67369 dispatch."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product

import sympy


def k_bounds(rank_parameter: int) -> tuple[int, int]:
    return (rank_parameter + 5) // 4, (2 * rank_parameter + 1) // 3


def endpoint_envelope(rank_parameter: int) -> int:
    lower, _ = k_bounds(rank_parameter)
    denominator = 4 * lower - rank_parameter - 1
    return lower * (lower + 1) // denominator


def endpoint_closed_form(rank_parameter: int) -> int:
    quotient, residue = divmod(rank_parameter, 4)
    if residue == 0:
        return (quotient + 1) * (quotient + 2) // 3
    if residue == 1:
        return (quotient + 1) * (quotient + 2) // 2
    if residue == 2:
        return (quotient + 1) * (quotient + 2)
    return (quotient + 2) * (quotient + 3) // 4


def verify_endpoint_identity(rank_parameter: int) -> None:
    lower, upper = k_bounds(rank_parameter)
    denominator = 4 * lower - rank_parameter - 1
    endpoint = Fraction(lower * (lower + 1), denominator)
    for linear_parameter in range(lower, upper + 1):
        offset = linear_parameter - lower
        current_denominator = 4 * linear_parameter - rank_parameter - 1
        current = Fraction(
            linear_parameter * (linear_parameter + 1), current_denominator
        )
        difference_numerator = offset * (
            4 * lower * (lower + 1) - denominator * (2 * lower + offset + 1)
        )
        stated_difference = Fraction(
            difference_numerator, denominator * (denominator + 4 * offset)
        )
        if endpoint - current != stated_difference or current > endpoint:
            raise AssertionError(f"endpoint envelope failed for r={rank_parameter}")

    envelope = endpoint_envelope(rank_parameter)
    if not (
        envelope == endpoint_closed_form(rank_parameter)
        and Fraction(envelope)
        <= Fraction((rank_parameter + 2) * (rank_parameter + 6), 16)
    ):
        raise AssertionError(f"closed endpoint bound failed for r={rank_parameter}")


def signed_residues(modulus: int, factors: dict[int, int]) -> set[int]:
    residues: set[int] = set()
    bases = tuple(factors)
    for exponents in product(
        *(range(-factors[base], factors[base] + 1) for base in bases)
    ):
        residue = 1
        for base, exponent in zip(bases, exponents, strict=True):
            if exponent >= 0:
                residue = residue * pow(base, exponent, modulus) % modulus
            else:
                inverse_power = pow(base, -exponent, modulus)
                residue = residue * pow(inverse_power, -1, modulus) % modulus
        residues.add(residue)
    return residues


def split_log_sets(
    modulus: int,
    generator: int,
    factors: dict[int, int],
    split_index: int,
) -> tuple[dict[int, int], set[int], set[int]]:
    order = int(sympy.totient(modulus))
    bases = tuple(factors)
    logarithms = {
        base: int(sympy.discrete_log(modulus, base % modulus, generator))
        for base in bases
    }
    left_bases = bases[:split_index]
    right_bases = bases[split_index:]
    left = {
        sum(
            exponent * logarithms[base]
            for base, exponent in zip(left_bases, exponents, strict=True)
        )
        % order
        for exponents in product(
            *(range(-factors[base], factors[base] + 1) for base in left_bases)
        )
    }
    target_minus_right = {
        (
            order // 2
            - sum(
                exponent * logarithms[base]
                for base, exponent in zip(right_bases, exponents, strict=True)
            )
        )
        % order
        for exponents in product(
            *(range(-factors[base], factors[base] + 1) for base in right_bases)
        )
    }
    return logarithms, left, target_minus_right


def verify_p67369_dispatch() -> None:
    prime = 67_369
    base = (prime - 1) // 4
    small_part = 42
    large_prime = 401
    if not (
        sympy.isprime(prime)
        and prime % 24 == 1
        and base == small_part * large_prime
        and sympy.isprime(large_prime)
        and 16 * large_prime > (small_part + 2) * (small_part + 6)
    ):
        raise AssertionError("large-prime allocation hypothesis failed")

    for rank_parameter in sympy.divisors(base):
        cofactor = base // rank_parameter
        if rank_parameter % large_prime:
            if not (
                rank_parameter in sympy.divisors(small_part)
                and cofactor >= large_prime
                and cofactor > endpoint_envelope(rank_parameter)
            ):
                raise AssertionError("large prime was not forced into the source rank")

    expected_factors = {
        1: {16_843: 1},
        2: {2: 2, 4_211: 1},
        3: {3: 1, 5: 1, 1_123: 1},
        6: {2: 4, 3: 4, 13: 1},
        7: {7: 1, 29: 1, 83: 1},
        14: {2: 3, 7: 2, 43: 1},
        21: {3: 1, 7: 1, 11: 1, 73: 1},
        42: {2: 2, 3: 2, 7: 1, 67: 1},
    }
    g_fibers = {1, 2, 3, 6, 14}
    f_fixtures = {
        7: {
            "generator": 2,
            "logs": {7: 16, 29: 1, 83: 1},
            "left": {0, 2, 16},
            "right": {7, 8, 9, 10, 11},
        },
        21: {
            "generator": 2,
            "logs": {3: 72, 7: 8, 11: 24, 73: 69},
            "left": {0, 2, 8, 10, 18, 64, 72, 74, 80},
            "right": {4, 17, 28, 30, 41, 52, 54, 65, 78},
        },
        42: {
            "generator": 5,
            "logs": {2: 40, 3: 94, 7: 118, 67: 165},
            "left": {
                0,
                8,
                14,
                18,
                22,
                32,
                40,
                54,
                58,
                62,
                64,
                72,
                80,
                86,
                94,
                102,
                104,
                108,
                112,
                126,
                134,
                144,
                148,
                152,
                158,
            },
            "right": {34, 35, 36, 82, 83, 84, 130, 131, 132},
        },
    }

    for cofactor, expected in expected_factors.items():
        modulus = 4 * cofactor - 1
        first_denominator = base + cofactor
        factors = {
            int(key): value for key, value in sympy.factorint(first_denominator).items()
        }
        if factors != expected:
            raise AssertionError(f"factorization changed for q={cofactor}")
        residues = signed_residues(modulus, factors)
        if modulus - 1 in residues:
            raise AssertionError(f"Type II target unexpectedly hit for q={cofactor}")

        direct_hits = tuple(
            divisor
            for divisor in sympy.divisors(first_denominator * first_denominator)
            if (first_denominator + divisor) % modulus == 0
        )
        if direct_hits:
            raise AssertionError(
                f"direct divisor fiber unexpectedly hit for q={cofactor}"
            )

        if cofactor in g_fibers:
            if not (
                all(sympy.jacobi_symbol(factor, modulus) == 1 for factor in factors)
                and sympy.jacobi_symbol(-1, modulus) == -1
            ):
                raise AssertionError(f"Jacobi G certificate failed for q={cofactor}")
            continue

        fixture = f_fixtures[cofactor]
        generator = fixture["generator"]
        order = int(sympy.totient(modulus))
        if not (
            sympy.n_order(generator, modulus) == order
            and pow(generator, order // 2, modulus) == modulus - 1
        ):
            raise AssertionError(f"primitive-root control failed for q={cofactor}")
        logs, left, target_minus_right = split_log_sets(
            modulus, generator, factors, len(factors) // 2
        )
        if not (
            logs == fixture["logs"]
            and left == fixture["left"]
            and target_minus_right == fixture["right"]
            and left.isdisjoint(target_minus_right)
        ):
            raise AssertionError(f"F log-box certificate failed for q={cofactor}")

    gap = 31
    first_denominator = 16_850
    divisor = 3_370
    denominator_2 = (prime * first_denominator + divisor) // gap
    denominator_3 = (
        prime * (first_denominator + prime * first_denominator**2 // divisor) // gap
    )
    target = (first_denominator, denominator_2, denominator_3)
    if not (
        first_denominator * first_denominator % divisor == 0
        and (prime * first_denominator + divisor) % gap == 0
        and target == (16_850, 36_618_420, 12_334_731_684_900)
        and sum((Fraction(1, value) for value in target), Fraction())
        == Fraction(4, prime)
    ):
        raise AssertionError("p=67369 Type I terminal failed")


def verify() -> None:
    for rank_parameter in range(1, 129):
        verify_endpoint_identity(rank_parameter)
    verify_p67369_dispatch()

    print("PASS: TYPE_II_P_MINUS_ONE_ENDPOINT_ENVELOPE_LARGE_PRIME_ALLOCATION")
    print("endpoint_formula_checked_r=1..128")
    print("p67369_allocation=q_divides_42")
    print("p67369_fibers=5_G_plus_3_F_all_empty")
    print("p67369_dispatch=P_MINUS_ONE_TYPE_II_EMPTY->TYPE_I_TERMINAL")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
