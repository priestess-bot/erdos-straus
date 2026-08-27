from __future__ import annotations

import hashlib
import importlib.util
import sys
import types
import unittest
from dataclasses import fields
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "t6_q_one_phase_root_prestate_v2_under_test",
    ROOT / "scripts" / "t6_q_one_phase_root_prestate_v2.py",
)
assert SPEC and SPEC.loader
prestate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prestate
SPEC.loader.exec_module(prestate)


def digest(label: str) -> str:
    return prestate.canonical_digest_v2({"fixture": label})


def state_id(label: str) -> str:
    return "state:" + digest(label)


def source_binding(prime: int):
    return prestate.make_external_q_one_source_binding_v2(
        v1_source_state_id=state_id(f"source:{prime}"),
        v1_source_wire_digest=digest(f"source:{prime}"),
        source_prefix_receipt_digest=digest(f"prefix:{prime}"),
        source_phase_root_preimage_digest=digest(f"preimage:{prime}"),
    )


def forge_resealed_artifact(original, **changes):
    """Bypass frozen/init guards while preserving the artifact-local seal."""

    cls = type(original)
    forged = object.__new__(cls)
    values = {}
    for field in fields(cls):
        if field.name in {cls.ID_FIELD, "digest"}:
            continue
        value = changes.get(field.name, getattr(original, field.name))
        values[field.name] = value
        object.__setattr__(forged, field.name, value)
    unsigned = prestate._unsigned_mapping(cls, values)
    forged_digest = prestate.canonical_digest_v2(unsigned)
    object.__setattr__(forged, cls.ID_FIELD, cls.ID_PREFIX + forged_digest)
    object.__setattr__(forged, "digest", forged_digest)
    return forged


def build_chain(prime: int):
    projection = prestate.make_canonical_phase_root_projection_v2(prime)
    classification = prestate.make_phase_root_preclassification_v2(projection)
    binding = source_binding(prime)
    scope = prestate.make_phase_root_finite_target_scope_v2(
        projection, binding
    )
    draft = prestate.make_phase_root_t5_coordinate_draft_v2(projection)
    anchor = prestate.make_phase_root_edge_anchor_v2(
        projection,
        classification,
        scope,
        draft,
        binding,
    )
    return projection, classification, scope, draft, anchor, binding


