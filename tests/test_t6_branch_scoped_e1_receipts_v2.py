from __future__ import annotations

import copy
from dataclasses import fields
import hashlib
import json
from pathlib import Path
import sys
import unittest

from jsonschema import Draft202012Validator, ValidationError


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import t6_branch_scoped_e1_receipts_v2 as receipts  # noqa: E402


SCHEMA = json.loads(
    (ROOT / "schemas/t6-branch-scoped-e1-receipts-v2.schema.json").read_text(
        encoding="ascii"
    )
)


def digest(label: str) -> str:
    return hashlib.sha256(label.encode("ascii")).hexdigest()


def seal(payload: dict[str, object]) -> dict[str, object]:
    result = copy.deepcopy(payload)
    result.pop("digest", None)
    result["digest"] = receipts.canonical_digest_v2(result)
    return result


def reseal_receipt(
    wire: dict[str, object], prefix: str
) -> dict[str, object]:
    result = copy.deepcopy(wire)
    result.pop("receipt_id", None)
    result.pop("digest", None)
    result_digest = receipts.canonical_digest_v2(result)
    result["receipt_id"] = prefix + result_digest
    result["digest"] = result_digest
    return result


def terminal_decision(index: int, label: str) -> dict[str, object]:
    return {
        "decision_index": index,
        "decision_id": f"decision:{label}",
        "decision_kind": "TERMINAL",
        "decision_contract_digest": digest(f"decision-contract:{label}"),
        "producer_id": None,
        "producer_digest": None,
        "branch_id": None,
        "branch_contract_digest": None,
        "expected_occurrence_path": None,
        "expected_occurrence_path_digest": None,
    }


def producer_decision(
    index: int, label: str, occurrence_path: list[str | int]
) -> dict[str, object]:
    return {
        "decision_index": index,
        "decision_id": f"decision:{label}",
        "decision_kind": "PRODUCER",
        "decision_contract_digest": digest(f"decision-contract:{label}"),
        "producer_id": f"producer:{label}",
        "producer_digest": digest(f"producer:{label}"),
        "branch_id": f"branch:{label}",
        "branch_contract_digest": digest(f"branch-contract:{label}"),
        "expected_occurrence_path": occurrence_path,
        "expected_occurrence_path_digest": receipts.canonical_digest_v2(
            occurrence_path
        ),
    }


