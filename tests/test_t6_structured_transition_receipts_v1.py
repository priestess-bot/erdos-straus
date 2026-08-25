from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from dataclasses import FrozenInstanceError, fields
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "t6_structured_transition_receipts_v1",
    ROOT / "scripts" / "t6_structured_transition_receipts_v1.py",
)
assert SPEC and SPEC.loader
receipts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = receipts
SPEC.loader.exec_module(receipts)


ARTIFACT_IDS = (
    "producer.test",
    "terminal.complete.test",
    "claim.test",
    "reproduction.occurrence.test",
    "validator.independent.test",
    "projector.test",
    "tie-break.test",
    "normal-form.test",
    "precedence.test",
    "grammar.test",
    "admission.test",
    "lift-map.test",
    "symbolic-verifier.test",
    "reproduction.lift.test",
    "taxonomy.test",
)


def artifact_digest(artifact_id: str) -> str:
    return receipts.canonical_digest_v1({"artifact_id": artifact_id, "version": 1})


def seal(payload):
    result = dict(payload)
    result["digest"] = receipts.canonical_digest_v1(result)
    return result


def fixture_manifest(**overrides):
    digests = {artifact_id: artifact_digest(artifact_id) for artifact_id in ARTIFACT_IDS}
    digests.update(overrides)
    return receipts.ArtifactDigestManifestV1(digests)


def fixture_context(**overrides):
    source_state = {
        "schema_id": "t6_persistent_selector_state_v1",
        "schema_version": 1,
        "state_id": "state:source",
        "facts": {
            "occurrences": [
                {"kind": "control", "value": 17},
                {"kind": "actual", "value": 19},
            ]
        },
    }
    target_state = {
        "schema_id": "t6_persistent_selector_state_v1",
        "schema_version": 1,
        "state_id": "state:target",
        "facts": {"chart_R": 75, "chart_K": 1369},
    }
    source_potential = seal(
        {
            "schema_id": "t5_n7_potential_receipt_v1",
            "schema_version": 1,
            "state_id": "state:source",
            "coordinates": [73, 2, 4, 9, 0, 0, 0],
        }
    )
    target_potential = seal(
        {
            "schema_id": "t5_n7_potential_receipt_v1",
            "schema_version": 1,
            "state_id": "state:target",
            "coordinates": [73, 2, 4, 8, 7, 0, 0],
        }
    )
    values = {
        "source_state_id": "state:source",
        "source_state_payload": source_state,
        "parent_transition_id": receipts.ROOT_INITIALIZER,
        "parent_transition_payload": None,
        "producer_id": "producer.test",
        "branch_id": "branch.test",
        "scope": "for every admitted source in branch.test",
        "occurrence_path": ("facts", "occurrences", 1),
        "provenance_payload": {
            "source": "root initializer",
            "occurrence_kind": "actual",
        },
        "source_terminal_schedule_id": "terminal.complete.test",
        "source_terminal_result": receipts.MISS_COMPLETE,
        "source_terminal_result_payload": {
            "schedule_id": "terminal.complete.test",
            "outcome": receipts.MISS_COMPLETE,
            "coverage": "GLOBAL_COMPLETE",
        },
        "candidate_witness_payload": {"raw_word": [19, 37, 73]},
        "target_projection_payload": target_state,
        "family_predicate_results": {
            "type_i_low_support_persistent_overflow": True,
            "type_i_full_carrier_post_g": False,
        },
        "target_owner": "type_i_low_support_persistent_overflow",
        "target_owner_digest": receipts.canonical_digest_v1(
            {
                "owner": "type_i_low_support_persistent_overflow",
                "target": "state:target",
            }
        ),
        "source_equation_interface": {"rank": 73, "solution_map": "Sol(73)"},
        "target_equation_interface": {"rank": 73, "solution_map": "Sol(73)"},
        "source_potential_receipt": source_potential,
        "target_potential_receipt": target_potential,
        "universal_quantifier_statement": (
            "for every target solution, lift-map.test returns a source solution"
        ),
        "negative_mutation_ids": tuple(sorted(receipts.NEGATIVE_MUTATION_IDS)),
        "ticket_type": "LOCAL_DROP",
        "claim_id": "claim.test",
        "reproduction_id": "reproduction.occurrence.test",
        "independent_verifier_id": "validator.independent.test",
        "projector_id": "projector.test",
        "tie_break_rule_id": "tie-break.test",
        "normal_form_verifier_id": "normal-form.test",
        "precedence_table_id": "precedence.test",
        "grammar_id": "grammar.test",
        "admission_gate_id": "admission.test",
        "admission_gate_version": 1,
        "lift_map_id": "lift-map.test",
        "symbolic_verifier_id": "symbolic-verifier.test",
        "lift_reproduction_id": "reproduction.lift.test",
        "taxonomy_id": "taxonomy.test",
    }
    values.update(overrides)
    return receipts.TransitionReplayContextV1(**values)


