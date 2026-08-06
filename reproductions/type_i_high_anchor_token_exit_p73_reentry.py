#!/usr/bin/env python3
"""Verify focused p=73 token-exit and reentry boundaries.

This is a deliberately small, read-only analysis of the frozen selector
artifact.  It does not run the selector.  It separates three statements:

* fixed-n/fixed-s paid resets in the current artifact strictly lower Pi;
* the only p=73 paid-reset target below p is A=18, whose support-preserving
  descendants below p are all low canonical charts;
* forgetful RESET and an illicit fresh-root reuse are outside that rank.

The last point is a boundary, not a recursive counterexample: fresh roots are
allowed only as roots, and the current p=73 high-R complete-excess replay has
no positive gated cofactor step from any canonical high support below p.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path
from typing import Iterator

from type_i_high_r_chart_two_anchor import canonical_chart, high_R_path_anchored_bundle


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-token-exit-p73-reentry-results.json"
PRIME = 73
B_P = (PRIME - 1) ** 2 // 4


def omega(value: int) -> int:
    if value <= 0:
        raise AssertionError("Omega needs a positive integer")
    count = 0
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            value //= divisor
            count += 1
        divisor = 3 if divisor == 2 else divisor + 2
    return count + int(value > 1)


def lambda_rank(prime: int, support: int, K: int) -> tuple[int, int]:
    if K % support:
        raise AssertionError("charged support must divide K")
    B_prime = (prime - 1) ** 2 // 4
    return B_prime // support, omega(K // support)


def walk_objects(value: object) -> Iterator[dict[str, object]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_objects(child)


def state_records(payload: dict[str, object]) -> list[dict[str, object]]:
    records: dict[str, dict[str, object]] = {}
    for row in walk_objects(payload):
        if row.get("selector_status") != "verified_edge":
            continue
        edge_id = row.get("edge_id")
        source = row.get("source_state")
        target = row.get("successor_state")
        if not isinstance(edge_id, str) or not isinstance(source, dict) or not isinstance(target, dict):
            continue
        if not isinstance(source.get("absorbed_support"), int) or not isinstance(
            target.get("absorbed_support"), int
        ):
            continue
        equation = source.get("equation_target")
        if not isinstance(equation, list) or len(equation) != 2 or not isinstance(equation[1], int):
            continue
        records[edge_id] = row
    return [records[key] for key in sorted(records)]


def record_summary(record: dict[str, object]) -> dict[str, object]:
    source = record["source_state"]
    target = record["successor_state"]
    if not isinstance(source, dict) or not isinstance(target, dict):
        raise AssertionError("state record shape changed")
    equation = source["equation_target"]
    if not isinstance(equation, list):
        raise AssertionError("equation target shape changed")
    prime = int(equation[1])
    source_A = int(source["absorbed_support"])
    target_A = int(target["absorbed_support"])
    source_K = int(source["K"])
    target_K = int(target["K"])
    return {
        "edge_id": record["edge_id"],
        "certificate_type": record.get("certificate_type"),
        "phase": record.get("phase"),
        "prime": prime,
        "source": {
            "A": source_A,
            "R": int(source["R"]),
            "K": source_K,
            "Lambda": list(lambda_rank(prime, source_A, source_K)),
        },
        "target": {
            "A": target_A,
            "R": int(target["R"]),
            "K": target_K,
            "Lambda": list(lambda_rank(prime, target_A, target_K)),
        },
        "support_reset_paid": bool(
            isinstance(record.get("potential_record"), dict)
            and record["potential_record"].get("support_reset_paid")
        ),
    }


def algebraic_positive_gate_rows() -> tuple[list[dict[str, object]], dict[int, list[dict[str, int]]]]:
    high_rows: list[dict[str, object]] = []
    positive: dict[int, list[dict[str, int]]] = {}
    for support in range(1, PRIME):
        R, K = canonical_chart(PRIME, support)
        if R <= PRIME:
            continue
        rows: list[dict[str, int]] = []
        for r in range(1, PRIME):
            for C in range(1, PRIME):
                numerator = 4 * r * C - 1
                if numerator % PRIME:
                    continue
                cofactor_support = lcm(support, C)
                if r * C % cofactor_support:
                    continue
                difference = r * C - K
                if difference % (PRIME * support):
                    raise AssertionError("gated phase was not integral")
                h = difference // (PRIME * support)
                if h <= 0:
                    continue
                rows.append(
                    {
                        "r": r,
                        "C": C,
                        "h": h,
                        "A_target": cofactor_support,
                        "R_target": numerator // PRIME,
                    }
                )
        rows.sort(key=lambda row: (row["r"], row["C"]))
        high_rows.append({"A": support, "R": R, "K": K, "positive_gate_rows": rows})
        if rows:
            positive[support] = rows
    return high_rows, positive


def forced_high_bundle_rows(high_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for source in high_rows:
        support = int(source["A"])
        R = int(source["R"])
        K = int(source["K"])
        bundle = high_R_path_anchored_bundle(prime=PRIME, R=R, support=support)
        rechart = bundle["rechart"]
        if not isinstance(rechart, dict):
            raise AssertionError("high-R rechart shape changed")
        C = int(rechart["C"])
        M = int(rechart["M"])
        r = M % PRIME
        a = support // gcd(support, C)
        gate = r % a == 0
        h: int | None = None
        if gate:
            difference = r * C - K
            if difference % (PRIME * support):
                raise AssertionError("forced high bundle gate lost phase integrality")
            h = difference // (PRIME * support)
        rows.append(
            {
                "A": support,
                "R": R,
                "K": K,
                "Q": int(bundle["complete_excess_bundle"]["Q"]),
                "M": M,
                "C": C,
                "r": r,
                "a": a,
                "gate": gate,
                "h": h,
            }
        )
    return rows


def build_result() -> dict[str, object]:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise AssertionError("selector artifact root changed")
    records = state_records(payload)
    summaries = [record_summary(record) for record in records]
    all_pi_decrease = all(
        int(row["target"]["Lambda"][0]) < int(row["source"]["Lambda"][0])
        for row in summaries
    )
    if not all_pi_decrease:
        raise AssertionError("current complete state receipts no longer all pay Pi")

    paid = [row for row in summaries if row["support_reset_paid"]]
    paid_p73 = [row for row in paid if row["prime"] == PRIME]
    below_prime = [row for row in paid_p73 if int(row["target"]["A"]) < PRIME]
    if len(below_prime) != 1 or below_prime[0]["target"]["A"] != 18:
        raise AssertionError("p=73 paid-reset below-p boundary changed")

    inherited_supports = list(range(18, PRIME, 18))
    inherited_charts = []
    for support in inherited_supports:
        R, K = canonical_chart(PRIME, support)
        inherited_charts.append({"A": support, "R": R, "K": K, "high": R > PRIME})
    if any(row["high"] for row in inherited_charts):
        raise AssertionError("A=18 support-preserving p=73 reentry boundary changed")

    high_rows, algebraic_positive = algebraic_positive_gate_rows()
    if set(algebraic_positive) != {31, 34}:
        raise AssertionError("p=73 high algebraic positive-gate census changed")
    forced_rows = forced_high_bundle_rows(high_rows)
    forced_gate_rows = [row for row in forced_rows if row["gate"]]
    if forced_gate_rows != [
        {
            "A": 69,
            "R": 155,
            "K": 2829,
            "Q": 154,
            "M": 10626,
            "C": 69,
            "r": 41,
            "a": 1,
            "gate": True,
            "h": 0,
        }
    ]:
        raise AssertionError("p=73 forced high-bundle gate census changed")

    root = [
        row
        for row in summaries
        if row["certificate_type"] == "overflow_same_chart_support_promotion"
        and row["prime"] == PRIME
        and row["source"]["A"] == 1
        and row["source"]["R"] == 95
        and row["target"]["A"] == 34
        and row["target"]["R"] == 95
    ]
    if len(root) != 1:
        raise AssertionError("p=73 fresh-root support-promotion receipt changed")

    cycle = {
        "node_132": {"R": 311, "K": 5676, "A": 132},
        "node_330": {"R": 1103, "K": 20130, "A": 330},
    }
    for node in cycle.values():
        if PRIME * node["R"] + 1 != 4 * node["K"]:
            raise AssertionError("p=73 reset-cycle chart changed")
        node["Lambda"] = list(lambda_rank(PRIME, node["A"], node["K"]))
    if not (cycle["node_132"]["Lambda"] > cycle["node_330"]["Lambda"]):
        raise AssertionError("p=73 RESET cycle no longer contains Lambda rise")

    # This is deliberately not asserted as an edge.  It records why a fresh
    # root may never be called from a spent charged history.
    illegal_reentry = {
        "spent_gate_level_target": {"A": 68, "R": 231, "K": 4216},
        "fresh_root_source": {"A": 1, "R": 95, "K": 1734},
        "status": "not_a_legal_transition_without_root_scope",
    }
    for state in (illegal_reentry["spent_gate_level_target"], illegal_reentry["fresh_root_source"]):
        if PRIME * state["R"] + 1 != 4 * state["K"]:
            raise AssertionError("fresh-root rank boundary chart changed")
        state["Lambda"] = list(lambda_rank(PRIME, state["A"], state["K"]))
    if not (
        illegal_reentry["fresh_root_source"]["Lambda"]
        > illegal_reentry["spent_gate_level_target"]["Lambda"]
    ):
        raise AssertionError("fresh-root misuse no longer raises Lambda")

    return {
        "schema_version": 1,
        "purpose": "focused token-exit/reentry boundary; not a global selector proof",
        "input": INPUT.name,
        "prime": PRIME,
        "B_p": B_P,
        "lambda_definition": "(floor(B_p/A), Omega(K/A))",
        "artifact_state_edges": {
            "count": len(summaries),
            "all_strictly_decrease_first_coordinate": all_pi_decrease,
            "support_reset_paid": paid,
        },
        "p73_paid_reset_boundary": {
            "records": paid_p73,
            "targets_below_p": below_prime,
            "support_preserving_multiples_of_18_below_p": inherited_charts,
            "conclusion": (
                "The only current verified paid reset below p lands at A=18.  Any "
                "support-preserving descendant below p has A in {18,36,54,72} and "
                "canonical R=71<p, so it cannot start a high positive cofactor phase."
            ),
        },
        "p73_high_gate_vs_forced_bundle": {
            "canonical_high_supports_below_p": high_rows,
            "algebraic_positive_gate_supports": algebraic_positive,
            "forced_complete_excess_rows": forced_rows,
            "forced_gate_rows": forced_gate_rows,
            "conclusion": (
                "At chart level A=31 and A=34 admit h=1 gates, but the forced "
                "complete-excess replay from every p=73 canonical high A<p has no "
                "positive gated row.  In particular the fresh-root A=34 chart has "
                "Q=47, M=1598, C=57, r=65 and fails 34|65."
            ),
        },
        "forgetful_reset_counterexample_to_lambda": {
            "cycle": cycle,
            "conclusion": (
                "The candidate RESET continuation 132 -> 330 -> 132 has Lambda "
                "(9,1) -> (3,1) -> (9,1); forgetful RESET cannot be admitted under "
                "the Lambda rank."
            ),
        },
        "fresh_root_scope_boundary": {
            "root_support_promotion": root[0],
            "illegal_historical_reentry_example": illegal_reentry,
            "conclusion": (
                "The root A=1 -> A=34 receipt is decreasing only at a true root.  "
                "Treating it as a transition from a spent history can raise Lambda, "
                "so source_tree_scope/root-entry must remain part of state identity."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.verify:
        print("verified p=73 token-exit Lambda and reentry boundaries")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
