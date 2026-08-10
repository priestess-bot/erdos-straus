#!/usr/bin/env python3
"""Verify equal-tail source admission and one-coordinate terminal collapse."""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd

import sympy


def reciprocal_sum(denominators: tuple[int, int, int]) -> Fraction:
    return sum((Fraction(1, value) for value in denominators), Fraction())


def equal_tail_menu(prime: int) -> tuple[int, ...]:
    base = (prime - 1) // 4
    return tuple(
        divisor for divisor in sympy.divisors(2 * base * base) if divisor <= base
    )


def equal_tail_source(prime: int, gap_parameter: int) -> tuple[int, int, int] | None:
    base = (prime - 1) // 4
    if (2 * base * base) % gap_parameter:
        return None
    marker = base + gap_parameter
    tail = 2 * base * marker // gap_parameter
    return marker, tail, tail


def complete_factor_witnesses(
    prime: int, gap_parameter: int
) -> tuple[tuple[int, int, int], ...]:
    base = (prime - 1) // 4
    marker = base + gap_parameter
    gap = 4 * gap_parameter - 1
    product_root = prime * marker
    rows: list[tuple[int, int, int]] = []
    for factor in sympy.divisors(product_root * product_root):
        complement = product_root * product_root // factor
        if (product_root + factor) % gap:
            continue
        if (product_root + complement) % gap:
            raise AssertionError("the complementary factor congruence did not follow")
        rows.append(
            (
                factor,
                (product_root + factor) // gap,
                (product_root + complement) // gap,
            )
        )
    return tuple(rows)


def reduced_gate_records(prime: int, gap_parameter: int) -> tuple[tuple[str, int], ...]:
    base = (prime - 1) // 4
    marker = base + gap_parameter
    gap = 4 * gap_parameter - 1
    rows: list[tuple[str, int]] = []
    for divisor in sympy.divisors(marker * marker):
        if (4 * divisor + 1) % gap == 0:
            rows.append(("I", divisor))
        if (marker + divisor) % gap == 0:
            rows.append(("II", divisor))
    return tuple(rows)


def verify_p_adic_split(prime: int, gap_parameter: int) -> None:
    base = (prime - 1) // 4
    marker = base + gap_parameter
    gap = 4 * gap_parameter - 1
    complete = complete_factor_witnesses(prime, gap_parameter)
    reduced = reduced_gate_records(prime, gap_parameter)
    if bool(complete) != bool(reduced):
        raise AssertionError(
            f"factor/reduced gate mismatch: p={prime}, h={gap_parameter}"
        )

    for factor, denominator_1, denominator_2 in complete:
        p_exponent = 0
        p_free_factor = factor
        while p_free_factor % prime == 0:
            p_free_factor //= prime
            p_exponent += 1
        if p_exponent not in (0, 1, 2) or marker * marker % p_free_factor:
            raise AssertionError("invalid p-adic factor split")
        if p_exponent == 0:
            reduced_divisor = marker * marker // p_free_factor
            gate_holds = (4 * reduced_divisor + 1) % gap == 0
        elif p_exponent == 1:
            reduced_divisor = p_free_factor
            gate_holds = (marker + reduced_divisor) % gap == 0
        else:
            reduced_divisor = p_free_factor
            gate_holds = (4 * reduced_divisor + 1) % gap == 0
        target = (marker, denominator_1, denominator_2)
        if not gate_holds or reciprocal_sum(target) != Fraction(4, prime):
            raise AssertionError("complete witness did not enter a Type I/II branch")

    for branch, divisor in reduced:
        if branch == "I":
            type_i_divisor = marker * marker // divisor
            factor = type_i_divisor
            target = (
                marker,
                (prime * marker + type_i_divisor) // gap,
                prime * (marker + prime * divisor) // gap,
            )
        else:
            normalized = min(divisor, marker * marker // divisor)
            if normalized >= marker or (marker + normalized) % gap:
                raise AssertionError("Type II complement normalization failed")
            factor = prime * normalized
            target = (
                marker,
                prime * (marker + normalized) // gap,
                prime * (marker + marker * marker // normalized) // gap,
            )
        if (prime * marker + factor) % gap or reciprocal_sum(target) != Fraction(
            4, prime
        ):
            raise AssertionError(f"reduced {branch} branch did not reconstruct")


def verify_source_admission(prime: int) -> None:
    base = (prime - 1) // 4
    menu = equal_tail_menu(prime)
    for gap_parameter in range(1, base + 1):
        source = equal_tail_source(prime, gap_parameter)
        admitted = gap_parameter in menu
        common = gcd(gap_parameter, base)
        gcd_form = (2 * common) % (gap_parameter // common) == 0
        valuations = all(
            exponent
            <= 2 * int(sympy.factorint(base).get(prime_factor, 0))
            + int(prime_factor == 2)
            for prime_factor, exponent in sympy.factorint(gap_parameter).items()
        )
        if (
            admitted != gcd_form
            or admitted != valuations
            or admitted != (source is not None)
        ):
            raise AssertionError(
                f"source admission mismatch: p={prime}, h={gap_parameter}"
            )
        if source is not None:
            if not (
                reciprocal_sum(source) == Fraction(4, prime - 1)
                and source[1] == source[2]
                and source[1] >= 2 * source[0]
            ):
                raise AssertionError(
                    f"equal-tail source reconstruction failed: {source}"
                )


def verify_controls() -> None:
    if equal_tail_menu(73) != (1, 2, 3, 4, 6, 8, 9, 12, 18):
        raise AssertionError("p=73 exact source menu changed")
    if equal_tail_source(73, 5) is not None:
        raise AssertionError("p=73, h=5 must be source-inadmissible")
    if equal_tail_source(73, 8) != (26, 117, 117):
        raise AssertionError("p=73, h=8 source control changed")
    if complete_factor_witnesses(73, 8):
        raise AssertionError("p=73, h=8 target fiber must be empty")

    controls = {
        (73, 2): ((20, 360, 360), (20, 219, 4380)),
        (97, 1): ((25, 1200, 1200), (25, 970, 4850)),
    }
    for (prime, gap_parameter), (expected_source, expected_target) in controls.items():
        source = equal_tail_source(prime, gap_parameter)
        actual_targets = {
            tuple(
                sorted(
                    (
                        (prime - 1) // 4 + gap_parameter,
                        denominator_1,
                        denominator_2,
                    )
                )
            )
            for _, denominator_1, denominator_2 in complete_factor_witnesses(
                prime, gap_parameter
            )
        }
        if (
            source != expected_source
            or tuple(sorted(expected_target)) not in actual_targets
        ):
            raise AssertionError(
                f"terminal control changed: p={prime}, h={gap_parameter}"
            )


def verify() -> None:
    for prime in (73, 97):
        if not sympy.isprime(prime) or prime % 24 != 1:
            raise AssertionError("expected a core prime")
        verify_source_admission(prime)
        base = (prime - 1) // 4
        for gap_parameter in range(1, base + 1):
            verify_p_adic_split(prime, gap_parameter)
    verify_controls()

    print("PASS: TYPE_I_P_MINUS_ONE_EQUAL_TAIL_MARKER_CAPACITY")
    print(f"p73_source_menu={equal_tail_menu(73)}")
    print("p73_h5=source_absent p73_h8=target_fiber_empty")
    print("terminal_controls=((73, 2), (97, 1))")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
