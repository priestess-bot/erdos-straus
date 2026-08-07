#!/usr/bin/env python3
"""Verify the Type-II two-tail / dyadic-source nonoverlap control.

The claim contains the universal proof.  This script recomputes the algebraic
identities used there and one prime core-19 61-carrier affine control.  It does
not prove that every parameter is prime or create a selector edge.
"""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_high_r_chart_two_anchor as shared


GAP = 191
M_BASE = 12_424_897_516
M_STEP = 34_021_221_780
P_BASE = 145_520_399_707_201
P_STEP = 398_456_549_487_360
ADAPTIVE_P_BASE = 181_740_263_041
ADAPTIVE_P_STEP = 204_127_330_680
ADAPTIVE_R_BASE = 787_541_139_831
ADAPTIVE_R_STEP = 884_551_766_280


def valuation_two(value: int) -> int:
    """Return the two-adic valuation of one positive integer."""
    if value <= 0:
        raise AssertionError("two-adic valuation expects a positive integer")
    return (value & -value).bit_length() - 1


def assert_egyptian(denominator: int, terms: tuple[int, int, int]) -> None:
    """Check one displayed three-unit-fraction identity without fractions."""
    first, second, third = terms
    if min(terms) <= 0 or 4 * first * second * third != denominator * (
        second * third + first * third + first * second
    ):
        raise AssertionError("two-tail Egyptian identity changed")


def factor_pair_source(*, p: int, gap: int, A: int, B: int, C: int) -> tuple[int, int]:
    """Verify the complete factor-pair data and return (n, x)."""
    if not (
        p % 4 == 1
        and gap % 4 == 3
        and 3 <= gap <= p - 2
        and (p - 1) % (gap + 1) == 0
    ):
        raise AssertionError("gap or divisibility hypotheses changed")
    n = (p + gap) // (gap + 1)
    x = (p + gap) // 4
    if not (
        2 <= n < p
        and x == A * B * C
        and gcd(A, B) == 1
        and A <= B
        and (A + B) % gap == 0
    ):
        raise AssertionError("Type-II factor-pair normal form changed")
    carrier = (A + B) // gap
    divisor = A * A * C
    if divisor > x or x * x % divisor or (x + divisor) % gap:
        raise AssertionError("Type-II divisor conditions changed")
    assert_egyptian(n, (x, A * C * carrier, B * C * carrier))
    assert_egyptian(p, (x, p * A * C * carrier, p * B * C * carrier))
    return n, x


def forced_factor_receipt(*, p: int, R: int, K: int, gap: int, n: int) -> dict[str, int | bool]:
    """Recompute the universal proof identities for one two-tail source."""
    if not (p % 4 == 1 and R % 4 == 3 and 4 * K == p * R + 1):
        raise AssertionError("Type-I chart hypotheses changed")
    a = gap * R
    E = 4 * K - n * R
    if not (
        p - n == gap * (n - 1)
        and E == a * (n - 1) + 1
        and E % R == 1
        and gcd(E, R) == 1
    ):
        raise AssertionError("forced dyadic factor identities changed")

    n_square_gap = n * n - E
    a_square_gap = (a - 1) * (a - 1) - E
    if n_square_gap != (n - 1) * (n - a + 1):
        raise AssertionError("first affine-square factorization changed")
    if a_square_gap != a * (a - n - 1):
        raise AssertionError("second affine-square factorization changed")
    if E <= n * n:
        raise AssertionError("focused carrier no longer exhibits the visible square barrier")
    if (2 * K) * (2 * K) % E == 0:
        raise AssertionError("focused carrier unexpectedly became a dyadic terminal")

    return {
        "a_equals_gap_times_R": a,
        "forced_E": E,
        "n_square_gap": n_square_gap,
        "a_square_gap": a_square_gap,
        "v2_forced_E": valuation_two(E),
        "v2_dyadic_square": valuation_two(4 * K * K),
        "E_exceeds_n_square": E > n * n,
        "E_divides_dyadic_square": (2 * K) * (2 * K) % E == 0,
    }


def verify_core19_61_affine_control() -> dict[str, object]:
    """Check one prime point on z=1+4u, where every N is divisible by four."""
    u = 1
    M = M_BASE + M_STEP * u
    N = 61 * M
    p = P_BASE + P_STEP * u
    v = 712 + 1_952 * u
    R = 832 * N - 841
    K = (p * R + 1) // 4
    if not (
        M % 4 == 0
        and M_STEP % 4 == 0
        and N % 4 == 0
        and P_BASE == 11_712 * M_BASE - GAP
        and P_STEP == 11_712 * M_STEP
        and p == 11_712 * M - GAP
        and p % 24 == 1
        and p == ADAPTIVE_P_BASE + ADAPTIVE_P_STEP * v
        and R == ADAPTIVE_R_BASE + ADAPTIVE_R_STEP * v
        and 4 * K == p * R + 1
        and gcd(P_BASE, P_STEP) == 1
        and v == 224 + 488 * (1 + 4 * u)
        and shared.is_prime(p)
    ):
        raise AssertionError("core-19 61-carrier affine normalization changed")

    n, x = factor_pair_source(p=p, gap=GAP, A=8, B=183, C=2 * M)
    if n != N or x != 2_928 * M:
        raise AssertionError("core-19 source or first denominator changed")
    receipt = forced_factor_receipt(p=p, R=R, K=K, gap=GAP, n=n)
    if receipt["a_equals_gap_times_R"] - (n + 1) <= 0:
        raise AssertionError("core-19 square barrier direction changed")

    return {
        "affine_parameter": {"u": u, "v": v},
        "M": M,
        "N": N,
        "p": p,
        "R": R,
        "K": K,
        "primitive_p_progression": {"base": P_BASE, "step": P_STEP, "gcd": 1},
        "control_point_is_prime": True,
        "factor_pair": {"gap": GAP, "A": 8, "B": 183, "C": 2 * M, "x": x},
        "source_divisible_by_four": True,
        "forced_factor_receipt": receipt,
    }


def build_result() -> dict[str, object]:
    """Build the narrow affine receipt; the general argument remains in the claim."""
    return {
        "certificate_type": "type_ii_factor_pair_dyadic_source_nonoverlap_v1",
        "scope": (
            "One primitive 61-carrier affine control for the universal nonoverlap "
            "theorem. It certifies only the displayed u=1 prime point, not every "
            "affine parameter or a selector edge."
        ),
        "core19_61_affine_control": verify_core19_61_affine_control(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified Type-II two-tail / dyadic-source nonoverlap control")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