class PhaseRootPrestateV2Tests(unittest.TestCase):
    def assert_code(self, code, callback):
        with self.assertRaises(prestate.PrestateValidationError) as raised:
            callback()
        self.assertEqual(raised.exception.code, code)

    def test_1201_round_trips_full_zero_authority_chain(self):
        projection, classification, scope, draft, anchor, binding = build_chain(1201)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )

        parsed_projection = prestate.parse_canonical_phase_root_projection_v2(
            prestate.artifact_to_mapping_v2(projection)
        )
        parsed_classification = prestate.parse_phase_root_preclassification_v2(
            prestate.artifact_to_mapping_v2(classification), parsed_projection
        )
        parsed_scope = prestate.parse_phase_root_finite_target_scope_v2(
            prestate.artifact_to_mapping_v2(scope), parsed_projection, binding
        )
        parsed_draft = prestate.parse_phase_root_t5_coordinate_draft_v2(
            prestate.artifact_to_mapping_v2(draft), parsed_projection
        )
        parsed_anchor = prestate.parse_phase_root_edge_anchor_v2(
            prestate.artifact_to_mapping_v2(anchor),
            parsed_projection,
            parsed_classification,
            parsed_scope,
            parsed_draft,
            binding,
        )
        parsed_target = prestate.parse_phase_root_target_prestate_v2(
            prestate.artifact_to_mapping_v2(target),
            parsed_projection,
            parsed_anchor,
            parsed_scope,
            binding,
        )

        self.assertEqual(parsed_target.state_id, target.state_id)
        self.assertEqual(scope.scope_outcome, prestate.TARGET_SCOPE_MISS)
        self.assertFalse(scope.global_exhaustion)
        self.assertEqual(scope.next_unchecked_gap, 15)
        self.assertEqual(
            classification.predicted_owner_label,
            "type_i_full_carrier_post_g",
        )
        self.assertEqual(classification.predicted_precedence_index, 14)
        self.assertEqual(
            classification.family_precedence,
            tuple(item.family_id for item in prestate.state_contract.FAMILY_PREDICATES_V1),
        )
        self.assertEqual(
            prestate.STATE_CONTRACT_MODULE_DIGEST,
            hashlib.sha256(
                (ROOT / "scripts" / "t6_persistent_selector_state_v1.py").read_bytes()
            ).hexdigest(),
        )
        self.assertEqual(target.prestate_kind, prestate.PHASE_ROOT_PRESTATE_KIND)

    def test_2521_miss_constructs_prestate_and_target_t5_draft(self):
        projection, classification, scope, draft, anchor, binding = build_chain(2521)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )

        t = (2521 - 1) // 24
        self.assertEqual(projection.facts["chart_R"], 16 * t + 3)
        self.assertEqual(
            projection.facts["chart_K"], (6 * t + 1) * (16 * t + 1)
        )
        self.assertEqual(scope.scope_outcome, prestate.TARGET_SCOPE_MISS)
        self.assertEqual(
            draft.target_coordinates,
            (2521, 2, 4, (2520**2) // 4, projection.facts["chart_K"], 0, 0),
        )
        self.assertEqual(target.successor_origin.edge_anchor_id, anchor.edge_anchor_id)
        self.assertEqual(anchor.preclassification_id, classification.preclassification_id)

    def test_gap_seven_hit_preempts_anchor_and_prestate(self):
        projection = prestate.make_canonical_phase_root_projection_v2(73)
        classification = prestate.make_phase_root_preclassification_v2(projection)
        binding = source_binding(73)
        scope = prestate.make_phase_root_finite_target_scope_v2(
            projection, binding
        )
        draft = prestate.make_phase_root_t5_coordinate_draft_v2(projection)
        self.assertEqual(scope.scope_outcome, prestate.TARGET_SCOPE_HIT)
        self.assertEqual(scope.hit_index, 1)
        self.assertIsNotNone(scope.hit_certificate_digest)
        self.assertIsNone(scope.next_unchecked_gap)
        self.assert_code(
            prestate.PrestateRejectCode.TARGET_SCOPE_HIT,
            lambda: prestate.make_phase_root_edge_anchor_v2(
                projection,
                classification,
                scope,
                draft,
                binding,
            ),
        )

    def test_projection_rejects_non_g_x_factorization(self):
        self.assert_code(
            prestate.PrestateRejectCode.MATH_MISMATCH,
            lambda: prestate.make_canonical_phase_root_projection_v2(97),
        )

    def test_forbidden_owner_bundle_e_and_admission_fields_are_rejected(self):
        projection, _classification, scope, _draft, anchor, binding = build_chain(1201)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )
        mapping = prestate.artifact_to_mapping_v2(target)
        for field in (
            "owner_digest",
            "transition_bundle_digest",
            "E1",
            "admission_result",
            "queue_gate",
        ):
            with self.subTest(field=field):
                mutated = dict(mapping)
                mutated[field] = "forbidden"
                self.assert_code(
                    prestate.PrestateRejectCode.FIELD_SET_MISMATCH,
                    lambda mutated=mutated: prestate.parse_phase_root_target_prestate_v2(
                        mutated, projection, anchor, scope, binding
                    ),
                )
        origin = dict(mapping["successor_origin"])
        origin["transition_id"] = "transition:" + digest("forbidden")
        mapping = dict(mapping)
        mapping["successor_origin"] = origin
        self.assert_code(
            prestate.PrestateRejectCode.DIGEST_MISMATCH,
            lambda: prestate.parse_phase_root_target_prestate_v2(
                mapping, projection, anchor, scope, binding
            ),
        )

    def test_dependency_swaps_and_fact_authority_injection_fail_closed(self):
        first = build_chain(1201)
        second = build_chain(2521)
        projection, classification, scope, draft, anchor, binding = first
        self.assert_code(
            prestate.PrestateRejectCode.DIGEST_MISMATCH,
            lambda: prestate.parse_phase_root_edge_anchor_v2(
                prestate.artifact_to_mapping_v2(anchor),
                second[0],
                classification,
                scope,
                draft,
                binding,
            ),
        )
        projection_mapping = prestate.artifact_to_mapping_v2(projection)
        facts = dict(projection_mapping["facts"])
        facts["owner"] = "type_i_full_carrier_post_g"
        projection_mapping["facts"] = facts
        self.assert_code(
            prestate.PrestateRejectCode.DIGEST_MISMATCH,
            lambda: prestate.parse_canonical_phase_root_projection_v2(
                projection_mapping
            ),
        )

    def test_wire_type_confusion_is_rejected_with_or_without_reseal(self):
        projection, _classification, scope, _draft, anchor, binding = build_chain(1201)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )
        mapping = prestate.artifact_to_mapping_v2(target)
        facts = dict(mapping["facts"])
        facts["t5_eta_p"] = False
        mapping["facts"] = facts
        self.assert_code(
            prestate.PrestateRejectCode.DIGEST_MISMATCH,
            lambda: prestate.parse_phase_root_target_prestate_v2(
                mapping, projection, anchor, scope, binding
            ),
        )
        resealed = dict(mapping)
        unsigned = {
            key: value
            for key, value in resealed.items()
            if key not in {"state_id", "digest"}
        }
        resealed["digest"] = prestate.canonical_digest_v2(unsigned)
        resealed["state_id"] = "state:" + resealed["digest"]
        self.assert_code(
            prestate.PrestateRejectCode.DIGEST_MISMATCH,
            lambda: prestate.parse_phase_root_target_prestate_v2(
                resealed, projection, anchor, scope, binding
            ),
        )
        projection_mapping = prestate.artifact_to_mapping_v2(projection)
        projection_mapping["root_context"] = "1201"
        unsigned = {
            key: value
            for key, value in projection_mapping.items()
            if key not in {"projection_id", "digest"}
        }
        projection_mapping["digest"] = prestate.canonical_digest_v2(unsigned)
        projection_mapping["projection_id"] = (
            "phase-root-projection:" + projection_mapping["digest"]
        )
        self.assert_code(
            prestate.PrestateRejectCode.MALFORMED_FIELD,
            lambda: prestate.parse_canonical_phase_root_projection_v2(
                projection_mapping
            ),
        )

    def test_public_serializer_rejects_resealed_semantic_q_forgery(self):
        projection, _classification, scope, _draft, anchor, binding = build_chain(1201)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )
        forged = forge_resealed_artifact(target, prestate_kind="FORGED")
        self.assert_code(
            prestate.PrestateRejectCode.MATH_MISMATCH,
            lambda: prestate.artifact_to_mapping_v2(forged),
        )

    def test_source_binding_is_distinct_and_private_loader_ignores_preload(self):
        projection, _classification, scope, _draft, anchor, binding = build_chain(1201)
        target = prestate.make_phase_root_target_prestate_v2(
            projection, anchor, scope, binding
        )
        self.assertEqual(
            binding.binding_scope,
            prestate.EXTERNAL_SOURCE_BINDING_SCOPE,
        )
        for artifact in (projection, _classification, scope, _draft, anchor, target):
            with self.subTest(artifact=type(artifact).__name__):
                self.assert_code(
                    prestate.PrestateRejectCode.FIELD_SET_MISMATCH,
                    lambda artifact=artifact: prestate.parse_external_q_one_source_binding_v2(
                        prestate.artifact_to_mapping_v2(artifact)
                    ),
                )
        view = prestate._predicate_view(projection)
        self.assertNotIsInstance(
            view, prestate.state_contract.VerifiedSelectorHeaderV1
        )
        with self.assertRaises(AttributeError):
            prestate.state_contract.classify_selector_owner_v1(view)

        public_name = "t6_persistent_selector_state_v1"
        private_name = prestate.STATE_CONTRACT_PRIVATE_MODULE_NAME
        saved_public = sys.modules.get(public_name)
        saved_private = sys.modules.get(private_name)
        poison = types.ModuleType(public_name)
        private_poison = types.ModuleType(private_name)
        sys.modules[public_name] = poison
        sys.modules[private_name] = private_poison
        try:
            spec = importlib.util.spec_from_file_location(
                "prestate_private_loader_control",
                ROOT / "scripts" / "t6_q_one_phase_root_prestate_v2.py",
            )
            assert spec and spec.loader
            reloaded = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = reloaded
            spec.loader.exec_module(reloaded)
            self.assertIsNot(reloaded.state_contract, poison)
            self.assertIsNot(reloaded.state_contract, private_poison)
            self.assertEqual(
                reloaded.STATE_CONTRACT_MODULE_DIGEST,
                hashlib.sha256(
                    (ROOT / "scripts" / "t6_persistent_selector_state_v1.py").read_bytes()
                ).hexdigest(),
            )
            replay = reloaded.make_phase_root_preclassification_v2(
                reloaded.make_canonical_phase_root_projection_v2(1201)
            )
            self.assertEqual(replay.predicted_precedence_index, 14)
        finally:
            sys.modules.pop("prestate_private_loader_control", None)
            if saved_public is None:
                sys.modules.pop(public_name, None)
            else:
                sys.modules[public_name] = saved_public
            if saved_private is None:
                sys.modules.pop(private_name, None)
            else:
                sys.modules[private_name] = saved_private

    def test_canonical_json_rejects_duplicate_keys_and_floats(self):
        self.assert_code(
            prestate.PrestateRejectCode.FIELD_SET_MISMATCH,
            lambda: prestate.loads_strict_v2('{"a":1,"a":2}'),
        )
        self.assert_code(
            prestate.PrestateRejectCode.MALFORMED_FIELD,
            lambda: prestate.loads_strict_v2('{"a":1.5}'),
        )
        self.assertEqual(
            prestate.canonical_json_v2({"b": [True, None], "a": 1}),
            '{"a":1,"b":[true,null]}',
        )


if __name__ == "__main__":
    unittest.main()
