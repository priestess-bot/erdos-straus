#!/usr/bin/env python3
"""Verify fixed actual receipts for strict root-carry support rebasing."""

from __future__ import annotations

import argparse
from math import lcm

from type_i_root_capacity_general_endpoint_divisor_gate import chart


def canonical_target(p: int, support: int) -> dict[str, int]:
    cofactor = pow(4 * support, -1, p)
    capacity = support * cofactor
    remainder = (4 * capacity - 1) // p
    deficit = p - cofactor
    denominator = 4 * support - remainder
    return {
        "cofactor": cofactor,
        "capacity": capacity,
        "remainder": remainder,
        "deficit": deficit,
        "denominator": denominator,
    }


def verify_strict_root_control(p: int, r: int, expected_cofactor: int) -> None:
    receipt = chart(p, r)
    support = receipt["A"]
    capacity = receipt["K"]
    remainder = receipt["R"]
    multiplier = receipt["E"]
    root_cofactor = (-pow(multiplier, -1, p)) % p
    endpoint_cofactor = (
        receipt["D"] * pow(receipt["h"] - 1, -1, p)
    ) % p

    old_target = canonical_target(p, support)
    rebased_support = lcm(support, receipt["Q"])
    rebased_target = canonical_target(p, rebased_support)
    bound = (p - 1) ** 2 // 4
    source_rank = (bound // support, capacity // support)
    target_rank = (
        bound // rebased_support,
        rebased_target["capacity"] // rebased_support,
    )

    if not (
        receipt["u"] < receipt["M"]
        and multiplier % p != 0
        and root_cofactor == endpoint_cofactor == expected_cofactor < p - 1
        and old_target["cofactor"] == p - 1
        and old_target["capacity"] == capacity
        and old_target["remainder"] == remainder
        and rebased_support == support * multiplier
        and rebased_target["cofactor"] == root_cofactor
        and rebased_support > support
        and capacity % rebased_support != 0
        and rebased_target["remainder"] > p
        and 2 <= rebased_target["deficit"] <= p - 1
        and p * rebased_target["denominator"]
        == 4 * rebased_support * rebased_target["deficit"] + 1
        and support > bound
        and rebased_support > bound
        and source_rank == (0, p - 1)
        and source_rank == (0, old_target["cofactor"])
        and target_rank == (0, root_cofactor)
        and target_rank < source_rank
    ):
        raise AssertionError("strict root-carry support rebase changed")


def verify() -> None:
    verify_strict_root_control(73, 3, 37)
    verify_strict_root_control(313, 271, 298)
    print(
        "verified strict root-carry support rebasing, old-support stutter, "
        "and high-support rank descent"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()


if __name__ == "__main__":
    main()
