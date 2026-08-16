#!/usr/bin/env python3
"""Verify the q=1 immediate d=1 residual-capacity-one exclusion.

The odd branch is an exact finite boundary forced by p <= 554. The even
branch is a finite algebraic shape table. No unbounded prime or terminal scan
is performed.
"""

from __future__ import annotations

import argparse

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


def odd_capacity_one_exclusion() -> dict[str, int]:
    """Replay every q=1 odd-t root in the forced finite core-prime boundary."""
    prime_candidates = tuple(
        (t, 24 * t + 1)
        for t in range(1, 24, 2)
        if rail.is_prime(24 * t + 1)
    )
    if prime_candidates != ((3, 73), (13, 313), (17, 409), (19, 457)):
        raise AssertionError("odd c=1 core-prime boundary changed")

    q_one_candidates = tuple(
        (t, prime)
        for t, prime in prime_candidates
        if rail.q_one_g(6 * t + 1)
    )
    if not (
        q_one_candidates == ((3, 73), (13, 313), (17, 409))
        and rail.factorization(115) == {5: 1, 23: 1}
        and not rail.q_one_g(115)
    ):
        raise AssertionError("ordinary q=1 boundary filter changed")

    expected = {
        3: {"prime": 73, "delta": 5, "n": 17, "j": 1, "g": 1, "obstruction": -8},
        13: {
            "prime": 313,
            "delta": 201,
            "n": 673,
            "j": 9,
            "g": 1,
            "obstruction": 48,
        },
        17: {
            "prime": 409,
            "delta": 29,
            "n": 97,
            "j": 1,
            "g": 1,
            "obstruction": -8,
        },
    }
    for t, expected_row in expected.items():
        row = capacity_two.receiver_data("odd", t)
        actual = {key: int(row[key]) for key in ("prime", "delta", "n", "j", "g")}
        actual["obstruction"] = 7 * actual["j"] + 27 - 42 * actual["g"]
        if not (
            actual == expected_row
            and int(row["c"]) * (7 * actual["j"] + 27) % actual["prime"]
            == (42 * actual["g"]) % actual["prime"]
            and actual["obstruction"] % actual["prime"] != 0
        ):
            raise AssertionError("odd q=1 c=1 boundary receipt changed")
    return {"candidate_count": len(q_one_candidates), "largest_prime": 409}


def even_shape_menu() -> tuple[tuple[int, int, int, int], ...]:
    """Check g | 8-k and the j mod 3 condition for 1 <= k <= 3."""
    shapes: list[tuple[int, int, int, int]] = []
    for k in range(1, 4):
        for g in range(1, 9):
            if not ((8 - k) % g == 0 and g % 2 == 1 and g % 3 != 0):
                continue
            if (k - (2 + 2 * g)) % 3 != 0:
                continue
            slope, intercept = 48 * k, 12 + k - 8 * g
            shapes.append((k, g, slope, intercept))
    result = tuple(shapes)
    if result != ((1, 1, 48, 5), (1, 7, 48, -43), (3, 5, 144, -25)):
        raise AssertionError("even c=1 finite shape menu changed")
    return result


def even_shape_exclusion() -> dict[str, int]:
    """Verify every remaining affine j formula exceeds j < 18s-3."""
    lower_s = 2
    gaps = tuple(
        (slope - 18) * lower_s + intercept + 3
        for _, _, slope, intercept in even_shape_menu()
    )
    if min(gaps) <= 0:
        raise AssertionError("c=1 affine q-star bound changed")
    return {"shape_count": len(gaps), "minimum_gap": min(gaps)}


def verify() -> None:
    odd = odd_capacity_one_exclusion()
    even = even_shape_exclusion()
    if not (
        odd["candidate_count"] == 3
        and odd["largest_prime"] == 409
        and even["shape_count"] == 3
        and even["minimum_gap"] == 20
    ):
        raise AssertionError("q=1 capacity-one exclusion receipt changed")
    print(
        "verified q=1 immediate d=1 capacity-one exclusion: "
        "finite odd boundary and all even shapes are impossible"
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
