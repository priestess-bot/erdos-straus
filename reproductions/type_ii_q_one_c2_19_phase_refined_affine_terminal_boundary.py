#!/usr/bin/env python3
"""Verify the refined affine terminal boundary in the q=1 C=2 19 phase.

The input is the 33-class residual left by the 63-class affine terminal
dispatch. On every fixed u (mod 119) progression this script exhausts
integer-progression-uniform affine square divisors; it does not scan prime
parameters or Egyptian-fraction solutions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import cache
from math import gcd, isqrt

from short_certificate import (
    type_i_normal_form,
    type_i_normal_form_certificate,
    type_ii_normal_form,
    type_ii_normal_form_certificate,
    verify_certificate,
)


STEP = 912 * 119
X_SLOPE = STEP // 4
BASE_RESIDUAL = frozenset(
    {
        1,
        5,
        6,
        8,
        13,
        15,
        19,
        20,
        22,
        26,
        27,
        34,
        36,
        40,
        41,
        43,
        54,
        57,
        62,
        68,
        69,
        75,
        78,
        83,
        85,
        90,
        92,
        96,
        99,
        103,
        104,
        111,
        117,
    }
)
FINAL_RESIDUAL = BASE_RESIDUAL - {13, 20}


@dataclass(frozen=True)
class AffineTypeIICandidate:
    gap: int
    common: int
    square_scale: int
    n_slope: int
    n_base: int
    a: int
    b: int
    c_base: int
    divisor_base: int


EXPECTED_NONCONSTANT_TYPE_II = {
    13: (
        AffineTypeIICandidate(23, 102, 36, 266, 31, 6, 17, 31, 1116),
    ),
    20: (
        AffineTypeIICandidate(31, 476, 392, 57, 10, 14, 17, 20, 3920),
    ),
}


@cache
def positive_divisors(value: int) -> tuple[int, ...]:
    if value <= 0:
        raise ValueError("positive divisor input required")
    result: list[int] = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor:
            continue
        result.append(divisor)
        paired = value // divisor
        if paired != divisor:
            result.append(paired)
    return tuple(sorted(result))


def base_prime(u: int) -> int:
    return 912 * u + 769


def check_prime(value: int) -> bool:
    """Use trial division only for the two named terminal controls."""
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


def affine_type_ii_candidates(u: int) -> tuple[AffineTypeIICandidate, ...]:
    """Exhaust nonconstant affine Type-II square divisors on one progression."""
    base = base_prime(u)
    rows: list[AffineTypeIICandidate] = []
    # Rigidity gives d(t)=a*x(t)/E, a | E^2 and a <= E. Since m | E+a,
    # a legal fixed gap is at most 2*X_SLOPE.
    for gap in range(3, min(base - 2, 2 * X_SLOPE) + 1, 4):
        support = (base + gap) // 4
        common = gcd(X_SLOPE, support)
        n_slope = X_SLOPE // common
        n_base = support // common
        for square_scale in positive_divisors(common * common):
            if square_scale > common or (common + square_scale) % gap:
                continue
            divisor = square_scale * n_base
            normal = type_ii_normal_form(base, gap, divisor)
            if normal is None:
                raise AssertionError("rigidity candidate did not normalize as Type II")
            a, b, c = normal
            certificate = type_ii_normal_form_certificate(base, gap, a, b)
            if certificate is None or not verify_certificate(certificate):
                raise AssertionError("Type II affine terminal did not reconstruct")
            next_normal = type_ii_normal_form(
                base + STEP, gap, square_scale * (n_base + n_slope)
            )
            if next_normal is None or next_normal[:2] != (a, b):
                raise AssertionError("affine Type II coordinates did not persist")
            rows.append(
                AffineTypeIICandidate(
                    gap,
                    common,
                    square_scale,
                    n_slope,
                    n_base,
                    a,
                    b,
                    c,
                    divisor,
                )
            )
    return tuple(rows)


def constant_type_ii_candidates(u: int) -> tuple[tuple[int, int, int], ...]:
    """Exhaust constant Type-II square divisors on one progression."""
    base = base_prime(u)
    rows: list[tuple[int, int, int]] = []
    for gap in range(3, min(base - 2, X_SLOPE) + 1, 4):
        if X_SLOPE % gap:
            continue
        support = (base + gap) // 4
        common = gcd(X_SLOPE, support)
        for divisor in positive_divisors(common * common):
            if divisor > support or (support + divisor) % gap:
                continue
            if type_ii_normal_form(base, gap, divisor) is None:
                raise AssertionError("constant Type II candidate did not normalize")
            if type_ii_normal_form(base + STEP, gap, divisor) is None:
                raise AssertionError("constant Type II condition did not persist")
            rows.append((gap, common, divisor))
    return tuple(rows)


def affine_type_i_candidates(u: int) -> tuple[tuple[int, int, int], ...]:
    """Exhaust nonconstant affine Type-I square divisors on one progression."""
    base = base_prime(u)
    rows: list[tuple[int, int, int]] = []
    for gap in range(3, base - 1, 4):
        support = (base + gap) // 4
        common = gcd(X_SLOPE, support)
        n_slope = X_SLOPE // common
        n_base = support // common
        second_difference = 8 * common * common * n_slope * n_slope
        for square_scale in positive_divisors(common * common):
            first_value = n_base * (4 * common * common * n_base + square_scale)
            first_difference = n_slope * (
                4 * common * common * (2 * n_base + n_slope) + square_scale
            )
            if first_value % gap or first_difference % gap or second_difference % gap:
                continue
            divisor = square_scale * n_base
            normal = type_i_normal_form(base, gap, divisor)
            if normal is None:
                raise AssertionError("rigidity candidate did not normalize as Type I")
            a, b, _ = normal
            certificate = type_i_normal_form_certificate(base, gap, a, b)
            if certificate is None or not verify_certificate(certificate):
                raise AssertionError("Type I affine terminal did not reconstruct")
            if type_i_normal_form(
                base + STEP, gap, square_scale * (n_base + n_slope)
            ) is None:
                raise AssertionError("affine Type I condition did not persist")
            rows.append((gap, common, square_scale))
    return tuple(rows)


def constant_type_i_candidates(u: int) -> tuple[tuple[int, int, int], ...]:
    """Exhaust constant Type-I square divisors on one progression."""
    base = base_prime(u)
    rows: list[tuple[int, int, int]] = []
    for gap in range(3, base - 1, 4):
        support = (base + gap) // 4
        common = gcd(X_SLOPE, support)
        first_square = 4 * support * support
        first_difference = 4 * X_SLOPE * (2 * support + X_SLOPE)
        second_difference = 8 * X_SLOPE * X_SLOPE
        if first_difference % gap or second_difference % gap:
            continue
        for divisor in positive_divisors(common * common):
            if (first_square + divisor) % gap:
                continue
            normal = type_i_normal_form(base, gap, divisor)
            if normal is None:
                raise AssertionError("constant Type I candidate did not normalize")
            a, b, _ = normal
            certificate = type_i_normal_form_certificate(base, gap, a, b)
            if certificate is None or not verify_certificate(certificate):
                raise AssertionError("constant Type I terminal did not reconstruct")
            if type_i_normal_form(base + STEP, gap, divisor) is None:
                raise AssertionError("constant Type I condition did not persist")
            rows.append((gap, common, divisor))
    return tuple(rows)


def verify_named_terminal_controls() -> None:
    controls = (
        (13, 2, 23, 6, 17, (57426, 20268, 775862418, 2198276851)),
        (20, 0, 31, 14, 17, (4760, 3920, 5322520, 6463060)),
    )
    for u, parameter, gap, a, b, expected in controls:
        prime = base_prime(u) + STEP * parameter
        if not check_prime(prime):
            raise AssertionError("named affine terminal control was not prime")
        certificate = type_ii_normal_form_certificate(prime, gap, a, b)
        if certificate is None or not verify_certificate(certificate):
            raise AssertionError("named affine terminal control did not verify")
        if (certificate.x, certificate.divisor, certificate.y, certificate.z) != expected:
            raise AssertionError("named affine terminal denominator control changed")


def verify() -> None:
    nonconstant_type_ii = {
        u: rows
        for u in sorted(BASE_RESIDUAL)
        if (rows := affine_type_ii_candidates(u))
    }
    constant_type_ii = {
        u: rows
        for u in sorted(BASE_RESIDUAL)
        if (rows := constant_type_ii_candidates(u))
    }
    nonconstant_type_i = {
        u: rows
        for u in sorted(BASE_RESIDUAL)
        if (rows := affine_type_i_candidates(u))
    }
    constant_type_i = {
        u: rows
        for u in sorted(BASE_RESIDUAL)
        if (rows := constant_type_i_candidates(u))
    }
    if nonconstant_type_ii != EXPECTED_NONCONSTANT_TYPE_II:
        raise AssertionError("the exact refined affine Type II terminal table changed")
    if constant_type_ii or nonconstant_type_i or constant_type_i:
        raise AssertionError("a supposedly empty uniform affine terminal family gained a row")
    if not (
        len(BASE_RESIDUAL) == 33
        and len(FINAL_RESIDUAL) == 31
        and BASE_RESIDUAL - set(nonconstant_type_ii) == FINAL_RESIDUAL
        and all(gcd(base_prime(u), STEP) == 1 for u in nonconstant_type_ii)
    ):
        raise AssertionError("the refined residue boundary changed")
    verify_named_terminal_controls()
    print(
        "verified q=1 C=2 refined affine terminal boundary: "
        "2 Type II additions, no uniform affine Type I rows, 31 residual classes"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact affine receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
