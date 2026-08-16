#!/usr/bin/env python3
"""Verify the q=1 immediate d=1 residual-capacity-four exclusion.

This focused receipt checks the sole odd-branch boundary and the finite
even-branch shape table. It does not scan primes or enumerate terminal paths.
"""

from __future__ import annotations

import argparse

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two


def odd_capacity_four_exclusion() -> dict[str, int]:
    """Replay the only odd-t core-prime boundary left by p <= 215."""
    row = capacity_two.receiver_data("odd", 3)
    prime, j, g, capacity = (
        int(row[key]) for key in ("prime", "j", "g", "c")
    )
    obstruction = 14 * j + 54 - 21 * g
    if not (
        prime == 73
        and j == 1
        and g == 1
        and capacity == 27
        and obstruction == 47
        and -100 <= obstruction <= 215
        and obstruction % 7 == 5
        and obstruction % prime != 0
        and (capacity * (7 * j + 27) - 42 * g) % prime == 0
    ):
        raise AssertionError("odd q=1 capacity-four boundary changed")
    return {"prime": prime, "j": j, "g": g, "obstruction": obstruction}


def even_shape_menu() -> tuple[tuple[int, int, int, int], ...]:
    """Check the c=4 finite k, g menu after parity and j mod 3."""
    shapes: list[tuple[int, int, int, int]] = []
    for k in range(3):
        for g in range(1, 17):
            if not ((16 - k) % g == 0 and g % 2 == 1 and g % 3 != 0):
                continue
            if k % 2 != 0:
                continue
            numerator_constant = 24 + k - 4 * g
            if numerator_constant % 2 != 0:
                raise AssertionError("even k did not make j integral")
            slope, intercept = 24 * k, numerator_constant // 2
            if intercept % 3 == 2:
                shapes.append((k, g, slope, intercept))
    result = tuple(shapes)
    if result != ((2, 1, 48, 11), (2, 7, 48, -1)):
        raise AssertionError("even capacity-four finite shape menu changed")
    return result


def even_shape_exclusion() -> dict[str, int]:
    """Verify both remaining affine j formulas exceed j < 18s-3."""
    shapes = even_shape_menu()
    lower_s = 2
    gaps = tuple(
        (slope - 18, intercept + 3) for _, _, slope, intercept in shapes
    )
    gap_values = tuple(slope * lower_s + intercept for slope, intercept in gaps)
    if not (
        all(slope > 0 for slope, _ in gaps)
        and all(gap > 0 for gap in gap_values)
    ):
        raise AssertionError("c=4 affine q-star bound changed")
    return {
        "shape_count": len(shapes),
        "minimum_s": lower_s,
        "minimum_gap": min(gap_values),
    }


def verify() -> None:
    odd = odd_capacity_four_exclusion()
    even = even_shape_exclusion()
    if not (
        odd["prime"] == 73
        and odd["obstruction"] == 47
        and even["shape_count"] == 2
        and even["minimum_gap"] == 62
    ):
        raise AssertionError("q=1 capacity-four exclusion receipt changed")
    print(
        "verified q=1 immediate d=1 capacity-four exclusion: "
        "odd boundary and both even shapes are impossible"
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
