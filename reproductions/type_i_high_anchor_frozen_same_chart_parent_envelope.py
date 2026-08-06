#!/usr/bin/env python3
"""Wrap frozen same-chart high parents in a content-addressed evidence API.

The legacy selector receipt has a proved identity lift but predates the macro
parent schema.  This focused replay reconstructs exactly one normal-form
family, ``overflow_same_chart_support_promotion_v1``, from the immutable
selector artifact.  It deliberately assigns a *frozen-artifact* scope, rather
than pretending to recover an unrecorded live selector tree.  Its fiber is the
already-recorded global marking ``Sol(p)``; a local F/G/hit classification is
explicitly left for a separate reclassification proof.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Iterator

import type_i_high_r_chart_two_anchor as shared


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reproductions" / "type-i-representation-dual-capacity-selector-results.json"
DEFAULT_OUTPUT = (
    ROOT / "reproductions" / "type-i-high-anchor-frozen-same-chart-parent-envelope-results.json"
)

NORMAL_FORM = "overflow_same_chart_support_promotion_v1"
ADAPTER = "frozen_same_chart_parent_envelope_v1"
ADAPTER_VERSION = 2
IDENTITY_LIFT = {"source": "Sol(p)", "successor": "Sol(p)", "lift": "identity"}
EXPECTED_HIGH_PARENT_FAMILY_COUNTS = {
    "overflow_fixed_n_bounded_divisor_outer_rank_v1": 12,
    "overflow_fixed_n_outer_rank_reset_v1": 6,
    "overflow_fixed_s_bounded_divisor_outer_rank_v1": 10,
    "overflow_fixed_s_outer_rank_reset_v1": 7,
    "overflow_outer_rank_reset_v1": 5,
    NORMAL_FORM: 11,
}


def canonical_hash(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode(
            "ascii"
        )
    ).hexdigest()


def expected_legacy_edge_id(receipt: dict[str, object]) -> str:
    return "edge:" + canonical_hash(
        {"source": receipt["source_state"], "successor": receipt["successor_state"]}
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


def high_canonical_anchor(prime: int, state: dict[str, object]) -> bool:
    R, K, A = (int(state["R"]), int(state["K"]), int(state["absorbed_support"]))
    return bool(
        shared.is_prime(prime)
        and prime % 24 == 1
        and A > 0
        and K % A == 0
        and prime * R + 1 == 4 * K
        and shared.canonical_chart(prime, A) == (R, K)
        and prime < R < 4 * A
        and R % prime != 0
        and state.get("state_class") == "overflow"
    )


def strict_verified_parent_receipt(receipt: dict[str, object]) -> bool:
    """Use the parent-atlas definition, not merely a numerically high successor."""
    return bool(
        receipt.get("selector_status") == "verified_edge"
        and receipt.get("recursive_edge_eligible") is True
        and receipt.get("e1_e5") == {f"E{index}": True for index in range(1, 6)}
        and receipt.get("marked_solution_set") == IDENTITY_LIFT
    )


def recover_parent(receipt: dict[str, object], artifact_sha256: str) -> dict[str, object]:
    """Recompute the legacy same-chart edge and seal it into a finite scope."""
    source = receipt.get("source_state")
    successor = receipt.get("successor_state")
    context = receipt.get("certificate_context")
    if not all(isinstance(value, dict) for value in (source, successor, context)):
        raise AssertionError("legacy same-chart receipt shape changed")
    source = source
    successor = successor
    context = context
    equation = source.get("equation_target")
    determinant = context.get("determinant")
    if not (
        isinstance(equation, list)
        and len(equation) == 2
        and equation[0] == 4
        and isinstance(equation[1], int)
        and isinstance(determinant, dict)
    ):
        raise AssertionError("legacy same-chart equation or determinant is absent")
    prime = int(equation[1])
    A = int(source["absorbed_support"])
    M = int(successor["absorbed_support"])
    R = int(successor["R"])
    K = int(successor["K"])
    d = int(determinant["d"])
    n = int(determinant["pn"]) // prime
    B_p = (prime - 1) ** 2 // 4
    expected_source = {
        "equation_target": [4, prime],
        "R": R,
        "K": K,
        "absorbed_support": A,
        "state_class": "overflow",
    }
    expected_successor = {
        "equation_target": [4, prime],
        "R": R,
        "K": K,
        "absorbed_support": M,
        "state_class": "overflow",
    }
    checks = {
        "family_and_legacy_edge": bool(
            receipt.get("certificate_type") == "overflow_same_chart_support_promotion"
            and receipt.get("normal_form") == NORMAL_FORM
            and receipt.get("edge_id") == expected_legacy_edge_id(receipt)
            and receipt.get("selector_status") == "verified_edge"
            and receipt.get("recursive_edge_eligible") is True
            and receipt.get("e1_e5") == {f"E{i}": True for i in range(1, 6)}
        ),
        "source_and_successor_exact": source == expected_source and successor == expected_successor,
        "determinant": bool(
            int(determinant["M"]) == M
            and int(determinant["R_M"]) == R
            and int(determinant["K_M"]) == K
            and prime * n == int(determinant["pn"])
            and prime * n == int(determinant["four_M_d_plus_1"])
            and prime * n == 4 * M * d + 1
            and R == 4 * M - n
            and K == M * (prime - d)
        ),
        "canonical_same_chart_promotion": bool(
            0 < A < M <= B_p
            and M % A == 0
            and M // A >= 2
            and K % M == 0
            and shared.canonical_chart(prime, M) == (R, K)
            and B_p // M < B_p // A
        ),
        "global_marking": bool(
            receipt.get("marked_solution_set") == IDENTITY_LIFT
            and receipt.get("lift_status") == "proved_identity"
            and receipt.get("signed_defect", {}).get("status") == "not_applicable"
            and receipt.get("target_fiber", {}).get("status") == "inherited_full_solution_set"
        ),
        "high_canonical_successor": high_canonical_anchor(prime, successor),
    }
    if not all(checks.values()):
        raise AssertionError("same-chart parent replay failed")

    scope = f"frozen_selector_artifact_sha256:{artifact_sha256}"
    fiber = {
        "kind": "global_solution_marking",
        "status": "inherited_full_solution_set",
        "marking": "Sol(p)",
        "identity_lift": IDENTITY_LIFT,
        "legacy_target_fiber": receipt["target_fiber"],
        "local_chart_classification": "unclassified",
        "reclassification_required": True,
    }
    wrapped_source = shared.make_state(
        prime=prime,
        R=R,
        K=K,
        support=A,
        state_class="overflow",
        fiber_class="global_solution_marking",
        source_tree_scope=scope,
    )
    wrapped_successor = shared.make_state(
        prime=prime,
        R=R,
        K=K,
        support=M,
        state_class="overflow",
        fiber_class="global_solution_marking",
        source_tree_scope=scope,
    )
    wrapper = {
        "certificate_type": "frozen_same_chart_parent_envelope",
        "normal_form_replay_adapter": ADAPTER,
        "adapter_version": ADAPTER_VERSION,
        "selector_status": "analysis_evidence",
        "recursive_edge_eligible": False,
        "parent_api_status": "verified_frozen_envelope",
        "scope_semantics": (
            "Finite content-addressed evidence namespace only; this does not recover or "
            "assert a live global selector-tree origin."
        ),
        "source_state": wrapped_source,
        "successor_state": wrapped_successor,
        "fiber_certificate": fiber,
        "marked_solution_set": IDENTITY_LIFT,
        "checks": checks,
        "legacy_binding": {
            "artifact_sha256": artifact_sha256,
            "legacy_receipt_digest": canonical_hash(receipt),
            "legacy_edge_id": receipt["edge_id"],
            "legacy_normal_form": NORMAL_FORM,
            "receipt_replayed_from_artifact": True,
        },
        "macro_boundary": {
            "parent_chain_content_addressed_in_frozen_scope": True,
            "local_H_S_T_FG_reclassification": "not_carried",
            "terminal_or_alternate_first_menu": "not_carried",
            "global_selector_registration": "not_attempted",
        },
    }
    wrapper["edge_id"] = "edge:" + canonical_hash(
        {
            "adapter": ADAPTER,
            "legacy_binding": wrapper["legacy_binding"],
            "source": wrapped_source,
            "successor": wrapped_successor,
        }
    )
    return wrapper


def frozen_receipt_index(
    receipts: list[dict[str, object]],
) -> dict[str, dict[str, object]]:
    """Index immutable receipts by their canonical content digest."""
    index: dict[str, dict[str, object]] = {}
    for receipt in receipts:
        digest = canonical_hash(receipt)
        previous = index.setdefault(digest, receipt)
        if previous != receipt:
            raise AssertionError("content digest collision in frozen selector artifact")
    return index


def verify_envelope(
    wrapper: dict[str, object],
    *,
    receipts_by_digest: dict[str, dict[str, object]],
    artifact_sha256: str,
) -> bool:
    """Verify the wrapper against the immutable legacy receipt, not only itself."""
    source = wrapper.get("source_state")
    successor = wrapper.get("successor_state")
    fiber = wrapper.get("fiber_certificate")
    binding = wrapper.get("legacy_binding")
    checks = wrapper.get("checks")
    if not all(isinstance(value, dict) for value in (source, successor, fiber, binding, checks)):
        return False
    digest = binding.get("legacy_receipt_digest")
    if not isinstance(digest, str):
        return False
    legacy_receipt = receipts_by_digest.get(digest)
    scope = f"frozen_selector_artifact_sha256:{artifact_sha256}"
    if not (
        binding.get("artifact_sha256") == artifact_sha256
        and binding.get("receipt_replayed_from_artifact") is True
        and isinstance(legacy_receipt, dict)
        and canonical_hash(legacy_receipt) == digest
        and source.get("source_tree_scope") == scope
        and successor.get("source_tree_scope") == scope
    ):
        return False
    try:
        expected = recover_parent(legacy_receipt, artifact_sha256)
    except (AssertionError, KeyError, TypeError, ValueError):
        return False
    return wrapper == expected


def build_result() -> dict[str, object]:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    artifact_sha256 = hashlib.sha256(INPUT.read_bytes()).hexdigest()
    all_receipts = list(iter_verified_receipts(payload))
    receipts_by_digest = frozen_receipt_index(all_receipts)
    high_parent_receipts = []
    for receipt in all_receipts:
        if not strict_verified_parent_receipt(receipt):
            continue
        state = receipt["successor_state"]
        equation = state.get("equation_target")
        if isinstance(equation, list) and len(equation) == 2 and equation[0] == 4:
            if high_canonical_anchor(int(equation[1]), state):
                high_parent_receipts.append(receipt)
    high_parent_counts = Counter(str(receipt.get("normal_form")) for receipt in high_parent_receipts)
    if dict(sorted(high_parent_counts.items())) != EXPECTED_HIGH_PARENT_FAMILY_COUNTS:
        raise AssertionError("frozen high-parent family inventory changed")
    family_receipts = [
        receipt
        for receipt in all_receipts
        if strict_verified_parent_receipt(receipt)
        and receipt.get("normal_form") == NORMAL_FORM
        and receipt.get("certificate_type") == "overflow_same_chart_support_promotion"
    ]
    high_receipts = []
    for receipt in family_receipts:
        state = receipt["successor_state"]
        equation = state.get("equation_target")
        if isinstance(equation, list) and len(equation) == 2 and equation[0] == 4:
            if high_canonical_anchor(int(equation[1]), state):
                high_receipts.append(receipt)
    envelopes = [recover_parent(receipt, artifact_sha256) for receipt in high_receipts]
    return {
        "schema_version": 2,
        "certificate_type": "type_i_high_anchor_frozen_same_chart_parent_envelope_atlas_v1",
        "input": {
            "path": str(INPUT.relative_to(ROOT)),
            "sha256": artifact_sha256,
        },
        "scope": (
            "One-family read-only reconstruction of frozen same-chart verified parents. "
            "It neither runs the selector nor converts envelopes into selector edges."
        ),
        "six_family_audit": {
            "high_parent_occurrences_by_normal_form": dict(sorted(high_parent_counts.items())),
            "total_strict_high_parent_occurrences": len(high_parent_receipts),
            "selected_family_adapter_additions": [
                "content_addressed_state_ids_in_frozen_scope",
                "legacy_receipt_digest_bound_to_input_artifact",
                "named_replay_adapter_and_checks_for_same_chart_family",
            ],
            "macro_information_not_added_by_this_adapter": [
                "local_H_S_T_FG_or_hit_reclassification",
                "terminal_or_alternate_first_menu",
            ],
            "selected_family_reason": (
                "The same-chart family has no hidden branch choice after its receipt is fixed: "
                "the exact source/successor chart, M/A>=2, determinant, canonicality, and "
                "absorbed-support rank are all recomputable from the receipt itself."
            ),
            "full_macro_no_go_from_legacy_alone": (
                "This one-family adapter does not add local F/G/hit certificates for H, S, "
                "and T or a terminal-first result. A global Sol(p) identity marking does not "
                "substitute for those missing local proofs."
            ),
        },
        "summary": {
            "family_verified_receipt_occurrences": len(family_receipts),
            "strict_high_anchor_occurrences": len(high_receipts),
            "verified_frozen_parent_envelopes": sum(
                verify_envelope(
                    row,
                    receipts_by_digest=receipts_by_digest,
                    artifact_sha256=artifact_sha256,
                )
                for row in envelopes
            ),
            "selector_edges_registered": 0,
            "full_macro_E4_certificates_constructed": 0,
        },
        "envelopes": envelopes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = build_result()
    summary = result["summary"]
    if args.verify:
        payload = json.loads(INPUT.read_text(encoding="utf-8"))
        artifact_sha256 = hashlib.sha256(INPUT.read_bytes()).hexdigest()
        receipts_by_digest = frozen_receipt_index(list(iter_verified_receipts(payload)))
        assert summary["strict_high_anchor_occurrences"] == 11
        assert summary["verified_frozen_parent_envelopes"] == 11
        assert summary["selector_edges_registered"] == 0
        assert summary["full_macro_E4_certificates_constructed"] == 0
        tampered = copy.deepcopy(result["envelopes"][0])
        tampered["successor_state"]["absorbed_support"] = 1
        assert not verify_envelope(
            tampered,
            receipts_by_digest=receipts_by_digest,
            artifact_sha256=artifact_sha256,
        )
        print("verified 11 frozen same-chart parent envelopes; no selector edge registered")
        return
    args.output.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
