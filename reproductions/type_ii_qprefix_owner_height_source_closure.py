#!/usr/bin/env python3
"""Verify the p=433 q-prefix owner-height closure gate."""

from __future__ import annotations

import argparse


def valuation(value: int, prime: int) -> int:
    height = 0
    while value % prime == 0:
        value //= prime
        height += 1
    return height


def verify() -> None:
    prime = 433
    q = 7
    shifts = (16, 100)
    numerators = tuple(prime + 4 * shift for shift in shifts)
    heights = tuple(valuation(numerator, q) for numerator in numerators)
    if numerators != (497, 833) or heights != (1, 2):
        raise AssertionError("p=433 owner heights changed")

    layer_one = tuple(index for index, height in enumerate(heights) if height >= 1)
    layer_two = tuple(index for index, height in enumerate(heights) if height >= 2)
    if layer_one != (0, 1) or layer_two != (1,):
        raise AssertionError("owner layer sets changed")

    residue_capacity = {
        layer: max(
            sum(shift % (q**layer) == residue for shift in shifts)
            for residue in range(q**layer)
        )
        for layer in (1, 2)
    }
    if residue_capacity != {1: 2, 2: 1}:
        raise AssertionError("q-prefix residue capacity changed")
    if sum(heights) != sum(residue_capacity.values()) != 3:
        raise AssertionError("tight q-height capacity changed")

    # Layer 1 dominates both owners; layer 2 leaves shift 16 uncovered.
    if set(layer_one) != {0, 1}:
        raise AssertionError("layer-one source domination changed")
    escape = (shifts[0], heights[0], 2)
    if escape != (16, 1, 2):
        raise AssertionError("owner escape witness changed")

    demand = 2
    layer_two_slots = len(layer_two)
    if demand - layer_two_slots != 1:
        raise AssertionError("layer-two capacity deficit changed")

    print(
        "verified p=433 q=7 owner closure: "
        "layer-one domination, layer-two escape, tight capacity"
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
