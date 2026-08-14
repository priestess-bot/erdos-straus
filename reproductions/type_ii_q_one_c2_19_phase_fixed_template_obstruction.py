#!/usr/bin/env python3
"""Verify the fixed-template obstruction for the q=1 high C=2 19 phase.

This is a finite divisor receipt for symbolic progression identities.  It does
not enumerate primes, scan for Egyptian-fraction solutions, or test a numeric
range of parameters.
"""

from __future__ import annotations

import argparse
from math import gcd


P0 = 769
STEP = 912


def divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    for candidate in range(1, value + 1):
        if value % candidate == 0:
            result.append(candidate)
    return tuple(result)


def factor_triples(product: int) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for a in divisors(product):
        for c in divisors(product // a):
            k = product // (a * c)
            rows.append((a, c, k))
    return tuple(rows)


def verify_phase_prime_obstruction() -> None:
    triples = factor_triples(5)
    residues = tuple((a, c, k, (k * P0 + a) % 19) for a, c, k in triples)
    expected = ((1, 1, 5, 8), (1, 5, 1, 10), (5, 1, 1, 14))
    if triples != tuple(row[:3] for row in expected) or residues != expected:
        raise AssertionError("the exact h=19 factor triples changed")
    if any(residue == 0 for _, _, _, residue in residues):
        raise AssertionError("a q=19 Type II AC ray unexpectedly appeared")


def verify_uniform_type_ii_obstruction() -> None:
    candidate_factors = tuple(h for h in divisors(STEP) if h % 4 == 3)
    if candidate_factors != (3, 19):
        raise AssertionError("the h | 912, h == 3 (mod 4) divisor reduction changed")

    rows: list[tuple[int, tuple[tuple[int, int, int, int], ...]]] = []
    for h in candidate_factors:
        product = (h + 1) // 4
        triple_rows = tuple(
            (a, c, k, (k * P0 + a) % h)
            for a, c, k in factor_triples(product)
        )
        rows.append((h, triple_rows))

    expected = (
        (3, ((1, 1, 1, 2),)),
        (19, ((1, 1, 5, 8), (1, 5, 1, 10), (5, 1, 1, 14))),
    )
    if tuple(rows) != expected:
        raise AssertionError("the finite uniform Type II obstruction table changed")
    if any(residue == 0 for _, triples in rows for *_, residue in triples):
        raise AssertionError("a uniform Type II AC ray unexpectedly appeared")


def verify_uniform_type_i_obstruction() -> None:
    # A fixed normal-form identity has AB | STEP/4 and m in {3, 19}.
    candidate_gaps = tuple(m for m in divisors(3 * 19) if m % 4 == 3)
    if candidate_gaps != (3, 19):
        raise AssertionError("the fixed Type I odd-gap reduction changed")

    rows: list[tuple[int, int, int, int]] = []
    for m in candidate_gaps:
        base_support = (P0 + m) // 4
        common = gcd(STEP // 4, base_support)
        terminal_residue = (P0 + 1) % m
        rows.append((m, base_support, common, terminal_residue))

    expected = ((3, 193, 1, 2), (19, 197, 1, 10))
    if tuple(rows) != expected:
        raise AssertionError("the fixed Type I obstruction table changed")
    if any(common != 1 or residue == 0 for _, _, common, residue in rows):
        raise AssertionError("a uniform Type I normal-form template unexpectedly appeared")


def verify_uniform_aligned_type_ii_factor_pair_obstruction() -> None:
    lift_modulus = gcd(P0 - 1, STEP)
    candidate_gaps = tuple(
        divisor - 1
        for divisor in divisors(lift_modulus)
        if divisor - 1 >= 3 and (divisor - 1) % 4 == 3
    )
    if lift_modulus != 48 or candidate_gaps != (3, 7, 11, 15, 23, 47):
        raise AssertionError("the universally aligned Type II gap list changed")

    rows = tuple(
        (m, gcd(STEP // 4, (P0 + m) // 4)) for m in candidate_gaps
    )
    expected = ((3, 1), (7, 2), (11, 3), (15, 4), (23, 6), (47, 12))
    if rows != expected:
        raise AssertionError("the fixed-factor Type II common-divisor table changed")
    if any(common + 1 >= m for m, common in rows):
        raise AssertionError("a fixed aligned Type II factor pair may be possible")


def verify() -> None:
    if P0 % 19 != 9 or STEP % 19 != 0:
        raise AssertionError("the q=1 C=2 progression changed")
    verify_phase_prime_obstruction()
    verify_uniform_type_ii_obstruction()
    verify_uniform_type_i_obstruction()
    verify_uniform_aligned_type_ii_factor_pair_obstruction()
    print(
        "verified q=1 high C=2 fixed-template obstruction: "
        "q=19 unavailable, and no uniform Type I or Type II template"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact finite receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
