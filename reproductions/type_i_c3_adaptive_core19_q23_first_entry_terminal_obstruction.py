#!/usr/bin/env python3
"""Verify the q=23-first C=19 raw language and its terminal obstruction."""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_c3_factor_block_even_tail_root_entry as factor_blocks
import type_i_high_r_chart_two_anchor as shared


def prime_word(value: int) -> list[int]:
    """Expand one positive integer into its ordered prime factor word."""
    word: list[int] = []
    for prime, exponent in shared.factorization(value):
        word.extend([prime] * exponent)
    return word


def type_ii_factor_pair(prime: int, gap: int, divisor: int) -> dict[str, int]:
    """Verify one direct Type II factor-pair certificate."""
    x = (prime + gap) // 4
    if not (
        prime % 4 == 1
        and divisor <= x
        and x * x % divisor == 0
        and (x + divisor) % gap == 0
    ):
        raise AssertionError("factor-pair terminal conditions failed")
    y = prime * (x + divisor) // gap
    z = prime * (x + x * x // divisor) // gap
    if 4 * x * y * z != prime * (x * y + x * z + y * z):
        raise AssertionError("factor-pair terminal identity failed")
    return {"gap": gap, "divisor": divisor, "x": x, "y": y, "z": z}


def verify_q23_first_terminal_obstruction() -> dict[str, object]:
    """Encode the all-parameter proof after h=20+23u."""
    h_base, h_step = 20, 23
    p_base, p_step = 24 * h_base + 1, 24 * h_step
    x_base, x_step = (p_base + 23) // 4, p_step // 4
    if not (
        (104 * h_base - 10) % 23 == 0
        and 104 * h_step % 23 == 0
        and (x_base, x_step) == (126, 138)
        and x_base == 6 * (h_base + 1)
        and x_step == 6 * h_step
        and x_base * x_base % 12 == 0
        and x_step % 6 == 0
        and (x_base + 12) % 23 == 0
        and x_step % 23 == 0
    ):
        raise AssertionError("q=23 first-label terminal algebra changed")
    return {
        "first_label_condition": "23 divides R-1 iff h == 20 (mod 23)",
        "factor_pair": {"m": 23, "d": 12, "x": "6*(h+1)"},
        "proof_identities": {
            "d_divides_x_squared": "x^2/12 = 3*(h+1)^2",
            "m_divides_x_plus_d": "x+12 = 6*(h+3)",
        },
        "selector_status": "terminal_first_obstruction_for_every_q23_first_branch",
    }


def verify_q23_c19_control() -> dict[str, object]:
    """Replay the smallest focused actual q=23-first C=19 word."""
    v = 1
    h = 388 + 437 * v
    prime = 24 * h + 1
    R = 104 * h - 9
    M = 26 * h + 1
    K = M * (prime - 3)
    b = (R - 1) // 23
    Q = (R - b) // 19
    if not (
        prime == 19_801
        and shared.is_prime(prime)
        and R == 85_791
        and R - 1 == 23 * b
        and R - b == 19 * Q
        and shared.factorization(Q) == [(7, 1), (617, 1)]
        and gcd(Q, K * R) == 1
        and K % 23 != 0
        and R % 23 == 1
    ):
        raise AssertionError("q=23 C=19 control arithmetic changed")

    source = (prime, R * (prime - 1) - prime, prime - 1)
    p_edge = raw.ordered_raw_step(
        modulus=R,
        K=K,
        source=source,
        selected_coordinate_index=0,
        q=prime,
        expected_destination=(1, R - 1, 1),
        name="q23_control_universal_p_edge",
    )
    first = raw.ordered_raw_step(
        modulus=R,
        K=K,
        source=(1, R - 1, 1),
        selected_coordinate_index=1,
        q=23,
        expected_destination=(b, R - b, 1),
        name="q23_control_first_label",
    )
    _, block = factor_blocks.replay_block(
        modulus=R,
        K=K,
        source=(b, R - b, 1),
        selected_coordinate_index=1,
        word=prime_word(Q),
        endpoint=(19, R - 19, 1),
        name="q23_control_c19_block",
    )
    rows = [p_edge, first, *block]
    if any(
        not row["strict_capacity"]
        or not row["unit_condition"]
        or row["gcd_reduction"] != 1
        for row in rows
    ):
        raise AssertionError("q=23 C=19 raw word lost a primitive edge")
    return {
        "parameters": {"v": v, "h": h, "p": prime, "R": R, "b": b, "Q": Q},
        "raw_word": [[1, 23], [1, 7], [0, 617]],
        "destination": [19, R - 19, 1],
        "terminal_first_control": type_ii_factor_pair(prime, 7, 4),
    }


def build_result() -> dict[str, object]:
    """Build a theorem control, not a terminal-free selector edge."""
    return {
        "certificate_type": "c3_core19_q23_first_terminal_obstruction_v1",
        "obstruction": verify_q23_first_terminal_obstruction(),
        "actual_raw_control": verify_q23_c19_control(),
        "selector_status": "terminal_preempted_no_selector_edge",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified q=23-first C=19 raw language and terminal obstruction")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
