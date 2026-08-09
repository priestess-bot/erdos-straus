#!/usr/bin/env python3
"""Verify exact generalized-dyadic relation capacity on two controls."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd


CONTROLS = (
    {
        "p": 433,
        "R": 15,
        "K": 1624,
        "expected_E": (16, 196, 256, 406, 3136),
        "expected_symmetric_relations": 9,
        "expected_outer_oriented": 1,
        "duplicate_E": 3136,
        "expected_duplicate_witnesses": (
            (28, 29, 1),
            (56, 29, 2),
            (112, 29, 3),
        ),
    },
    {
        "p": 673,
        "R": 83,
        "K": 13965,
        "expected_E": (84, 8550),
        "expected_symmetric_relations": 3,
        "expected_outer_oriented": 1,
        "duplicate_E": 8550,
        "expected_duplicate_witnesses": (
            (15, 49, 1),
            (30, 49, 2),
        ),
    },
)


def factorization(value: int) -> dict[int, int]:
    """Return the prime factorization of a positive control integer."""
    if value <= 0:
        raise AssertionError("factorization expects a positive integer")
    factors: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def divisors(value: int) -> tuple[int, ...]:
    """Enumerate all positive divisors of a small control integer."""
    values = [1]
    for prime, exponent in factorization(value).items():
        values = [base * prime**power for base in values for power in range(exponent + 1)]
    return tuple(sorted(values))


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rational_height(primes: tuple[int, ...], exponents: tuple[int, ...]) -> Fraction:
    """Evaluate the exact positive rational product q^lambda_q."""
    value = Fraction(1, 1)
    for prime, exponent in zip(primes, exponents):
        if exponent >= 0:
            value *= prime**exponent
        else:
            value /= prime ** (-exponent)
    return value


def relation_residue(
    primes: tuple[int, ...], exponents: tuple[int, ...], modulus: int
) -> int:
    """Evaluate a signed-exponent relation in the unit group modulo R."""
    residue = 1
    for prime, exponent in zip(primes, exponents):
        if exponent >= 0:
            factor = pow(prime, exponent, modulus)
        else:
            factor = pow(pow(prime, -exponent, modulus), -1, modulus)
        residue = residue * factor % modulus
    return residue


def verify_terminal(*, p: int, R: int, K: int, E: int) -> int:
    """Check the arithmetic even-predecessor conditions and return n."""
    L = 2 * K
    if not (
        E > 0
        and E < 4 * K
        and E % 2 == 0
        and L * L % E == 0
        and E % R == 1
        and (4 * K - E) % R == 0
    ):
        raise AssertionError(f"illegal arithmetic terminal E={E}")
    n = (4 * K - E) // R
    if not (0 < n < p and n % 2 == 0):
        raise AssertionError(f"illegal even predecessor n={n} from E={E}")
    return n


def enumerate_generalized_terminals(
    *, p: int, R: int, K: int
) -> dict[int, set[tuple[int, int, int]]]:
    """Enumerate every legal coprime (A,B,j), grouped by its terminal E."""
    L = 2 * K
    terminal_witnesses: dict[int, set[tuple[int, int, int]]] = {}
    for A in divisors(L):
        for B in divisors(L):
            if gcd(A, B) != 1:
                continue
            maximum_j = valuation(L, 2) + valuation(A, 2) - valuation(B, 2)
            for j in range(1, maximum_j + 1):
                if (A - pow(2, j, R) * B) % R != 0 or A >= 2**j * B:
                    continue
                E_fraction = Fraction(2 * L * A, 2**j * B)
                if E_fraction.denominator != 1:
                    raise AssertionError("dyadic budget admitted a nonintegral E")
                E = E_fraction.numerator
                verify_terminal(p=p, R=R, K=K, E=E)

                normalized = Fraction(A, B * 2 ** (j - 1))
                if normalized != Fraction(E, L):
                    raise AssertionError("j=1 normalization changed E/L")
                if L % normalized.numerator or L % normalized.denominator:
                    raise AssertionError("normalized numerator or denominator left L-divisors")
                terminal_witnesses.setdefault(E, set()).add((A, B, j))
    return terminal_witnesses


def enumerate_relation_terminals(
    *, p: int, R: int, K: int
) -> tuple[dict[int, tuple[int, ...]], int, int]:
    """Enumerate the asymmetric relation box and evaluate the capacity formula."""
    factors = factorization(K)
    primes = tuple(sorted(set(factors) | {2}))
    budgets = {prime: factors.get(prime, 0) for prime in primes}
    dyadic_ranges = tuple(
        range(-budgets[prime] - 1, budgets[prime] + 1)
        if prime == 2
        else range(-budgets[prime], budgets[prime] + 1)
        for prime in primes
    )

    terminal_relations: dict[int, tuple[int, ...]] = {}
    outer_oriented = 0
    for exponents in product(*dyadic_ranges):
        if relation_residue(primes, exponents, R) != 1:
            continue
        rho = rational_height(primes, exponents)
        if rho >= 1:
            continue
        E_fraction = 4 * K * rho
        if E_fraction.denominator != 1:
            raise AssertionError("asymmetric relation box produced a nonintegral E")
        E = E_fraction.numerator
        verify_terminal(p=p, R=R, K=K, E=E)
        if E in terminal_relations:
            raise AssertionError("distinct relation vectors produced one E")
        terminal_relations[E] = exponents
        if exponents[primes.index(2)] == -budgets[2] - 1:
            outer_oriented += 1

    symmetric_ranges = tuple(
        range(-budgets[prime], budgets[prime] + 1) for prime in primes
    )
    symmetric_relation_count = sum(
        relation_residue(primes, exponents, R) == 1
        for exponents in product(*symmetric_ranges)
    )
    if symmetric_relation_count % 2 != 1:
        raise AssertionError("symmetric relation box lost its zero-plus-pairs parity")
    capacity = (symmetric_relation_count - 1) // 2 + outer_oriented
    if capacity != len(terminal_relations):
        raise AssertionError("exact relation capacity formula failed")
    return terminal_relations, symmetric_relation_count, outer_oriented


def verify_control(control: dict[str, object]) -> dict[str, object]:
    """Compare triple enumeration, relation enumeration, and exact capacity."""
    p = int(control["p"])
    R = int(control["R"])
    K = int(control["K"])
    if p <= 0 or K <= 0 or R <= 1 or 4 * K != p * R + 1 or R % 2 != 1:
        raise AssertionError("control is not a legal arithmetic chart")

    witnesses = enumerate_generalized_terminals(p=p, R=R, K=K)
    relations, symmetric_count, outer_count = enumerate_relation_terminals(
        p=p, R=R, K=K
    )
    triple_E = tuple(sorted(witnesses))
    relation_E = tuple(sorted(relations))
    expected_E = tuple(control["expected_E"])
    if triple_E != relation_E or triple_E != expected_E:
        raise AssertionError(
            f"p={p} terminal sets differ: triples={triple_E}, relations={relation_E}"
        )
    if symmetric_count != int(control["expected_symmetric_relations"]):
        raise AssertionError(f"p={p} symmetric relation count changed")
    if outer_count != int(control["expected_outer_oriented"]):
        raise AssertionError(f"p={p} outer oriented count changed")

    duplicate_E = int(control["duplicate_E"])
    duplicate_witnesses = tuple(sorted(witnesses[duplicate_E]))
    if duplicate_witnesses != tuple(control["expected_duplicate_witnesses"]):
        raise AssertionError(f"p={p} raw-j deduplication control changed")

    return {
        "p": p,
        "R": R,
        "K": K,
        "terminal_E": list(triple_E),
        "symmetric_relation_count": symmetric_count,
        "outer_oriented_count": outer_count,
        "capacity": (symmetric_count - 1) // 2 + outer_count,
        "duplicate_E": duplicate_E,
        "duplicate_witnesses": [list(item) for item in duplicate_witnesses],
    }


def build_result() -> dict[str, object]:
    """Build the two-control exact-capacity certificate."""
    return {
        "certificate_type": "generalized_dyadic_exact_relation_capacity_v1",
        "scope": (
            "Only p=433 and p=673 are enumerated. This verifies arithmetic terminal "
            "sets and the exact capacity formula, not an E1--E5 marked lift."
        ),
        "controls": [verify_control(control) for control in CONTROLS],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        summaries = ", ".join(
            f"p={item['p']}:capacity={item['capacity']}"
            for item in result["controls"]
        )
        print(f"verified generalized dyadic exact relation capacity ({summaries})")


if __name__ == "__main__":
    main()
