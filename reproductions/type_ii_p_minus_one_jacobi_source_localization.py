#!/usr/bin/env python3
"""Verify Jacobi source localization and cross-q collision capacity."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import sympy


@dataclass(frozen=True)
class JacobiState:
    prime: int
    base: int
    cofactor: int
    rank_parameter: int
    modulus: int
    first_denominator: int
    negative_sources: tuple[int, ...]


def endpoint_envelope(rank_parameter: int) -> int:
    lower = (rank_parameter + 5) // 4
    denominator = 4 * lower - rank_parameter - 1
    return lower * (lower + 1) // denominator


def prime_symbol(prime: int, source_prime: int) -> int:
    return int(sympy.kronecker_symbol(prime, source_prime))


def derive_state(prime: int, cofactor: int) -> JacobiState:
    if not (sympy.isprime(prime) and prime % 4 == 1):
        raise AssertionError("p must be a prime congruent to 1 modulo 4")

    base = (prime - 1) // 4
    if base % cofactor:
        raise AssertionError("q must divide U=(p-1)/4")

    rank_parameter = base // cofactor
    modulus = 4 * cofactor - 1
    first_denominator = base + cofactor
    if first_denominator != cofactor * (rank_parameter + 1):
        raise AssertionError("p-1 factor chart identity failed")
    if math.gcd(modulus, first_denominator) != 1:
        raise AssertionError("source support is not a unit modulo m")

    carrier_primes = tuple(int(value) for value in sympy.factorint(cofactor))
    source_primes = tuple(
        int(value) for value in sympy.factorint(rank_parameter + 1)
    )
    for source_prime in carrier_primes:
        if int(sympy.jacobi_symbol(source_prime, modulus)) != 1:
            raise AssertionError(
                f"q-side Jacobi neutrality failed for p={prime}, q={cofactor}"
            )

    for source_prime in source_primes:
        jacobi_value = int(sympy.jacobi_symbol(source_prime, modulus))
        if jacobi_value != prime_symbol(prime, source_prime):
            raise AssertionError(
                f"source reciprocity failed for p={prime}, q={cofactor}"
            )

    negative_sources = tuple(
        source_prime
        for source_prime in source_primes
        if prime_symbol(prime, source_prime) == -1
    )
    if set(negative_sources) & set(carrier_primes):
        raise AssertionError("a negative source prime also divides q")

    support_primes = tuple(
        int(value) for value in sympy.factorint(first_denominator)
    )
    negative_support = tuple(
        source_prime
        for source_prime in support_primes
        if int(sympy.jacobi_symbol(source_prime, modulus)) == -1
    )
    if negative_support != negative_sources:
        raise AssertionError("negative support was not localized to r+1")
    if int(sympy.jacobi_symbol(-1, modulus)) != -1:
        raise AssertionError("target -1 is not Jacobi-negative")
    if not negative_sources and any(
        int(sympy.jacobi_symbol(source_prime, modulus)) != 1
        for source_prime in support_primes
    ):
        raise AssertionError("empty negative-source set did not yield a G separator")

    for source_prime in support_primes:
        incidence = (
            (base + cofactor) % source_prime == 0
            and prime_symbol(prime, source_prime) == -1
        )
        if incidence != (source_prime in negative_sources):
            raise AssertionError("U+q incidence formula failed")

    return JacobiState(
        prime=prime,
        base=base,
        cofactor=cofactor,
        rank_parameter=rank_parameter,
        modulus=modulus,
        first_denominator=first_denominator,
        negative_sources=negative_sources,
    )


def verify_hit_parity(state: JacobiState, divisor: int) -> None:
    first_denominator = state.first_denominator
    if not (
        divisor > 0
        and first_denominator * first_denominator % divisor == 0
        and divisor < first_denominator
        and (first_denominator + divisor) % state.modulus == 0
    ):
        raise AssertionError("declared divisor is not a Type II hit")

    denominator_factors = {
        int(source_prime): exponent
        for source_prime, exponent in sympy.factorint(first_denominator).items()
    }
    divisor_factors = {
        int(source_prime): exponent
        for source_prime, exponent in sympy.factorint(divisor).items()
    }
    negative_parity = sum(
        divisor_factors.get(source_prime, 0)
        - denominator_factors[source_prime]
        for source_prime in state.negative_sources
    )
    if negative_parity % 2 != 1:
        raise AssertionError("Type II hit did not cross an odd negative-source parity")

    ratio = divisor * pow(first_denominator, -1, state.modulus) % state.modulus
    if not (
        ratio == state.modulus - 1
        and int(sympy.jacobi_symbol(ratio, state.modulus)) == -1
    ):
        raise AssertionError("signed ratio did not equal the Jacobi-negative target")


def generated_subgroup(modulus: int, bases: tuple[int, ...]) -> set[int]:
    subgroup = {1}
    for base in bases:
        cyclic = set()
        value = 1
        while value not in cyclic:
            cyclic.add(value)
            value = value * base % modulus
        subgroup = {
            left * right % modulus for left in subgroup for right in cyclic
        }
    return subgroup


def occurrence_states(
    prime: int, cofactors: tuple[int, ...], source_prime: int
) -> tuple[int, ...]:
    return tuple(
        state.cofactor
        for state in (derive_state(prime, cofactor) for cofactor in cofactors)
        if source_prime in state.negative_sources
    )


def verify() -> None:
    states_73 = {
        cofactor: derive_state(73, cofactor) for cofactor in (1, 2, 3, 6)
    }
    expected_73 = {1: (), 2: (5,), 3: (7,), 6: ()}
    if {
        cofactor: state.negative_sources for cofactor, state in states_73.items()
    } != expected_73:
        raise AssertionError("p=73 negative-source fixture changed")
    verify_hit_parity(states_73[2], 1)

    states_337 = {
        cofactor: derive_state(337, cofactor) for cofactor in (1, 6)
    }
    if not (
        5 in states_337[1].negative_sources
        and states_337[6].negative_sources == (5,)
        and all(
            state.cofactor <= endpoint_envelope(state.rank_parameter)
            for state in states_337.values()
        )
    ):
        raise AssertionError("p=337 allowed-domain collision fixture failed")
    occurrences_337 = occurrence_states(337, (1, 6), 5)
    collision_bound_337 = (6 - 1) // 5 + 1
    if not (
        occurrences_337 == (1, 6)
        and len(occurrences_337) == collision_bound_337 == 2
        and (occurrences_337[1] - occurrences_337[0]) % 5 == 0
    ):
        raise AssertionError("cross-q collision bound did not attain equality")
    verify_hit_parity(states_337[6], 2)

    cofactors_67369 = (1, 2, 3, 6, 7, 14, 21, 42)
    states_67369 = {
        cofactor: derive_state(67_369, cofactor)
        for cofactor in cofactors_67369
    }
    expected_67369 = {
        1: (),
        2: (),
        3: (),
        6: (),
        7: (29, 83),
        14: (),
        21: (73,),
        42: (67,),
    }
    if {
        cofactor: state.negative_sources
        for cofactor, state in states_67369.items()
    } != expected_67369:
        raise AssertionError("p=67369 source localization changed")

    for cofactor in (7, 21, 42):
        state = states_67369[cofactor]
        support_primes = tuple(
            int(value) for value in sympy.factorint(state.first_denominator)
        )
        group_order = int(sympy.totient(state.modulus))
        if not (
            group_order % 2 == 0
            and (group_order // 2) % 2 == 1
            and state.modulus - 1
            in generated_subgroup(state.modulus, support_primes)
        ):
            raise AssertionError(
                f"negative source did not put -1 in support for q={cofactor}"
            )

    for cofactor in (1, 2, 3, 6, 14):
        state = states_67369[cofactor]
        support_primes = tuple(
            int(value) for value in sympy.factorint(state.first_denominator)
        )
        if state.modulus - 1 in generated_subgroup(state.modulus, support_primes):
            raise AssertionError(
                f"empty negative source unexpectedly reached -1 for q={cofactor}"
            )

    for source_prime in (29, 83, 73, 67):
        occurrences = occurrence_states(
            67_369, cofactors_67369, source_prime
        )
        interval_bound = (42 - 1) // source_prime + 1
        if len(occurrences) > interval_bound:
            raise AssertionError("p=67369 occurrence capacity failed")
        if any(
            (cofactor + 16_842) % source_prime
            for cofactor in occurrences
        ):
            raise AssertionError("p=67369 incidence residue failed")

    print("PASS: TYPE_II_P_MINUS_ONE_JACOBI_SOURCE_LOCALIZATION")
    print("p73=negative_source_parity_hit")
    print("p337=allowed_q_collision_capacity_equality")
    print("p67369=five_source_trivial_G_and_three_source_visible_F")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
