#!/usr/bin/env python3
"""Verify the q=1 immediate d=1 residual-capacity-three exclusion.

This focused arithmetic receipt replays the sole odd-branch boundary, the
finite even (k, g) menu, and the final polynomial identity. It does not scan
primes, enumerate terminals, or search for Egyptian-fraction decompositions.
"""

from __future__ import annotations

import argparse

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two


def odd_capacity_three_exclusion() -> dict[str, int]:
    """Replay the only odd-t core-prime boundary left by p <= 106."""
    row = capacity_two.receiver_data("odd", 3)
    prime, j, n, g, capacity = (
        int(row[key]) for key in ("prime", "j", "n", "g", "c")
    )
    obstruction = 7 * j + 27 - 14 * g
    if not (
        prime == 73
        and j == 1
        and n == 17
        and g == 1
        and capacity == 27
        and obstruction == 20
        and -106 <= obstruction <= 104
        and obstruction % 7 == 6
        and obstruction % prime != 0
        and (capacity * (7 * j + 27) - 42 * g) % prime == 0
    ):
        raise AssertionError("odd q=1 capacity-three boundary changed")
    return {"prime": prime, "j": j, "g": g, "obstruction": obstruction}


def even_shape_menu() -> tuple[tuple[int, int], ...]:
    """Check g | 24-k, parity, and mod-three conditions for 0 <= k <= 4."""
    shapes: list[tuple[int, int]] = []
    for k in range(5):
        for g in range(1, 25):
            if (
                (24 - k) % g == 0
                and g % 2 == 1
                and g % 3 != 0
                and (k + g) % 3 == 0
            ):
                shapes.append((k, g))
    result = tuple(shapes)
    if result != ((1, 23), (2, 1), (4, 5)):
        raise AssertionError("even capacity-three finite shape menu changed")
    return result


def even_capacity_formula_control() -> dict[str, int]:
    """Replay one inherited even-branch capacity congruence without a scan."""
    row = capacity_two.receiver_data("even", 32)
    prime, q_star, j, g, capacity = (
        int(row[key]) for key in ("prime", "q_star", "j", "g", "c")
    )
    if not (
        prime == 769
        and q_star == 19
        and j == 8
        and g == 1
        and capacity == 2
        and (capacity * (12 - j) - 8 * g) % prime == 0
    ):
        raise AssertionError("inherited even capacity congruence changed")
    return {"prime": prime, "j": j, "g": g, "capacity": capacity}


def multiply_linear(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int, int]:
    """Multiply descending-coefficient linear polynomials."""
    a, b = left
    c, d = right
    return (a * c, a * d + b * c, b * d)


def even_shape_exclusion() -> dict[str, int]:
    """Verify the affine contradictions and the q-star divisor identity."""
    shapes = even_shape_menu()
    if shapes != ((1, 23), (2, 1), (4, 5)):
        raise AssertionError("unexpected even shape order")

    # For s >= 2, the two non-23 shapes already exceed j < 18s-3.
    two_one_gap = (32 - 18, 10 + 3)
    four_five_gap = (64 - 18, 3)
    if not (
        all(slope > 0 and slope * 2 + intercept > 0 for slope, intercept in (
            two_one_gap,
            four_five_gap,
        ))
    ):
        raise AssertionError("affine j bounds changed")

    # g=23 forces s=23u+22 and hence j=368u+303.
    s_min = 22
    p_min = 48 * s_min + 1
    j_min = 16 * s_min - 49
    if not (
        (24 * s_min + 1) % 23 == 0
        and p_min == 1057
        and j_min == 303
        and 16 * 23 == 368
        and j_min > 3 * 59
    ):
        raise AssertionError("g=23 lower-bound receipt changed")

    # Expand both sides of 3(jp+4)+1239=(6s-1)(384s-1104).
    jp = multiply_linear((16, -49), (48, 1))
    left_coefficients = (3 * jp[0], 3 * jp[1], 3 * (jp[2] + 4) + 1239)
    right_coefficients = multiply_linear((6, -1), (384, -1104))
    if not (
        left_coefficients == right_coefficients
        and left_coefficients == (2304, -7008, 1104)
        and 1239 == 3 * 7 * 59
        and 303 > 3 * 59
    ):
        raise AssertionError("q-star divisor identity changed")
    return {"minimum_s": s_min, "minimum_j": j_min, "largest_q_star": 59}


def verify() -> None:
    odd = odd_capacity_three_exclusion()
    even_control = even_capacity_formula_control()
    even = even_shape_exclusion()
    if not (
        odd["prime"] == 73
        and odd["obstruction"] == 20
        and even_control["capacity"] == 2
        and even["minimum_j"] == 303
        and even["largest_q_star"] == 59
    ):
        raise AssertionError("q=1 capacity-three exclusion receipt changed")
    print(
        "verified q=1 immediate d=1 capacity-three exclusion: "
        "odd boundary and all three even shapes are impossible"
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
