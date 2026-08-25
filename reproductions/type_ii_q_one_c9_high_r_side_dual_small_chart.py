#!/usr/bin/env python3
"""Verify the q=1 C=9 high r-side dual small-chart classification."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "reproductions", ROOT / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import t6_persistent_selector_runtime_v1 as runtime  # noqa: E402
import type_ii_q_one_type_i_carrier_rail_dispatch as rail  # noqa: E402


def c9_r_side_dual(prime: int) -> dict[str, object]:
    if prime % 336 != 25:
        raise AssertionError("C=9 dual has the wrong q=1 residual class")
    k = (prime - 25) // 336
    if not (rail.is_prime(prime) and rail.q_one_g((prime + 3) // 4)):
        raise AssertionError("input is not an ordinary q=1 C=9 row")
    support = 2 * (140 * k + 11) * (40 * k + 3)
    source_r = 1200 * k + 95
    source_k = 9 * support
    d = prime - 9
    r = support % prime
    source_n = 4 * support - source_r
    quotient = (support - r) // prime
    s = source_n - 4 * quotient * d
    r_side_r = 4 * r - s
    d_side_r = 4 * d - s
    r_side_k = 9 * r
    expected_r = {0: 23, 1: 35, 2: 11}[k % 3]
    b_p = (prime - 1) ** 2 // 4

    if not (
        36 * support - 1 == prime * source_r
        and 36 * r % prime == 1
        and 4 * source_k == prime * source_r + 1
        and 4 * r_side_k == prime * r_side_r + 1
        and r_side_r == expected_r
        and r_side_k == (expected_r * prime + 1) // 4
        and r == (expected_r * prime + 1) // 36
        and r < d
        and d_side_r - r_side_r == 4 * (d - r)
        and 3 <= r_side_r < prime
        and r_side_k % r == 0
        and support <= b_p
    ):
        raise AssertionError("C=9 r-side dual arithmetic changed")

    source_potential = runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "CHARGED",
            "support_A": support,
            "chart_K": source_k,
            "t5_eta_p": 0,
        },
        root_context=prime,
        equation_rank=prime,
    )
    target_potential = runtime.compute_t5_potential_v1(
        descriptor=runtime.T5StateDescriptorV1(
            induction_rank=prime,
            major_phase="TYPEI",
            type_i_protocol="ABSORB",
            absorb_m=1,
            absorb_r_epsilon=1,
        ),
        facts={
            "major_phase": "TYPEI",
            "type_i_protocol": "ABSORB",
            "chart_R": r_side_r,
            "absorb_m": 1,
            "absorb_r_epsilon": 1,
        },
        root_context=prime,
        equation_rank=prime,
    )
    runtime.verify_t5_ticket_v1("PHASE_DROP", source_potential, target_potential)
    return {
        "prime": prime,
        "k": k,
        "source": {"R": source_r, "K": source_k, "support": support, "cofactor": 9},
        "r_side": {"R": r_side_r, "K": r_side_k, "support": r},
        "d_side_R": d_side_r,
        "ticket": "PHASE_DROP",
        "potentials": {"source": source_potential, "target": target_potential},
    }


def verify() -> None:
    expected = {
        1033: (3, (23, 5940, 660)),
        2713: (8, (11, 7461, 829)),
        9433: (28, (35, 82539, 9171)),
    }
    for prime, (k, r_side) in expected.items():
        receipt = c9_r_side_dual(prime)
        target = receipt["r_side"]
        if not (
            receipt["k"] == k
            and (target["R"], target["K"], target["support"]) == r_side
            and receipt["d_side_R"] > target["R"]
            and receipt["potentials"]["source"] > receipt["potentials"]["target"]
        ):
            raise AssertionError(f"C=9 r-side control changed for p={prime}")
    print("verified q=1 C=9 high r-side dual to R=11/23/35")


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