class BranchScopedE1ReceiptV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Draft202012Validator.check_schema(SCHEMA)
        cls.validator = Draft202012Validator(SCHEMA)

    def setUp(self) -> None:
        body: dict[str, object] = {
            "state_kind": "persistent-source-v2",
            "prime": 1_201,
            "payload": {
                "occurrences": [31, 47],
                "derived": {"candidate": 59},
                "bool_occurrence": True,
                "text_occurrence": "47",
            },
        }
        self.source: dict[str, object] = {
            "state_id": "state:" + receipts.canonical_digest_v2(body),
            **body,
        }
        self.source_digest = receipts.canonical_digest_v2(self.source)
        self.decisions = [
            terminal_decision(0, "terminal-low"),
            producer_decision(
                1, "earlier-producer", ["payload", "occurrences", 0]
            ),
            producer_decision(
                2, "selected-producer", ["payload", "occurrences", 1]
            ),
        ]
        self.policy = seal(
            {
                "policy_type": "BranchDecisionPolicyV2",
                "schema_version": 2,
                "head_sha": "1" * 40,
                "head_tree_sha": "2" * 40,
                "source_state_id": self.source["state_id"],
                "source_state_digest": self.source_digest,
                "source_owner_id": "owner:q1-g",
                "source_owner_digest": digest("owner:q1-g"),
                "owner_domain_id": "domain:q1-g",
                "owner_domain_digest": digest("domain:q1-g"),
                "coordinator_route_registry_id": "registry:t6-routes-v2",
                "coordinator_route_registry_version": 2,
                "coordinator_route_registry_digest": digest("route-registry-v2"),
                "policy_id": "policy:q1-g-v2",
                "policy_version": 2,
                "decisions": self.decisions,
                "global_exhaustion": False,
            }
        )
        self.prior = [
            self._prior_replay(self.decisions[0], "TERMINAL_MISS", "terminal"),
            self._prior_replay(self.decisions[1], "GUARD_FALSE", "producer"),
        ]
        self.guard = self._guard_replay()
        self.selection = receipts.make_branch_selection_receipt_v2(
            self.policy, self.prior, self.guard
        )
        self.lineage = self._lineage()
        self.e1 = receipts.make_e1_occurrence_receipt_v2(
            self.source,
            ["payload", "occurrences", 1],
            self.lineage,
            self.selection,
        )
        self.replay_evidence = self._independent_evidence(self.e1)
        self.independent = receipts.make_e1_independent_replay_receipt_v2(
            self.selection, self.e1, self.replay_evidence
        )

    def _prior_replay(
        self,
        decision: dict[str, object],
        outcome: str,
        suffix: str,
    ) -> dict[str, object]:
        return seal(
            {
                "evidence_type": "PriorDecisionReplayEvidenceV2",
                "schema_version": 2,
                "source_state_id": self.source["state_id"],
                "source_state_digest": self.source_digest,
                "policy_id": self.policy["policy_id"],
                "policy_version": self.policy["policy_version"],
                "policy_digest": self.policy["digest"],
                "decision_id": decision["decision_id"],
                "decision_index": decision["decision_index"],
                "decision_kind": decision["decision_kind"],
                "decision_contract_digest": decision["decision_contract_digest"],
                "producer_id": decision["producer_id"],
                "producer_digest": decision["producer_digest"],
                "branch_id": decision["branch_id"],
                "branch_contract_digest": decision["branch_contract_digest"],
                "expected_occurrence_path": decision[
                    "expected_occurrence_path"
                ],
                "expected_occurrence_path_digest": decision[
                    "expected_occurrence_path_digest"
                ],
                "replay_outcome": outcome,
                "replay_result_digest": digest(f"prior-result:{suffix}"),
                "replayer_id": f"prior-replayer:{suffix}",
                "replayer_digest": digest(f"prior-replayer:{suffix}"),
                "replay_complete": True,
                "authority": False,
            }
        )

    def _guard_replay(self) -> dict[str, object]:
        selected = self.decisions[2]
        return seal(
            {
                "evidence_type": "SelectedBranchGuardReplayEvidenceV2",
                "schema_version": 2,
                "source_state_id": self.source["state_id"],
                "source_state_digest": self.source_digest,
                "policy_id": self.policy["policy_id"],
                "policy_version": self.policy["policy_version"],
                "policy_digest": self.policy["digest"],
                "selected_decision_id": selected["decision_id"],
                "selected_decision_contract_digest": selected[
                    "decision_contract_digest"
                ],
                "producer_id": selected["producer_id"],
                "producer_digest": selected["producer_digest"],
                "selected_branch_id": selected["branch_id"],
                "selected_branch_index": selected["decision_index"],
                "selected_branch_contract_digest": selected[
                    "branch_contract_digest"
                ],
                "expected_occurrence_path": selected[
                    "expected_occurrence_path"
                ],
                "expected_occurrence_path_digest": selected[
                    "expected_occurrence_path_digest"
                ],
                "branch_guard_id": "guard:selected-producer",
                "branch_guard_digest": digest("guard:selected-producer"),
                "branch_guard_result_digest": digest("guard-result:true"),
                "branch_guard_result": True,
                "replayer_id": "guard-replayer:selected",
                "replayer_digest": digest("guard-replayer:selected"),
                "replay_complete": True,
                "authority": False,
            }
        )

    def _lineage(self, **updates: object) -> dict[str, object]:
        selected = self.decisions[2]
        payload: dict[str, object] = {
            "evidence_type": "SourceLineageReplayEvidenceV2",
            "schema_version": 2,
            "head_sha": self.policy["head_sha"],
            "head_tree_sha": self.policy["head_tree_sha"],
            "signed_gate0_manifest_digest": digest("gate0-manifest"),
            "external_trust_anchor_digest": digest("external-anchor"),
            "authority_policy_digest": digest("external-authority-policy"),
            "policy_id": self.policy["policy_id"],
            "policy_version": self.policy["policy_version"],
            "policy_digest": self.policy["digest"],
            "coordinator_registry_id": self.policy[
                "coordinator_route_registry_id"
            ],
            "coordinator_registry_version": self.policy[
                "coordinator_route_registry_version"
            ],
            "coordinator_registry_digest": self.policy[
                "coordinator_route_registry_digest"
            ],
            "role_grant_id": "grant:lineage-role",
            "role_grant_digest": digest("grant:lineage-role"),
            "issuer_id": "issuer:lineage",
            "issuer_digest": digest("issuer:lineage"),
            "issuer_grant_id": "grant:issuer",
            "issuer_grant_digest": digest("grant:issuer"),
            "independent_verifier_id": "verifier:independent",
            "independent_verifier_digest": digest("verifier:independent"),
            "claim_id": "claim:q1-source",
            "claim_version": 1,
            "claim_digest": digest("claim:q1-source"),
            "reproduction_id": "reproduction:q1-source",
            "reproduction_digest": digest("reproduction:q1-source"),
            "source_schema_id": "schema:persistent-source-v2",
            "source_schema_version": 2,
            "source_state_id": self.source["state_id"],
            "source_state_wire_digest": self.source_digest,
            "source_owner_id": self.policy["source_owner_id"],
            "source_owner_digest": self.policy["source_owner_digest"],
            "source_base_admission_receipt_id": "admission:source-base",
            "source_base_admission_receipt_digest": digest("admission:source-base"),
            "parent_kind": "TYPEII_G_HANDOFF",
            "parent_id": "parent:q1-g",
            "parent_digest": digest("parent:q1-g"),
            "parent_replay_digest": digest("parent-replay:q1-g"),
            "e1_scope_kind": "BRANCH_SCOPED",
            "e1_scope_id": "scope:q1-phase-root",
            "e1_scope_digest": digest("scope:q1-phase-root"),
            "route_decision_id": selected["decision_id"],
            "route_decision_index": selected["decision_index"],
            "route_decision_contract_digest": selected[
                "decision_contract_digest"
            ],
            "expected_occurrence_path": selected["expected_occurrence_path"],
            "expected_occurrence_path_digest": selected[
                "expected_occurrence_path_digest"
            ],
            "producer_id": selected["producer_id"],
            "producer_digest": selected["producer_digest"],
            "branch_id": selected["branch_id"],
            "branch_contract_digest": selected["branch_contract_digest"],
            "source_domain_id": self.policy["owner_domain_id"],
            "source_domain_digest": self.policy["owner_domain_digest"],
            "domain_membership_replay_digest": digest("domain-membership"),
            "branch_guard_id": self.guard["branch_guard_id"],
            "branch_guard_digest": self.guard["branch_guard_digest"],
            "branch_guard_result_digest": self.guard["branch_guard_result_digest"],
            "occurrence_namespace": "PERSISTENT_SOURCE_STATE_WIRE",
            "provenance_digest": digest("source-provenance"),
            "source_lineage_replayer_id": "replayer:lineage",
            "source_lineage_replayer_digest": digest("replayer:lineage"),
            "source_lineage_replay_result_digest": digest("lineage-result:pass"),
            "source_lineage_replay_result": "PASS",
            "authority": False,
        }
        payload.update(updates)
        return seal(payload)

    def _independent_evidence(
        self,
        e1: receipts.E1OccurrenceReceiptV2,
        **updates: object,
    ) -> dict[str, object]:
        payload: dict[str, object] = {
            "evidence_type": "E1IndependentReplayEvidenceInputV2",
            "schema_version": 2,
            "source_state_id": e1.source_state_id,
            "source_state_digest": e1.source_state_wire_digest,
            "selection_receipt_id": self.selection.receipt_id,
            "selection_receipt_digest": self.selection.digest,
            "e1_occurrence_receipt_id": e1.receipt_id,
            "e1_occurrence_receipt_digest": e1.digest,
            "replayer_id": e1.independent_verifier_id,
            "replayer_digest": e1.independent_verifier_digest,
            "selection_replay_result": "PASS",
            "occurrence_replay_result": "PASS",
            "source_lineage_replay_result": "PASS",
            "upstream_revalidation_complete": True,
            "evidence_only": True,
            "authority": False,
        }
        payload.update(updates)
        return seal(payload)

    def assert_rejected(
        self,
        code: receipts.BranchScopedE1RejectCode,
        callable_,
    ) -> None:
        with self.assertRaises(receipts.BranchScopedE1ValidationError) as raised:
            callable_()
        self.assertEqual(raised.exception.code, code)

    def test_three_receipts_roundtrip_and_match_schema(self) -> None:
        cases = (
            (self.selection, receipts.BranchSelectionReceiptV2),
            (self.e1, receipts.E1OccurrenceReceiptV2),
            (self.independent, receipts.E1IndependentReplayReceiptV2),
        )
        for receipt, expected_type in cases:
            with self.subTest(receipt_type=expected_type.__name__):
                wire = receipts.receipt_to_mapping_v2(receipt)
                self.validator.validate(wire)
                parsed = receipts.parse_receipt_json_v2(
                    receipts.receipt_to_json_v2(receipt)
                )
                self.assertIs(type(parsed), expected_type)
                self.assertEqual(receipts.receipt_to_mapping_v2(parsed), wire)
                self.assertEqual(receipt.receipt_id, expected_type.ID_PREFIX + receipt.digest)
                for name in (
                    "authority",
                    "e1_authority",
                    "producer_authority",
                    "admission_authority",
                    "persistent_admission",
                    "queue_authority",
                    "enqueue_authority",
                    "goal_gate2_e1_authority",
                    "complete_terminal_schedule_authority",
                    "goal_gate4_authority",
                    "goal_gate5_authority",
                    "global_exhaustion",
                    "universe_miss_authority",
                ):
                    self.assertFalse(wire[name], name)
                self.assertEqual(
                    wire["clearance_outcome"],
                    "MISS_HIGHER_PRIORITY_POLICY_COMPLETE",
                )
                self.assertEqual(
                    wire["terminal_universe_status"], "NOT_ASSERTED_NOT_REQUIRED"
                )
        self.assertNotEqual(
            self.e1.authority_policy_digest,
            self.e1.policy_digest,
        )
        self.assertEqual(
            self.e1.consumption_evidence_status,
            "STRUCTURAL_BINDING_ONLY_NO_INDEPENDENT_CONSUMPTION_EVIDENCE",
        )

    def test_receipt_classes_are_factory_only_and_slotted(self) -> None:
        for receipt_type, receipt in (
            (receipts.BranchSelectionReceiptV2, self.selection),
            (receipts.E1OccurrenceReceiptV2, self.e1),
            (receipts.E1IndependentReplayReceiptV2, self.independent),
        ):
            with self.subTest(receipt_type=receipt_type.__name__):
                with self.assertRaises(TypeError):
                    receipt_type()
                self.assertFalse(hasattr(receipt, "__dict__"))
                self.assertNotIn(
                    "__dict__", {field.name for field in fields(receipt_type)}
                )

    def test_v1_casts_and_downcast_claims_are_rejected(self) -> None:
        for old_type in (
            "E1OccurrenceReceiptV1",
            "BranchSelectionReceiptV1",
            "E1IndependentReplayReceiptV1",
        ):
            self.assert_rejected(
                receipts.BranchScopedE1RejectCode.V1_INCOMPATIBLE,
                lambda old_type=old_type: receipts.parse_receipt_v2(
                    {"receipt_type": old_type}
                ),
            )
        for field_name in ("v1_compatible", "v1_downcast_authority"):
            wire = receipts.receipt_to_mapping_v2(self.selection)
            wire[field_name] = True
            wire = reseal_receipt(wire, receipts.BranchSelectionReceiptV2.ID_PREFIX)
            self.assert_rejected(
                receipts.BranchScopedE1RejectCode.DIGEST_MISMATCH,
                lambda wire=wire: receipts.parse_branch_selection_receipt_v2(wire),
            )

    def test_global_miss_relabels_and_global_policy_are_rejected(self) -> None:
        for field_name, bad_value in (
            ("clearance_outcome", "MISS_COMPLETE"),
            ("terminal_universe_status", "MISS_COMPLETE"),
            ("global_exhaustion", True),
            ("universe_miss_authority", True),
        ):
            wire = receipts.receipt_to_mapping_v2(self.selection)
            wire[field_name] = bad_value
            wire = reseal_receipt(wire, receipts.BranchSelectionReceiptV2.ID_PREFIX)
            self.assert_rejected(
                receipts.BranchScopedE1RejectCode.DIGEST_MISMATCH,
                lambda wire=wire: receipts.parse_branch_selection_receipt_v2(wire),
            )

        global_policy = copy.deepcopy(self.policy)
        global_policy["global_exhaustion"] = True
        global_policy = seal(global_policy)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.AUTHORITY_BOUNDARY_VIOLATION,
            lambda: receipts.make_branch_selection_receipt_v2(
                global_policy, self.prior, self.guard
            ),
        )

    def test_prior_prefix_omission_swap_and_kind_outcome_mismatch_fail(self) -> None:
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.PRIOR_DECISION_GAP,
            lambda: receipts.make_branch_selection_receipt_v2(
                self.policy, self.prior[:1], self.guard
            ),
        )
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.PRIOR_REPLAY_MISMATCH,
            lambda: receipts.make_branch_selection_receipt_v2(
                self.policy, list(reversed(self.prior)), self.guard
            ),
        )
        bad_outcome = copy.deepcopy(self.prior[0])
        bad_outcome["replay_outcome"] = "GUARD_FALSE"
        bad_outcome = seal(bad_outcome)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.PRIOR_REPLAY_MISMATCH,
            lambda: receipts.make_branch_selection_receipt_v2(
                self.policy, [bad_outcome, self.prior[1]], self.guard
            ),
        )

    def test_duplicate_producer_action_key_is_rejected(self) -> None:
        duplicate = copy.deepcopy(self.decisions[1])
        duplicate["decision_index"] = 2
        duplicate["decision_id"] = "decision:duplicate-action-slot"
        policy = copy.deepcopy(self.policy)
        policy["decisions"] = [
            copy.deepcopy(self.decisions[0]),
            copy.deepcopy(self.decisions[1]),
            duplicate,
        ]
        policy = seal(policy)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.POLICY_BINDING_MISMATCH,
            lambda: receipts.make_branch_selection_receipt_v2(
                policy, self.prior, self.guard
            ),
        )

    def test_route_producer_branch_source_and_policy_swaps_fail_closed(self) -> None:
        cases = (
            ("route_decision_id", "decision:other-route"),
            ("producer_id", "producer:other"),
            ("branch_id", "branch:other"),
            ("source_state_id", "state:other"),
            ("policy_id", "policy:other"),
        )
        for field_name, bad_value in cases:
            with self.subTest(field=field_name):
                lineage = self._lineage(**{field_name: bad_value})
                with self.assertRaises(receipts.BranchScopedE1ValidationError) as raised:
                    receipts.make_e1_occurrence_receipt_v2(
                        self.source,
                        ["payload", "occurrences", 1],
                        lineage,
                        self.selection,
                    )
                self.assertIn(
                    raised.exception.code,
                    {
                        receipts.BranchScopedE1RejectCode.SOURCE_BINDING_MISMATCH,
                        receipts.BranchScopedE1RejectCode.CROSS_RECEIPT_MISMATCH,
                    },
                )

    def test_bool_and_non_integer_occurrences_are_rejected(self) -> None:
        for path in (
            ["payload", "bool_occurrence"],
            ["payload", "text_occurrence"],
        ):
            with self.subTest(path=path):
                self.assert_rejected(
                    receipts.BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
                    lambda path=path: receipts.make_e1_occurrence_receipt_v2(
                        self.source, path, self.lineage, self.selection
                    ),
                )

    def test_caller_and_lineage_path_swaps_fail_closed(self) -> None:
        other_path = ["payload", "occurrences", 0]
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
            lambda: receipts.make_e1_occurrence_receipt_v2(
                self.source, other_path, self.lineage, self.selection
            ),
        )

        swapped_lineage = self._lineage(
            expected_occurrence_path=other_path,
            expected_occurrence_path_digest=receipts.canonical_digest_v2(
                other_path
            ),
        )
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.CROSS_RECEIPT_MISMATCH,
            lambda: receipts.make_e1_occurrence_receipt_v2(
                self.source,
                ["payload", "occurrences", 1],
                swapped_lineage,
                self.selection,
            ),
        )

    def test_derived_path_or_occurrence_value_cannot_relabel_a_sealed_occurrence(self) -> None:
        wire = receipts.receipt_to_mapping_v2(self.e1)
        wire["occurrence_path"] = ["payload", "derived", "candidate"]
        wire = reseal_receipt(wire, receipts.E1OccurrenceReceiptV2.ID_PREFIX)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.OCCURRENCE_REPLAY_FAILED,
            lambda: receipts.parse_e1_occurrence_receipt_v2(wire),
        )

        wire = receipts.receipt_to_mapping_v2(self.e1)
        wire["occurrence_value"] = 59
        wire["occurrence_value_digest"] = receipts.canonical_digest_v2(59)
        wire = reseal_receipt(wire, receipts.E1OccurrenceReceiptV2.ID_PREFIX)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.DIGEST_MISMATCH,
            lambda: receipts.parse_e1_occurrence_receipt_v2(wire),
        )

    def test_independent_replayer_id_and_digest_reuse_fail_closed(self) -> None:
        reused_id_lineage = self._lineage(
            independent_verifier_id=self.guard["replayer_id"]
        )
        reused_id_e1 = receipts.make_e1_occurrence_receipt_v2(
            self.source,
            ["payload", "occurrences", 1],
            reused_id_lineage,
            self.selection,
        )
        reused_id_evidence = self._independent_evidence(reused_id_e1)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            lambda: receipts.make_e1_independent_replay_receipt_v2(
                self.selection, reused_id_e1, reused_id_evidence
            ),
        )

        reused_digest_lineage = self._lineage(
            independent_verifier_digest=self.selection.selected_producer_digest
        )
        reused_digest_e1 = receipts.make_e1_occurrence_receipt_v2(
            self.source,
            ["payload", "occurrences", 1],
            reused_digest_lineage,
            self.selection,
        )
        reused_digest_evidence = self._independent_evidence(reused_digest_e1)
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.REPLAY_EVIDENCE_MISMATCH,
            lambda: receipts.make_e1_independent_replay_receipt_v2(
                self.selection, reused_digest_e1, reused_digest_evidence
            ),
        )

    def test_reseal_cannot_grant_authority_and_extra_authority_is_rejected(self) -> None:
        wire = receipts.receipt_to_mapping_v2(self.independent)
        wire["authority"] = True
        wire = reseal_receipt(
            wire, receipts.E1IndependentReplayReceiptV2.ID_PREFIX
        )
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.DIGEST_MISMATCH,
            lambda: receipts.parse_e1_independent_replay_receipt_v2(wire),
        )

        extra = receipts.receipt_to_mapping_v2(self.independent)
        extra["runtime_authority"] = True
        self.assert_rejected(
            receipts.BranchScopedE1RejectCode.FIELD_SET_MISMATCH,
            lambda: receipts.parse_e1_independent_replay_receipt_v2(extra),
        )
        with self.assertRaises(ValidationError):
            self.validator.validate(extra)


if __name__ == "__main__":
    unittest.main()
