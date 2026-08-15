#!/usr/bin/env python3
"""Verify the H4 full-overlap-to-finite-menu exclusion.

The first control is a local chart, deliberately not an actual 19-phase
predecessor: full overlap is arithmetically possible in general.  The second
control replays the exact fixed-constant factor screen and verifies that no
actual H3-to-H4 receipt can satisfy the additional 19-phase constraints.
"""

from __future__ import annotations

import argparse
from math import gcd

from type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_sieve_completion import (
    AFFINE_ROW,
    factor_phase_menu,
)


def local_full_overlap_contract() -> dict[str, int]:
    """Check the algebraic reduction on a non-phase full-overlap chart."""
    p = 73
    m4 = 110
    c4 = 37
    k4 = m4 * c4
    r4 = (4 * k4 - 1) // p
    w = (p + 1) // 2
    h = gcd(r4 - 1, k4)
    d = gcd(w, m4)
    j, remainder = divmod(2 * d * c4, p + 1)

    if not (
        p * r4 + 1 == 4 * k4
        and h == p + 1
        and k4 % w == 0
        and remainder == 0
        and c4 == j * (p + 1) // (2 * d)
        and 1 <= j < 2 * d
    ):
        raise AssertionError("the full-overlap-to-j contract changed")
    return {"p": p, "R4": r4, "K4": k4, "h": h, "d": d, "j": j}


def actual_phase_screen() -> dict[str, object]:
    """Reuse the exact finite factorization with the H4 interpretation."""
    result = factor_phase_menu()
    if not (
        result["rows"] == 571_777
        and result["distinct_constants"] == 377_516
        and result["phase_factor_rows"] == 23
        and result["affine_rows"] == [AFFINE_ROW]
        and result["actual_h4_rows"] == []
    ):
        raise AssertionError("the actual H3-to-H4 full-overlap screen changed")
    return result


def verify() -> None:
    local = local_full_overlap_contract()
    screen = actual_phase_screen()
    if not (
        local == {"p": 73, "R4": 223, "K4": 4_070, "h": 74, "d": 1, "j": 1}
        and screen["actual_h4_rows"] == []
    ):
        raise AssertionError("the H4 full-overlap predecessor exclusion changed")
    print(
        "verified H4 full-overlap reduction: a local positive control and "
        "0 actual H3-to-H4 predecessors in the exact 377516-constant screen"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="run the full-overlap predecessor receipt")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
