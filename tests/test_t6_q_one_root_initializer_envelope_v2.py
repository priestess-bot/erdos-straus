from __future__ import annotations

import copy
from dataclasses import FrozenInstanceError, fields
import hashlib
import inspect
import json
from pathlib import Path
import sys
import unittest

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_q_one_root_initializer_envelope_v2 as envelope  # noqa: E402


def raw_q_one_g(prime: int, factors: list[list[int]]) -> dict[str, object]:
    return {
        "schema_id": "q1_root_initializer_raw_v2",
        "schema_version": 2,
        "root_context": prime,
        "equation_rank": prime,
        "equation_numerator": 4,
        "equation_denominator": prime,
        "q": 1,
        "gap_three_x": (prime + 3) // 4,
        "endpoint_fiber_code": 2,
        "major_phase_code": 3,
        "provenance_code": 1,
        "mark_kind_code": 1,
        "mark_root_context": prime,
        "mark_equation_rank": prime,
        "gap_three_factorization": factors,
    }


RAW_73 = raw_q_one_g(73, [[19, 1]])
RAW_76129 = raw_q_one_g(76_129, [[7, 1], [2_719, 1]])


def make_chain(raw: dict[str, object]):
    body = envelope.make_canonical_q_one_g_source_body_v2(copy.deepcopy(raw))
    anchor = envelope.make_root_initializer_anchor_v2(body)
    state = envelope.make_raw_root_source_state_v2(body, anchor)
    return body, anchor, state


def forge_exact(value: object, **changes: object) -> object:
    forged = object.__new__(type(value))
    for field in fields(type(value)):
        object.__setattr__(
            forged,
            field.name,
            changes.get(field.name, getattr(value, field.name)),
        )
    return forged


def reseal_exact(value: object, **changes: object) -> object:
    provisional = forge_exact(value, **changes)
    cls = type(provisional)
    values = {field.name: getattr(provisional, field.name) for field in fields(cls)}
    digest = envelope.canonical_digest_v2(
        envelope._unsigned_mapping_v2(cls, values)
    )
    return forge_exact(
        provisional,
        **{cls.ID_FIELD: cls.ID_PREFIX + digest, "digest": digest},
    )


class SpoofedInt(int):
    def __new__(cls, raw: int, expected: int) -> SpoofedInt:
        value = int.__new__(cls, raw)
        value.expected = expected
        return value

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class SpoofedText(str):
    def __new__(cls, raw: str, expected: str) -> SpoofedText:
        value = str.__new__(cls, raw)
        value.expected = expected
        return value

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class SpoofedKey(str):
    def __new__(cls, raw: str, expected: str) -> SpoofedKey:
        value = str.__new__(cls, raw)
        value.expected = expected
        return value

    def __hash__(self) -> int:
        return hash(self.expected)

    def __eq__(self, other: object) -> bool:
        return other == self.expected


