#!/usr/bin/env python3
"""Verify the p=6121 same-source two-leaf c=3 raw-tree control.

The control proves raw provenance for both arithmetic rows in the core-19
pair, then separately records why it is not a q=19 selector control: a
direct Type II terminal is available and U(R) has no 19-primary character.
It does not create a root, a sound/complete selector transcript, or an edge.
"""

from __future__ import annotations

import argparse
import json

import type_i_c3_affine_prime_even_tail_root_entry as raw
import type_i_high_r_chart_two_anchor as shared
import type_i_ordered_raw_lineage_normalized_phase_rigidity as lineage
import type_i_raw_transcript_persistent_carry_core as carry


P = 6121
R = 26511
K = 40568458
SOURCE = (P, R * (P - 1) - P, P - 1)

PREFIX = (
    (0, P, (1, 26510, 1), "p"),
    (1, 5, (5302, 21209, 1), "five"),
)
C1_SUFFIX = (
    (1, 167, (127, 26384, 1), "one67"),
    (1, 2, (13192, 13319, 1), "two"),
    (1, 701, (19, 26492, 1), "seven01"),
)
C0_SUFFIX = (
    (0, 11, (482, 26029, 1), "eleven"),
    (0, 241, (2, 26509, 1), "two41"),
    (1, 7, (3787, 22724, 1), "seven"),
    (0, 541, (7, 26504, 1), "five41"),
    (1, 2, (13252, 13259, 1), "enter2"),
    (0, 3313, (4, 26507, 1), "gamma"),
    (1, 13, (2039, 24472, 1), "thirteen"),
    (1, 2, (12236, 14275, 1), "tail2a"),
    (0, 2, (6118, 20393, 1), "tail2b"),
)


def replay_word(
    specs: tuple[tuple[int, int, tuple[int, int, int], str], ...],
) -> list[dict[str, object]]:
    """Replay one declared raw word from the shared universal source."""
    current = SOURCE
    rows: list[dict[str, object]] = []
    for side, prime, destination, name in specs:
        row = raw.ordered_raw_step(
            modulus=R,
            K=K,
            source=current,
            selected_coordinate_index=side,
            q=prime,
            expected_destination=destination,
            name=f"p6121_{name}",
        )
        if not (
            row["strict_capacity"]
            and row["unit_condition"]
            and row["gcd_reduction"] == 1
        ):
            raise AssertionError("p=6121 raw row lost a declared primitive condition")
        rows.append(row)
        current = destination
    return rows


def verify_raw_tree() -> dict[str, object]:
    """Verify the common prefix and both distinct leaf words."""
    c0_specs = PREFIX + C0_SUFFIX
    c1_specs = PREFIX + C1_SUFFIX
    c0_rows = replay_word(c0_specs)
    c1_rows = replay_word(c1_specs)
    if [row["destination"] for row in c0_rows[:2]] != [
        row["destination"] for row in c1_rows[:2]
    ]:
        raise AssertionError("p=6121 leaf words no longer share their declared prefix")
    if c0_rows[-1]["destination"] != [6118, 20393, 1]:
        raise AssertionError("p=6121 C=p-3 word reached the wrong leaf")
    if c1_rows[-1]["destination"] != [19, 26492, 1]:
        raise AssertionError("p=6121 C=19 word reached the wrong leaf")

    c0_trace = lineage.trace_lineage(
        modulus=R,
        carrier=K,
        source=SOURCE,
        source_coordinate_index=0,
        specs=c0_specs,
    )
    c1_trace = lineage.trace_lineage(
        modulus=R,
        carrier=K,
        source=SOURCE,
        source_coordinate_index=0,
        specs=c1_specs,
    )
    if c0_trace["coordinates"] != [
        6121,
        1,
        21209,
        26029,
        26509,
        3787,
        7,
        13259,
        26507,
        2039,
        14275,
        20393,
    ] or c0_trace["phases"] != [
        1988,
        26510,
        26506,
        26456,
        13256,
        13259,
        15149,
        3787,
        6628,
        6631,
        13262,
        13,
    ]:
        raise AssertionError("p=6121 C=p-3 p-line trace changed")
    if c1_trace["coordinates"] != [6121, 1, 21209, 127, 13319, 19] or c1_trace[
        "products"
    ] != [1, 6121, 4094, 20923, 15335, 12880] or c1_trace["phases"] != [
        1988,
        26510,
        26506,
        25676,
        24841,
        22325,
    ]:
        raise AssertionError("p=6121 C=19 p-line trace changed")

    return {
        "source": list(SOURCE),
        "shared_prefix_steps": c0_rows[:2],
        "C0_raw_steps": c0_rows,
        "C1_raw_steps": c1_rows,
        "C0_p_line": c0_trace,
        "C1_p_line": c1_trace,
    }


