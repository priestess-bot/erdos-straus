#!/usr/bin/env python3
"""Build a read-only atlas of verified parents that land at high anchors.

The frozen selector artifact contains many nested verified receipts.  This
program follows only their exact ``successor_state`` objects, tests whether
that state is a high canonical anchor, and deterministically replays the
high-R complete-excess bundle.  It intentionally does *not* promote a row to
a recursive macro edge: legacy selector receipts lack the scope/content and
typed-fiber material required by the macro E1--E4 contract.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
from typing import Iterator

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"
DEFAULT_OUTPUT = ROOT / "reproductions" / "type-i-high-anchor-parent-atlas-results.json"

IDENTITY_LIFT = {"source": "Sol(p)", "successor": "Sol(p)", "lift": "identity"}


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode(
            "ascii"
        )
    ).hexdigest()


def omega(value: int) -> int:
    return sum(exponent for _prime, exponent in shared.factorization(value))


def lambda_rank(prime: int, K: int, support: int) -> list[int]:
    if support <= 0 or K % support:
        raise AssertionError("Lambda requires a positive charged support dividing K")
    return [((prime - 1) ** 2 // 4) // support, omega(K // support)]


def lex_decreases(source: list[int], target: list[int]) -> bool:
    return target[0] < source[0] or (
        target[0] == source[0] and target[1] < source[1]
    )


def iter_verified_receipts(value: object) -> Iterator[dict[str, object]]:
    if isinstance(value, dict):
        if (
            value.get("selector_status") == "verified_edge"
            and value.get("recursive_edge_eligible") is True
            and isinstance(value.get("source_state"), dict)
            and isinstance(value.get("successor_state"), dict)
        ):
            yield value
        for child in value.values():
            yield from iter_verified_receipts(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_verified_receipts(child)


def parent_receipt_contract(receipt: dict[str, object]) -> dict[str, object]:
    """Separate a verified legacy parent from the stronger macro parent API."""
    e1_e5 = receipt.get("e1_e5")
    source = receipt["source_state"]
    successor = receipt["successor_state"]
    if not isinstance(source, dict) or not isinstance(successor, dict):
        raise AssertionError("verified receipt state shape changed")
    verified_ledger = bool(
        receipt.get("selector_status") == "verified_edge"
        and receipt.get("recursive_edge_eligible") is True
        and e1_e5 == {f"E{index}": True for index in range(1, 6)}
        and receipt.get("marked_solution_set") == IDENTITY_LIFT
    )
    # The macro contract needs reproducible typed state, not just an edge id.
    missing: list[str] = []
    if not isinstance(receipt.get("normal_form_replay_adapter"), str):
        missing.append("parent_normal_form_replay_adapter")
    if not isinstance(receipt.get("checks"), dict):
        missing.append("parent_replay_checks")
    if not isinstance(successor.get("state_id"), str):
        missing.append("successor_content_address")
    if not isinstance(source.get("state_id"), str):
        missing.append("source_content_address")
    if not isinstance(successor.get("source_tree_scope"), str):
        missing.append("source_tree_scope")
    if not isinstance(receipt.get("fiber_certificate"), dict):
        missing.append("parent_typed_fiber")
    return {
        "verified_parent_ledger": verified_ledger,
        "receipt_edge_id": receipt.get("edge_id"),
        "receipt_digest": canonical_hash(receipt),
        "macro_parent_api_complete": not missing,
        "macro_parent_api_missing": missing,
    }


def anchor_conditions(prime: int, state: dict[str, object]) -> dict[str, bool]:
    R = int(state["R"])
    K = int(state["K"])
    A = int(state["absorbed_support"])
    return {
        "core_prime": shared.is_prime(prime) and prime % 24 == 1,
        "positive_support": A > 0,
        "charged_support_divides_K": A > 0 and K % A == 0,
        "chart_equation": prime * R + 1 == 4 * K,
        "canonical_chart": A > 0 and shared.canonical_chart(prime, A) == (R, K),
        "high_window": prime < R < 4 * A,
        "raw_source_primitive": R % prime != 0,
        "overflow_class": state.get("state_class") == "overflow",
    }


def cofactor_replay(prime: int, A: int, K: int, bundle: dict[str, object]) -> dict[str, object]:
    rechart = bundle.get("rechart")
    if not isinstance(rechart, dict):
        raise AssertionError("bundle rechart shape changed")
    if rechart.get("result_class") != "overflow":
        return {
            "bundle_result_class": rechart.get("result_class"),
            "cofactor_attempted": False,
            "routing": "bundle_marked_absorb",
        }
    M = int(rechart["M"])
    R_M = int(rechart["R"])
    K_M = int(rechart["K"])
    C = int(rechart["C"])
    d = int(rechart["d"])
    n = int(rechart["n"])
    _k, r = divmod(M, prime)
    s_numerator = 4 * r * d + 1
    integral_s = r > 0 and s_numerator % prime == 0
    s = s_numerator // prime if integral_s else None
    R_T = 4 * r - s if isinstance(s, int) else None
    K_T = r * C
    g = gcd(A, C)
    a = A // g
    A_T = lcm(A, C)
    gate = a > 0 and r % a == 0
    target_divisible = gate and K_T % A_T == 0
    target_chart = (
        isinstance(R_T, int)
        and target_divisible
        and shared.canonical_chart(prime, A_T) == (R_T, K_T)
    )
    target_route = (
        "overflow"
        if isinstance(R_T, int) and R_T > prime
        else "marked_absorb"
        if isinstance(R_T, int) and 0 < R_T < prime
        else "invalid_nonpositive_or_boundary_target"
    )
    h_numerator = K_T - K
    h_denominator = prime * A
    h_integral = h_denominator > 0 and h_numerator % h_denominator == 0
    h = h_numerator // h_denominator if h_integral else None
    arithmetic = {
        "intermediate_chart": shared.canonical_chart(prime, M) == (R_M, K_M),
        "intermediate_determinant": prime * n == 4 * M * d + 1,
        "cofactor_identity": integral_s and prime * int(s) == 4 * r * d + 1,
        "target_chart_equation": isinstance(R_T, int) and prime * R_T + 1 == 4 * K_T,
        "support_gate": gate,
        "target_support_divides_K": target_divisible,
        "canonical_target": target_chart,
        "three_phase_window": h in {0, 1, 2},
        "gate_size_obstruction_A_over_gcd_gt_r": a > r,
    }
    target = {
        "R": R_T,
        "K": K_T,
        "absorbed_support": A_T,
        "route": target_route,
    }
    rank: dict[str, object] = {"defined": False}
    if target_divisible:
        source_lambda = lambda_rank(prime, K, A)
        target_lambda = lambda_rank(prime, K_T, A_T)
        rank = {
            "defined": True,
            "source": source_lambda,
            "target": target_lambda,
            "strict_lexicographic_decrease": lex_decreases(source_lambda, target_lambda),
        }
    return {
        "bundle_result_class": "overflow",
        "cofactor_attempted": True,
        "intermediate": {"M": M, "R": R_M, "K": K_M, "C": C, "d": d, "n": n},
        "cofactor": {"r": r, "s": s, "gcd_A_C": g, "A_over_gcd": a},
        "target": target,
        "phase": {"h": h, "integral": h_integral},
        "arithmetic_checks": arithmetic,
        "lambda_p": rank,
    }


def classify_anchor(receipt: dict[str, object], ordinal: int) -> dict[str, object]:
    state = receipt["successor_state"]
    if not isinstance(state, dict):
        raise AssertionError("successor state shape changed")
    equation = state.get("equation_target", receipt.get("equation_target"))
    if not (
        isinstance(equation, list)
        and len(equation) == 2
        and equation[0] == 4
        and isinstance(equation[1], int)
    ):
        raise AssertionError("fixed-p equation target is absent")
    prime = equation[1]
    R, K, A = (int(state["R"]), int(state["K"]), int(state["absorbed_support"]))
    parent = parent_receipt_contract(receipt)
    conditions = anchor_conditions(prime, state)
    numeric_high = all(conditions.values())
    high = bool(parent["verified_parent_ledger"] and numeric_high)
    row: dict[str, object] = {
        "atlas_row_id": f"high-parent:{ordinal}:{canonical_hash(receipt)[:16]}",
        "parent": parent,
        "parent_certificate_type": receipt.get("certificate_type"),
        "parent_normal_form": receipt.get("normal_form"),
        "anchor": {"p": prime, "R": R, "K": K, "absorbed_support": A},
        "anchor_conditions": conditions,
        "numeric_high_successor": numeric_high,
        "high_anchor_candidate": high,
    }
    if not high:
        return row
    try:
        bundle = shared.high_R_path_anchored_bundle(prime=prime, R=R, support=A)
    except AssertionError as error:
        row["bundle_replay"] = {"passed": False, "error": str(error)}
        row["macro_admission"] = {
            "E1_arithmetic_parent_and_bundle": False,
            "E2_cofactor_normal_form": False,
            "E3_chain_scope_content": False,
            "E4_typed_FG_identity_lift": False,
            "closed_E1_E4": False,
            "boundary": "high_anchor_bundle_replay_failed",
        }
        return row
    cofactor = cofactor_replay(prime, A, K, bundle)
    row["bundle_replay"] = {
        "passed": True,
        "adapter": bundle["adapter"],
        "digest": canonical_hash(bundle),
        "result_class": bundle["rechart"]["result_class"],
        "conditions": bundle["conditions"],
    }
    row["cofactor_replay"] = cofactor
    arithmetic = cofactor.get("arithmetic_checks", {})
    e1 = bool(parent["verified_parent_ledger"] and all(conditions.values()))
    # The size-obstruction flag is a failure diagnostic, not an E2 requirement.
    e2_required_checks = {
        "intermediate_chart",
        "intermediate_determinant",
        "cofactor_identity",
        "target_chart_equation",
        "support_gate",
        "target_support_divides_K",
        "canonical_target",
        "three_phase_window",
    }
    e2 = isinstance(arithmetic, dict) and all(
        arithmetic.get(check) is True for check in e2_required_checks
    )
    # E3/E4 are deliberately not inferred from untyped legacy selector fields.
    missing_e3 = list(parent["macro_parent_api_missing"])
    missing_e3.extend(["bundle_to_intermediate_scoped_state", "cofactor_target_scoped_state"])
    typed_gap = [
        "anchor_typed_FG_or_hit_certificate",
        "intermediate_typed_FG_or_hit_certificate",
        "target_typed_FG_or_hit_certificate",
        "typed_solution_lift_direction_T_to_H",
    ]
    row["macro_admission"] = {
        "E1_arithmetic_parent_and_bundle": e1,
        "E2_cofactor_normal_form": e2,
        "E3_chain_scope_content": False,
        "E4_typed_FG_identity_lift": False,
        "closed_E1_E4": False,
        "missing_E3": missing_e3,
        "missing_E4": typed_gap,
        "boundary": "legacy_verified_parent_is_not_the_macro_parent_API",
    }
    return row


def count_by(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key))
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def build_result() -> dict[str, object]:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    receipts = list(iter_verified_receipts(payload))
    rows = [classify_anchor(receipt, ordinal) for ordinal, receipt in enumerate(receipts, 1)]
    numeric_high_rows = [row for row in rows if row["numeric_high_successor"]]
    high_rows = [row for row in rows if row["high_anchor_candidate"]]
    bundle_overflow = [
        row
        for row in high_rows
        if row.get("bundle_replay", {}).get("result_class") == "overflow"
    ]
    cofactor_gate = [
        row
        for row in bundle_overflow
        if row.get("cofactor_replay", {}).get("arithmetic_checks", {}).get("support_gate")
    ]
    lambda_paid = [
        row
        for row in cofactor_gate
        if row.get("cofactor_replay", {}).get("lambda_p", {}).get("strict_lexicographic_decrease")
    ]
    gate_size_obstruction = [
        row
        for row in bundle_overflow
        if row.get("cofactor_replay", {})
        .get("arithmetic_checks", {})
        .get("gate_size_obstruction_A_over_gcd_gt_r")
    ]
    gate_residue_obstruction = [
        row
        for row in bundle_overflow
        if not row.get("cofactor_replay", {})
        .get("arithmetic_checks", {})
        .get("gate_size_obstruction_A_over_gcd_gt_r")
    ]
    return {
        "schema_version": 1,
        "certificate_type": "type_i_high_anchor_parent_atlas_v1",
        "input": {"path": str(INPUT.relative_to(ROOT)), "sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest()},
        "scope": (
            "Read-only extraction from exact frozen verified parent receipts. A numerical "
            "high chart without a listed receipt is not included, and no row is registered "
            "as a selector edge."
        ),
        "summary": {
            "verified_receipt_occurrences": len(receipts),
            "numeric_high_successor_occurrences": len(numeric_high_rows),
            "high_anchor_receipt_occurrences": len(high_rows),
            "bundle_overflow_occurrences": len(bundle_overflow),
            "cofactor_gate_occurrences": len(cofactor_gate),
            "lambda_paid_occurrences": len(lambda_paid),
            "gate_size_obstruction_A_over_gcd_gt_r_occurrences": len(gate_size_obstruction),
            "gate_residue_nondivisibility_occurrences": len(gate_residue_obstruction),
            "fully_closed_E1_E4_occurrences": sum(
                bool(row.get("macro_admission", {}).get("closed_E1_E4")) for row in high_rows
            ),
            "parent_certificate_type_counts": count_by(high_rows, "parent_certificate_type"),
        },
        "decisive_gap": {
            "claim": (
                "All strict verified-parent high anchors in this frozen artifact replay to an "
                "overflow bundle, but none passes A/gcd(A,C) | r. In the listed finite "
                "atlas, failure splits into A/gcd(A,C)>r and a nonzero residue modulo a "
                "smaller A/gcd(A,C). Separately, the legacy receipts carry neither the scoped "
                "content-addressed states nor the typed H/S/T F/G certificates required "
                "to compose a macro E1--E4 receipt."
            ),
            "consequence": (
                "A passing arithmetic bundle/gate/Lambda replay is evidence for a candidate "
                "macro only; it cannot be promoted to a recursive edge from this artifact."
            ),
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    summary = result["summary"]
    if args.verify:
        assert summary["verified_receipt_occurrences"] > 0
        assert summary["high_anchor_receipt_occurrences"] > 0
        assert summary["cofactor_gate_occurrences"] == 0
        assert (
            summary["gate_size_obstruction_A_over_gcd_gt_r_occurrences"]
            + summary["gate_residue_nondivisibility_occurrences"]
            == summary["bundle_overflow_occurrences"]
        )
        assert summary["fully_closed_E1_E4_occurrences"] == 0
        print(
            "verified high-anchor parent atlas: "
            f"{summary['high_anchor_receipt_occurrences']} high parents, "
            f"{summary['lambda_paid_occurrences']} Lambda-paid arithmetic candidates"
        )
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
