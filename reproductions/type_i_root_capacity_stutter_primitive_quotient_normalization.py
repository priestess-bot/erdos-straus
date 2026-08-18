#!/usr/bin/env python3
"""Verify primitive quotient normalization for proper-root stutter arithmetic.

The controls verify exact integer identities only. They deliberately do not
search for actual receipts, source occurrences, terminal certificates, or
selector edges.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class StutterData:
    p: int
    h: int
    m: int
    e: int
    a: int
    b: int
    norm: int
    k: int


@dataclass(frozen=True)
class PrimitiveQuotient:
    g: int
    A: int
    B: int
    alpha: int
    kappa: int
    M: int


def stutter_data(p: int, h: int, m: int, e: int) -> StutterData:
    """Reconstruct one integral stutter tuple from its linear data."""
    a = e * m - h
    b = e - 1
    norm = a * a - a * b + b * b
    if a <= 0 or b <= 0 or norm % h:
        raise AssertionError("control is not a positive integral stutter tuple")
    data = StutterData(p, h, m, e, a, b, norm, norm // h)
    if p * a != e * (h - 1) + 1:
        raise AssertionError("stutter linear identity changed")
    return data


def normalize(data: StutterData) -> PrimitiveQuotient:
    """Separate the common Eisenstein factor from the primitive quotient."""
    g = gcd(data.a, data.b)
    if data.h % g or data.k % g or data.m % g:
        raise AssertionError("common factor no longer divides h, k, and m")
    return PrimitiveQuotient(
        g=g,
        A=data.a // g,
        B=data.b // g,
        alpha=data.h // g,
        kappa=data.k // g,
        M=data.m // g,
    )


def verify_primitive_system(data: StutterData, normal: PrimitiveQuotient) -> None:
    """Check the normalized stutter equations before using the root gate."""
    g, A, B, alpha, kappa, M = (
        normal.g,
        normal.A,
        normal.B,
        normal.alpha,
        normal.kappa,
        normal.M,
    )
    if not (
        gcd(A, B) == 1
        and data.e == g * B + 1
        and data.a == g * A
        and data.b == g * B
        and data.h == g * alpha
        and data.k == g * kappa
        and data.m == g * M
        and A * A - A * B + B * B == alpha * kappa
        and A + alpha == data.e * M
        and data.p * A + B == data.e * alpha
    ):
        raise AssertionError("primitive quotient normalization changed")


def verify_cyclotomic_saturation(
    data: StutterData, normal: PrimitiveQuotient
) -> None:
    """Check the normalized quotient identity available only at an actual root."""
    cyclotomic = data.p * data.p + data.p + 1
    if cyclotomic % data.h:
        raise AssertionError("control does not satisfy the cyclotomic root gate")
    saturation = (
        data.e * data.e * normal.alpha
        + data.e * (normal.A - 2 * normal.B)
        + normal.kappa
    )
    if not (
        saturation == normal.g * normal.A * normal.A * (cyclotomic // data.h)
        and saturation % (normal.g * normal.A * normal.A) == 0
        and (normal.alpha + normal.kappa + normal.A - 2 * normal.B) % normal.g
        == 0
    ):
        raise AssertionError("cyclotomic saturation identity changed")


def is_prime(value: int) -> bool:
    """Return whether a positive integer is prime for the fixed controls."""
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def verify_quotient_only_cyclotomic_split(
    data: StutterData, normal: PrimitiveQuotient, q: int
) -> None:
    """Check the exact q|C_p/h split for one quotient-only prime."""
    cyclotomic = data.p * data.p + data.p + 1
    if cyclotomic % data.h:
        raise AssertionError("control does not satisfy the cyclotomic root gate")
    v = cyclotomic // data.h
    linear = (data.p + 1) * normal.A - normal.B
    bridge = normal.kappa + data.e * linear
    right_branch = data.e % q == 0 or linear % q == 0
    if not (
        is_prime(q)
        and normal.kappa % q == 0
        and data.h % q != 0
        and gcd(q, normal.g * normal.A * normal.B * normal.alpha) == 1
        and bridge == normal.g * normal.A * normal.A * v
        and (v % q == 0) == right_branch
    ):
        raise AssertionError("quotient-only cyclotomic split changed")


def verify_shared_factor_control() -> None:
    """Replay a root-shape tuple with a nontrivial shared g=3 factor."""
    data = stutter_data(25_957, 9_327, 3, 3_532)
    normal = normalize(data)
    verify_primitive_system(data, normal)
    verify_cyclotomic_saturation(data, normal)
    if not (
        (normal.g, normal.A, normal.B, normal.alpha, normal.kappa, normal.M)
        == (3, 423, 1_177, 3_109, 343, 1)
        and normal.g * normal.kappa == data.k
    ):
        raise AssertionError("shared-factor primitive control changed")


def verify_primitive_quotient_control() -> None:
    """Replay a root-shape tuple whose quotient carrier is outside h."""
    data = stutter_data(54_481, 12_063, 13, 944)
    normal = normalize(data)
    verify_primitive_system(data, normal)
    verify_cyclotomic_saturation(data, normal)
    verify_quotient_only_cyclotomic_split(data, normal, 61)
    cyclotomic_complement = (data.p * data.p + data.p + 1) // data.h
    linear = (data.p + 1) * normal.A - normal.B
    if not (
        (normal.g, normal.A, normal.B, normal.alpha, normal.kappa, normal.M)
        == (1, 209, 943, 12_063, 61, 13)
        and gcd(normal.kappa, data.h) == 1
        and data.k == normal.kappa
        and cyclotomic_complement % 61 != 0
        and data.e % 61 != 0
        and linear % 61 != 0
    ):
        raise AssertionError("primitive quotient-only control changed")


def verify_cyclotomic_complement_control() -> None:
    """Replay the q|e branch of the quotient-only cyclotomic split."""
    data = stutter_data(11, 19, 3, 14)
    normal = normalize(data)
    verify_primitive_system(data, normal)
    verify_cyclotomic_saturation(data, normal)
    verify_quotient_only_cyclotomic_split(data, normal, 7)
    cyclotomic_complement = (data.p * data.p + data.p + 1) // data.h
    linear = (data.p + 1) * normal.A - normal.B
    if not (
        (normal.g, normal.A, normal.B, normal.alpha, normal.kappa, normal.M)
        == (1, 23, 13, 19, 21, 3)
        and cyclotomic_complement == 7
        and data.e % 7 == 0
        and linear % 7 != 0
    ):
        raise AssertionError("cyclotomic-complement control changed")


def verify_missing_root_boundary() -> None:
    """Keep root saturation separate from the abstract k=3 curve equations."""
    data = stutter_data(939, 129, 6, 22)
    normal = normalize(data)
    verify_primitive_system(data, normal)
    cyclotomic = data.p * data.p + data.p + 1
    saturation = (
        data.e * data.e * normal.alpha
        + data.e * (normal.A - 2 * normal.B)
        + normal.kappa
    )
    if not (
        cyclotomic % data.h == 43
        and (normal.g, normal.A, normal.B, normal.alpha, normal.kappa, normal.M)
        == (3, 1, 7, 43, 1, 2)
        and saturation % (normal.g * normal.A * normal.A) == 1
    ):
        raise AssertionError("missing-root saturation boundary changed")


def verify() -> None:
    verify_shared_factor_control()
    verify_primitive_quotient_control()
    verify_cyclotomic_complement_control()
    verify_missing_root_boundary()
    print("verified primitive quotient normalization and cyclotomic split")
    print("no receipt, source, terminal, or selector search is performed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