def verify_two_row_arithmetic() -> dict[str, object]:
    """Check the two raw leaves decode to the same-chart A=19 pair."""
    rows = [
        {"p": P, "A": 19, "M": 6631, "C": 6118, "d": 3, "n": 13},
        {"p": P, "A": 19, "M": 2135182, "C": 19, "d": 6102, "n": 8514217},
    ]
    if K != rows[0]["M"] * rows[0]["C"] or K != rows[1]["M"] * rows[1]["C"]:
        raise AssertionError("p=6121 leaves no longer share K")
    for row in rows:
        carry.verify_overflow_row(row)
        if not carry.e2_passes(A=19, C=row["C"], M=row["M"], p=P):
            raise AssertionError("p=6121 A=19 E2 control failed")
    if carry.persistent_carry_core(rows=rows, e2_indices={0, 1}) != 19:
        raise AssertionError("p=6121 two-leaf carry core changed")

    c0_tail = lineage.verify_physical_tail(
        prime=P,
        modulus=R,
        carrier=6631,
        cofactor=6118,
        tail=1,
        orientation=-1,
        coordinate=20393,
        expected_phase=13,
    )
    c1_tail = lineage.verify_physical_tail(
        prime=P,
        modulus=R,
        carrier=2135182,
        cofactor=19,
        tail=1,
        orientation=1,
        coordinate=19,
        expected_phase=22325,
    )
    return {
        "rows": [{**row, "r": row["M"] % P} for row in rows],
        "carry_core_for_T_equals_I_equals_0_1": 19,
        "physical_tail_readings": {"C0": c0_tail, "C1": c1_tail},
    }


def verify_terminal_and_q19_boundaries() -> dict[str, object]:
    """Record the two independent reasons this raw tree is not a q=19 root."""
    m, x, divisor = 7, (P + 7) // 4, 1
    if not (
        P % 7 == 3
        and divisor <= x
        and x * x % divisor == 0
        and (x + divisor) % m == 0
    ):
        raise AssertionError("p=6121 gap-seven terminal predicate changed")
    y = P * (x + divisor) // m
    z = P * (x + x * x // divisor) // m
    if 4 * x * y * z != P * (y * z + x * z + x * y):
        raise AssertionError("p=6121 Type II terminal identity changed")

    factors = shared.factorization(R)
    phi = (3 - 1) * (8837 - 1)
    if factors != [(3, 1), (8837, 1)] or not shared.is_prime(8837):
        raise AssertionError("p=6121 R factorization changed")
    if phi != 17672 or shared.factorization(phi) != [(2, 3), (47, 2)] or phi % 19 == 0:
        raise AssertionError("p=6121 q=19 unit-group obstruction changed")
    return {
        "direct_type_ii_terminal": {
            "gap": m,
            "x": x,
            "divisor": divisor,
            "denominators": [x, y, z],
        },
        "unit_group_order": phi,
        "unit_group_order_factorization": [[2, 3], [47, 2]],
        "q19_primary_character": "impossible_in_any_U(R)_subquotient",
    }


def build_result() -> dict[str, object]:
    """Build the one fixed dual-leaf provenance and boundary control."""
    if not shared.is_prime(P) or P % 24 != 1 or K != (P * R + 1) // 4:
        raise AssertionError("p=6121 chart control changed")
    return {
        "certificate_type": "c3_p6121_same_source_dual_leaf_raw_tree_v1",
        "scope": (
            "A fixed same-source two-leaf raw provenance control. It is terminal-preempted "
            "and has no q=19 Fourier direction, so it is not a root or selector edge."
        ),
        "raw_tree": verify_raw_tree(),
        "two_row_arithmetic": verify_two_row_arithmetic(),
        "terminal_and_q19_boundaries": verify_terminal_and_q19_boundaries(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=6121 same-source dual-leaf raw-tree control")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
