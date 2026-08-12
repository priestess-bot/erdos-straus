#!/usr/bin/env python3
"""Verify the fixed two-sided capacity-tree and split-carrier receipts.

This focused verifier checks one depth-three CRT tree and two local contract
boundaries. It performs no prime-range, denominator, or historical scan.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm


P = 73
TREE_DEPTH = 3
TREE_PARAMETER = (
    32_150_457_426_076_906_549_030_965_202_251_906_656_011_250_208_523_768_862_218_456_903
)
TREE_MODULUS = 549_292_384_417_183_915_231_271_884_719_311_373_697_168_902_443_727_883_898_439_155
EXPECTED_LEVELS = (
    (74,),
    (5_403, 5_330),
    (394_420, 394_347, 389_091, 389_018),
    (
        28_792_661,
        28_792_588,
        28_787_332,
        28_787_259,
        28_403_644,
        28_403_571,
        28_398_315,
        28_398_242,
    ),
)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def complete_excess(value: int, capacity: int) -> tuple[int, int]:
    block = 1
    for prime, exponent in factorization(value).items():
        if exponent > valuation(capacity, prime):
            block *= prime**exponent
    return block, value // block


def chart(prime: int, parameter: int) -> tuple[int, int, int, int, int, int]:
    b = 2 * prime * parameter - 1
    n = (prime + 1) * b - 1
    support = (prime * n - 1) // 4
    residual = (prime - 1) * n - 1
    capacity = support * (prime - 1)
    adjustable = prime * prime * parameter - (prime + 1) // 2
    return b, n, support, residual, capacity, adjustable


def successors(prime: int, anchor: int) -> tuple[int, int]:
    return prime * anchor + 1, prime * anchor - prime + 1


def raw_p_peel(residual: int, anchor: int, prime: int) -> tuple[int, int]:
    departure = residual - anchor
    if valuation(departure, prime) != 1:
        raise AssertionError("departure is not exactly p-primary")
    selected = departure // prime
    other = residual - selected
    if gcd(selected, other) != 1:
        raise AssertionError("unexpected gcd reduction in the raw p-edge")
    return selected, other


def verify_binary_tree() -> None:
    p = P
    g = (p + 1) // 2
    fixed_base = (p * p - 1) // 2
    levels: list[list[int]] = [[p + 1]]
    for _ in range(TREE_DEPTH):
        levels.append(
            [child for anchor in levels[-1] for child in successors(p, anchor)]
        )

    if tuple(tuple(level) for level in levels) != EXPECTED_LEVELS:
        raise AssertionError("fixed P/M tree changed")

    modulus = 1
    for anchor in (anchor for level in levels for anchor in level):
        modulus = lcm(modulus, anchor // gcd(anchor, fixed_base))
    if modulus != TREE_MODULUS:
        raise AssertionError("fixed CRT tree modulus changed")

    _, _, support, residual, capacity, adjustable = chart(p, TREE_PARAMETER)
    forbidden_parameters = {(-pow(2, -1, p)) % p, p - 1}
    if not (
        p * residual + 1 == 4 * capacity
        and support == g * adjustable
        and capacity == fixed_base * adjustable
        and adjustable % modulus == 0
        and TREE_PARAMETER % p not in forbidden_parameters
        and gcd(residual, capacity) == 1
    ):
        raise AssertionError("fixed CRT chart changed")

    for anchor in (anchor for level in levels for anchor in level):
        if not (
            anchor % p == 1
            and capacity % anchor == 0
            and anchor % (p * p) in (1, p + 1)
        ):
            raise AssertionError(f"tree-node capacity changed at {anchor}")

    edge_count = 0
    for depth, parents in enumerate(levels[:-1]):
        expected_children = levels[depth + 1]
        for index, anchor in enumerate(parents):
            selected, other = raw_p_peel(residual, anchor, p)
            plus, minus = successors(p, anchor)
            if (plus, minus) != tuple(expected_children[2 * index : 2 * index + 2]):
                raise AssertionError("tree edge ordering changed")
            if not (
                p * p * selected == 4 * capacity - plus
                and p * p * other == 4 * (p - 1) * capacity + minus
                and gcd(selected, capacity) == plus
                and gcd(other, capacity) == minus
                and gcd(plus, minus) == 1
                and capacity % (plus * minus) == 0
                and selected > plus
                and other > minus
                and (residual - plus) % p == 0
                and (residual - minus) % p == 0
                and capacity % p != 0
            ):
                raise AssertionError(f"two-sided capacity macro changed at {anchor}")
            edge_count += 2

    if edge_count != 14:
        raise AssertionError("depth-three tree edge count changed")


def assert_pairwise_coprime(values: tuple[int, ...]) -> None:
    if any(gcd(left, right) != 1 for left, right in combinations(values, 2)):
        raise AssertionError("split complete-excess factors are no longer pairwise coprime")


def split_receipt(parameter: int, anchor: int) -> dict[str, int]:
    p = P
    _, _, support, residual, capacity, _ = chart(p, parameter)
    selected, other = raw_p_peel(residual, anchor, p)
    q_selected, beta_selected = complete_excess(selected, capacity)
    q_other, beta_other = complete_excess(other, capacity)
    assert_pairwise_coprime((q_selected, beta_selected, q_other, beta_other))
    if not (
        q_selected * beta_selected == selected
        and q_other * beta_other == other
        and capacity % (beta_selected * beta_other) == 0
        and q_selected > 1
        and q_other > 1
        and capacity % (other * beta_selected) != 0
        and capacity % (selected * beta_other) != 0
    ):
        raise AssertionError("double-excess single-side admission boundary changed")

    target_support = lcm(support, q_selected, q_other)
    multiplier = target_support // support
    target_cofactor = pow(4 * target_support, -1, p)
    target_capacity = target_support * target_cofactor
    target_residual = (4 * target_capacity - 1) // p
    if not (
        (q_selected * q_other) % p != 0
        and target_support % support == 0
        and target_capacity % target_support == 0
        and p * target_residual + 1 == 4 * target_capacity
    ):
        raise AssertionError("split-carrier canonical arithmetic changed")

    return {
        "support": support,
        "residual": residual,
        "capacity": capacity,
        "selected": selected,
        "other": other,
        "q_selected": q_selected,
        "beta_selected": beta_selected,
        "q_other": q_other,
        "beta_other": beta_other,
        "target_support": target_support,
        "multiplier": multiplier,
        "target_cofactor": target_cofactor,
        "target_capacity": target_capacity,
        "target_residual": target_residual,
    }


def verify_split_boundaries() -> None:
    strict = split_receipt(parameter=1, anchor=1)
    if strict != {
        "support": 195_804,
        "residual": 772_487,
        "capacity": 14_097_888,
        "selected": 10_582,
        "other": 761_905,
        "q_selected": 143,
        "beta_selected": 74,
        "q_other": 761_905,
        "beta_other": 1,
        "target_support": 21_333_318_666_660,
        "multiplier": 108_952_415,
        "target_cofactor": 67,
        "target_capacity": 1_429_332_350_666_220,
        "target_residual": 78_319_580_858_423,
    }:
        raise AssertionError("strict split-carrier fixture changed")
    if strict["target_cofactor"] >= strict["capacity"] // strict["support"]:
        raise AssertionError("strict split-carrier target stopped descending")

    stutter = split_receipt(parameter=50, anchor=74)
    if stutter != {
        "support": 9_857_281,
        "residual": 38_888_999,
        "capacity": 709_724_232,
        "selected": 532_725,
        "other": 38_356_274,
        "q_selected": 177_575,
        "beta_selected": 3,
        "q_other": 19_178_137,
        "beta_other": 2,
        "target_support": 33_569_538_991_535_629_775,
        "multiplier": 3_405_557_677_775,
        "target_cofactor": 72,
        "target_capacity": 2_417_006_807_390_565_343_800,
        "target_residual": 132_438_729_172_085_772_263,
    }:
        raise AssertionError("stuttering split-carrier fixture changed")
    if not (
        stutter["multiplier"] % P == 1
        and stutter["target_cofactor"] == stutter["capacity"] // stutter["support"]
        and {
            pow(4 * lcm(stutter["support"], stutter["q_selected"]), -1, P),
            pow(4 * lcm(stutter["support"], stutter["q_other"]), -1, P),
        }
        == {34, 58}
    ):
        raise AssertionError("split carry-stutter boundary changed")

    if Fraction(4, P) != (
        Fraction(1, 20) + Fraction(1, 219) + Fraction(1, 4_380)
    ):
        raise AssertionError("fixed p=73 terminal-first control changed")


def verify() -> None:
    verify_binary_tree()
    verify_split_boundaries()
    print(
        "verified 1 depth-3 two-sided capacity tree (15 nodes, 14 macros), "
        "1 strict split boundary, and 1 split carry stutter"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify to run the fixed receipt")
    verify()


if __name__ == "__main__":
    main()
