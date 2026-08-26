from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from dataclasses import FrozenInstanceError, fields
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "t6_acyclic_transition_bundle_v2_under_test",
    ROOT / "scripts" / "t6_acyclic_transition_bundle_v2.py",
)
assert SPEC and SPEC.loader
acyclic = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = acyclic
SPEC.loader.exec_module(acyclic)


SEALED_CLASSES = (
    acyclic.CanonicalTargetProjectionV2,
    acyclic.PreclassificationDigestV2,
    acyclic.TerminalDigestSetV2,
    acyclic.T5CoordinateDraftV2,
    acyclic.EdgeAnchorV2,
    acyclic.RawTargetStateV2,
    acyclic.FinalTransitionReceiptBundleV2,
    acyclic.StateAdmissionSidecarV2,
)


def digest(label: str) -> str:
    return acyclic.canonical_digest_v2({"fixture": label})


def reseal(mapping, cls):
    result = dict(mapping)
    unsigned = {
        key: value
        for key, value in result.items()
        if key not in {cls.ID_FIELD, "digest"}
    }
    result["digest"] = acyclic.canonical_digest_v2(unsigned)
    result[cls.ID_FIELD] = cls.ID_PREFIX + result["digest"]
    return result


def forge_exact_artifact(original, **changes):
    """Bypass frozen/init guards and give the forged object a valid local seal."""

    cls = type(original)
    forged = object.__new__(cls)
    values = {}
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        values[field.name] = changes.get(field.name, getattr(original, field.name))
        object.__setattr__(forged, field.name, values[field.name])
    unsigned = acyclic._unsigned_mapping(cls, values)
    forged_digest = acyclic.canonical_digest_v2(unsigned)
    object.__setattr__(forged, cls.ID_FIELD, cls.ID_PREFIX + forged_digest)
    object.__setattr__(forged, "digest", forged_digest)
    return forged


def make_projection(*, equation_rank=73, facts=None):
    return acyclic.make_canonical_target_projection_v2(
        target_schema_id="t6_persistent_selector_state_v2",
        target_schema_version=2,
        root_context="root:p=73",
        equation_rank=equation_rank,
        facts={"chart_R": 75, "chart_K": 1369} if facts is None else facts,
        mark_behavior="IDENTITY_MARK",
        projector_id="projector.fixture.v2",
        projector_digest=digest("projector"),
        tie_break_rule_id="tie-break.fixture.v2",
        tie_break_rule_digest=digest("tie-break"),
    )


def make_chain(*, projection=None, owner_id="owner.fixture"):
    projection = make_projection() if projection is None else projection
    preclassification = acyclic.make_preclassification_digest_v2(
        projection,
        normal_form_verifier_id="normal-form.fixture.v2",
        normal_form_verifier_digest=digest("normal-form"),
        predicate_results_digest=digest("predicate-results"),
        precedence_table_id="precedence.fixture.v2",
        precedence_table_digest=digest("precedence"),
    )
    terminal = acyclic.make_terminal_digest_set_v2(
        projection,
        source_state_id="state:source-fixture",
        source_state_digest=digest("source-state"),
        schedule_id="terminal.fixture.v2",
        schedule_digest=digest("terminal-schedule"),
        result_digest=digest("terminal-result"),
        coverage_scope_digest=digest("terminal-scope"),
    )
    t5_draft = acyclic.make_t5_coordinate_draft_v2(
        projection,
        taxonomy_id="taxonomy.fixture.v2",
        taxonomy_digest=digest("taxonomy"),
        coordinates=(73, 2, 4, 8, 7, 0, 0),
    )
    anchor = acyclic.make_edge_anchor_v2(
        projection,
        preclassification,
        terminal,
        t5_draft,
        producer_id="producer.fixture.v2",
        producer_digest=digest("producer"),
        branch_id="branch.fixture.v2",
        candidate_witness_digest=digest("candidate-witness"),
    )
    target = acyclic.make_raw_target_state_v2(projection, anchor)
    bundle = acyclic.make_final_transition_receipt_bundle_v2(
        anchor,
        target,
        e1_occurrence_receipt_digest=digest("E1"),
        e2_projection_receipt_digest=digest("E2"),
        e3_typing_receipt_digest=digest("E3"),
        e4_lift_receipt_digest=digest("E4"),
        e5_ticket_receipt_digest=digest("E5"),
    )
    sidecar = acyclic.make_state_admission_sidecar_v2(
        target,
        bundle,
        owner_id=owner_id,
        owner_digest=digest(f"owner:{owner_id}"),
        grammar_digest=digest("grammar"),
        admission_gate_digest=digest("admission-gate"),
        target_potential_receipt_digest=digest("target-potential"),
        state_admission_receipt_digest=digest("state-admission-receipt"),
    )
    return {
        "projection": projection,
        "preclassification": preclassification,
        "terminal": terminal,
        "t5_draft": t5_draft,
        "anchor": anchor,
        "target": target,
        "bundle": bundle,
        "sidecar": sidecar,
    }


