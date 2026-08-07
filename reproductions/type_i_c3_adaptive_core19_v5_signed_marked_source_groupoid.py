#!/usr/bin/env python3
"""Verify the v=5 signed marked-tail raw-source groupoid boundary."""

from __future__ import annotations

import argparse
import json
from math import gcd

import type_i_c3_adaptive_core19_v5_dual_leaf_f19_control as v5
import type_i_c3_adaptive_divisor_factor_block_normal_form as adaptive
import type_i_ordered_raw_lineage_normalized_phase_rigidity as lineage


CONDUCTOR = 191
ZETA = 150
BRANCH0 = (7, 2, 2, 2, 2, 72_106_829_959, 13, 2, 2)
BRANCH1 = (92_660_501, 5, 10_798_549_169, 5, 54_845_262_851)


def product_mod(values: tuple[int, ...], modulus: int) -> int:
    """Multiply a short declared raw label word modulo one chart modulus."""
    value = 1
    for label in values:
        value = value * label % modulus
    return value


def valuation(value: int, prime: int) -> int:
    """Return the exact valuation of a nonzero positive integer."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def signed_mark(*, K: int, M: int, tail: int, orientation: int, R: int) -> int:
    """Encode a physical signed tail as the raw propagation phase mu=-z^-1."""
    if orientation not in (-1, 1) or gcd(K * tail, R) != 1:
        raise AssertionError("signed tail is not a unit raw mark")
    return (-orientation * pow(K, -1, R) * M * pow(tail, -1, R)) % R


def all_primitive(rows: list[dict[str, object]]) -> bool:
    """Keep the groupoid dependent on explicit primitive raw receipts only."""
    return all(
        bool(row["strict_capacity"])
        and bool(row["unit_condition"])
        and row["gcd_reduction"] == 1
        for row in rows
    )


def verify_declared_source_groupoid() -> dict[str, object]:
    """Close precisely the two declared v=5 paths and their frame diamond."""
    parameters = adaptive.c3_parameters(h=v5.H, a=v5.A, b=v5.B)
    c0_rows = adaptive.replay_positive_control(parameters)
    c1_rows = v5.replay_word(v5.COMMON + v5.C1_SUFFIX)
    raw_tree = v5.verify_raw_tree()
    if not (all_primitive(c0_rows) and all_primitive(c1_rows)):
        raise AssertionError("declared groupoid lost a primitive raw path")

    labels0 = tuple(int(row["q"]) for row in c0_rows[2:])
    labels1 = tuple(int(row["q"]) for row in c1_rows[2:])
    anchor = (1, v5.R - 1, 1)
    swapped_anchor = (v5.R - 1, 1, 1)
    Q = (v5.B, v5.R - v5.B, 1)
    p_trace = lineage.trace_lineage(
        modulus=v5.R,
        carrier=v5.K,
        source=v5.SOURCE,
        source_coordinate_index=0,
        specs=(v5.COMMON[0],),
    )
    c0_trace = lineage.trace_lineage(
        modulus=v5.R,
        carrier=v5.K,
        source=swapped_anchor,
        source_coordinate_index=1,
        specs=v5.c0_specs(c0_rows)[1:],
    )
    c1_trace = lineage.trace_lineage(
        modulus=v5.R,
        carrier=v5.K,
        source=v5.SOURCE,
        source_coordinate_index=0,
        specs=v5.COMMON + v5.C1_SUFFIX,
    )
    if not (
        c0_rows[0]["destination"] == list(anchor)
        and c1_rows[0]["destination"] == list(anchor)
        and c0_rows[1]["source"] == list(swapped_anchor)
        and c0_rows[1]["selected_coordinate_index"] == 0
        and c1_rows[1]["source"] == list(anchor)
        and c1_rows[1]["selected_coordinate_index"] == 1
        and c0_rows[1]["destination"] == c1_rows[1]["destination"] == list(Q)
        and labels0 == BRANCH0
        and labels1 == BRANCH1
        and raw_tree["common_ordered_raw_prefix_length"] == 1
        and p_trace["coordinates"][-1] == 1
        and c0_trace["coordinates"][-1] == (-v5.C0) % v5.R
        and c1_trace["coordinates"][-1] == v5.C1
    ):
        raise AssertionError("v=5 frame-aware raw topology changed")

    mu_source = -pow(v5.P, -1, v5.R) % v5.R
    mu_anchor = v5.P * mu_source % v5.R
    mu_q = 5 * mu_anchor % v5.R
    mu0 = signed_mark(K=v5.K, M=v5.M0, tail=1, orientation=-1, R=v5.R)
    mu1 = signed_mark(K=v5.K, M=v5.M1, tail=1, orientation=1, R=v5.R)
    z0 = (-v5.C0) % v5.R
    z1 = v5.C1
    gamma0 = product_mod(BRANCH0, v5.R)
    gamma1 = product_mod(BRANCH1, v5.R)
    relative = mu1 * pow(mu0, -1, v5.R) % v5.R
    if not (
        mu_source == 390_772_497_842
        and mu_anchor == v5.R - 1
        and mu_q == v5.R - 5
        and mu0 == 13 == -pow(z0, -1, v5.R) % v5.R
        and mu1 == 4_387_621_028_405 == -pow(z1, -1, v5.R) % v5.R
        and gamma0 == 3_126_179_982_736
        and gamma1 == 4_332_775_765_550
        and mu_q * gamma0 % v5.R == mu0
        and mu_q * gamma1 % v5.R == mu1
        and relative == 5_147_016_975_629
        and (5 * pow(5, -1, v5.R)) % v5.R == 1
        and p_trace["phases"][-1] == mu_anchor
        and c0_trace["phases"][0] == mu_anchor
        and c0_trace["phases"][-1] == mu0
        and c1_trace["phases"][-1] == mu1
    ):
        raise AssertionError("signed marked-tail groupoid arithmetic changed")
    return {
        "source_universe": "two declared primitive raw paths plus one explicit frame arrow",
        "frame_diamond_holonomy": 1,
        "marks": {
            "source": mu_source,
            "anchor": mu_anchor,
            "after_five": mu_q,
            "C0": mu0,
            "C1": mu1,
            "relative_C1_over_C0": relative,
        },
        "branch_tokens": {"C0": gamma0, "C1": gamma1},
        "raw_words_after_Q": {"C0": list(BRANCH0), "C1": list(BRANCH1)},
    }


def verify_q19_relation() -> dict[str, object]:
    """Record the nonzero abstract 19-primary relation, not a Type-II lift."""
    phase_table = {pow(ZETA, exponent, CONDUCTOR): exponent for exponent in range(19)}

    def phase(value: int) -> int:
        return phase_table[pow(value, 10, CONDUCTOR)]

    mu0 = signed_mark(K=v5.K, M=v5.M0, tail=1, orientation=-1, R=v5.R)
    mu1 = signed_mark(K=v5.K, M=v5.M1, tail=1, orientation=1, R=v5.R)
    relative = mu1 * pow(mu0, -1, v5.R) % v5.R
    if not (
        len(phase_table) == 19
        and pow(ZETA, 19, CONDUCTOR) == 1
        and phase(mu0) == 16
        and phase(mu1) == 8
        and phase(relative) == 11
        and (phase(mu1) - phase(mu0)) % 19 == phase(relative)
    ):
        raise AssertionError("v=5 q=19 relation changed")
    return {
        "H_row": "<mu_C0, mu_C1> in U(R)",
        "quotient": "H_row / <mu_C1 * mu_C0^-1>",
        "kernel_relation": "e_C1 - e_C0",
        "eta_exponents": {"mu_C0": 16, "mu_C1": 8, "relative": 11},
        "abstract_consequence": "A_pi / A_pi^19 is nonzero",
        "status": "finite_raw_source_relation_only",
    }


def verify_integer_lift_boundary() -> dict[str, object]:
    """Show why the two existing E2 residues do not supply the missing lift."""
    r0 = v5.M0 % v5.P
    r1 = v5.M1 % v5.P
    if not (
        r0 == 100_198_076_370
        and r1 == 996_707_180_734
        and 4 * r0 < v5.P
        and valuation(v5.P + 4 * r0, 19) == 0
        and 4 * r1 > v5.P
        and valuation(v5.P + 4 * r1, 19) == 2
    ):
        raise AssertionError("v=5 natural integer residue boundary changed")
    return {
        "natural_remainders": {"C0": r0, "C1": r1},
        "C0": {"range": "4r<p", "q19_height": 0},
        "C1": {"range": "4r>p", "q19_height": 2},
        "conclusion": "these E2 residues cannot simultaneously supply range and q=19 height",
    }


def build_result() -> dict[str, object]:
    """Build a finite nonnative source presentation, deliberately not an edge."""
    return {
        "certificate_type": "nonnative_signed_marked_source_tree_v1",
        "status": "analysis_evidence_only",
        "mark_rule": "mu(M,t,epsilon)=-epsilon*K^-1*M*t^-1=-z^-1 mod R",
        "raw_edge_rule": "q*g*z_next=z_prev implies mu_next=(q*g)*mu_prev",
        "frame_edge_rule": "tracked-coordinate transport has token one",
        "declared_source_groupoid": verify_declared_source_groupoid(),
        "q19_relation": verify_q19_relation(),
        "integer_lift_boundary": verify_integer_lift_boundary(),
        "missing_for_capacity_or_descent": [
            "complete transition/source universe",
            "finite parameter fiber and occurrence projection",
            "integer map to (D_star,A,b) with q-height and range",
            "demand_to_slot, E4/E5, and terminal-first clearance",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified v=5 signed marked-tail source groupoid boundary")
        return
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
