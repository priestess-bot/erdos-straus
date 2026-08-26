from __future__ import annotations

import copy
from dataclasses import fields
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from tests.test_t6_coordinator_role_registry_v3 import RepositoryFixture  # noqa: E402
from tests.test_t6_q_one_terminal_issuer_v1 import RAW as ISSUER_RAW  # noqa: E402

import t6_q_one_registered_prefix_e1_consumer_v2 as consumer  # noqa: E402
import t6_persistent_selector_state_v1 as persistent_state  # noqa: E402
import t6_q_one_root_owner_classifier_v2 as owner  # noqa: E402
import t6_q_one_root_initializer_envelope_v2 as root_envelope  # noqa: E402
import t6_q_one_scope_aware_e1_validator_v2 as scope_validator  # noqa: E402


SCHEMA = json.loads(
    (ROOT / "schemas/t6-q-one-root-prefix-scoped-e1-v2.schema.json").read_text(
        encoding="utf-8"
    )
)


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


RAW = {
    prime: raw_q_one_g(prime, value["gap_three_factorization"])  # type: ignore[index]
    for prime, value in ISSUER_RAW.items()
    if prime in {73, 193, 1_201, 2_521, 241_441}
}


ISSUE_DRIVER = r"""
import json
import sys
from pathlib import Path

import t6_q_one_terminal_issuer_v1 as issuer

root = Path(sys.argv[1])
head = sys.argv[2]
raw = json.loads(sys.stdin.read())
receipt = issuer.issue_q_one_terminal_decision_v1(
    root=root, requested_head=head, raw_q_one_g=raw
)
print(json.dumps({
    "actualness": issuer.actualness_receipt_to_mapping_v1(receipt.root_actualness),
    "terminal": issuer.production_terminal_receipt_to_mapping_v1(receipt),
}, sort_keys=True))
"""


def _issue(root: Path, head: str, raw: dict[str, object]) -> dict[str, object]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(root / "scripts")
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, "-c", ISSUE_DRIVER, str(root), head],
        cwd=root,
        input=json.dumps(raw),
        text=True,
        capture_output=True,
        check=True,
        env=environment,
    )
    return json.loads(completed.stdout)


def _grant(module: object) -> dict[str, object]:
    return {
        "grant_id": module.GRANT_ID,
        "role": module.ROLE,
        "artifact_id": module.ARTIFACT_ID,
        "artifact_path": module.ARTIFACT_PATH,
        "artifact_symbols": list(module.ARTIFACT_SYMBOLS),
        "capabilities": list(module.CAPABILITIES),
        "authority_class": module.AUTHORITY_CLASS,
        # The exact-HEAD registry supplies the real semantic pin.  Pure roles
        # only accept a well-formed pin; provenance is checked by the coordinator.
        "artifact_semantic_sha256": "a" * 64,
    }