class AcyclicTransitionBundleV2Tests(unittest.TestCase):
    def setUp(self):
        self.chain = make_chain()

    def assert_reject_code(self, code, callback):
        with self.assertRaises(acyclic.AcyclicBundleValidationError) as raised:
            callback()
        self.assertEqual(raised.exception.code, code)

    def test_complete_chain_round_trips_in_dependency_order(self):
        projection = acyclic.parse_canonical_target_projection_v2(
            acyclic.artifact_to_mapping_v2(self.chain["projection"])
        )
        preclassification = acyclic.parse_preclassification_digest_v2(
            acyclic.artifact_to_mapping_v2(self.chain["preclassification"]),
            projection,
        )
        terminal = acyclic.parse_terminal_digest_set_v2(
            acyclic.artifact_to_mapping_v2(self.chain["terminal"]), projection
        )
        t5_draft = acyclic.parse_t5_coordinate_draft_v2(
            acyclic.artifact_to_mapping_v2(self.chain["t5_draft"]), projection
        )
        anchor = acyclic.parse_edge_anchor_v2(
            acyclic.artifact_to_mapping_v2(self.chain["anchor"]),
            projection,
            preclassification,
            terminal,
            t5_draft,
        )
        target = acyclic.parse_raw_target_state_v2(
            acyclic.artifact_to_mapping_v2(self.chain["target"]),
            projection,
            anchor,
        )
        bundle = acyclic.parse_final_transition_receipt_bundle_v2(
            acyclic.artifact_to_mapping_v2(self.chain["bundle"]), anchor, target
        )
        sidecar = acyclic.parse_state_admission_sidecar_v2(
            acyclic.artifact_to_mapping_v2(self.chain["sidecar"]), target, bundle
        )
        self.assertEqual(target.state_id, self.chain["target"].state_id)
        self.assertEqual(bundle.transition_id, self.chain["bundle"].transition_id)
        self.assertEqual(sidecar.sidecar_id, self.chain["sidecar"].sidecar_id)
        self.assertEqual(
            acyclic.DEPENDENCY_ORDER_V2[-1], "StateAdmissionSidecarV2"
        )

    def test_schema_required_fields_exactly_match_all_sealed_dataclasses(self):
        schema = json.loads(
            (
                ROOT
                / "schemas"
                / "t6-acyclic-transition-bundle-v2.schema.json"
            ).read_text(encoding="ascii")
        )
        for cls in SEALED_CLASSES:
            with self.subTest(artifact_type=cls.ARTIFACT_TYPE):
                expected = {field.name for field in fields(cls)} | {
                    "artifact_type",
                    "schema_version",
                }
                actual = set(schema["$defs"][cls.ARTIFACT_TYPE]["required"])
                self.assertEqual(actual, expected)
                self.assertFalse(
                    schema["$defs"][cls.ARTIFACT_TYPE]["additionalProperties"]
                )
        self.assertEqual(
            set(schema["$defs"]["SuccessorOriginAnchorRefV2"]["required"]),
            {field.name for field in fields(acyclic.SuccessorOriginAnchorRefV2)},
        )

    def test_schema_enforces_structural_reserved_field_constraints(self):
        schema = json.loads(
            (
                ROOT
                / "schemas"
                / "t6-acyclic-transition-bundle-v2.schema.json"
            ).read_text(encoding="ascii")
        )
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        for artifact in self.chain.values():
            self.assertFalse(
                list(validator.iter_errors(acyclic.artifact_to_mapping_v2(artifact)))
            )

        projection = acyclic.artifact_to_mapping_v2(self.chain["projection"])
        projection["facts"] = {"state_id": self.chain["target"].state_id}
        empty_key_projection = acyclic.artifact_to_mapping_v2(
            self.chain["projection"]
        )
        empty_key_projection["facts"] = {"": 7}
        t5_draft = acyclic.artifact_to_mapping_v2(self.chain["t5_draft"])
        t5_draft["coordinates"] = [73, 2, True, 8, 7, 0, 0]
        target = acyclic.artifact_to_mapping_v2(self.chain["target"])
        target["transition_id"] = self.chain["bundle"].transition_id
        sidecar = acyclic.artifact_to_mapping_v2(self.chain["sidecar"])
        sidecar["owner_digest"] = "sha256:" + sidecar["owner_digest"]
        for invalid in (
            projection,
            empty_key_projection,
            t5_draft,
            target,
            sidecar,
        ):
            with self.subTest(artifact_type=invalid["artifact_type"]):
                self.assertTrue(list(validator.iter_errors(invalid)))

    def test_public_outputs_are_slotted_and_frozen_for_normal_assignment(self):
        for cls in (*SEALED_CLASSES, acyclic.SuccessorOriginAnchorRefV2):
            with self.subTest(cls=cls.__name__):
                self.assertIn("__slots__", cls.__dict__)
                with self.assertRaises(TypeError):
                    cls()
        for name, artifact in self.chain.items():
            with self.subTest(name=name):
                self.assertFalse(hasattr(artifact, "__dict__"))
                with self.assertRaises(FrozenInstanceError):
                    artifact.digest = digest("mutation")

    def test_forged_exact_projection_with_recomputed_seal_is_revalidated(self):
        forged = forge_exact_artifact(
            self.chain["projection"], equation_rank=0
        )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.artifact_to_mapping_v2(forged),
        )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.make_preclassification_digest_v2(
                forged,
                normal_form_verifier_id="normal-form.fixture.v2",
                normal_form_verifier_digest=digest("normal-form"),
                predicate_results_digest=digest("predicate-results"),
                precedence_table_id="precedence.fixture.v2",
                precedence_table_digest=digest("precedence"),
            ),
        )

    def test_downstream_factory_revalidates_all_typed_sibling_fields(self):
        forged_terminal = forge_exact_artifact(
            self.chain["terminal"], schedule_digest="declared-not-a-digest"
        )
        forged_t5 = forge_exact_artifact(
            self.chain["t5_draft"],
            coordinates=list(self.chain["t5_draft"].coordinates),
        )
        for terminal, t5_draft in (
            (forged_terminal, self.chain["t5_draft"]),
            (self.chain["terminal"], forged_t5),
        ):
            with self.subTest(
                terminal_forged=terminal is forged_terminal,
                t5_forged=t5_draft is forged_t5,
            ):
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
                    lambda terminal=terminal, t5_draft=t5_draft: acyclic.make_edge_anchor_v2(
                        self.chain["projection"],
                        self.chain["preclassification"],
                        terminal,
                        t5_draft,
                        producer_id="producer.fixture.v2",
                        producer_digest=digest("producer"),
                        branch_id="branch.fixture.v2",
                        candidate_witness_digest=digest("candidate-witness"),
                    ),
                )

    def test_revalidation_uses_exact_string_int_facts_and_origin_types(self):
        class TextSubclass(str):
            pass

        class IntSubclass(int):
            pass

        forged_values = (
            forge_exact_artifact(
                self.chain["projection"], equation_rank=IntSubclass(73)
            ),
            forge_exact_artifact(
                self.chain["projection"], facts=dict(self.chain["projection"].facts)
            ),
            forge_exact_artifact(
                self.chain["terminal"], schedule_id=TextSubclass("terminal.fixture.v2")
            ),
            forge_exact_artifact(
                self.chain["terminal"],
                schedule_digest=TextSubclass(self.chain["terminal"].schedule_digest),
            ),
            forge_exact_artifact(
                self.chain["target"],
                successor_origin={
                    "edge_anchor_id": self.chain["anchor"].edge_anchor_id,
                    "edge_anchor_digest": self.chain["anchor"].digest,
                },
            ),
        )
        for forged in forged_values:
            with self.subTest(artifact_type=type(forged).__name__):
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
                    lambda forged=forged: acyclic.artifact_to_mapping_v2(forged),
                )

        forged_ref = object.__new__(acyclic.SuccessorOriginAnchorRefV2)
        object.__setattr__(
            forged_ref, "edge_anchor_id", self.chain["anchor"].edge_anchor_id
        )
        object.__setattr__(forged_ref, "edge_anchor_digest", "not-a-digest")
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.parse_successor_origin_anchor_ref_v2(
                forged_ref, self.chain["anchor"]
            ),
        )

    def test_canonical_json_rejects_boolean_float_and_duplicate_keys(self):
        for value in (True, 1.25, {"nested": False}):
            with self.subTest(value=value):
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
                    lambda value=value: acyclic.canonical_json_v2(value),
                )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            lambda: acyclic.loads_strict_v2('{"a":1,"a":2}'),
        )

    def test_projection_rejects_every_downstream_or_authority_key(self):
        forbidden = (
            "terminal_result_digest",
            "edge_anchor_id",
            "state_id",
            "target_state_id",
            "owner_digest",
            "potential_receipt",
            "transition_id",
            "verified_bundle",
            "E1",
            "e5_ticket",
            "admission_result",
        )
        for key in forbidden:
            with self.subTest(key=key):
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.FORBIDDEN_FIELD,
                    lambda key=key: make_projection(facts={"nested": {key: 7}}),
                )

    def test_unreserved_authority_synonyms_are_data_and_have_no_consumer(self):
        projection = make_projection(
            facts={
                "admitted": 1,
                "verified": "declared-only",
                "proof_status_synonym": "claimed",
            }
        )
        mapping = acyclic.artifact_to_mapping_v2(projection)
        self.assertEqual(mapping["facts"]["admitted"], 1)
        self.assertEqual(mapping["facts"]["verified"], "declared-only")
        public_action_prefixes = (
            "admit_",
            "dispatch_",
            "enqueue_",
            "issue_",
            "register_",
        )
        self.assertFalse(
            any(
                name.startswith(public_action_prefixes)
                for name in dir(acyclic)
                if not name.startswith("_")
            )
        )
        all_fields = {
            field.name for cls in SEALED_CLASSES for field in fields(cls)
        }
        self.assertNotIn("accepted", all_fields)
        self.assertNotIn("verified", all_fields)

    def test_edge_anchor_rejects_target_transition_and_e3_e5_fields(self):
        for key, value in (
            ("target_state_id", "state:future"),
            ("transition_id", "transition:future"),
            ("e3_typing_receipt_digest", digest("forged-E3")),
            ("e4_lift_receipt_digest", digest("forged-E4")),
            ("e5_ticket_receipt_digest", digest("forged-E5")),
        ):
            with self.subTest(key=key):
                mapping = acyclic.artifact_to_mapping_v2(self.chain["anchor"])
                mapping[key] = value
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
                    lambda mapping=mapping: acyclic.parse_edge_anchor_v2(
                        mapping,
                        self.chain["projection"],
                        self.chain["preclassification"],
                        self.chain["terminal"],
                        self.chain["t5_draft"],
                    ),
                )

    def test_raw_state_rejects_bundle_transition_and_e_boolean_in_facts(self):
        for key, value in (
            ("transition_id", "transition:future"),
            ("bundle_digest", digest("future-bundle")),
            ("E1", True),
            ("e4_lift", True),
        ):
            with self.subTest(key=key):
                mapping = acyclic.artifact_to_mapping_v2(self.chain["target"])
                mapping["facts"] = dict(mapping["facts"])
                mapping["facts"][key] = value
                if not isinstance(value, bool):
                    mapping = reseal(mapping, acyclic.RawTargetStateV2)
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.FORBIDDEN_FIELD,
                    lambda mapping=mapping: acyclic.parse_raw_target_state_v2(
                        mapping,
                        self.chain["projection"],
                        self.chain["anchor"],
                    ),
                )

    def test_raw_state_contains_only_a_two_field_anchor_reference(self):
        mapping = acyclic.artifact_to_mapping_v2(self.chain["target"])
        mapping["successor_origin"] = dict(mapping["successor_origin"])
        mapping["successor_origin"]["projection_id"] = self.chain[
            "projection"
        ].projection_id
        mapping = reseal(mapping, acyclic.RawTargetStateV2)
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            lambda: acyclic.parse_raw_target_state_v2(
                mapping, self.chain["projection"], self.chain["anchor"]
            ),
        )

    def test_bool_as_integer_and_bool_as_digest_are_rejected(self):
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: make_projection(equation_rank=True),
        )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.make_t5_coordinate_draft_v2(
                self.chain["projection"],
                taxonomy_id="taxonomy.fixture.v2",
                taxonomy_digest=digest("taxonomy"),
                coordinates=(73, 2, 4, True, 7, 0, 0),
            ),
        )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.make_final_transition_receipt_bundle_v2(
                self.chain["anchor"],
                self.chain["target"],
                e1_occurrence_receipt_digest=True,
                e2_projection_receipt_digest=digest("E2"),
                e3_typing_receipt_digest=digest("E3"),
                e4_lift_receipt_digest=digest("E4"),
                e5_ticket_receipt_digest=digest("E5"),
            ),
        )

    def test_json_schema_integer_is_structural_but_python_parser_is_stricter(self):
        schema = json.loads(
            (
                ROOT
                / "schemas"
                / "t6-acyclic-transition-bundle-v2.schema.json"
            ).read_text(encoding="ascii")
        )
        validator = Draft202012Validator(schema)
        projection_mapping = acyclic.artifact_to_mapping_v2(
            self.chain["projection"]
        )
        projection_mapping["target_schema_version"] = 2.0
        self.assertFalse(list(validator.iter_errors(projection_mapping)))
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
            lambda: acyclic.parse_canonical_target_projection_v2(
                projection_mapping
            ),
        )

    def test_owner_digest_must_be_bare_lowercase_hex(self):
        for invalid in (
            "sha256:" + digest("owner"),
            digest("owner").upper(),
            "owner:" + digest("owner"),
            True,
        ):
            with self.subTest(invalid=invalid):
                self.assert_reject_code(
                    acyclic.AcyclicBundleRejectCode.MALFORMED_FIELD,
                    lambda invalid=invalid: acyclic.make_state_admission_sidecar_v2(
                        self.chain["target"],
                        self.chain["bundle"],
                        owner_id="owner.fixture",
                        owner_digest=invalid,
                        grammar_digest=digest("grammar"),
                        admission_gate_digest=digest("admission-gate"),
                        target_potential_receipt_digest=digest("target-potential"),
                        state_admission_receipt_digest=digest(
                            "state-admission-receipt"
                        ),
                    ),
                )

    def test_projection_swap_is_rejected_even_after_attacker_reseals(self):
        other_projection = make_projection(equation_rank=79)
        mapping = acyclic.artifact_to_mapping_v2(self.chain["preclassification"])
        mapping["projection_id"] = other_projection.projection_id
        mapping["projection_digest"] = other_projection.digest
        mapping = reseal(mapping, acyclic.PreclassificationDigestV2)
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.DIGEST_MISMATCH,
            lambda: acyclic.parse_preclassification_digest_v2(
                mapping, self.chain["projection"]
            ),
        )

    def test_sibling_swap_is_rejected_by_edge_anchor_dependency_replay(self):
        other_terminal = acyclic.make_terminal_digest_set_v2(
            self.chain["projection"],
            source_state_id="state:other-source",
            source_state_digest=digest("other-source"),
            schedule_id="terminal.other.v2",
            schedule_digest=digest("other-schedule"),
            result_digest=digest("other-result"),
            coverage_scope_digest=digest("other-scope"),
        )
        mapping = acyclic.artifact_to_mapping_v2(self.chain["anchor"])
        mapping["source_state_id"] = other_terminal.source_state_id
        mapping["source_state_digest"] = other_terminal.source_state_digest
        mapping["terminal_digest_set_id"] = other_terminal.terminal_digest_set_id
        mapping["terminal_digest_set_digest"] = other_terminal.digest
        mapping = reseal(mapping, acyclic.EdgeAnchorV2)
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.DIGEST_MISMATCH,
            lambda: acyclic.parse_edge_anchor_v2(
                mapping,
                self.chain["projection"],
                self.chain["preclassification"],
                self.chain["terminal"],
                self.chain["t5_draft"],
            ),
        )

    def test_anchor_swap_in_raw_state_is_rejected_after_reseal(self):
        other_projection = make_projection(equation_rank=79)
        other = make_chain(projection=other_projection)
        mapping = acyclic.artifact_to_mapping_v2(self.chain["target"])
        mapping["successor_origin"] = {
            "edge_anchor_id": other["anchor"].edge_anchor_id,
            "edge_anchor_digest": other["anchor"].digest,
        }
        mapping = reseal(mapping, acyclic.RawTargetStateV2)
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.DEPENDENCY_MISMATCH,
            lambda: acyclic.parse_raw_target_state_v2(
                mapping, self.chain["projection"], self.chain["anchor"]
            ),
        )

    def test_target_swap_in_bundle_and_bundle_swap_in_sidecar_are_rejected(self):
        other = make_chain(projection=make_projection(equation_rank=79))
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.DIGEST_MISMATCH,
            lambda: acyclic.parse_final_transition_receipt_bundle_v2(
                acyclic.artifact_to_mapping_v2(other["bundle"]),
                self.chain["anchor"],
                self.chain["target"],
            ),
        )
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.DIGEST_MISMATCH,
            lambda: acyclic.parse_state_admission_sidecar_v2(
                acyclic.artifact_to_mapping_v2(other["sidecar"]),
                self.chain["target"],
                self.chain["bundle"],
            ),
        )

    def test_upstream_ids_are_independent_of_all_downstream_objects(self):
        first = self.chain
        second_bundle = acyclic.make_final_transition_receipt_bundle_v2(
            first["anchor"],
            first["target"],
            e1_occurrence_receipt_digest=digest("new-E1"),
            e2_projection_receipt_digest=digest("new-E2"),
            e3_typing_receipt_digest=digest("new-E3"),
            e4_lift_receipt_digest=digest("new-E4"),
            e5_ticket_receipt_digest=digest("new-E5"),
        )
        second_sidecar = acyclic.make_state_admission_sidecar_v2(
            first["target"],
            second_bundle,
            owner_id="owner.changed",
            owner_digest=digest("owner.changed"),
            grammar_digest=digest("grammar.changed"),
            admission_gate_digest=digest("gate.changed"),
            target_potential_receipt_digest=digest("potential.changed"),
            state_admission_receipt_digest=digest("admission.changed"),
        )
        self.assertEqual(first["projection"].projection_id, first["anchor"].projection_id)
        self.assertEqual(first["anchor"].edge_anchor_id, first["target"].successor_origin.edge_anchor_id)
        self.assertEqual(first["target"].state_id, second_bundle.target_state_id)
        self.assertNotEqual(first["bundle"].transition_id, second_bundle.transition_id)
        self.assertNotEqual(first["sidecar"].sidecar_id, second_sidecar.sidecar_id)
        self.assertEqual(first["target"].state_id, first["bundle"].target_state_id)
        self.assertEqual(first["target"].state_id, second_bundle.target_state_id)

    def test_cycle_fields_cannot_be_imported_at_an_earlier_layer(self):
        projection_mapping = acyclic.artifact_to_mapping_v2(
            self.chain["projection"]
        )
        projection_mapping["target_state_id"] = self.chain["target"].state_id
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            lambda: acyclic.parse_canonical_target_projection_v2(
                projection_mapping
            ),
        )
        anchor_mapping = acyclic.artifact_to_mapping_v2(self.chain["anchor"])
        anchor_mapping["transition_id"] = self.chain["bundle"].transition_id
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            lambda: acyclic.parse_edge_anchor_v2(
                anchor_mapping,
                self.chain["projection"],
                self.chain["preclassification"],
                self.chain["terminal"],
                self.chain["t5_draft"],
            ),
        )

    def test_legacy_boolean_validation_has_no_fallback_parser(self):
        legacy = {
            "source_state_id": "state:source",
            "E1": True,
            "E2": True,
            "E3_pre_admission": True,
            "E4": True,
        }
        self.assert_reject_code(
            acyclic.AcyclicBundleRejectCode.FIELD_SET_MISMATCH,
            lambda: acyclic.parse_final_transition_receipt_bundle_v2(
                legacy, self.chain["anchor"], self.chain["target"]
            ),
        )


if __name__ == "__main__":
    unittest.main()