class StructuredTransitionReceiptTests(unittest.TestCase):
    def setUp(self):
        self.context = fixture_context()
        self.manifest = fixture_manifest()
        self.bundle = receipts.make_verified_transition_bundle_v1(
            self.context, self.manifest
        )

    def test_bundle_round_trips_and_replays_all_e1_e5_bindings(self):
        serialized = receipts.receipt_to_mapping_v1(self.bundle)
        encoded = receipts.canonical_json_v1(serialized)
        replayed = receipts.verify_structured_transition_evidence_v1(
            json.loads(encoded), self.context, self.manifest
        )
        self.assertEqual(replayed.transition_id, self.bundle.transition_id)
        self.assertEqual(replayed.digest, self.bundle.digest)
        self.assertEqual(
            serialized["e1_occurrence"]["receipt_type"], "E1OccurrenceReceiptV1"
        )
        self.assertEqual(
            serialized["e5_ticket"]["comparison_scope"],
            receipts.PARENT_TO_FINAL_TARGET,
        )

    def test_canonical_serialization_is_mapping_order_independent(self):
        left = {"outer": {"b": 2, "a": 1}, "items": [3, 2, 1]}
        right = {"items": [3, 2, 1], "outer": {"a": 1, "b": 2}}
        self.assertEqual(
            receipts.canonical_json_v1(left), receipts.canonical_json_v1(right)
        )
        self.assertEqual(
            receipts.canonical_digest_v1(left), receipts.canonical_digest_v1(right)
        )

    def test_machine_schema_required_fields_match_the_dataclasses(self):
        schema_path = ROOT / "schemas" / "t6-structured-transition-receipts-v1.schema.json"
        schema = json.loads(schema_path.read_text(encoding="ascii"))
        for receipt_class in (
            receipts.E1OccurrenceReceiptV1,
            receipts.E2ProjectionReceiptV1,
            receipts.E3TypingReceiptV1,
            receipts.E4LiftReceiptV1,
            receipts.E5TicketReceiptV1,
            receipts.VerifiedTransitionBundleV1,
        ):
            with self.subTest(receipt_type=receipt_class.RECEIPT_TYPE):
                required = set(schema["$defs"][receipt_class.RECEIPT_TYPE]["required"])
                expected = {field.name for field in fields(receipt_class)} | {
                    "receipt_type",
                    "schema_version",
                }
                self.assertEqual(required, expected)

    def test_legacy_boolean_validation_is_audited_and_rejected(self):
        legacy = {
            "source_state_id": "state:source",
            "producer_id": "producer.test",
            "branch_id": "branch.test",
            "projection_digest": "unbound",
            "E1": True,
            "E2": True,
            "E3_pre_admission": True,
            "E4": True,
            "evidence_ids": ("claim:test",),
        }
        weaknesses = receipts.legacy_transition_validation_weaknesses_v1(legacy)
        self.assertIn("BOOLEAN_E1_E4_NOT_REPLAYABLE", weaknesses)
        self.assertIn("NO_PARENT_TO_FINAL_E5_RECEIPT", weaknesses)
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.verify_structured_transition_evidence_v1(
                legacy, self.context, self.manifest
            )
        self.assertEqual(
            raised.exception.code, receipts.ReceiptRejectCode.LEGACY_BOOLEAN_VALIDATION
        )

    def test_all_named_mutations_fail_after_attacker_reseals_hashes(self):
        for mutation_id in sorted(receipts.NEGATIVE_MUTATION_IDS):
            with self.subTest(mutation_id=mutation_id):
                mutated = receipts.apply_negative_mutation_v1(
                    self.bundle, mutation_id
                )
                with self.assertRaises(receipts.ReceiptValidationError):
                    receipts.verify_verified_transition_bundle_v1(
                        mutated, self.context, self.manifest
                    )

    def test_artifact_hash_drift_invalidates_an_old_bundle(self):
        for artifact_id in (
            "claim.test",
            "reproduction.occurrence.test",
            "validator.independent.test",
            "projector.test",
            "grammar.test",
            "taxonomy.test",
        ):
            with self.subTest(artifact_id=artifact_id):
                drifted = fixture_manifest(
                    **{
                        artifact_id: receipts.canonical_digest_v1(
                            {"artifact_id": artifact_id, "version": 2}
                        )
                    }
                )
                with self.assertRaises(receipts.ReceiptValidationError) as raised:
                    receipts.verify_verified_transition_bundle_v1(
                        self.bundle, self.context, drifted
                    )
                self.assertEqual(
                    raised.exception.code,
                    receipts.ReceiptRejectCode.UNTRUSTED_ARTIFACT,
                )

    def test_occurrence_is_replayed_from_serialized_source(self):
        source = dict(self.context.source_state_payload)
        source["facts"] = {
            "occurrences": [
                {"kind": "control", "value": 17},
                {"kind": "actual", "value": 23},
            ]
        }
        changed_context = fixture_context(source_state_payload=source)
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.verify_verified_transition_bundle_v1(
                self.bundle, changed_context, self.manifest
            )
        self.assertEqual(
            raised.exception.code,
            receipts.ReceiptRejectCode.SOURCE_BINDING_MISMATCH,
        )

    def test_local_terminal_result_cannot_build_an_e1_receipt(self):
        local = fixture_context(
            source_terminal_result="MISS_LOCAL",
            source_terminal_result_payload={
                "schedule_id": "terminal.complete.test",
                "outcome": "MISS_LOCAL",
            },
        )
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.make_verified_transition_bundle_v1(local, self.manifest)
        self.assertEqual(
            raised.exception.code,
            receipts.ReceiptRejectCode.TERMINAL_BINDING_MISMATCH,
        )

    def test_symbolic_verifier_cannot_be_the_producer_module(self):
        manifest = fixture_manifest(
            **{"symbolic-verifier.test": artifact_digest("producer.test")}
        )
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.make_verified_transition_bundle_v1(self.context, manifest)
        self.assertEqual(
            raised.exception.code,
            receipts.ReceiptRejectCode.UNTRUSTED_ARTIFACT,
        )

    def test_e5_requires_a_parent_to_final_strict_ticket(self):
        nondecreasing = seal(
            {
                "schema_id": "t5_n7_potential_receipt_v1",
                "schema_version": 1,
                "state_id": "state:target",
                "coordinates": [73, 2, 4, 9, 0, 0, 0],
            }
        )
        context = fixture_context(target_potential_receipt=nondecreasing)
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.make_verified_transition_bundle_v1(context, self.manifest)
        self.assertEqual(
            raised.exception.code,
            receipts.ReceiptRejectCode.TICKET_BINDING_MISMATCH,
        )

    def test_unknown_fields_fail_even_when_the_attacker_reseals(self):
        serialized = receipts.receipt_to_mapping_v1(self.bundle)
        serialized["e1_occurrence"]["recursive_edge_eligible"] = True
        mutated = receipts.apply_negative_mutation_v1(
            self.bundle, "CONTROL_AS_ACTUAL_BY_LABEL"
        )
        with self.assertRaises(receipts.ReceiptValidationError) as raised:
            receipts.parse_verified_transition_bundle_v1(mutated)
        self.assertEqual(
            raised.exception.code,
            receipts.ReceiptRejectCode.FIELD_SET_MISMATCH,
        )

    def test_receipt_dataclasses_are_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            self.bundle.digest = "forged"


if __name__ == "__main__":
    unittest.main()
