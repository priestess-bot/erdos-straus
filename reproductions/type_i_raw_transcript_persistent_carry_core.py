#!/usr/bin/env python3
"""Verify the persistent-ledger carry core for physical overflow transcripts.

For rows that already have a sound raw-to-overflow interpretation, this
script computes the largest old ledger charge that can survive every row and
pass E2 wherever E2 is required.  The p=5281 raw ledger is also checked as a
negative scope control: its rows are not cofactor-overflow rows, so E2 cannot
be invoked there.
"""

from __future__ import annotations

import argparse
from math import gcd
from typing import Iterable

import type_i_g_anchor_jacobi_p5281_physical_ledger as jacobi_ledger


def gcd_all(values: Iterable[int]) -> int:
    """Return the positive gcd of a nonempty finite iterable."""
    result = 0
    for value in values:
        if value <= 0:
            raise AssertionError("carry-core inputs must be positive")
        result = gcd(result, value)
    if result <= 0:
        raise AssertionError("carry core requires at least one input")
    return result


def e2_parameter(A: int, C: int) -> int:
    """Return the cofactor E2 divisor A / gcd(A, C)."""
    if A <= 0 or C <= 0:
        raise AssertionError("E2 parameters must be positive")
    return A // gcd(A, C)


def e2_passes(*, A: int, C: int, M: int, p: int) -> bool:
    """Evaluate the exact cofactor E2 divisibility gate for one row."""
    if not (A > 0 and C > 0 and M > 0 and M % A == 0 and p > 1 and M % p):
        raise AssertionError("invalid physical carry row")
    return M % p % e2_parameter(A, C) == 0


def persistent_carry_core(
    *, rows: list[dict[str, int]], e2_indices: set[int]
) -> int:
    """Return gcd(M_i, C_i * (M_i mod p)) for the declared transcript."""
    if not rows or not e2_indices <= set(range(len(rows))):
        raise AssertionError("invalid transcript or E2 row subset")
    values = [row["M"] for row in rows]
    values.extend(
        rows[index]["C"] * (rows[index]["M"] % rows[index]["p"])
        for index in sorted(e2_indices)
    )
    return gcd_all(values)


def verify_overflow_row(row: dict[str, int]) -> None:
    """Check the physical hypotheses needed before calling the carry theorem."""
    p, A, M, C, d, n = (row[key] for key in ("p", "A", "M", "C", "d", "n"))
    if not (
        p > 1
        and A > 0
        and M % A == 0
        and A <= M
        and C == p - d
        and 0 < d < p
        and p * n == 4 * M * d + 1
        and 4 * M - n > p
        and M % p != 0
    ):
        raise AssertionError("declared row is not a physical cofactor-overflow row")


def verify_p73_controls() -> dict[str, object]:
    """Use one failing and one passing physical overflow row as exact controls."""
    failing = {"p": 73, "A": 34, "M": 1598, "C": 57, "d": 16, "n": 1401}
    passing = {"p": 73, "A": 69, "M": 10626, "C": 69, "d": 4, "n": 2329}
    for row in (failing, passing):
        verify_overflow_row(row)
    if failing["M"] % failing["p"] != 65 or passing["M"] % passing["p"] != 41:
        raise AssertionError("p=73 carry residues changed")

    failing_core = persistent_carry_core(rows=[failing], e2_indices={0})
    passing_core = persistent_carry_core(rows=[passing], e2_indices={0})
    if failing_core != 1 or passing_core != 69:
        raise AssertionError("p=73 carry cores changed")
    if e2_passes(A=failing["A"], C=failing["C"], M=failing["M"], p=failing["p"]):
        raise AssertionError("known p=73 E2 failure passed")
    if not e2_passes(A=passing["A"], C=passing["C"], M=passing["M"], p=passing["p"]):
        raise AssertionError("known p=73 E2 positive control failed")

    for candidate in (1, 2, 17, 34):
        retained = failing["M"] % candidate == 0
        e2 = retained and e2_passes(
            A=candidate, C=failing["C"], M=failing["M"], p=failing["p"]
        )
        if e2 != (failing_core % candidate == 0):
            raise AssertionError("carry-core iff check failed on the negative control")
    for candidate in (1, 3, 23, 69):
        retained = passing["M"] % candidate == 0
        e2 = retained and e2_passes(
            A=candidate, C=passing["C"], M=passing["M"], p=passing["p"]
        )
        if e2 != (passing_core % candidate == 0):
            raise AssertionError("carry-core iff check failed on the positive control")
    return {
        "failing_row": {**failing, "r": failing["M"] % failing["p"], "core": failing_core},
        "passing_row": {**passing, "r": passing["M"] % passing["p"], "core": passing_core},
    }


def verify_p5281_scope_control() -> dict[str, object]:
    """Show that a raw determinant menu can fail before cofactor E2 exists."""
    parameters = jacobi_ledger.ledger_parameters()
    p = parameters["p"]
    R = parameters["R"]
    menu = (7, 91, 203, 2639)
    rows = {
        delta: jacobi_ledger.row_from_delta(delta=delta, parameters=parameters)
        for delta in menu
    }
    if any(4 * int(row["M"]) - int(row["n"]) != R for row in rows.values()):
        raise AssertionError("p=5281 row remainder changed")
    if not R < p:
        raise AssertionError("p=5281 rows unexpectedly became cofactor overflows")

    source = rows[7]
    target = rows[91]
    diagnostic_core = gcd_all(
        [int(source["M"]), int(target["M"]), int(target["C"]) * (int(target["M"]) % p)]
    )
    if target["M"] % p != 3961 or diagnostic_core != 1:
        raise AssertionError("p=5281 first-edge carry diagnostic changed")
    return {
        "reason_e2_is_inapplicable": "4M-n=R=p-2<p for every declared row",
        "first_menu_edge_diagnostic": {
            "edge": [7, 13, 91],
            "source_M": int(source["M"]),
            "target_M": int(target["M"]),
            "target_C": int(target["C"]),
            "target_r": int(target["M"]) % p,
            "hypothetical_carry_core": diagnostic_core,
        },
    }


def build_result() -> dict[str, object]:
    """Build the focused theorem controls only."""
    return {
        "certificate_type": "raw_transcript_persistent_ledger_carry_core_v1",
        "scope": (
            "The carry core applies only after an independently sound raw-to-overflow "
            "row map has been supplied. It does not create that map or establish E1, "
            "E3, E4, E5, a source-complete selector, or a descent edge."
        ),
        "p73_overflow_controls": verify_p73_controls(),
        "p5281_pre_e2_scope_control": verify_p5281_scope_control(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    build_result()
    if args.verify:
        print("verified persistent-ledger carry-core controls")


if __name__ == "__main__":
    main()
