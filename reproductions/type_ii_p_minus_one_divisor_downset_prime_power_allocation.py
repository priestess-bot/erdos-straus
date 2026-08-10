#!/usr/bin/env python3
"""Verify the p-1 Type II endpoint downset and allocation controls."""

from __future__ import annotations

import argparse

import sympy


def endpoint_envelope(rank_parameter: int) -> int:
    lower = (rank_parameter + 5) // 4
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


def endpoint_capacity_domain(base: int) -> tuple[int, ...]:
    return tuple(
        cofactor
        for cofactor in sympy.divisors(base)
        if cofactor <= endpoint_envelope(base // cofactor)
    )


def minimal_forbidden_antichain(base: int) -> tuple[int, ...]:
    divisors = tuple(sympy.divisors(base))
    forbidden = {
        cofactor
        for cofactor in divisors
        if cofactor > endpoint_envelope(base // cofactor)
    }
    return tuple(
        cofactor
        for cofactor in divisors
        if cofactor in forbidden
        and not any(
            proper in forbidden and cofactor % proper == 0
            for proper in divisors
            if proper < cofactor
        )
    )


def type_ii_hit_cofactors(prime: int) -> tuple[int, ...]:
    base = (prime - 1) // 4
    hits: list[int] = []
    for cofactor in sympy.divisors(base):
        rank_parameter = base // cofactor
        modulus = 4 * cofactor - 1
        first_denominator = cofactor * (rank_parameter + 1)
        if any(
            divisor < first_denominator and (first_denominator + divisor) % modulus == 0
            for divisor in sympy.divisors(first_denominator * first_denominator)
        ):
            hits.append(cofactor)
    return tuple(hits)


def verify_downset(base: int) -> None:
    divisors = tuple(sympy.divisors(base))
    capacity = set(endpoint_capacity_domain(base))
    forbidden = set(divisors) - capacity
    boundary = set(minimal_forbidden_antichain(base))

    for larger in capacity:
        for smaller in divisors:
            if larger % smaller == 0 and smaller not in capacity:
                raise AssertionError(
                    f"endpoint capacity domain is not down-closed for U={base}"
                )

    for smaller in forbidden:
        for larger in divisors:
            if larger % smaller == 0 and larger not in forbidden:
                raise AssertionError(f"forbidden set is not up-closed for U={base}")

    reconstructed = {
        cofactor
        for cofactor in divisors
        if not any(cofactor % forbidden_chunk == 0 for forbidden_chunk in boundary)
    }
    if reconstructed != capacity:
        raise AssertionError(f"minimal forbidden antichain failed for U={base}")

    ranks = tuple(sympy.divisors(base))
    for smaller_rank in ranks:
        for larger_rank in ranks:
            if larger_rank % smaller_rank == 0 and endpoint_envelope(
                smaller_rank
            ) > endpoint_envelope(larger_rank):
                raise AssertionError(
                    f"divisibility monotonicity failed in control U={base}"
                )
        if endpoint_envelope(smaller_rank) != endpoint_closed_form(smaller_rank):
            raise AssertionError(f"closed endpoint formula failed for r={smaller_rank}")


def verify() -> None:
    fixtures = {
        601: {
            "base": 150,
            "domain": (1, 2, 3, 5, 6),
            "boundary": (10, 15, 25),
            "hits": (2, 3),
        },
        1_321: {
            "base": 330,
            "domain": (1, 2, 3, 5, 6, 10, 11, 15),
            "boundary": (22, 30, 33, 55),
            "hits": (2, 6, 10, 15),
        },
        67_369: {
            "base": 16_842,
            "domain": (1, 2, 3, 6, 7, 14, 21, 42),
            "boundary": (401,),
            "hits": (),
        },
    }

    for prime, fixture in fixtures.items():
        base = fixture["base"]
        if not (sympy.isprime(prime) and prime % 24 == 1 and (prime - 1) // 4 == base):
            raise AssertionError(f"core-prime fixture failed for p={prime}")
        verify_downset(base)
        if endpoint_capacity_domain(base) != fixture["domain"]:
            raise AssertionError(f"endpoint capacity domain changed for p={prime}")
        if minimal_forbidden_antichain(base) != fixture["boundary"]:
            raise AssertionError(f"forbidden antichain changed for p={prime}")
        if type_ii_hit_cofactors(prime) != fixture["hits"]:
            raise AssertionError(f"Type II hit set changed for p={prime}")

    domain_601 = set(fixtures[601]["domain"])
    if not (
        5 in domain_601
        and 25 not in domain_601
        and endpoint_envelope(150 // 25) == 6
        and all(sympy.factorint(cofactor).get(5, 0) <= 1 for cofactor in domain_601)
    ):
        raise AssertionError("prime-power allocation control failed for p=601")

    domain_1321 = set(fixtures[1_321]["domain"])
    boundary_1321 = set(fixtures[1_321]["boundary"])
    if not (
        {5, 11} <= domain_1321
        and 55 in boundary_1321
        and endpoint_envelope(330 // 55) == 6
        and all(cofactor % 55 for cofactor in domain_1321)
    ):
        raise AssertionError("cross-prime forbidden-chunk control failed for p=1321")

    if not (
        fixtures[67_369]["boundary"] == (401,)
        and fixtures[67_369]["domain"] == tuple(sympy.divisors(42))
    ):
        raise AssertionError("single-large-prime control failed for p=67369")

    print("PASS: TYPE_II_P_MINUS_ONE_DIVISOR_DOWNSET_PRIME_POWER_ALLOCATION")
    print("p601=prime_power_5^2_forbidden")
    print("p1321=cross_prime_5x11_forbidden_without_single_coordinate_exclusion")
    print("p67369=single_boundary_401_and_type_II_empty")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
