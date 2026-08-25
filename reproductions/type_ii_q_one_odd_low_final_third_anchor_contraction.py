#!/usr/bin/env python3
"""Verify the q=1 odd low-final third-anchor C=9 contraction."""

from __future__ import annotations

import argparse
from math import gcd
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_runtime_v1 as runtime  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


def low_checkpoint_to_c9(prime: int) -> dict[str, object]:
    if prime % 336 != 25:
        raise AssertionError("third-anchor contraction has the wrong residual class")
    k = (prime - 25) // 336
    t = (prime - 1) // 24
    if not (
        rail.is_prime(prime)
        and prime == 336 * k + 25
        and t == 14 * k + 1
        and t % 2 == 1
        and rail.q_one_g(6 * t + 1)
    ):
        raise AssertionError("input is not an ordinary q=1 odd low-final row")

    low_r = 80 * k + 7
    low_k = 4 * (140 * k + 11) * (12 * k + 1)
    low_a = 2 * (140 * k + 11)
    q = 40 * k + 3
    anchor = low_r - 1
    carrier = low_a * q
    high_r = 1200 * k + 95
    high_k = 9 * carrier
    b_p = (prime - 1) ** 2 // 4

    if not (
        anchor == 2 * q
        and low_k % low_a == 0
        and low_k % q != 0
        and low_k % 4 == 0
        and q % 2 == 1
        and gcd(q, 140 * k + 11) == 1
        and gcd(q, 12 * k + 1) == 1
        and carrier == 2 * (140 * k + 11) * (40 * k + 3)
        and 36 * carrier - 1 == prime * high_r
        and 4 * high_k == prime * high_r + 1
        and high_r > prime
        and b_p - carrier == 17_024 * k * k + 2_312 * k + 78
        and carrier <= b_p
    ):
        raise AssertionError("third-anchor C=9 arithmetic changed")

    root_k = (6 * t + 1) * (16 * t + 1)
    root_potential = runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "support_A": 1,
            "chart_K": root_k,
            "t5_eta_p": 0,
        },
        root_context=prime,
        equation_rank=prime,
    )
    high_potential = runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "support_A": carrier,
            "chart_K": high_k,
            "t5_eta_p": 0,
        },
        root_context=prime,
        equation_rank=prime,
    )
    runtime.verify_t5_ticket_v1("LOCAL_DROP", root_potential, high_potential)
    return {
        "prime": prime,
        "k": k,
        "low_checkpoint": {"R": low_r, "K": low_k, "support": low_a, "Q": q},
        "final_high": {"R": high_r, "K": high_k, "support": carrier, "cofactor": 9},
        "potentials": {"root": root_potential, "high": high_potential},
    }


def verify() -> None:
    expected = {
        1033: (3, (247, 63788, 862, 123), (3695, 954234, 106026)),
        2713: (8, (647, 438828, 2262, 323), (9695, 6575634, 730626)),
    }
    for prime, (k, low, high) in expected.items():
        receipt = low_checkpoint_to_c9(prime)
        got_low = receipt["low_checkpoint"]
        got_high = receipt["final_high"]
        if not (
            receipt["k"] == k
            and (got_low["R"], got_low["K"], got_low["support"], got_low["Q"]) == low
            and (got_high["R"], got_high["K"], got_high["support"]) == high
            and receipt["potentials"]["root"] > receipt["potentials"]["high"]
        ):
            raise AssertionError(f"C=9 contraction changed for p={prime}")
    print("verified q=1 odd low-final third-anchor C=9 contraction")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("use --verify")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
