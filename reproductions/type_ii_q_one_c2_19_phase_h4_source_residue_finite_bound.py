#!/usr/bin/env python3
"""Verify the finite p-adic bound for the H4 p-source/p-free gate."""

from __future__ import annotations

import argparse
from math import gcd, lcm

import sympy

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    base_prime,
    h3_data,
    selector_a,
)
from type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion import (
    complete_excess,
    positive_divisors,
)


D_OFFSET = 11_943_424
D_MULTIPLIER = 2_261
CAPACITY_NUMERATOR = 4_718_592
RESIDUE_CONSTANT = 2_032_214_838_431_711_232
ZERO_COEFFICIENT = 52_042_924_032
RESIDUE_DENOMINATOR = 10_668_736_512
SOURCE_RESIDUE_EXCEPTION_BOUND = 2_008_653_632_908_535_334_215


def symbolic_h4_carrier_coefficients() -> None:
    """Derive the first two p-adic coefficients of M4 exactly."""
    prime, a, lambda_value = sympy.symbols("prime a lambda", nonzero=True)
    f = 2 * prime**2 - 3 * prime - 1
    m0 = (prime - 1) * (2 * prime + 1) * f / 8
    r0 = sympy.cancel((8 * m0 - 1) / prime)
    q0 = sympy.cancel((r0 - 1) / 2)
    m1 = sympy.cancel(m0 * q0)
    c1 = (2 * prime + 4) / 3
    r1 = sympy.cancel((4 * m1 * c1 - 1) / prime)
    q1 = sympy.cancel((r1 - 1) / 2)
    m2 = sympy.cancel(m1 * q1)
    c2 = (13 * prime + 16) / 19
    r2 = sympy.cancel((4 * m2 * c2 - 1) / prime)
    q2 = sympy.cancel((r2 - 1) / 2)
    m3 = sympy.cancel(m2 * q2)
    c3 = (1_536 + a * prime) / D_MULTIPLIER
    r3 = sympy.cancel((4 * m3 * c3 - 1) / prime)
    l4 = sympy.cancel((r3 - 1) / (2 * lambda_value))
    m4 = sympy.cancel(m3 * l4)
    coefficients = sympy.Poly(m4, prime)
    expected_constant = (D_MULTIPLIER * a - D_OFFSET) / (18_874_368 * lambda_value)
    expected_linear = -(
        1_168_937 * a + 14_013_490_384
    ) / (2_000_388_096 * lambda_value)
    if not (
        coefficients.degree() == 56
        and sympy.cancel(coefficients.nth(0) - expected_constant) == 0
        and sympy.cancel(coefficients.nth(1) - expected_linear) == 0
    ):
        raise AssertionError("the symbolic H4 carrier expansion changed")


def source_residue_numerator(a: int, lambda_value: int, lift: int, target: int) -> int:
    """Return the cleared numerator for R4 == target modulo p."""
    if target not in {0, 1}:
        raise ValueError("only the p-source and p-free gate residues are supported")
    d_value = D_OFFSET - D_MULTIPLIER * a
    coefficient = ZERO_COEFFICIENT + target * RESIDUE_DENOMINATOR
    return RESIDUE_CONSTANT * lambda_value - d_value * (
        coefficient * lambda_value + D_MULTIPLIER * lift
    )


