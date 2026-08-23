#!/usr/bin/env python3
"""Focused owner-shape replay for H4 clean-q targets."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))

import type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier as clean_q  # noqa: E402


def verify() -> dict[str, object]:
    controls = []
    for p, peeled in ((73, 3366), (241, 29886)):
        receipt = clean_q.verify_h4_macro(clean_q.make_control_input(p, peeled, f"p{p}"))
        target = receipt["target"]
        support = int(target["absorbed_support"])
        R = int(target["R"])
        K = int(target["K"])
        capacity = int(receipt["corrected_support"]["capacity"])
        B_p = (p - 1) ** 2 // 4
        if not (
            support > B_p
            and R > p
            and K == support * capacity
            and 1 <= capacity <= p - 2
            and p * R + 1 == 4 * K
            and target["marked_solution_set"] == "Sol(p)"
            and target["dispatch_status"] == "pending_dispatch"
            and receipt["recursive_edge_eligible"] is False
        ):
            raise AssertionError("H4 target owner shape changed")
        controls.append(
            {
                "p": p,
                "branch": receipt["endpoint"]["branch"],
                "support_gt_Bp": True,
                "R_gt_p": True,
                "capacity": capacity,
                "owner_fallback": "type_i_a_gt_one_overflow_residual",
                "recursive_edge_eligible": False,
            }
        )
    return {
        "status": "FOCUSED_H4_HIGH_SUPPORT_OWNER_SHAPES_REPLAYED",
        "controls": controls,
        "scope": "owner-shape-only_common-admission-not-replayed",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    print(verify()["status"])


if __name__ == "__main__":
    main()