class QOneRootInitializerEnvelopeV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema_path = (
            ROOT
            / "schemas"
            / "t6-q-one-root-initializer-envelope-v2.schema.json"
        )
        cls.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(cls.schema)
        cls.validator = jsonschema.Draft202012Validator(cls.schema)

    def assert_reject(self, code, callback) -> None:
        with self.assertRaises(envelope.RootInitializerValidationError) as caught:
            callback()
        self.assertEqual(caught.exception.code, code)

    def test_factory_chain_replays_single_and_multifactor_q_one_g(self):
        for raw, expected in (
            (RAW_73, (73, 19, ((19, 1),))),
            (RAW_76129, (76_129, 19_033, ((7, 1), (2_719, 1)))),
        ):
            with self.subTest(prime=expected[0]):
                body, anchor, state = make_chain(raw)
                self.assertEqual(
                    (
                        state.root_context,
                        state.gap_three_x,
                        state.gap_three_factorization,
                    ),
                    expected,
                )
                self.assertEqual(anchor.body_id, body.body_id)
                self.assertEqual(state.body_id, body.body_id)
                self.assertEqual(
                    state.root_origin.root_initializer_anchor_id,
                    anchor.anchor_id,
                )
                self.assertTrue(state.state_id.startswith("state:"))
                for artifact in (body, anchor, state):
                    mapping = envelope.artifact_to_mapping_v2(artifact)
                    self.assertFalse(list(self.validator.iter_errors(mapping)))
                    self.assertEqual(mapping["evidence_class"], "EVIDENCE_ONLY_ROOT_SOURCE")
                    self.assertFalse(mapping["initializer_authority"])
                    self.assertFalse(mapping["admission_authority"])
                    self.assertFalse(mapping["queue_authority"])

    def test_parsers_require_and_replay_explicit_upstreams(self):
        body, anchor, state = make_chain(RAW_73)
        body_mapping = envelope.artifact_to_mapping_v2(body)
        anchor_mapping = envelope.artifact_to_mapping_v2(anchor)
        state_mapping = envelope.artifact_to_mapping_v2(state)
        self.assertEqual(
            envelope.parse_canonical_q_one_g_source_body_v2(
                body_mapping, copy.deepcopy(RAW_73)
            ),
            body,
        )
        self.assertEqual(
            envelope.parse_root_initializer_anchor_v2(anchor_mapping, body),
            anchor,
        )
        self.assertEqual(
            envelope.parse_raw_root_source_state_v2(
                state_mapping, body, anchor
            ),
            state,
        )

        other_body, other_anchor, _other_state = make_chain(RAW_76129)
        self.assert_reject(
            envelope.RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            lambda: envelope.parse_root_initializer_anchor_v2(
                anchor_mapping, other_body
            ),
        )
        self.assert_reject(
            envelope.RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            lambda: envelope.parse_raw_root_source_state_v2(
                state_mapping, body, other_anchor
            ),
        )

    def test_anchor_has_no_state_id_and_state_has_only_root_origin_ref(self):
        _body, anchor, state = make_chain(RAW_73)
        anchor_mapping = envelope.artifact_to_mapping_v2(anchor)
        state_mapping = envelope.artifact_to_mapping_v2(state)
        self.assertNotIn("state_id", anchor_mapping)
        self.assertEqual(
            set(state_mapping["root_origin"]),
            {"root_initializer_anchor_id", "digest"},
        )
        forbidden_fragments = (
            "terminal",
            "schedule",
            "result",
            "owner",
            "potential",
            "transition",
            "e1",
            "e2",
            "e3",
            "e4",
            "e5",
        )
        for mapping in (anchor_mapping, state_mapping):
            for key in mapping:
                self.assertTrue(
                    all(fragment not in key.lower() for fragment in forbidden_fragments),
                    key,
                )

    def test_schedule_and_terminal_sidecars_cannot_change_ids(self):
        body, anchor, state = make_chain(RAW_73)
        baseline = (body.body_id, anchor.anchor_id, state.state_id)
        signatures = (
            inspect.signature(envelope.make_canonical_q_one_g_source_body_v2),
            inspect.signature(envelope.make_root_initializer_anchor_v2),
            inspect.signature(envelope.make_raw_root_source_state_v2),
        )
        flattened_parameters = {
            name for signature in signatures for name in signature.parameters
        }
        self.assertTrue(
            flattened_parameters.isdisjoint(
                {"terminal", "schedule", "result", "owner", "potential", "e1", "queue"}
            )
        )
        sidecars = (
            {"schedule": "gap-3", "outcome": "MISS"},
            {"schedule": "gaps-3-7-11", "outcome": "PREFIX_MISS"},
            {"terminal": {"type": "ROOT_TERMINAL_HIT"}},
        )
        self.assertEqual(len({hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest() for item in sidecars}), 3)
        for _sidecar in sidecars:
            rebuilt = make_chain(RAW_73)
            self.assertEqual(
                (rebuilt[0].body_id, rebuilt[1].anchor_id, rebuilt[2].state_id),
                baseline,
            )

    def test_raw_authority_legacy_terminal_and_queue_fields_are_rejected(self):
        for field, value in (
            ("initializer_authority", True),
            ("admission_authority", True),
            ("queue_authority", True),
            ("terminal_first", {"outcome": "MISS"}),
            ("schedule_result", "MISS_COMPLETE"),
            ("state_id", "legacy-state"),
            ("source_receipt", {"E1": True}),
        ):
            raw = copy.deepcopy(RAW_73)
            raw[field] = value
            with self.subTest(field=field):
                self.assert_reject(
                    envelope.RootInitializerRejectCode.FIELD_SET_MISMATCH,
                    lambda raw=raw: envelope.make_canonical_q_one_g_source_body_v2(raw),
                )

    def test_noncore_fake_g_and_factorization_swap_are_rejected(self):
        noncore = raw_q_one_g(25, [[7, 1]])
        self.assert_reject(
            envelope.RootInitializerRejectCode.NOT_CORE_PRIME,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(noncore),
        )
        fake_g = raw_q_one_g(97, [[5, 2]])
        self.assert_reject(
            envelope.RootInitializerRejectCode.DOMAIN_MISMATCH,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(fake_g),
        )
        swapped = copy.deepcopy(RAW_73)
        swapped["gap_three_factorization"] = [[7, 1], [2_719, 1]]
        self.assert_reject(
            envelope.RootInitializerRejectCode.FACTORIZATION_MISMATCH,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(swapped),
        )

    def test_bool_and_builtin_subclasses_fail_closed(self):
        raw = copy.deepcopy(RAW_73)
        raw["q"] = True
        self.assert_reject(
            envelope.RootInitializerRejectCode.MALFORMED_FIELD,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(raw),
        )
        raw = copy.deepcopy(RAW_73)
        raw["schema_version"] = SpoofedInt(3, 2)
        self.assert_reject(
            envelope.RootInitializerRejectCode.WRONG_SCHEMA_VERSION,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(raw),
        )
        raw = copy.deepcopy(RAW_73)
        raw["schema_id"] = SpoofedText("legacy", "q1_root_initializer_raw_v2")
        self.assert_reject(
            envelope.RootInitializerRejectCode.WRONG_SCHEMA,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(raw),
        )
        raw = copy.deepcopy(RAW_73)
        q_value = raw.pop("q")
        raw[SpoofedKey("evil_q", "q")] = q_value
        self.assert_reject(
            envelope.RootInitializerRejectCode.MALFORMED_FIELD,
            lambda: envelope.make_canonical_q_one_g_source_body_v2(raw),
        )

    def test_object_new_resealed_authority_and_semantic_forgery_are_rejected(self):
        body, anchor, state = make_chain(RAW_73)
        for artifact, changes in (
            (body, {"q": True}),
            (body, {"initializer_authority": True}),
            (anchor, {"initializer_authority": True}),
            (anchor, {"domain_replay_digest": "0" * 64}),
            (state, {"queue_authority": True}),
            (state, {"root_context": 76_129}),
        ):
            forged = reseal_exact(artifact, **changes)
            with self.subTest(artifact=type(artifact).__name__, changes=changes):
                with self.assertRaises(envelope.RootInitializerValidationError):
                    envelope.artifact_to_mapping_v2(forged)

    def test_resealed_anchor_and_origin_swaps_require_explicit_upstreams(self):
        body, anchor, state = make_chain(RAW_73)
        other_body, other_anchor, _other_state = make_chain(RAW_76129)
        forged_anchor = reseal_exact(
            anchor,
            body_id=other_body.body_id,
            body_digest=other_body.digest,
            domain_replay_digest=envelope._domain_replay_digest_v2(
                other_body.body_id, other_body.digest
            ),
        )
        forged_anchor_mapping = envelope.artifact_to_mapping_v2(forged_anchor)
        self.assert_reject(
            envelope.RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            lambda: envelope.parse_root_initializer_anchor_v2(
                forged_anchor_mapping, body
            ),
        )

        forged_origin = envelope.make_root_origin_anchor_ref_v2(other_anchor)
        forged_state = reseal_exact(state, root_origin=forged_origin)
        forged_state_mapping = envelope.artifact_to_mapping_v2(forged_state)
        self.assert_reject(
            envelope.RootInitializerRejectCode.DEPENDENCY_MISMATCH,
            lambda: envelope.parse_raw_root_source_state_v2(
                forged_state_mapping, body, anchor
            ),
        )

    def test_artifact_subclasses_and_normal_assignment_are_rejected(self):
        body, _anchor, _state = make_chain(RAW_73)

        class BodySubclass(envelope.CanonicalQOneGSourceBodyV2):
            pass

        subclass = object.__new__(BodySubclass)
        for field in fields(envelope.CanonicalQOneGSourceBodyV2):
            object.__setattr__(subclass, field.name, getattr(body, field.name))
        self.assert_reject(
            envelope.RootInitializerRejectCode.INPUT_NOT_EXACT_TYPE,
            lambda: envelope.artifact_to_mapping_v2(subclass),
        )
        self.assertFalse(hasattr(body, "__dict__"))
        with self.assertRaises(FrozenInstanceError):
            body.q = 2

    def test_schema_rejects_authority_and_forbidden_field_injections(self):
        body, anchor, state = make_chain(RAW_73)
        for artifact in (body, anchor, state):
            mapping = envelope.artifact_to_mapping_v2(artifact)
            mapping["queue_authority"] = True
            self.assertTrue(list(self.validator.iter_errors(mapping)))

        state_mapping = envelope.artifact_to_mapping_v2(state)
        state_mapping["terminal_result_digest"] = "0" * 64
        self.assertTrue(list(self.validator.iter_errors(state_mapping)))


if __name__ == "__main__":
    unittest.main()