def finite_source_residue_bound() -> dict[str, object]:
    """Bound every possible nonzero cleared residue numerator without prime scans."""
    pair_count = 0
    d_max = 0
    lambda_max = 0
    lift_max = 0
    maximum = 0
    maximum_record: tuple[str, int, int, int, int, int] | None = None
    zero_roots: list[tuple[int, int, int, int, int]] = []

    for residue in sorted(FINAL_RESIDUAL):
        a = selector_a(base_prime(residue))
        d_value = D_OFFSET - D_MULTIPLIER * a
        if d_value <= 0:
            raise AssertionError("the H4 capacity denominator lost positivity")
        d_max = max(d_max, d_value)
        for lambda_value in positive_divisors(abs(1_536 - a)):
            pair_count += 1
            lambda_max = max(lambda_max, lambda_value)
            numerator = CAPACITY_NUMERATOR * lambda_value
            # D*c4 + N = t*p and c4 <= p-2 give this exact uniform interval.
            lift_limit = d_value + (numerator - 1) // 73
            lift_max = max(lift_max, lift_limit)
            for target in (0, 1):
                coefficient = ZERO_COEFFICIENT + target * RESIDUE_DENOMINATOR
                root_numerator = lambda_value * (RESIDUE_CONSTANT - d_value * coefficient)
                root_denominator = D_MULTIPLIER * d_value
                if root_numerator % root_denominator == 0:
                    root = root_numerator // root_denominator
                    if 1 <= root <= lift_limit:
                        zero_roots.append((target, residue, a, lambda_value, root))
                for lift in (1, lift_limit):
                    value = abs(source_residue_numerator(a, lambda_value, lift, target))
                    if value > maximum:
                        maximum = value
                        maximum_record = (
                            "zero" if target == 0 else "one",
                            residue,
                            a,
                            lambda_value,
                            lift,
                            lift_limit,
                        )

    if not (
        pair_count == 213
        and d_max == 11_656_277
        and lambda_max == 1_409
        and lift_max == 102_731_566
        and zero_roots == []
        and maximum == SOURCE_RESIDUE_EXCEPTION_BOUND
        and maximum_record == ("zero", 27, 127, 1_409, 1, 102_731_566)
        and SOURCE_RESIDUE_EXCEPTION_BOUND > RESIDUE_DENOMINATOR
    ):
        raise AssertionError("the H4 source-residue finite bound changed")

    return {
        "phase_lambda_pairs": pair_count,
        "max_D": d_max,
        "max_lambda": lambda_max,
        "max_lift": lift_max,
        "zero_numerator_roots": zero_roots,
        "source_residue_exception_bound": maximum,
    }


def h4_source_residue_control(prime: int) -> dict[str, int]:
    """Check the p-adic formula against a real H4 control state."""
    data = h3_data(prime)
    a = int(data["a"])
    m3 = int(data["M_3"])
    k3 = int(data["K_3"])
    r3 = int(data["R_3"])
    c3 = int(data["c_3"])
    block4, beta4 = complete_excess(r3 - 1, k3)
    overlap4 = gcd(m3, block4)
    lambda_value = beta4 * overlap4 // 2
    m4 = lcm(m3, block4)
    c4 = c3 * pow(m4 // m3, -1, prime) % prime
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // prime
    d_value = D_OFFSET - D_MULTIPLIER * a
    lift_numerator = d_value * c4 + CAPACITY_NUMERATOR * lambda_value
    lift, remainder = divmod(lift_numerator, prime)
    denominator = RESIDUE_DENOMINATOR * d_value * lambda_value
    formula_numerator = source_residue_numerator(a, lambda_value, lift, 0)

    if not (
        prime % 24 == 1
        and 1 <= c4 <= prime - 2
        and remainder == 0
        and lift >= 1
        and gcd(denominator, prime) == 1
        and r4 % prime
        == formula_numerator * pow(denominator, -1, prime) % prime
    ):
        raise AssertionError("the H4 source-residue control changed")

    return {
        "p": prime,
        "a": a,
        "lambda": lambda_value,
        "lift": lift,
        "r4_mod_p": r4 % prime,
    }


def verify() -> None:
    symbolic_h4_carrier_coefficients()
    finite = finite_source_residue_bound()
    hard = h4_source_residue_control(14_449)
    clean = h4_source_residue_control(665_617)
    if not (
        finite
        == {
            "phase_lambda_pairs": 213,
            "max_D": 11_656_277,
            "max_lambda": 1_409,
            "max_lift": 102_731_566,
            "zero_numerator_roots": [],
            "source_residue_exception_bound": SOURCE_RESIDUE_EXCEPTION_BOUND,
        }
        and hard
        == {
            "p": 14_449,
            "a": 431,
            "lambda": 5,
            "lift": 10_167_387,
            "r4_mod_p": 4_039,
        }
        and clean
        == {
            "p": 665_617,
            "a": 431,
            "lambda": 1,
            "lift": 335_988,
            "r4_mod_p": 333_704,
        }
    ):
        raise AssertionError("the H4 finite source-residue receipts changed")
    print("verified the finite H4 p-source/p-free residue bound")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the exact finite residue receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
