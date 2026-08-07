#!/usr/bin/env python3
"""Verify the direct carrier-residue q=19 Type-II lift obstruction."""

from __future__ import annotations

import argparse
import json


def core19_rows(u: int) -> dict[str, int]:
    """Return the two c=3 core-19 carrier rows at h=8+19*u."""
    if u < 0:
        raise AssertionError("the declared core-19 ray has nonnegative u")
    h = 8 + 19 * u
    p = 24 * h + 1
    R = 104 * h - 9
    M0 = 26 * h + 1
    C0 = p - 3
    K = M0 * C0
    if K % 19:
        raise AssertionError("the C=19 carrier ceased to be integral")
    M1 = K // 19
    r0 = M0 % p
    r1 = M1 % p
    return {
        "u": u,
        "h": h,
        "p": p,
        "R": R,
        "M0": M0,
        "M1": M1,
        "K": K,
        "r0": r0,
        "r1": r1,
    }


def verify_family_row(u: int) -> dict[str, int]:
    """Check the two canonical remainders and their incompatible gates."""
    row = core19_rows(u)
    p = row["p"]
    r0 = row["r0"]
    r1 = row["r1"]
    expected_r0 = (p - 1) // 12
    expected_r1 = (63 * p + 1) // 76
    if not (
        row["h"] % 19 == 8
        and p == 193 + 456 * u
        and row["R"] == 823 + 1_976 * u
        and row["M0"] == 209 + 494 * u
        and p % 76 == 41
        and 4 * row["K"] == p * row["R"] + 1
        and row["M0"] % 19 == 0
        and 19 * row["M1"] == row["K"]
        and r0 == expected_r0 == 16 + 38 * u
        and r1 == expected_r1 == 160 + 378 * u
        and 0 < r0
        and 4 * r0 < p
        and (p + 4 * r0) % 19 == 10
        and 0 < r1 < p
        and 4 * r1 > p
        and (4 * 19 * r1 - 1) % p == 0
    ):
        raise AssertionError("core-19 direct carrier remainder identities changed")
    return {
        "u": u,
        "p": p,
        "r_C0": r0,
        "r_C19": r1,
        "C0_q19_residue": (p + 4 * r0) % 19,
        "C19_range_excess": 4 * r1 - p,
    }


def build_result() -> dict[str, object]:
    """Build algebraic controls, not a search over possible source maps."""
    controls = (
        verify_family_row(0),
        verify_family_row(13),
        verify_family_row(2_636_791_483),
    )
    if not (
        controls[0]["p"] == 193
        and controls[1]["p"] == 6_121
        and controls[2]["p"] == 1_202_376_916_441
        and controls[2]["r_C0"] == 100_198_076_370
        and controls[2]["r_C19"] == 996_707_180_734
    ):
        raise AssertionError("named core-19 controls changed")
    return {
        "certificate_type": "c3_core19_direct_carrier_residue_lift_no_go_v1",
        "direct_lift_contract": {
            "label": "b congruent to M_i modulo p",
            "range": "0 < b < p/4",
            "qheight": "19 divides p + 4*b",
        },
        "row_outcomes": {
            "C0": "the only in-range representative is r0, but p+4*r0 is 10 mod 19",
            "C19": "the canonical representative r1 is already larger than p/4",
        },
        "controls": list(controls),
        "scope": (
            "Excludes only direction-preserving direct carrier-residue labels; "
            "it does not exclude signed, affine, or otherwise nonnative source maps."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified core-19 direct carrier-residue q=19 lift obstruction")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
