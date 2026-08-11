#!/usr/bin/env python3
"""Verify the rank-one Jacobi source-SNF and anchor dichotomy."""

from __future__ import annotations

import argparse
from itertools import product

import sympy

from type_ii_p_minus_one_jacobi_source_localization import (
    derive_state,
    generated_subgroup,
)


def source_primes(state) -> tuple[int, ...]:
    return tuple(int(value) for value in sympy.factorint(state.first_denominator))


def evaluation_row(state) -> tuple[int, ...]:
    return tuple(
        int(source_prime in state.negative_sources)
        for source_prime in source_primes(state)
    )


def verify_relation_annihilation(state) -> None:
    factors = source_primes(state)
    exponents = tuple(
        range(-int(sympy.factorint(state.first_denominator)[source_prime]),
              int(sympy.factorint(state.first_denominator)[source_prime]) + 1)
        for source_prime in factors
    )
    row = evaluation_row(state)
    for vector in product(*exponents):
        residue = 1
        for source_prime, exponent in zip(factors, vector, strict=True):
            residue = residue * pow(source_prime, exponent, state.modulus) % state.modulus
        if residue == 1 and sum(
            coordinate * bit for coordinate, bit in zip(vector, row, strict=True)
        ) % 2:
            raise AssertionError("Jacobi row failed on a source relation")


def verify_state(state, expected_rank: int, expected_target: bool) -> None:
    row = evaluation_row(state)
    rank = int(any(row))
    if rank != expected_rank:
        raise AssertionError(
            f"Jacobi source-SNF rank changed for q={state.cofactor}: {row}"
        )

    generated = generated_subgroup(state.modulus, source_primes(state))
    target_in_source = state.modulus - 1 in generated
    if target_in_source != expected_target:
        raise AssertionError(
            f"anchor membership changed for q={state.cofactor}: "
            f"{target_in_source}"
        )
    verify_relation_annihilation(state)

    parity_values = {
        sum(coordinate * bit for coordinate, bit in zip(vector, row, strict=True)) % 2
        for vector in product(
            *(
                range(
                    -int(sympy.factorint(state.first_denominator)[source_prime]),
                    int(sympy.factorint(state.first_denominator)[source_prime]) + 1,
                )
                for source_prime in source_primes(state)
            )
        )
    }
    expected_parity = {0} if expected_rank == 0 else {0, 1}
    if parity_values != expected_parity:
        raise AssertionError(
            f"C2 signed-box projection changed for q={state.cofactor}: "
            f"{parity_values}"
        )


def verify() -> None:
    controls = {
        73: {
            1: (0, False),
            2: (1, True),
            3: (1, True),
            6: (0, False),
        },
        337: {
            1: (1, True),
            6: (1, True),
        },
        67_369: {
            1: (0, False),
            2: (0, False),
            3: (0, False),
            6: (0, False),
            7: (1, True),
            14: (0, False),
            21: (1, True),
            42: (1, True),
        },
    }

    for prime, states in controls.items():
        for cofactor, (rank, target_in_source) in states.items():
            state = derive_state(prime, cofactor)
            verify_state(state, rank, target_in_source)

    state_67369_q7 = derive_state(67_369, 7)
    if not (
        evaluation_row(state_67369_q7) == (0, 1, 1)
        and len(state_67369_q7.negative_sources) == 2
    ):
        raise AssertionError("q=7 negative factors were incorrectly charged as rank two")

    state_337_q6 = derive_state(337, 6)
    if not (
        state_337_q6.negative_sources == (5,)
        and state_337_q6.modulus - 1
        in generated_subgroup(
            state_337_q6.modulus, source_primes(state_337_q6)
        )
    ):
        raise AssertionError("p=337 q=6 source-target control failed")

    print("PASS: TYPE_II_P_MINUS_ONE_JACOBI_SOURCE_SNF_RANK_ONE")
    print("p73=zero_or_one_rank_and_anchor_dichotomy")
    print("p337=multiple_negative_factors_compress_to_rank_one")
    print("p67369=five_G_three_rank_one_source_target_states")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