class QOneRootPrefixScopedE1RoleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="q1-v4-roles-")
        self.fixture = RepositoryFixture(Path(self.temp.name))
        self.root, self.head = self.fixture.commit()
        self.artifacts: dict[int, dict[str, object]] = {}

    def tearDown(self) -> None:
        self.temp.cleanup()

    def case(self, prime: int) -> dict[str, object]:
        cached = self.artifacts.get(prime)
        if cached is not None:
            return cached
        raw = copy.deepcopy(RAW[prime])
        issued = _issue(self.root, self.head, raw)
        body = root_envelope.make_canonical_q_one_g_source_body_v2(raw)
        anchor = root_envelope.make_root_initializer_anchor_v2(body)
        state = root_envelope.make_raw_root_source_state_v2(body, anchor)
        result = {
            "raw": raw,
            "actualness": issued["actualness"],
            "terminal": issued["terminal"],
            "body": root_envelope.artifact_to_mapping_v2(body),
            "anchor": root_envelope.artifact_to_mapping_v2(anchor),
            "state": root_envelope.artifact_to_mapping_v2(state),
        }
        self.artifacts[prime] = result
        return result

    def owner_for(self, prime: int) -> dict[str, object]:
        value = self.case(prime)
        receipt = owner.classify_q_one_root_owner_v2(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            role_grant=_grant(owner),
        )
        return owner.root_owner_receipt_to_mapping_v2(receipt)

    def validation_for(self, prime: int) -> dict[str, object]:
        value = self.case(prime)
        receipt = scope_validator.validate_q_one_registered_prefix_e1_scope_v2(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            owner_receipt=self.owner_for(prime),
            terminal_receipt=value["terminal"],
            role_grant=_grant(scope_validator),
        )
        return scope_validator.scope_validation_receipt_to_mapping_v2(receipt)

    def test_owner_positive_controls_and_no_terminal_dependency(self) -> None:
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                receipt = self.owner_for(prime)
                self.assertEqual(receipt["owner"], owner.OWNER)
                self.assertEqual(receipt["owner_scope"], "ROOT_SOURCE_DISPATCH_ONLY")
                self.assertEqual(receipt["matched_families"], [owner.OWNER])
                self.assertTrue(receipt["common_owner_authority"])
                self.assertFalse(receipt["terminal_receipt_dependency"])
                self.assertFalse(receipt["persistent_admission"])
                for field in (
                    "registered_prefix_miss_authority",
                    "scope_validation_authority",
                    "root_source_scoped_e1",
                    "e1_authority",
                    "producer_authority",
                    "queue_authority",
                ):
                    self.assertFalse(receipt[field], field)

    def test_owner_source_and_actualness_swaps_reject(self) -> None:
        first = self.case(1_201)
        second = self.case(2_521)
        kwargs = {
            "raw_q_one_g": first["raw"],
            "source_body": second["body"],
            "root_anchor": second["anchor"],
            "source_state": second["state"],
            "root_actualness": first["actualness"],
            "role_grant": _grant(owner),
        }
        with self.assertRaises(owner.RootOwnerClassificationError) as raised:
            owner.classify_q_one_root_owner_v2(**kwargs)
        self.assertIn(raised.exception.code, {owner.RootOwnerRejectCode.SOURCE_REPLAY_FAILED, owner.RootOwnerRejectCode.DIGEST_MISMATCH})
        kwargs.update(
            source_body=first["body"],
            root_anchor=first["anchor"],
            source_state=first["state"],
            root_actualness=second["actualness"],
        )
        with self.assertRaises(owner.RootOwnerClassificationError):
            owner.classify_q_one_root_owner_v2(**kwargs)

    def test_owner_exactly_replays_frozen_v1_grammar_classifier_and_digest(self) -> None:
        receipt = self.owner_for(1_201)
        facts = receipt["normalized_header"]["facts"]
        validated_facts = persistent_state._validate_facts(
            facts,
            receipt["root_context"],
            persistent_state.ROOT_SOL,
        )
        facts_digest = persistent_state.canonical_digest_v1(dict(validated_facts))
        header = persistent_state.VerifiedSelectorHeaderV1(
            state_id=receipt["state_id"],
            queue_gate=persistent_state.ROOT_INITIALIZER_OUTPUT,
            producer_id="v4_reference_equivalence_only",
            branch_id="q1_g_root",
            parent_state_id=None,
            root_context=receipt["root_context"],
            equation_rank=receipt["root_context"],
            mark_kind=persistent_state.ROOT_SOL,
            mark_receipt_digest="0" * 64,
            terminal_first_digest="1" * 64,
            source_receipt_digest="2" * 64,
            facts_digest=facts_digest,
            facts=validated_facts,
        )
        classification = persistent_state.classify_selector_owner_v1(header)
        expected_id = persistent_state.owner_digest_v1(
            header,
            classification.owner,
            classification.matched_families,
            classification.precedence_index,
        )
        self.assertEqual(classification.owner, owner.OWNER)
        self.assertEqual(classification.matched_families, (owner.OWNER,))
        self.assertEqual(classification.precedence_index, 2)
        self.assertEqual(receipt["facts_digest"], facts_digest)
        self.assertEqual(receipt["owner_id"], expected_id)
        self.assertEqual(receipt["owner_digest"], expected_id.removeprefix("owner:"))

    def test_validator_replays_prefix_and_records_gap23_boundary(self) -> None:
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                receipt = self.validation_for(prime)
                self.assertEqual(receipt["status"], scope_validator.STATUS)
                self.assertFalse(receipt["common_owner_authority"])
                self.assertTrue(receipt["scope_validation_authority"])
                self.assertTrue(receipt["registered_prefix_miss_authority"])
                self.assertFalse(receipt["root_source_scoped_e1"])
                self.assertFalse(receipt["e1_authority"])
                self.assertEqual(receipt["ordered_gaps"], list(scope_validator.ORDERED_GAPS))
                self.assertEqual(receipt["next_unchecked_gap"], 15)
                self.assertFalse(receipt["global_exhaustion"])
        outside = self.validation_for(1_201)
        matches = outside["outside_scope_gap_scans"][0]["matching_certificates"]
        self.assertTrue(any(item["gap"] == 23 and item["divisor"] == 34 for item in matches))

    def test_validator_and_consumer_reject_terminal_hits(self) -> None:
        for prime in (73, 193, 241_441):
            with self.subTest(prime=prime):
                value = self.case(prime)
                owner_receipt = self.owner_for(prime)
                with self.assertRaises(scope_validator.ScopeValidationError) as raised:
                    scope_validator.validate_q_one_registered_prefix_e1_scope_v2(
                        raw_q_one_g=value["raw"],
                        source_body=value["body"],
                        root_anchor=value["anchor"],
                        source_state=value["state"],
                        root_actualness=value["actualness"],
                        owner_receipt=owner_receipt,
                        terminal_receipt=value["terminal"],
                        role_grant=_grant(scope_validator),
                    )
                self.assertEqual(
                    raised.exception.code,
                    scope_validator.ScopeValidationRejectCode.TERMINAL_SOURCE_NOT_MISS,
                )
                with self.assertRaises(consumer.ConsumerError) as raised:
                    consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
                        raw_q_one_g=value["raw"],
                        source_body=value["body"],
                        root_anchor=value["anchor"],
                        source_state=value["state"],
                        root_actualness=value["actualness"],
                        owner_receipt=owner_receipt,
                        terminal_receipt=value["terminal"],
                        scope_validation_receipt={},
                        role_grant=_grant(consumer),
                    )
                self.assertEqual(
                    raised.exception.code,
                    consumer.ConsumerRejectCode.TERMINAL_SOURCE_NOT_MISS,
                )

    def test_consumer_issues_only_root_source_scoped_e1(self) -> None:
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                value = self.case(prime)
                result = consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
                    raw_q_one_g=value["raw"],
                    source_body=value["body"],
                    root_anchor=value["anchor"],
                    source_state=value["state"],
                    root_actualness=value["actualness"],
                    owner_receipt=self.owner_for(prime),
                    terminal_receipt=value["terminal"],
                    scope_validation_receipt=self.validation_for(prime),
                    role_grant=_grant(consumer),
                )
                wire = consumer.root_source_scoped_e1_receipt_to_mapping_v2(result)
                self.assertEqual(wire["status"], consumer.STATUS)
                self.assertTrue(wire["root_source_scoped_e1"])
                self.assertTrue(wire["scope_aware_consumer_authority"])
                self.assertTrue(wire["root_source_occurrence_authority"])
                self.assertFalse(wire["e1_authority"])
                for field in (
                    "generic_e1",
                    "successor_e1",
                    "producer_authority",
                    "producer_continuation_allowed",
                    "persistent_admission",
                    "queue_authority",
                    "e2_authority",
                    "e3_authority",
                    "e4_authority",
                    "e5_authority",
                ):
                    self.assertFalse(wire[field], field)
                self.assertEqual(wire["math_replay"]["chart_r"], (prime - 1) // 24 * 16 + 3)
                self.assertFalse(wire["global_exhaustion"])

    def test_consumer_rejects_scope_owner_and_grant_swaps(self) -> None:
        value = self.case(1_201)
        owner_receipt = self.owner_for(1_201)
        validation = self.validation_for(1_201)
        bad_validation = copy.deepcopy(validation)
        bad_validation["common_owner_authority"] = True
        with self.assertRaises(consumer.ConsumerError) as raised:
            consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
                raw_q_one_g=value["raw"],
                source_body=value["body"],
                root_anchor=value["anchor"],
                source_state=value["state"],
                root_actualness=value["actualness"],
                owner_receipt=owner_receipt,
                terminal_receipt=value["terminal"],
                scope_validation_receipt=bad_validation,
                role_grant=_grant(consumer),
            )
        self.assertEqual(raised.exception.code, consumer.ConsumerRejectCode.DIGEST_MISMATCH)
        bad_grant = _grant(consumer)
        bad_grant["grant_id"] = "q1_scope_aware_e1_validator_grant_v4"
        with self.assertRaises(consumer.ConsumerError) as raised:
            consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
                raw_q_one_g=value["raw"],
                source_body=value["body"],
                root_anchor=value["anchor"],
                source_state=value["state"],
                root_actualness=value["actualness"],
                owner_receipt=owner_receipt,
                terminal_receipt=value["terminal"],
                scope_validation_receipt=validation,
                role_grant=bad_grant,
            )
        self.assertEqual(raised.exception.code, consumer.ConsumerRejectCode.GRANT_MISMATCH)

    def test_schema_accepts_three_wires_and_rejects_authority_or_prefix_mutations(self) -> None:
        validator = jsonschema.Draft202012Validator(SCHEMA)
        owner_wire = self.owner_for(1_201)
        validation_wire = self.validation_for(1_201)
        value = self.case(1_201)
        consumer_wire = consumer.root_source_scoped_e1_receipt_to_mapping_v2(
            consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
                raw_q_one_g=value["raw"],
                source_body=value["body"],
                root_anchor=value["anchor"],
                source_state=value["state"],
                root_actualness=value["actualness"],
                owner_receipt=owner_wire,
                terminal_receipt=value["terminal"],
                scope_validation_receipt=validation_wire,
                role_grant=_grant(consumer),
            )
        )
        for wire in (owner_wire, validation_wire, consumer_wire):
            self.assertEqual(list(validator.iter_errors(wire)), [])
        registry = json.loads(
            (ROOT / "data/t6-wave1/t6-coordinator-role-registry-v4.json").read_text(
                encoding="ascii"
            )
        )
        matrix = registry["receipt_authority_matrix"]
        for wire in (owner_wire, validation_wire, consumer_wire):
            expected = matrix[wire["receipt_type"]]
            self.assertTrue(set(expected) <= set(wire))
            self.assertEqual({name: wire[name] for name in expected}, expected)
        bad_owner = copy.deepcopy(owner_wire)
        bad_owner["owner_scope"] = "COMMON_PERSISTENT_SELECTOR_OWNER"
        self.assertTrue(list(validator.iter_errors(bad_owner)))
        bad_consumer = copy.deepcopy(consumer_wire)
        bad_consumer["e1_authority"] = True
        self.assertTrue(list(validator.iter_errors(bad_consumer)))

    def test_serializer_rejects_forged_authority_after_object_new(self) -> None:
        value = self.case(1_201)
        receipt = consumer.consume_q_one_registered_prefix_miss_for_e1_v2(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            owner_receipt=self.owner_for(1_201),
            terminal_receipt=value["terminal"],
            scope_validation_receipt=self.validation_for(1_201),
            role_grant=_grant(consumer),
        )
        forged = object.__new__(type(receipt))
        for field in fields(type(receipt)):
            field = field.name
            object.__setattr__(forged, field, getattr(receipt, field))
        object.__setattr__(forged, "e1_authority", True)
        with self.assertRaises(consumer.ConsumerError) as raised:
            consumer.root_source_scoped_e1_receipt_to_mapping_v2(forged)
        self.assertEqual(raised.exception.code, consumer.ConsumerRejectCode.DIGEST_MISMATCH)
        values = {field.name: getattr(forged, field.name) for field in fields(type(forged))}
        resealed = consumer.canonical_digest_v2(consumer._unsigned(values))
        object.__setattr__(forged, "receipt_id", consumer.RECEIPT_ID_PREFIX + resealed)
        object.__setattr__(forged, "digest", resealed)
        with self.assertRaises(consumer.ConsumerError) as raised:
            consumer.root_source_scoped_e1_receipt_to_mapping_v2(forged)
        self.assertEqual(raised.exception.code, consumer.ConsumerRejectCode.AUTHORITY_BOUNDARY_VIOLATION)


if __name__ == "__main__":
    unittest.main()
