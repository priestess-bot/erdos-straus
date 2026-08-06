#!/usr/bin/env python3
"""Replay the fixed p=1009 c=3 non-p universal-source raw bypass.

This is a local raw-transcript check.  It deliberately does not assign an
initial phase mark, create a root, or register a selector edge.
"""

from __future__ import annotations

import argparse
from math import gcd

import type_i_c3_affine_prime_even_tail_root_entry as prime_entry
import type_i_high_r_chart_two_anchor as shared


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation for one positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_bypass() -> dict[str, object]:
    """Replay all six raw steps and record the phase mismatch explicitly."""
    h = 42
    p = 1009
    R = 104 * h - 9
    M = 26 * h + 1
    x = p - 3
    K = M * x
    source = (p, R * (p - 1) - p, p - 1)
    expected_source = (1009, 4392863, 1008)
    if source != expected_source or not shared.is_prime(p):
        raise AssertionError("p=1009 universal source changed")
    if shared.factorization(K) != [(2, 1), (503, 1), (1093, 1)]:
        raise AssertionError("p=1009 carrier factorization changed")

    steps = (
        (source, 1, 349, (12587, 490, 3), "source_bypass_349"),
        ((12587, 490, 3), 0, 41, (307, 4052, 1), "source_bypass_41"),
        ((307, 4052, 1), 1, 1013, (4, 4355, 1), "source_bypass_1013"),
        ((4, 4355, 1), 1, 13, (335, 4024, 1), "source_bypass_13"),
        ((335, 4024, 1), 1, 2, (2012, 2347, 1), "source_bypass_2a"),
        ((2012, 2347, 1), 0, 2, (1006, 3353, 1), "source_bypass_2b"),
    )

    rows: list[dict[str, object]] = []
    phase = 1
    phases: list[int] = []
    for source_node, side, prime, destination, name in steps:
        row = prime_entry.ordered_raw_step(
            modulus=R,
            K=K,
            source=source_node,
            selected_coordinate_index=side,
            q=prime,
            expected_destination=destination,
            name=name,
        )
        if not row["strict_capacity"] or not row["unit_condition"] or row["gcd_reduction"] != 1:
            raise AssertionError(f"{name}: raw contract failed")
        phase = phase * prime % R
        phases.append(phase)
        rows.append(row)

    if rows[-1]["destination"] != [x, R - x, 1]:
        raise AssertionError("bypass did not reach the c=3 complement seed")
    if gcd(4 * x, K) != x:
        raise AssertionError("exact t=4 physical-row carrier changed")
    if phases != [349, 1232, 1342, 10, 20, 40]:
        raise AssertionError("bypass phase transcript changed")
    if phases[3] == (-M) % R or phases[-1] == (-13) % R:
        raise AssertionError("bypass unexpectedly satisfied the p-first phase contract")

    return {
        "p": p,
        "h": h,
        "R": R,
        "M": M,
        "x": x,
        "K": K,
        "source": list(source),
        "step_count": len(rows),
        "final_destination": rows[-1]["destination"],
        "raw_phases": phases,
        "p_first_required_phases": {"t4": (-M) % R, "seed": (-13) % R},
    }


def verify_p_first_m_one_trap() -> dict[str, object]:
    """Check the two-node m=1 trap after the canonical p edge."""
    h = 42
    R = 104 * h - 9
    K = (26 * h + 1) * (24 * h - 2)
    if shared.factorization(R - 1) != [(2, 1), (2179, 1)]:
        raise AssertionError("canonical anchor factorization changed")
    if shared.factorization(R - 2) != [(4357, 1)]:
        raise AssertionError("N_R(2) factorization changed")
    if valuation(R - 1, 2) != valuation(K, 2) or valuation(2, 2) != valuation(K, 2):
        raise AssertionError("dyadic capacity trap changed")

    first = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(1, R - 1, 1),
        selected_coordinate_index=1,
        q=2179,
        expected_destination=(2, R - 2, 1),
        name="p_first_anchor_only_exit",
    )
    second = prime_entry.ordered_raw_step(
        modulus=R,
        K=K,
        source=(2, R - 2, 1),
        selected_coordinate_index=1,
        q=4357,
        expected_destination=(1, R - 1, 1),
        name="p_first_second_only_exit",
    )
    if any(not row["strict_capacity"] or not row["unit_condition"] for row in (first, second)):
        raise AssertionError("p-first m=1 trap edge failed")
    return {
        "nodes": [[1, R - 1, 1], [2, R - 2, 1]],
        "only_non_dyadic_labels": [2179, 4357],
    }


def build_result() -> dict[str, object]:
    """Build the fixed raw receipt and its explicit root-policy boundary."""
    return {
        "certificate_type": "c3_p1009_universal_source_bypass_raw_receipt_v1",
        "scope": (
            "One raw-source transcript and one p-first m=1 trap check only; "
            "the result is not a root, E3 phase proof, selector edge, or descent."
        ),
        "bypass": verify_bypass(),
        "p_first_trap": verify_p_first_m_one_trap(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified p=1009 c=3 universal-source bypass raw receipt")


if __name__ == "__main__":
    main()
