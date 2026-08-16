#!/usr/bin/env python3
"""Verify the three zero-k q=1 even-branch residual-capacity rays.

The receipt is symbolic: it enumerates the four possible j values under k=0,
checks the q-star annihilators, and replays the existing c=2 realization. It
does not search for actual c=8 or c=56 q=1 states.
"""

from __future__ import annotations

import argparse

import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as capacity_two
import type_ii_q_one_type_i_carrier_rail_dispatch as rail


def zero_k_shapes() -> tuple[tuple[int, int, int], ...]:
    """Solve 8g=c(12-j) using the exact even-branch j and g gates."""
    shapes: list[tuple[int, int, int]] = []
    for j in (2, 5, 8, 11):
        for g in range(1, 8):
            if (
                g % 2 == 1
                and g % 3 != 0
                and (j - 4) % g == 0
                and (8 * g) % (12 - j) == 0
            ):
                c = 8 * g // (12 - j)
                shapes.append((c, j, g))
    result = tuple(shapes)
    if result != ((2, 8, 1), (8, 11, 1), (56, 11, 7)):
        raise AssertionError("zero-k capacity shape classification changed")
    return result


def annihilator(c: int, k: int, g: int) -> int:
    """The q-star divisor forced by q-star | (6s-1) and q-star | (jp+4)."""
    return 112 * c + 81 * k - 72 * g


def q_star_phase_receipt() -> dict[str, int]:
    """Check the exact q-star factors and the three modular phase classes."""
    shapes = zero_k_shapes()
    expected_annihilators = {
        (2, 8, 1): 152,
        (8, 11, 1): 824,
        (56, 11, 7): 5768,
    }
    actual_annihilators = {
        shape: annihilator(shape[0], 0, shape[2]) for shape in shapes
    }
    if actual_annihilators != expected_annihilators:
        raise AssertionError("zero-k annihilator values changed")
    if not (
        rail.factorization(152) == {2: 3, 19: 1}
        and rail.factorization(824) == {2: 3, 103: 1}
        and rail.factorization(5768) == {2: 3, 7: 1, 103: 1}
    ):
        raise AssertionError("zero-k annihilator factorizations changed")

    s_19, s_103 = 16, 86
    c_fifty_six_u = ((2 - s_103) * pow(103, -1, 7)) % 7
    c_fifty_six_s = s_103 + 103 * c_fifty_six_u
    if not (
        pow(6, -1, 19) == s_19
        and pow(6, -1, 103) == s_103
        and (6 * s_19 - 1) % 19 == 0
        and (6 * s_103 - 1) % 103 == 0
        and (48 * s_19 + 1) % 19 == 9
        and (48 * s_103 + 1) % 103 == 9
        and (24 * s_103 + 1) % 7 == 0
        and (6 * s_103 - 1) % 7 != 0
        and 721 == 7 * 103
        and 103 % 7 == 5
        and c_fifty_six_u == 0
        and c_fifty_six_s == 86
        and c_fifty_six_s % 721 == 86
    ):
        raise AssertionError("zero-k q-star phase congruences changed")
    return {"c_two_s": s_19, "q_103_s": s_103, "c_fifty_six_modulus": 721}


def existing_c_two_control() -> dict[str, int]:
    """Replay the established actual q-star=19 zero-k realization."""
    row = capacity_two.receiver_data("even", 32)
    prime, s, q_star, j, g, capacity = (
        int(row[key]) for key in ("prime", "s", "q_star", "j", "g", "c")
    )
    if not (
        prime == 769
        and s == 16
        and q_star == 19
        and (capacity, j, g) == (2, 8, 1)
        and capacity * j + 8 * g == 12 * capacity
    ):
        raise AssertionError("actual c=2 zero-k realization changed")
    return {"prime": prime, "s": s, "q_star": q_star}


def verify() -> None:
    phase = q_star_phase_receipt()
    control = existing_c_two_control()
    if not (
        phase["c_two_s"] == 16
        and phase["q_103_s"] == 86
        and control["q_star"] == 19
    ):
        raise AssertionError("zero-k ray receipt changed")
    print(
        "verified q=1 even zero-k rays: c=2 at q*=19, "
        "and only necessary c=8/c=56 q*=103 rays remain"
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
