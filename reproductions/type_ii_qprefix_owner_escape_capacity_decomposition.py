#!/usr/bin/env python3
"""Verify tight/slack q-prefix owner escape decompositions."""

from __future__ import annotations

import argparse
from collections import Counter


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def layer_data(prime: int, q: int, shifts: tuple[int, ...], layer: int) -> tuple[int, int, int, tuple[int, ...]]:
    heights = tuple(valuation(prime + 4 * shift, q) for shift in shifts)
    active = tuple(index for index, height in enumerate(heights) if height >= layer)
    counts = Counter(shift % (q**layer) for shift in shifts)
    capacity = max(counts.values(), default=0)
    return len(active), capacity, capacity - len(active), active


def positive(value: int) -> int:
    return max(value, 0)


def check_decomposition(owner_count: int, capacity: int, demand: int, multiplicity: int) -> tuple[int, int, int]:
    owner_gap = positive(demand - multiplicity * owner_count)
    slack = multiplicity * (capacity - owner_count)
    global_gap = positive(demand - multiplicity * capacity)
    if global_gap != positive(owner_gap - slack):
        raise AssertionError("owner/capacity decomposition changed")
    return owner_gap, slack, global_gap


def verify() -> None:
    prime = 433
    q = 7

    tight = (16, 100)
    if layer_data(prime, q, tight, 1)[:3] != (2, 2, 0):
        raise AssertionError("tight layer one changed")
    if layer_data(prime, q, tight, 2)[:3] != (1, 1, 0):
        raise AssertionError("tight layer two changed")
    tight_gap = check_decomposition(owner_count=1, capacity=1, demand=2, multiplicity=1)
    if tight_gap != (1, 0, 1):
        raise AssertionError("tight q-prefix deficit changed")
    if valuation(tight[1] - tight[0], q) != 1:
        raise AssertionError("tight owner boundary changed")

    slack = (16, 100, 3, 10, 17)
    if layer_data(prime, q, slack, 1)[:3] != (2, 3, 1):
        raise AssertionError("slack layer one changed")
    slack_gap = check_decomposition(owner_count=2, capacity=3, demand=3, multiplicity=1)
    if slack_gap != (1, 1, 0):
        raise AssertionError("slack absorption changed")
    if layer_data(prime, q, slack, 2)[:3] != (1, 1, 0):
        raise AssertionError("slack layer two changed")
    if valuation(100 - 16, q) != 1:
        raise AssertionError("slack owner boundary changed")

    print(
        "verified q-prefix owner escape decomposition: "
        "p=433 tight boundary and alternate-capacity slack"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the focused exact check")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
