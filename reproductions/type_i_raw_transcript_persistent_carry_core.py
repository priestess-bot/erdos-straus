#!/usr/bin/env python3
"""Verify persistent-ledger carry cores and a local c=3 congruence screen.

For rows that already have a sound raw-to-overflow interpretation, this
script computes the largest old ledger charge that can survive every row and
pass E2 wherever E2 is required.  The p=5281 raw ledger is also checked as a
negative scope control: its rows are not cofactor-overflow rows, so E2 cannot
be invoked there.

The final c=3 calculation is deliberately weaker: it establishes a one-row
gcd screen and a same-chart two-row determinant/E2 arithmetic pair, not a
raw-source, sound/complete transcript, F-layer, terminal, or selector
certificate.
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


def standard_c3_local_core(h: int) -> dict[str, int]:
    """Evaluate the local c=3 core screen without claiming a source receipt."""
    if h <= 0:
        raise AssertionError("c=3 local screen requires positive h")
    p = 24 * h + 1
    M = 26 * h + 1
    C = 24 * h - 2
    r = M % p
    if r != 2 * h or gcd(M, 2 * h) != 1:
        raise AssertionError("c=3 local carrier reduction changed")
    core = gcd(M, C * r)
    expected_core = 19 if h % 19 == 8 else 1
    if core != expected_core:
        raise AssertionError("c=3 local core congruence changed")
    return {
        "h": h,
        "p_parameter": p,
        "M": M,
        "C": C,
        "r": r,
        "core": core,
        "expected_core": expected_core,
    }


def standard_c3_two_row_ledger_pair(h: int) -> dict[str, object]:
    """Build the same-chart two-row A=19 arithmetic pair in its exact class."""
    base = standard_c3_local_core(h)
    if h % 19 != 8 or base["core"] != 19:
        raise AssertionError("the two-row c=3 pair requires the core-19 class")

    t = (h - 8) // 19
    p, M0, C0 = (base[key] for key in ("p_parameter", "M", "C"))
    R = 104 * h - 9
    K = M0 * C0
    M1, C1 = K // 19, 19
    rows = [
        {"p": p, "A": 19, "M": M0, "C": C0, "d": p - C0, "n": 4 * M0 - R},
        {"p": p, "A": 19, "M": M1, "C": C1, "d": p - C1, "n": 4 * M1 - R},
    ]
    if K % 19 or rows[0]["d"] != 3 or rows[1]["d"] != p - 19:
        raise AssertionError("c=3 companion row parameters changed")
    if not (M1 > M0 and C1 < C0):
        raise AssertionError("c=3 companion is not a distinct physical row")
    if rows[0]["M"] % p != 2 * h or rows[1]["M"] % p != 378 * t + 160:
        raise AssertionError("c=3 two-row carry residues changed")
    for row in rows:
        verify_overflow_row(row)
        if not e2_passes(A=19, C=row["C"], M=row["M"], p=p):
            raise AssertionError("A=19 unexpectedly fails E2 on the c=3 pair")

    core = persistent_carry_core(rows=rows, e2_indices={0, 1})
    if core != 19:
        raise AssertionError("c=3 two-row carry core changed")
    return {
        "h": h,
        "chart": {"p": p, "R": R, "K": K},
        "old_ledger": 19,
        "rows": [{**row, "r": row["M"] % p} for row in rows],
        "carry_core": core,
        "scope": (
            "A same-chart determinant/E2 arithmetic pair only; it does not supply a "
            "sound complete raw transcript, F layer, terminal-first result, or selector edge."
        ),
    }


def verify_standard_c3_local_core_screen() -> dict[str, object]:
    """Check one representative of every h class modulo 19, without a scan."""
    residue_rows = []
    for residue in range(19):
        # Use h=19 for the zero residue so every arithmetic input is positive.
        h = residue if residue else 19
        row = standard_c3_local_core(h)
        if row["h"] % 19 != residue:
            raise AssertionError("c=3 residue representative changed")
        residue_rows.append(row)
    if [row["core"] for row in residue_rows] != [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        19,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]:
        raise AssertionError("c=3 residue core table changed")

    h8 = standard_c3_local_core(8)
    h297 = standard_c3_local_core(297)
    if h8 != {
        "h": 8,
        "p_parameter": 193,
        "M": 209,
        "C": 190,
        "r": 16,
        "core": 19,
        "expected_core": 19,
    }:
        raise AssertionError("c=3 h=8 arithmetic control changed")
    if h297 != {
        "h": 297,
        "p_parameter": 7129,
        "M": 7723,
        "C": 7126,
        "r": 594,
        "core": 1,
        "expected_core": 1,
    }:
        raise AssertionError("c=3 p=7129 local core control changed")
    h8_pair = standard_c3_two_row_ledger_pair(8)
    if h8_pair["rows"] != [
        {"p": 193, "A": 19, "M": 209, "C": 190, "d": 3, "n": 13, "r": 16},
        {"p": 193, "A": 19, "M": 2090, "C": 19, "d": 174, "n": 7537, "r": 160},
    ] or h8_pair["carry_core"] != 19:
        raise AssertionError("c=3 h=8 two-row ledger control changed")
    return {
        "scope": (
            "A one-row arithmetic screen plus a same-chart two-row determinant/E2 pair "
            "only. It does not assert primality, a raw source/transcript, an F layer, "
            "terminal status, or a selector edge."
        ),
        "residue_class_representatives_mod_19": residue_rows,
        "h8_arithmetic_positive_control": h8,
        "h8_two_row_ledger_pair": h8_pair,
        "p7129_h297_core_one_control": h297,
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
        "standard_c3_local_core_screen": verify_standard_c3_local_core_screen(),
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
