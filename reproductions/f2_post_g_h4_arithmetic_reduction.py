#!/usr/bin/env python3
"""Focused algebraic replay for the F2 post-G/H4 arithmetic reduction.

This verifier checks identities used by the branch-composition claim and a few
fixed controls from the existing H4 source-repair / clean-q implementations.
It deliberately does not claim actual-state totality, common admission, or
recursive re-entry; those remain explicit blockers in the receipt.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))

import type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary as carry  # noqa: E402
import type_ii_q_one_c2_19_phase_h4_clean_q_macro_verifier as clean_q  # noqa: E402
import type_ii_q_one_c2_19_phase_h4_raw_source_repair as raw_repair  # noqa: E402


@dataclass(frozen=True)
class Chart:
    p: int
    M: int
    c: int

    @property
    def K(self) -> int:
        return self.M * self.c

    @property
    def R(self) -> int:
        if (4 * self.K - 1) % self.p:
            raise AssertionError("chart is not integral")
        return (4 * self.K - 1) // self.p


def verify_chart(chart: Chart) -> None:
    if not (
        chart.p % 24 == 1
        and chart.M > 0
        and 1 <= chart.c < chart.p
        and chart.R > 0
        and chart.R % 4 == 3
        and chart.p * chart.R + 1 == 4 * chart.K
    ):
        raise AssertionError(f"invalid canonical chart: {chart}")


def verify_d1_top_capacity(chart: Chart) -> dict[str, int]:
    verify_chart(chart)
    if chart.c != chart.p - 1:
        raise AssertionError("control is not top-capacity")
    if (4 * chart.M + 1) % chart.p:
        raise AssertionError("top-capacity chart has no d=1 source integer")
    n = (4 * chart.M + 1) // chart.p
    if not (n > 1 and n % 4 == 1 and chart.R == (chart.p - 1) * n - 1):
        raise AssertionError("d=1 normal form identity changed")
    return {"p": chart.p, "M": chart.M, "c": chart.c, "n": n, "R": chart.R}


def verify_parent_drop(p: int, target_capacity: int) -> None:
    if not (1 <= target_capacity <= p - 2):
        raise AssertionError("target capacity is not a strict parent-macro endpoint")
    if not ((0, target_capacity) < (0, p - 1)):
        raise AssertionError("parent rank did not decrease")


def verify_nonzero_source(p: int, R: int) -> dict[str, int]:
    if R % p in {0, 1}:
        raise AssertionError("source control must use R mod p outside {0,1}")
    source = (p, R * (p - 1) - p, p - 1)
    anchor = (1, R - 1, 1)
    if not (
        source[1] > 0
        and source[0] + source[1] == R * source[2]
        and gcd(source[0], source[1]) == 1
        and anchor == (source[0] // p, (source[1] + R) // p, (source[2] + 1) // p)
    ):
        raise AssertionError("nonzero-residue source repair identity changed")
    return {"p": p, "R": R, "source_prime": p}


def verify_r1_proper_shape(p: int, R: int, K: int, M: int, c: int, h: int) -> dict[str, int]:
    if not (R % p == 1 and 1 < h < p + 1 and (p + 1) % h == 0):
        raise AssertionError("R=1 proper-overlap control changed")
    if not (p * R + 1 == 4 * K and K == M * c):
        raise AssertionError("H4 chart equation changed")
    z = R - h
    q = (p + 1) // h
    if not (z > 0 and q > 1 and h * q == p + 1):
        raise AssertionError("small-anchor q relation changed")
    return {"p": p, "R": R, "h": h, "z": z, "q": q}


def verify() -> dict[str, object]:
    # Existing exact controls: one R=0 source repair goes directly strict and
    # one reaches H5 top-capacity before the d=1 strict suffix.
    zero_controls = [raw_repair.audit(fixture) for fixture in raw_repair.FIXTURES]
    if [row["outcome"] for row in zero_controls] != [
        "direct_strict_capacity",
        "top_capacity_then_strict_61",
    ]:
        raise AssertionError("R=0 source-repair controls changed")

    # Existing actual H4/H5 controls demonstrate both local carry directions
    # while parent-macro endpoint remains strict.
    h4_other = carry.h4_next_maximal_carry_control(14_449)
    h4_other_rise = carry.h4_next_maximal_carry_control(665_617)
    if not all(row["parent_macro_endpoint_decreases"] for row in (h4_other, h4_other_rise)):
        raise AssertionError("R not in {0,1} parent-macro gate changed")
    verify_nonzero_source(14_449, 14_449 * 17 + 4039)

    # The R=1 clean-q controls are intentionally local controls; the existing
    # verifier keeps their recursive eligibility false until common admission.
    clean_controls = []
    for p, peeled in ((73, 3366), (241, 29886)):
        inp = clean_q.make_control_input(p, peeled, f"p{p}")
        receipt = clean_q.verify_h4_macro(inp)
        if not (
            receipt["corrected_support"]["capacity"] <= p - 2
            and receipt["premise_verification"]["recursive_edge_eligible"] is False
            and receipt["e1_e5"] == {f"E{i}": True for i in range(1, 6)}
        ):
            raise AssertionError("clean-q arithmetic control changed")
        clean_controls.append(
            {
                "p": p,
                "branch": receipt["endpoint"]["branch"],
                "capacity": receipt["corrected_support"]["capacity"],
                "admission_ready": False,
            }
        )

    # A small canonical d=1 identity control makes the top-capacity algebra
    # independently replayable without scanning any prime range.
    top = Chart(p=73, M=1332, c=72)
    top_identity = verify_d1_top_capacity(top)
    verify_parent_drop(73, 61)
    r4 = 1 + 73 * 3366
    k4 = (73 * r4 + 1) // 4
    verify_r1_proper_shape(73, r4, k4, k4, 1, 2)

    return {
        "status": "ARITHMETIC_CONTROLS_PASS_SEMANTIC_RESIDUAL_OPEN",
        "r4_mod_0": zero_controls,
        "r4_mod_other": [h4_other, h4_other_rise],
        "r4_mod_1_clean_q": clean_controls,
        "d1_identity": top_identity,
        "scope_boundary": {
            "common_admission": "not replayed",
            "recursive_reentry": "not replayed",
            "other_H4_branches": "not covered by this focused verifier",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    result = verify()
    print(result["status"])


if __name__ == "__main__":
    main()
