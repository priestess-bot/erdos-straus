#!/usr/bin/env python3
"""Focused controls for the q=1 C2 19-phase fused-macro reduction."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))

import type_ii_q_one_c2_19_phase_maximal_fourth_anchor_completion as h4  # noqa: E402
import type_ii_q_one_c2_19_phase_three_anchor_persistent_macro as h3  # noqa: E402
import type_ii_q_one_full_carrier_d_one_capacity_two_rigidity as c2  # noqa: E402


def verify() -> dict[str, object]:
    odd = c2.odd_capacity_two_exclusion()
    even = c2.even_capacity_two_phase()
    p = int(even["prime"])
    third = h3.macro_data(p)
    fourth = h4.maximal_h4(p)
    if not (
        odd["prime"] == 73
        and p == 769
        and even["q_star"] == 19
        and even["capacity"] == 2
        and p % 912 == 769
        and third["receiver_capacity"] == p - 1
        and 1 <= third["capacity_3"] <= p - 2
        and 1 <= fourth["c4"] <= p - 2
        and fourth["top_capacity"] is False
    ):
        raise AssertionError("C2 fused-macro focused composition changed")
    return {
        "status": "FOCUSED_C2_19_PHASE_CHECKPOINTS_REPLAYED",
        "odd_c2": "excluded",
        "even_c2": even,
        "checkpoints": {
            "queued": False,
            "H3_capacity": third["capacity_3"],
            "H4_capacity": fourth["c4"],
            "H4_R_mod_p": fourth["r4_mod_p"],
        },
        "final_E3": "not replayed; common serializer required",
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
