#!/usr/bin/env python3
"""Verify the fixed-source-rank Type II finite menu and cubic bound."""

from __future__ import annotations

import argparse
from fractions import Fraction

import sympy

Record = tuple[int, int, int, int]


def k_bounds(rank_parameter: int) -> tuple[int, int]:
    """Return ceil((r + 2) / 4) and floor((2r + 1) / 3)."""
    return (rank_parameter + 5) // 4, (2 * rank_parameter + 1) // 3


def finite_menu(rank_parameter: int) -> tuple[Record, ...]:
    """Return (k, d, q, p) records from the theorem's divisor menu."""
    lower, upper = k_bounds(rank_parameter)
    rows: list[Record] = []
    for linear_parameter in range(lower, upper + 1):
        coefficient = 4 * linear_parameter - rank_parameter - 1
        if coefficient <= 0:
            raise AssertionError("the stated lower k-bound is not positive")
        for divisor in sympy.divisors(linear_parameter * linear_parameter):
            if (divisor + linear_parameter) % coefficient:
                continue
            cofactor = (divisor + linear_parameter) // coefficient
            first_denominator = cofactor * (rank_parameter + 1)
            if divisor >= first_denominator:
                continue
            prime = 4 * cofactor * rank_parameter + 1
            if sympy.isprime(prime):
                rows.append((linear_parameter, divisor, cofactor, prime))
    return tuple(rows)


def direct_type_ii_menu(rank_parameter: int) -> tuple[Record, ...]:
    """Enumerate the original Type II divisor conditions inside the proved q-bound."""
    _, upper = k_bounds(rank_parameter)
    cofactor_bound = upper * (upper + 1)
    rows: list[Record] = []
    for cofactor in range(1, cofactor_bound + 1):
        prime = 4 * cofactor * rank_parameter + 1
        if not sympy.isprime(prime):
            continue
        gap = 4 * cofactor - 1
        first_denominator = cofactor * (rank_parameter + 1)
        for divisor in sympy.divisors(first_denominator * first_denominator):
            if divisor >= first_denominator or (first_denominator + divisor) % gap:
                continue
            linear_parameter = (first_denominator + divisor) // gap
            rows.append((linear_parameter, divisor, cofactor, prime))
    return tuple(sorted(rows))


def reciprocal_sum(denominators: tuple[int, int, int]) -> Fraction:
    return sum((Fraction(1, value) for value in denominators), Fraction())


def verify_record(rank_parameter: int, record: Record) -> None:
    linear_parameter, divisor, cofactor, prime = record
    gap = 4 * cofactor - 1
    first_denominator = cofactor * (rank_parameter + 1)
    coefficient = 4 * linear_parameter - rank_parameter - 1
    source_tail = (first_denominator + first_denominator**2 // divisor) // gap
    source = (first_denominator, linear_parameter, source_tail)
    target = (
        first_denominator,
        prime * linear_parameter,
        prime * source_tail,
    )
    lower, upper = k_bounds(rank_parameter)

    if not (
        lower <= linear_parameter <= upper
        and divisor < first_denominator
        and linear_parameter * linear_parameter % divisor == 0
        and divisor == cofactor * coefficient - linear_parameter
        and (first_denominator + divisor) % gap == 0
        and (first_denominator + first_denominator**2 // divisor) % gap == 0
        and reciprocal_sum(source) == Fraction(4, rank_parameter + 1)
        and reciprocal_sum(target) == Fraction(4, prime)
        and cofactor <= upper * (upper + 1)
        and prime - 1 <= 4 * rank_parameter * upper * (upper + 1)
        and 9 * (prime - 1)
        <= 8 * rank_parameter * (2 * rank_parameter + 1) * (rank_parameter + 2)
    ):
        raise AssertionError(
            f"fixed-rank reconstruction failed: r={rank_parameter}, {record}"
        )


def verify() -> None:
    expected_prime_pairs = {
        1: ((1, 5),),
        2: ((2, 17),),
        3: ((1, 13),),
        4: ((1, 17),),
        5: ((2, 41), (3, 61)),
        6: ((3, 73), (4, 97)),
    }

    menus: dict[int, tuple[Record, ...]] = {}
    for rank_parameter in range(1, 11):
        menu = tuple(sorted(finite_menu(rank_parameter)))
        direct = direct_type_ii_menu(rank_parameter)
        if menu != direct:
            raise AssertionError(f"finite-menu bijection failed for r={rank_parameter}")
        lower, upper = k_bounds(rank_parameter)
        capacity = sum(
            int(sympy.divisor_count(linear_parameter * linear_parameter))
            for linear_parameter in range(lower, upper + 1)
        )
        if len(menu) > capacity:
            raise AssertionError(f"capacity bound failed for r={rank_parameter}")
        for record in menu:
            verify_record(rank_parameter, record)
        menus[rank_parameter] = menu

    for rank_parameter, expected in expected_prime_pairs.items():
        actual = tuple(sorted({(row[2], row[3]) for row in menus[rank_parameter]}))
        if actual != expected:
            raise AssertionError(
                f"small-rank table changed for r={rank_parameter}: {actual}"
            )

    core_below_six = tuple(
        record
        for rank_parameter in range(1, 6)
        for record in menus[rank_parameter]
        if record[3] % 24 == 1
    )
    core_at_six = tuple(record for record in menus[6] if record[3] % 24 == 1)
    if core_below_six or core_at_six != ((2, 1, 3, 73), (2, 2, 4, 97)):
        raise AssertionError("core small-rank boundary changed")

    expected_controls = {
        73: ((21, 146, 3066), (21, 2, 42)),
        97: ((28, 194, 2716), (28, 2, 28)),
    }
    for record in core_at_six:
        linear_parameter, divisor, cofactor, prime = record
        first_denominator = cofactor * 7
        gap = 4 * cofactor - 1
        source_tail = (first_denominator + first_denominator**2 // divisor) // gap
        target = (first_denominator, prime * linear_parameter, prime * source_tail)
        source = (first_denominator, linear_parameter, source_tail)
        if (target, source) != expected_controls[prime]:
            raise AssertionError(f"positive control changed for p={prime}")

    for source_rank_bound in range(2, 11):
        threshold = 1 + Fraction(
            8
            * (source_rank_bound - 1)
            * (2 * source_rank_bound - 1)
            * (source_rank_bound + 1),
            9,
        )
        if any(
            Fraction(record[3]) > threshold
            for rank_parameter in range(1, source_rank_bound)
            for record in menus[rank_parameter]
        ):
            raise AssertionError(
                f"bounded-source-rank no-go failed for N={source_rank_bound}"
            )

    print("PASS: TYPE_II_P_MINUS_ONE_FIXED_SOURCE_RANK_FINITE_MENU_CUBIC_CAPACITY")
    print("checked_ranks=1..10")
    print("core_r_le_5=empty")
    print(f"core_r_6={core_at_six}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
