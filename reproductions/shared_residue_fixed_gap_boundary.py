#!/usr/bin/env python3
"""Verify a core-prime fixed-gap failure of the coupled shared selector."""

from __future__ import annotations

import json
import math


def divisors(value: int) -> tuple[int, ...]:
    """Return all positive divisors of a positive integer in increasing order."""
    if value < 1:
        raise ValueError("value must be positive")
    lower: list[int] = []
    upper: list[int] = []
    for candidate in range(1, math.isqrt(value) + 1):
        if value % candidate:
            continue
        lower.append(candidate)
        paired = value // candidate
        if paired != candidate:
            upper.append(paired)
    return tuple(lower + list(reversed(upper)))


def fixed_gap_coupled_failure() -> dict[str, object]:
    """Return the exact p=73, m=47 witness.

    This is a failure at one legal gap, not a counterexample to the
    existential shared-residue selector, which may choose another gap.
    """
    prime = 73
    gap = 47
    x = (prime + gap) // 4
    if 4 * x != prime + gap or prime % 24 != 1 or gap % 4 != 3:
        raise AssertionError("the witness must be a legal core-prime gap")

    square_divisors = divisors(x * x)
    shifted_divisors = divisors(4 * x)
    square_residues = frozenset(divisor % gap for divisor in square_divisors)
    nontrivial_shared_divisors = tuple(
        divisor
        for divisor in shifted_divisors
        if divisor > 1 and divisor % gap == 1
    )
    target = (-x) % gap

    return {
        "prime": prime,
        "gap": gap,
        "x": x,
        "factorizations": {
            "x": [[2, 1], [3, 1], [5, 1]],
            "x_squared": [[2, 2], [3, 2], [5, 2]],
            "four_x": [[2, 3], [3, 1], [5, 1]],
        },
        "type_ii_target_residue": target,
        "x_squared_divisor_residues": tuple(sorted(square_residues)),
        "type_ii_target_reached": target in square_residues,
        "four_x_divisors": shifted_divisors,
        "nontrivial_shared_divisors": nontrivial_shared_divisors,
        "shared_target_reached": bool(nontrivial_shared_divisors),
    }


def json_ready(value: object) -> object:
    if isinstance(value, (frozenset, tuple, list)):
        return [json_ready(item) for item in value]
    if isinstance(value, dict):
        return {key: json_ready(item) for key, item in value.items()}
    return value


def main() -> int:
    print(json.dumps(json_ready(fixed_gap_coupled_failure()), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
