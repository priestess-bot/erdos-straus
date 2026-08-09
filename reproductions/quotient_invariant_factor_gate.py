#!/usr/bin/env python3
"""Verify the invariant-factor quotient gate for finite abelian groups."""

from __future__ import annotations

import argparse


def quotient_surjection_gate(
    source_factors: tuple[int, ...],
    target_factors: tuple[int, ...],
) -> bool:
    """Return the invariant-factor criterion for an epimorphism."""
    source = tuple(factor for factor in source_factors if factor > 1)
    target = tuple(factor for factor in target_factors if factor > 1)
    if any(left > right or right % left for left, right in zip(source, source[1:])):
        raise AssertionError("source factors are not in invariant-factor order")
    if any(left > right or right % left for left, right in zip(target, target[1:])):
        raise AssertionError("target factors are not in invariant-factor order")
    if len(target) > len(source):
        return False
    offset = len(source) - len(target)
    return all(
        source[offset + index] % factor == 0
        for index, factor in enumerate(target)
    )


def verify() -> None:
    controls = {
        ((2,), (2, 2)): False,
        ((2, 2), (2, 2)): True,
        ((2, 4), (2, 2)): True,
        ((2, 4), (4, 4)): False,
        ((2, 4, 8), (2, 8)): True,
        ((2, 4, 8), (4, 8)): True,
        ((2, 6), (3,)): True,
        ((2, 6), (3, 3)): False,
    }
    for (source, target), expected in controls.items():
        actual = quotient_surjection_gate(source, target)
        if actual != expected:
            raise AssertionError(
                f"gate mismatch for A={source}, B={target}: {actual} != {expected}"
            )

    print("verified finite-abelian invariant-factor quotient gate")
    print(
        {
            "U4_to_C2xC2": quotient_surjection_gate((2,), (2, 2)),
            "U12_to_C2xC2": quotient_surjection_gate((2, 2), (2, 2)),
            "C2xC4_to_C4xC4": quotient_surjection_gate((2, 4), (4, 4)),
        }
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

