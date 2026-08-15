#!/usr/bin/env python3
"""Verify the finite low-p source gate for H4 q0 re-entry.

This enumerates the q values forced by the 31 exact phase progressions and
the low-p inequality.  It does not sieve a prime interval or construct H4
payloads: an empty necessary D-divisibility menu already closes the branch.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate import (
    FINAL_RESIDUAL,
    selector_a,
)
from type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion import (
    PHASE_OFFSET,
    PHASE_PERIOD,
    PHASE_STEP,
    delta,
    positive_divisors,
)


def positive_residue(value: int, modulus: int) -> int:
    """Return the representative of value modulo modulus in 1..modulus."""
    residue = value % modulus
    return residue if residue else modulus


def q_progression(phase_base: int, d: int) -> tuple[int, int] | None:
    """Solve 2*d*q - 1 == phase_base modulo the full phase period."""
    overlap = gcd(2 * d, PHASE_PERIOD)
    if (phase_base + 1) % overlap:
        return None
    modulus = PHASE_PERIOD // overlap
    residue = (
        ((phase_base + 1) // overlap)
        * pow((2 * d) // overlap, -1, modulus)
    ) % modulus
    return residue, modulus


def first_at_least(residue: int, modulus: int, lower: int) -> int:
    """Return the least nonnegative residue-class value at least lower."""
    if residue >= lower:
        return residue
    return residue + ((lower - residue + modulus - 1) // modulus) * modulus


def finite_low_p_source_screen() -> dict[str, object]:
    """Exhaust every low-p phase/D necessary condition without primality tests."""
    all_divisor_pairs = 0
    odd_divisor_pairs = 0
    linear_pairs = 0
    bounded_pairs = 0
    q_candidates = 0
    divisor_candidates = 0
    survivors: list[tuple[int, int, int, int, int, int, int, int]] = []

    for u in sorted(FINAL_RESIDUAL):
        phase_base = PHASE_STEP * u + PHASE_OFFSET
        selector = selector_a(phase_base)
        if selector_a(phase_base + PHASE_PERIOD) != selector:
            raise AssertionError("low-p screen left the fixed selector progression")

        for d in positive_divisors(abs(1536 - selector)):
            all_divisor_pairs += 1
            if d % 2 == 0:
                continue
            odd_divisor_pairs += 1
            progression = q_progression(phase_base, d)
            if progression is None:
                continue
            linear_pairs += 1
            residue, modulus = progression
            support = 4 * d * d - 2 * d + 1
            q_start = first_at_least(residue, modulus, 2)
            if q_start > support:
                continue
            bounded_pairs += 1
            delta_d = delta(d)

            for q in range(q_start, support + 1, modulus):
                q_candidates += 1
                prime = 2 * d * q - 1
                divisor_bound = (2 * d - 1) * ((2 * d + 1) * q - 1)
                residue_d = positive_residue(delta_d, prime)
                max_index = min(2 * d - 1, (divisor_bound - residue_d) // prime)
                if not (
                    prime >= phase_base
                    and prime <= delta_d
                    and (prime - phase_base) % PHASE_PERIOD == 0
                    and 2 <= q <= support
                ):
                    raise AssertionError("low-p q compression stopped reconstructing its phase point")
                for index in range(max(0, max_index + 1)):
                    divisor_candidates += 1
                    divisor = residue_d + index * prime
                    if not (
                        0 < divisor <= divisor_bound < 2 * d * prime
                        and (divisor - delta_d) % prime == 0
                    ):
                        raise AssertionError("low-p D candidate left the source residue menu")
                    if divisor_bound % divisor == 0:
                        survivors.append(
                            (
                                prime,
                                u,
                                selector,
                                d,
                                q,
                                divisor,
                                index,
                                divisor_bound // divisor,
                            )
                        )

    result = {
        "phase_classes": len(FINAL_RESIDUAL),
        "all_divisor_pairs": all_divisor_pairs,
        "odd_divisor_pairs": odd_divisor_pairs,
        "linear_pairs": linear_pairs,
        "bounded_pairs": bounded_pairs,
        "q_candidates": q_candidates,
        "divisor_candidates": divisor_candidates,
        "survivors": tuple(survivors),
    }
    expected = {
        "phase_classes": 31,
        "all_divisor_pairs": 213,
        "odd_divisor_pairs": 109,
        "linear_pairs": 82,
        "bounded_pairs": 28,
        "q_candidates": 2_204,
        "divisor_candidates": 4_475_827,
        "survivors": (),
    }
    if result != expected:
        raise AssertionError(f"low-p q0 source screen changed: {result}")
    return result


def verify() -> None:
    screen = finite_low_p_source_screen()
    print(
        "verified finite low-p q0 source gate: "
        f"{screen['q_candidates']} q candidates and "
        f"{screen['divisor_candidates']} D candidates, with no survivor"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the finite source-gate screen")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
