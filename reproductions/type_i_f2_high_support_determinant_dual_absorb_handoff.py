#!/usr/bin/env python3
"""Verify the canonical high-support determinant-dual handoff arithmetic.

This script proves target reconstruction only. It does not treat a chart
identity as an actual source event, terminal result, owner, or queue admission.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy


ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = (
    ROOT
    / "data"
    / "t6-wave1"
    / "f2-high-support-determinant-dual-absorb-handoff-v1.json"
)


def dual_row(prime: int, support: int, cofactor: int) -> dict[str, int | str]:
    """Rebuild both low determinant duals and their deterministic selection."""
    if prime % 24 != 1 or not sympy.isprime(prime):
        raise AssertionError("control prime is outside the core domain")
    bound = (prime - 1) ** 2 // 4
    if not (support > bound and 1 <= cofactor < prime):
        raise AssertionError("control is outside high-support scope")
    K = support * cofactor
    if (4 * K - 1) % prime:
        raise AssertionError("source chart identity changed")
    R = (4 * K - 1) // prime
    if not (prime < R < 4 * support and R % 4 == 3):
        raise AssertionError("source is not canonical high-support overflow")

    d = prime - cofactor
    n = 4 * support - R
    if prime * n != 4 * support * d + 1:
        raise AssertionError("determinant identity changed")
    k, r = divmod(support, prime)
    if not 1 <= r < prime:
        raise AssertionError("support residue escaped canonical range")
    s = n - 4 * k * d
    if prime * s != 4 * r * d + 1:
        raise AssertionError("symmetric remainder identity changed")

    R_d, K_d = 4 * d - s, d * (prime - r)
    R_r, K_r = 4 * r - s, r * (prime - d)
    if min(R_d, R_r) >= prime:
        raise AssertionError("low-dual theorem changed")
    for R_side, K_side, carrier in ((R_d, K_d, d), (R_r, K_r, r)):
        if not (
            R_side > 0
            and R_side % 4 == 3
            and prime * R_side + 1 == 4 * K_side
            and K_side % carrier == 0
        ):
            raise AssertionError("dual chart identity changed")

    if R_d <= R_r:
        side, selected_R, selected_K = "d", R_d, K_d
    else:
        side, selected_R, selected_K = "r", R_r, K_r
    if not (3 <= selected_R <= prime - 2):
        raise AssertionError("selected dual did not land in low-chart range")

    return {
        "p": prime,
        "A": support,
        "C": cofactor,
        "R": R,
        "d": d,
        "n": n,
        "r": r,
        "k": k,
        "s": s,
        "R_d": R_d,
        "K_d": K_d,
        "R_r": R_r,
        "K_r": K_r,
        "selected_side": side,
        "R_selected": selected_R,
        "K_selected": selected_K,
    }


def compact_control(name: str, prime: int, support: int, cofactor: int) -> dict[str, object]:
    row = dual_row(prime, support, cofactor)
    return {
        "name": name,
        "p": prime,
        "A": support,
        "C": cofactor,
        "R": row["R"],
        "d_side": [row["R_d"], row["K_d"]],
        "r_side": [row["R_r"], row["K_r"]],
        "selected_side": row["selected_side"],
    }


def build_receipt() -> dict[str, object]:
    controls = [
        compact_control("c1_minimal", 73, 1369, 1),
        compact_control("c2_high_support", 73, 1305, 2),
        compact_control("c9_empty_improvement_control", 193, 9323, 9),
    ]
    if controls != [
        {
            "name": "c1_minimal",
            "p": 73,
            "A": 1369,
            "C": 1,
            "R": 75,
            "d_side": [71, 1296],
            "r_side": [3, 55],
            "selected_side": "r",
        },
        {
            "name": "c2_high_support",
            "p": 73,
            "A": 1305,
            "C": 2,
            "R": 143,
            "d_side": [35, 639],
            "r_side": [7, 128],
            "selected_side": "r",
        },
        {
            "name": "c9_empty_improvement_control",
            "p": 193,
            "A": 9323,
            "C": 9,
            "R": 1739,
            "d_side": [511, 24656],
            "r_side": [11, 531],
            "selected_side": "r",
        },
    ]:
        raise AssertionError("focused determinant-dual controls changed")
    return {
        "artifact_id": "f2_high_support_determinant_dual_absorb_handoff_v1",
        "status": "CONDITIONAL_LOW_DUAL_TARGET_E1_E3_REENTRY_OPEN",
        "controls": controls,
        "conclusion": {
            "E1": "RELATIVE_ESTABLISHED_ON_ACTUAL_DETERMINANT_BOUND_M_EQUALS_A_SLICE; OPEN_ON_GENERIC_HIGH_SUPPORT",
            "E2": "ESTABLISHED_BY_DETERMINANT_DUAL_IDENTITIES",
            "E4": "IDENTITY_ON_Sol_4_p_RELATIVE_TO_ADMISSION",
            "E5": "CHARGED_TO_ABSORB_PHASE_DROP_RELATIVE_TO_ADMISSION",
            "E1_E3_reentry": "OPEN",
        },
        "canonical_absorb_cursor": {
            "formal_pair": ["1", "R_star-1", 1],
            "identity": "1+(R_star-1)=R_star*1 and gcd(1,R_star-1)=1",
            "epsilon": "min",
            "local_rank_payload": ["R_star", 1, 1],
            "source_relation": "the same pair is the anchor of the target universal p-source",
            "boundary": "This payload does not authorize E3 or re-entry; R_star=3 has a known terminal-free formal self-loop that remains nonrecursive.",
        },
    }


def verify() -> dict[str, object]:
    receipt = build_receipt()
    stored = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    if stored["artifact_id"] != receipt["artifact_id"]:
        raise AssertionError("stored artifact id changed")
    if stored["status"] != receipt["status"]:
        raise AssertionError("stored status changed")
    if stored["controls"] != receipt["controls"]:
        raise AssertionError("stored controls changed")
    if stored["canonical_absorb_cursor"] != receipt["canonical_absorb_cursor"]:
        raise AssertionError("stored canonical ABSORB cursor changed")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    receipt = verify() if args.verify else build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
