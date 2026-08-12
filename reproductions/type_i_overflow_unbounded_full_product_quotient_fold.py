#!/usr/bin/env python3
"""Verify focused algebraic receipts for unbounded full-product quotient folds.

The script checks the arithmetic target and exact lexicographic-rank payment.
It deliberately does not classify F/G/hit: a general typed charged-chart
adapter must independently do that work before a real receipt is admitted.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class Fixture:
    name: str
    prime: int
    carrier: int
    d: int
    denominator: int
    support: int
    expected_source_rank: tuple[int, int]
    expected_target_rank: tuple[int, int]
    strict: bool


FIXTURES = (
    Fixture(
        "p73_d_one_same_chart_support_upgrade",
        73,
        1332,
        1,
        73,
        6,
        (216, 15984),
        (0, 72),
        True,
    ),
    Fixture(
        "p73_h_rough_double_atlas_hole",
        73,
        2051,
        13,
        1461,
        293,
        (4, 420),
        (0, 72),
        True,
    ),
    Fixture(
        "p673_h_rough_double_atlas_hole",
        673,
        215923,
        647,
        830325,
        821,
        (137, 6838),
        (0, 672),
        True,
    ),
    Fixture(
        "p73_support_saturated_rough_g",
        73,
        97,
        19,
        101,
        97,
        (13, 54),
        (0, 72),
        True,
    ),
    Fixture(
        "p73_support_saturated_rough_f",
        73,
        56,
        29,
        89,
        56,
        (23, 44),
        (0, 72),
        True,
    ),
    Fixture(
        "p97_support_saturated_rough_g",
        97,
        79,
        31,
        101,
        79,
        (29, 66),
        (0, 96),
        True,
    ),
    Fixture(
        "p97_support_saturated_rough_f",
        97,
        70,
        53,
        153,
        70,
        (32, 44),
        (0, 96),
        True,
    ),
    Fixture(
        "p73_d_one_support_saturated_stutter",
        73,
        91,
        1,
        5,
        91,
        (14, 72),
        (14, 72),
        False,
    ),
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def audit(fixture: Fixture) -> dict[str, int | str | tuple[int, int]]:
    p = fixture.prime
    M = fixture.carrier
    d = fixture.d
    n = fixture.denominator
    A = fixture.support
    B = (p - 1) ** 2 // 4
    b, remainder = divmod(M, A)
    S = M * d
    source_R = 4 * M - n
    source_K = M * (p - d)
    source_rank = (B // A, source_K // A)
    target_M = S
    target_d = 1
    target_n = n
    target_R = 4 * S - n
    target_K = S * (p - 1)
    target_rank = (B // S, target_K // S)
    strict_rank = target_rank < source_rank

    if not (
        is_prime(p)
        and p % 24 == 1
        and 1 <= A <= B
        and remainder == 0
        and 1 <= d < p
        and p * n == 4 * M * d + 1
        and source_R > p
        and 4 * source_K == p * source_R + 1
        and source_K % A == 0
        and p * target_n == 4 * target_M * target_d + 1
        and 0 < target_R < 4 * target_M
        and target_R % 4 == 3
        and 4 * target_K == p * target_R + 1
        and target_K % S == 0
        and source_rank == fixture.expected_source_rank
        and target_rank == fixture.expected_target_rank
    ):
        raise AssertionError(f"{fixture.name}: algebraic contract changed")

    if fixture.strict:
        if not (
            S > A
            and S // A == b * d
            and B // S < B // A
            and strict_rank
        ):
            raise AssertionError(f"{fixture.name}: strict full-product rank payment changed")
        return {
            "name": fixture.name,
            "kind": "strict_full_product_quotient_fold",
            "target_support": S,
            "source_rank": source_rank,
            "target_rank": target_rank,
        }

    if not (
        S == A
        and b == 1
        and d == 1
        and target_M == M
        and target_R == source_R
        and target_K == source_K
        and not strict_rank
    ):
        raise AssertionError(f"{fixture.name}: exact stutter boundary changed")
    return {
        "name": fixture.name,
        "kind": "full_product_stutter_boundary",
        "target_support": S,
        "source_rank": source_rank,
        "target_rank": target_rank,
    }


def verify() -> None:
    receipts = [audit(fixture) for fixture in FIXTURES]
    strict_count = sum(
        receipt["kind"] == "strict_full_product_quotient_fold" for receipt in receipts
    )
    stutter_count = sum(
        receipt["kind"] == "full_product_stutter_boundary" for receipt in receipts
    )
    if (strict_count, stutter_count) != (7, 1):
        raise AssertionError("focused receipt classification changed")
    print(
        "verified 7 strict unbounded full-product quotient folds and "
        "1 exact d=1 support-saturated stutter boundary"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run focused exact checks")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
