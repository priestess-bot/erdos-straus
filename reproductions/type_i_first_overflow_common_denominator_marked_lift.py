#!/usr/bin/env python3
"""Focused verifier for the canonical first-overflow common-denominator marked lift."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd


def factorint(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n //= prime
        prime += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def divisors_from_factors(factors: dict[int, int]) -> list[int]:
    values = [1]
    for prime, exponent in sorted(factors.items()):
        values = [value * prime**power for value in values for power in range(exponent + 1)]
    return sorted(values)


def divisors(n: int) -> list[int]:
    return divisors_from_factors(factorint(n))


def factor_gate(q: int, c: int) -> list[int]:
    residual = 4 * c - q
    if residual <= 0:
        return []
    scale = q * c
    square_factors = {prime: 2 * exponent for prime, exponent in factorint(scale).items()}
    return [
        e
        for e in divisors_from_factors(square_factors)
        if (scale + e) % residual == 0
        and (scale + scale * scale // e) % residual == 0
    ]


def recover(q: int, c: int, e: int) -> tuple[int, int, int]:
    residual = 4 * c - q
    scale = q * c
    return tuple(sorted((c, (scale + e) // residual, (scale + scale * scale // e) // residual)))


def canonical_solutions(n: int) -> list[tuple[int, int, int]]:
    result = []
    for a in range(n // 4 + 1, 3 * n // 4 + 1):
        residual = 4 * a - n
        scale = n * a
        lower_b = max(a, scale // residual + 1)
        upper_b = 2 * scale // residual
        for b in range(lower_b, upper_b + 1):
            denominator = residual * b - scale
            numerator = scale * b
            if numerator % denominator != 0:
                continue
            c = numerator // denominator
            if c >= b:
                result.append((a, b, c))
    return result


def reciprocal_sum(triple: tuple[int, int, int]) -> Fraction:
    return sum((Fraction(1, value) for value in triple), Fraction(0, 1))


def quotient_multiple_rows(p: int, n: int) -> list[tuple[int, int, int, bool]]:
    lower = p // (4 * n) + 1
    upper = p // (2 * n)
    rows = []
    for k in range(lower, upper + 1):
        gap = 4 * k * n - p
        residue = (k * p + 1) % gap
        rows.append((k, gap, residue, residue == 0))
    return rows


def verify() -> None:
    p, modulus, y, gap, n = 73, 27, 29, 43, 7
    assert 4 * y - p == gap
    assert (p + 4 * y) // modulus == n
    assert gcd(modulus, y) == gcd(n, y) == 1

    source_residual = 4 * y - n
    source_scale = n * y
    target_scale = p * y
    assert source_residual == 109
    assert gcd(source_residual, source_scale) == 1
    assert gcd(gap, target_scale) == 1

    source_residues = {d % source_residual for d in divisors(source_scale * source_scale)}
    target_residues = {d % gap for d in divisors(target_scale * target_scale)}
    assert (-source_scale) % source_residual == 15
    assert source_residues == {1, 4, 7, 29, 49, 78, 94}
    assert (-target_scale) % gap == 33
    assert target_residues == {1, 10, 14, 24, 29, 30, 32, 40, 42}
    assert factor_gate(n, y) == []
    assert factor_gate(p, y) == []

    gap_divisors = divisors(y * y)
    assert not any((p * y + d) % gap == 0 for d in gap_divisors)
    assert not any(d <= y and (y + d) % gap == 0 for d in gap_divisors)

    rows = quotient_multiple_rows(p, n)
    assert rows == [(3, 11, 0, True), (4, 39, 20, False), (5, 67, 31, False)]
    k, alternate_gap = 3, 11
    assert n % 1 == 0 and n != 0
    assert n in divisors((k * n) ** 2)
    assert (p * k * n + n) % alternate_gap == 0
    ell = (k * p + 1) // alternate_gap
    quotient_solution = (k * n, n * ell, p * k * n * ell)
    assert quotient_solution == (21, 140, 30_660)
    assert reciprocal_sum(quotient_solution) == Fraction(4, p)

    solutions = canonical_solutions(n)
    expected_solutions = [
        (2, 15, 210),
        (2, 16, 112),
        (2, 18, 63),
        (2, 21, 42),
        (2, 28, 28),
        (3, 6, 14),
        (4, 4, 14),
    ]
    assert solutions == expected_solutions
    assert all(reciprocal_sum(solution) == Fraction(4, n) for solution in solutions)

    marked = []
    images: dict[tuple[int, int, int], tuple[int, int, int]] = {}
    witnesses: dict[tuple[int, int, int], tuple[int, int]] = {}
    for solution in solutions:
        eligible = []
        for coordinate in sorted(set(solution)):
            gates = factor_gate(p, coordinate)
            if gates:
                eligible.append((coordinate, min(gates)))
        if eligible:
            coordinate, e = min(eligible)
            marked.append(solution)
            witnesses[solution] = (coordinate, e)
            images[solution] = recover(p, coordinate, e)

    assert marked == [(2, 15, 210), (2, 21, 42)]
    assert witnesses[(2, 15, 210)] == (210, 10)
    assert witnesses[(2, 21, 42)] == (21, 7)
    assert images[(2, 15, 210)] == (20, 210, 30_660)
    assert images[(2, 21, 42)] == (21, 140, 30_660)
    assert all(reciprocal_sum(image) == Fraction(4, p) for image in images.values())

    failed_positive_coordinates = {28: (39, 23), 42: (95, 69), 63: (179, 55), 112: (375, 74)}
    for coordinate, (residual, required) in failed_positive_coordinates.items():
        assert 4 * coordinate - p == residual
        assert (-(p * coordinate)) % residual == required
        assert factor_gate(p, coordinate) == []

    assert max((3, 6, 14)) * 4 <= p
    assert all(4 * coordinate - p <= 0 for coordinate in (3, 6, 14))
    assert n < p

    t = n * (n + 1) // 4
    c_one = 3 * t // 2
    c_two = t * (t + 1)
    assert (t, c_one, c_two) == (14, 21, 210)
    assert reciprocal_sum(((n + 1) // 4, c_one, 3 * t)) == Fraction(4, n)
    assert (4 * c_one - p) > 0
    assert (4 * c_one * c_one + n) % (4 * c_one - p) == 0
    assert n in factor_gate(p, c_one)
    assert reciprocal_sum(((n + 1) // 4, t + 1, c_two)) == Fraction(4, n)
    assert (4 * c_two * c_two + 10) % (4 * c_two - p) == 0
    assert 10 in divisors(c_two * c_two)
    assert 10 in factor_gate(p, c_two)

    print("PASS: FIRST_OVERFLOW_COMMON_DENOMINATOR_MARKED_LIFT")
    print("natural_y_source_gate=EMPTY target_gate=EMPTY")
    print(f"quotient_multiple_rows={rows}")
    print(f"canonical_sol7_count={len(solutions)} marked_count={len(marked)}")
    print(f"marked={marked}")
    print(f"images={images}")
    print("canonical_full_domain_adaptive_one_denominator_lift=EMPTY_WITNESS_(3,6,14)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
