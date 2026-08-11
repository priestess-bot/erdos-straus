#!/usr/bin/env python3
"""Verify antipodal physical capacity in symmetric Type II divisor fibers."""

from __future__ import annotations

import argparse
from itertools import product
from math import gcd

import sympy

from type_ii_p_minus_one_jacobi_odd_kernel_affine_box import (
    direct_target,
    reduced_target,
    state_data,
)


def divisor_value(factors: dict[int, int], vector: tuple[int, ...]) -> int:
    value = 1
    for (prime_factor, exponent), coordinate in zip(
        factors.items(), vector, strict=True
    ):
        value *= prime_factor ** (exponent + coordinate)
    return value


def verify_antipodal_fiber(
    modulus: int,
    first_denominator: int,
    factors: dict[int, int],
    is_target,
) -> list[tuple[tuple[int, ...], int]]:
    ranges = tuple(range(-exponent, exponent + 1) for exponent in factors.values())
    rows = []
    for vector in product(*ranges):
        if not is_target(vector):
            continue
        complement = tuple(-coordinate for coordinate in vector)
        if not is_target(complement):
            raise AssertionError("target fiber is not closed under antipodes")
        divisor = divisor_value(factors, vector)
        complement_divisor = divisor_value(factors, complement)
        if divisor * complement_divisor != first_denominator**2:
            raise AssertionError("physical complement product changed")
        if divisor == first_denominator:
            raise AssertionError("target fiber acquired a fixed-size point")
        if (divisor < first_denominator) == (
            complement_divisor < first_denominator
        ):
            raise AssertionError("antipodal pair does not straddle the size gate")
        rows.append((vector, divisor))

    lower = sum(divisor < first_denominator for _, divisor in rows)
    upper = sum(divisor > first_denominator for _, divisor in rows)
    if lower != upper or lower + upper != len(rows):
        raise AssertionError("target fiber is not split equally by the size gate")
    return rows


def verify_cyclic_fixture(
    prime: int,
    cofactor: int,
    generator: int,
    expected_mode_counts: dict[tuple[int, ...], tuple[int, int, int]],
) -> None:
    data = state_data(prime, cofactor, generator)
    data["factor_order"] = tuple(data["factors"])
    rows = verify_antipodal_fiber(
        data["state"].modulus,
        data["state"].first_denominator,
        data["factors"],
        lambda vector: direct_target(data, vector),
    )

    factor_order = data["factor_order"]
    mode_counts: dict[tuple[int, ...], list[int]] = {}
    for vector, divisor in rows:
        mode = tuple(
            vector[factor_order.index(prime_factor)] % 2
            for prime_factor in data["negative"]
        )
        complement = tuple(-coordinate for coordinate in vector)
        complement_mode = tuple(
            complement[factor_order.index(prime_factor)] % 2
            for prime_factor in data["negative"]
        )
        if mode != complement_mode:
            raise AssertionError("antipode left its Jacobi parity mode")
        if not reduced_target(data, vector) or not reduced_target(data, complement):
            raise AssertionError("reduced odd-kernel mode is not antipodally closed")
        counts = mode_counts.setdefault(mode, [0, 0, 0])
        counts[0] += 1
        counts[1] += int(divisor < data["state"].first_denominator)
        counts[2] += int(divisor > data["state"].first_denominator)

    normalized = {mode: tuple(counts) for mode, counts in mode_counts.items()}
    if normalized != expected_mode_counts:
        raise AssertionError(
            f"mode capacity changed for p={prime}, q={cofactor}: {normalized}"
        )


def verify_noncyclic_control() -> None:
    prime = 41
    modulus = 15
    first_denominator = 14
    factors = {2: 1, 7: 1}
    if modulus != 4 * first_denominator - prime:
        raise AssertionError("noncyclic control left its Type II state")
    inverse = pow(first_denominator, -1, modulus)

    def is_target(vector: tuple[int, ...]) -> bool:
        divisor = divisor_value(factors, vector)
        return divisor * inverse % modulus == modulus - 1

    rows = verify_antipodal_fiber(
        modulus, first_denominator, factors, is_target
    )
    if rows != [((-1, -1), 1), ((1, 1), 196)]:
        raise AssertionError(f"noncyclic control changed: {rows}")

    units = [value for value in range(1, modulus) if gcd(value, modulus) == 1]
    generated = {
        pow(2, a, modulus) * pow(7, b, modulus) % modulus
        for a in range(4)
        for b in range(4)
    }
    if generated != set(units):
        raise AssertionError("2 and 7 no longer generate U(15)")
    if max(int(sympy.n_order(value, modulus)) for value in units) == len(units):
        raise AssertionError("U(15) unexpectedly passed the cyclic control")

    divisor = 1
    second_denominator = prime * (first_denominator + divisor) // modulus
    third_denominator = (
        prime
        * (first_denominator + first_denominator**2 // divisor)
        // modulus
    )
    if (second_denominator, third_denominator) != (41, 574):
        raise AssertionError("p=41 Type II reconstruction changed")
    if (
        4 * first_denominator * second_denominator * third_denominator
        != prime
        * (
            second_denominator * third_denominator
            + first_denominator * third_denominator
            + first_denominator * second_denominator
        )
    ):
        raise AssertionError("p=41 reconstructed denominators are not a solution")


def verify() -> None:
    verify_cyclic_fixture(73, 2, 3, {(1,): (4, 2, 2)})
    verify_cyclic_fixture(337, 6, 5, {(1,): (4, 2, 2)})
    verify_cyclic_fixture(67_369, 7, 2, {})
    verify_cyclic_fixture(67_369, 21, 2, {})
    verify_cyclic_fixture(67_369, 42, 5, {})
    verify_noncyclic_control()

    print("PASS: TYPE_II_SYMMETRIC_DIVISOR_FIBER_ANTIPODAL_CAPACITY")
    print("p73=p337=each_mode_4_targets_2_below_2_above")
    print("p67369=q7_q21_q42=empty")
    print("p41_noncyclic_U15=target_pair_1_196")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
