#!/usr/bin/env python3
"""Verify j=1 normalization and the two-adic target-fiber boundary."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def factorization(value: int) -> list[tuple[int, int]]:
    """Return the prime factorization of one positive control integer."""
    if value <= 0:
        raise AssertionError("factorization expects a positive integer")
    factors: list[tuple[int, int]] = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def is_prime(value: int) -> bool:
    """Use trial division for the two fixed prime controls."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def normalized_j_one_pair(A: int, B: int, j: int) -> tuple[int, int]:
    """Reduce 2^(1-j) A/B to its unique positive lowest-term pair."""
    if j < 1 or A <= 0 or B <= 0:
        raise AssertionError("invalid dyadic pair")
    ratio = Fraction(A, B * (2 ** (j - 1)))
    return ratio.numerator, ratio.denominator


def verify_dyadic_witness(
    *, p: int, R: int, K: int, A: int, B: int, j: int
) -> dict[str, int]:
    """Check one free divisor-pair witness and its canonical j=1 form."""
    L = 2 * K
    if not is_prime(p) or R % 2 != 1 or 4 * K != p * R + 1:
        raise AssertionError("Type I chart changed")
    if gcd(A, B) != 1 or L % A or L % B:
        raise AssertionError("dyadic pair is not a coprime L-divisor pair")
    if (A - pow(2, j, R) * B) % R or not A < (2**j) * B:
        raise AssertionError("dyadic congruence or orientation changed")

    lambda_two = valuation(L, 2)
    alpha = valuation(A, 2)
    beta = valuation(B, 2)
    if not 1 <= j <= lambda_two + alpha - beta:
        raise AssertionError("dyadic pair exceeds its two-adic budget")

    E = Fraction(2 * L * A, B * (2**j))
    if E.denominator != 1:
        raise AssertionError("dyadic terminal ceased to be integral")
    E_value = E.numerator
    if (2 * L - E_value) % R:
        raise AssertionError("dyadic terminal n ceased to be integral")
    n = (2 * L - E_value) // R
    if not (
        E_value > 0
        and E_value % 2 == 0
        and L * L % E_value == 0
        and E_value % R == 1
        and 0 < n < p
        and n % 2 == 0
    ):
        raise AssertionError("dyadic terminal conditions changed")

    A_sharp, B_sharp = normalized_j_one_pair(A, B, j)
    if (
        gcd(A_sharp, B_sharp) != 1
        or L % A_sharp
        or L % B_sharp
        or (A_sharp - 2 * B_sharp) % R
        or not A_sharp < 2 * B_sharp
    ):
        raise AssertionError("j=1 normalization ceased to be a legal divisor pair")
    sharp_budget = lambda_two + valuation(A_sharp, 2) - valuation(B_sharp, 2)
    if sharp_budget < 1:
        raise AssertionError("normalized pair lost the j=1 budget")
    sharp_E = Fraction(L * A_sharp, B_sharp)
    if sharp_E.denominator != 1 or sharp_E.numerator != E_value:
        raise AssertionError("normalization changed the terminal E")
    sharp_n = (2 * L - sharp_E.numerator) // R
    if sharp_n != n:
        raise AssertionError("normalization changed the terminal n")

    return {
        "A_sharp": A_sharp,
        "B_sharp": B_sharp,
        "E": E_value,
        "n": n,
        "v2_E": valuation(E_value, 2),
    }


def target_fiber(
    *, primes: tuple[int, ...], budgets: tuple[int, ...], R: int
) -> list[tuple[int, ...]]:
    """Enumerate a small fixed target fiber for the p=673 boundary only."""
    values: list[tuple[int, ...]] = []
    for exponents in product(*(range(-budget, budget + 1) for budget in budgets)):
        residue = 1
        for prime, exponent in zip(primes, exponents):
            residue = residue * pow(prime, exponent, R) % R
        if residue == R - 1:
            values.append(exponents)
    return values


def verify_outer_boundary() -> dict[str, object]:
    """Check the p=673 external dyadic terminal and its non-near fiber."""
    p, R, K = 673, 83, 13965
    if factorization(K) != [(3, 1), (5, 1), (7, 2), (19, 1)]:
        raise AssertionError("p=673 support changed")
    first = verify_dyadic_witness(p=p, R=R, K=K, A=15, B=49, j=1)
    second = verify_dyadic_witness(p=p, R=R, K=K, A=30, B=49, j=2)
    if first != second or first != {"A_sharp": 15, "B_sharp": 49, "E": 8550, "n": 570, "v2_E": 1}:
        raise AssertionError("p=673 normalization control changed")

    primes = (3, 5, 7, 19)
    budgets = (1, 1, 2, 1)
    fiber = target_fiber(primes=primes, budgets=budgets, R=R)
    expected_fiber = [(-1, 0, -2, 1), (1, 0, 2, -1)]
    if fiber != expected_fiber:
        raise AssertionError("p=673 target fiber changed")
    difference = tuple(left - right for left, right in zip(fiber[1], fiber[0]))
    if all(abs(value) <= budget for value, budget in zip(difference, budgets)):
        raise AssertionError("p=673 target fiber unexpectedly became near")

    relation = (-1, 1, 1, -2, 0)
    if relation[0] != -valuation(K, 2) - 1 or first["v2_E"] != 1 or first["n"] % 4 != 2:
        raise AssertionError("p=673 two-adic outer-layer boundary changed")
    return {
        "p": p,
        "R": R,
        "K": K,
        "normalized_pair": [first["A_sharp"], first["B_sharp"], 1],
        "terminal": {"E": first["E"], "n": first["n"]},
        "target_fiber": [list(point) for point in fiber],
        "relation_2_3_5_7_19": list(relation),
    }


def verify_j_three_control() -> dict[str, object]:
    """Check the existing j=3 near-normalization control after j=1 reduction."""
    p, R = 164150809, 23
    K = (p * R + 1) // 4
    if K != 943867152 or factorization(K) != [(2, 4), (3, 2), (61, 1), (107453, 1)]:
        raise AssertionError("j=3 support control changed")
    receipt = verify_dyadic_witness(p=p, R=R, K=K, A=1, B=3, j=3)
    expected = {"A_sharp": 1, "B_sharp": 12, "E": 157311192, "n": 157311192, "v2_E": 3}
    if receipt != expected:
        raise AssertionError("j=3 normalization control changed")
    return {
        "p": p,
        "R": R,
        "normalized_pair": [receipt["A_sharp"], receipt["B_sharp"], 1],
        "terminal": {"E": receipt["E"], "n": receipt["n"]},
    }


def build_result() -> dict[str, object]:
    """Build only the two fixed normalization and provenance controls."""
    return {
        "certificate_type": "generalized_dyadic_j_one_normalization_v1",
        "scope": (
            "Two fixed divisor-pair controls only; this verifies terminal normalization "
            "and the target-fiber boundary, not a marked lift or recursive edge."
        ),
        "outer_boundary": verify_outer_boundary(),
        "j_three_control": verify_j_three_control(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified generalized dyadic j=1 normalization controls")


if __name__ == "__main__":
    main()
