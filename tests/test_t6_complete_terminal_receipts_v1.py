from __future__ import annotations

import copy
from dataclasses import dataclass, fields
import importlib.util
import inspect
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_complete_terminal_receipts_v1.py"


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RECEIPTS = load_module("t6_complete_terminal_receipts_v1_under_test")


@dataclass(frozen=True, slots=True)
class EvilLocal(RECEIPTS.LocalTerminalMissReceiptV1):
    queue_gate: bool = True


@dataclass(frozen=True, slots=True)
class EvilComplete(RECEIPTS.CompleteTerminalMissReceiptV1):
    queue_gate: bool = True
    e1: bool = True

RUNTIME_PATH = ROOT / "scripts" / "t6_persistent_selector_runtime_v1.py"
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))
RUNTIME_SPEC = importlib.util.spec_from_file_location(
    "t6_persistent_selector_runtime_v1_legacy_miss_under_test", RUNTIME_PATH
)
assert RUNTIME_SPEC and RUNTIME_SPEC.loader
LEGACY_RUNTIME = importlib.util.module_from_spec(RUNTIME_SPEC)
sys.modules[RUNTIME_SPEC.name] = LEGACY_RUNTIME
RUNTIME_SPEC.loader.exec_module(LEGACY_RUNTIME)


HEAD_SHA = "1" * 40
SOURCE_SCHEDULE = "q_one_gap_three_then_odd_low_gap_seven_v1"
TARGET_SCHEDULE = "q_one_full_carrier_target_sink_v1"


def digest(label: str) -> str:
    return RECEIPTS.canonical_digest_v1({"test_label": label})


def source_material(state_id: str = "state:source"):
    source = {"state_id": state_id, "prime": 73, "owner": "source.owner"}
    binding = {
        "subject_kind": RECEIPTS.SOURCE_STATE,
        "source_state_id": state_id,
        "source_state_digest": RECEIPTS.canonical_digest_v1(source),
    }
    scheduler_input = {
        "subject_binding": binding,
        "terminal_policy_input_digest": digest("source-policy-input"),
    }
    return source, scheduler_input


def source_binding(state_id: str = "state:source"):
    source, scheduler_input = source_material(state_id)
    return RECEIPTS.bind_source_subject_v1(source, scheduler_input)


def target_material():
    source = {"state_id": "state:source", "prime": 73}
    projection = {
        "projection_id": "projection:target",
        "chart_R": 51,
        "chart_K": 931,
    }
    binding = {
        "subject_kind": RECEIPTS.TARGET_PROJECTION,
        "source_state_id": source["state_id"],
        "source_state_digest": RECEIPTS.canonical_digest_v1(source),
        "projection_id": projection["projection_id"],
        "projection_digest": RECEIPTS.canonical_digest_v1(projection),
    }
    scheduler_input = {
        "subject_binding": binding,
        "terminal_policy_input_digest": digest("target-policy-input"),
    }
    return source, projection, scheduler_input


def target_binding():
    source, projection, scheduler_input = target_material()
    return RECEIPTS.bind_target_projection_subject_v1(
        source, projection, scheduler_input
    )


def make_local(subject=None):
    subject = source_binding() if subject is None else subject
    return RECEIPTS.make_local_terminal_miss_receipt_v1(
        subject=subject,
        schedule_id=SOURCE_SCHEDULE,
        family_id="q_one_gap_three",
        attempt_index=0,
        evaluator_id="evaluator:q1-gap-three:v1",
        evaluator_digest=digest("evaluator"),
        input_digest=digest("input"),
        output_digest=digest("output"),
    )


def reseal_receipt(payload: dict) -> dict:
    result = copy.deepcopy(payload)
    result.pop("digest", None)
    result["digest"] = RECEIPTS.canonical_digest_v1(result)
    return result


def forged_complete_mapping(subject=None) -> dict:
    subject = source_binding() if subject is None else subject
    registry = RECEIPTS.load_production_registry_v1()
    payload = {
        "receipt_type": "CompleteTerminalMissReceiptV1",
        "schema_version": 1,
        "head_sha": HEAD_SHA,
        "authority_class": RECEIPTS.PRODUCTION,
        "registry_id": registry.registry_id,
        "registry_class": RECEIPTS.PRODUCTION,
        "registry_digest": registry.registry_digest,
        "schedule_id": "forged.complete.schedule.v1",
        "schedule_digest": digest("forged-schedule"),
        "schedule_registry_digest": registry.registry_digest,
        "subject_kind": subject.subject_kind,
        "subject_id": subject.subject_id,
        "subject_digest": subject.subject_digest,
        "scheduler_input_digest": subject.scheduler_input_digest,
        "owner_domain_id": "owner-domain:forged:v1",
        "owner_domain_digest": digest("owner-domain"),
        "domain_membership_replay_id": "domain-replay:forged:v1",
        "domain_membership_replay_artifact_digest": digest(
            "domain-replay-artifact"
        ),
        "domain_membership_replay_digest": digest("domain-replay"),
        "ordered_family_ids": ["family:forged"],
        "ordered_local_miss_digests": [digest("local-miss")],
        "coverage_theorem_id": "coverage-theorem:forged:v1",
        "coverage_theorem_digest": digest("coverage-theorem"),
        "coverage_reproduction_id": "coverage-reproduction:forged:v1",
        "coverage_reproduction_digest": digest("coverage-reproduction"),
        "coverage_verifier_id": "coverage-verifier:forged:v1",
        "coverage_verifier_digest": digest("coverage-verifier"),
        "coverage_replay_digest": digest("coverage-replay"),
        "outcome": RECEIPTS.MISS_COMPLETE,
    }
    return reseal_receipt(payload)


def raw_registry() -> dict:
    return json.loads(
        (
            ROOT
            / "data"
            / "t6-wave1"
            / "t6-complete-terminal-schedule-registry-v1.json"
        ).read_text(encoding="utf-8")
    )


class CompleteTerminalReceiptFoundationTests(unittest.TestCase):
    def test_production_registry_is_zero_complete_and_non_authorizing(self) -> None:
        registry = RECEIPTS.load_production_registry_v1()
        summary = RECEIPTS.production_registry_summary_v1()
        self.assertEqual(summary["registry_class"], RECEIPTS.PRODUCTION)
        self.assertEqual(
            summary["status"], RECEIPTS.NO_COMPLETE_SCHEDULE_AUTHORITY
        )
        self.assertEqual(
            summary["head_authority_status"],
            RECEIPTS.HEAD_ROLE_REGISTRY_REQUIRED,
        )
        self.assertEqual(summary["complete_schedule_count"], 0)
        self.assertIs(summary["complete_miss_issuance_enabled"], False)
        self.assertEqual(len(registry.local_schedules), 6)
        self.assertTrue(
            all(
                schedule["classification"] == RECEIPTS.LOCAL_ONLY
                for schedule in registry.local_schedules
            )
        )

    def test_local_receipt_is_strictly_sealed_but_never_global(self) -> None:
        subject = source_binding()
        local = make_local(subject)
        mapping = RECEIPTS.receipt_to_mapping_v1(local)
        parsed = RECEIPTS.parse_local_terminal_miss_receipt_v1(mapping)
        bound = RECEIPTS.verify_local_terminal_miss_binding_v1(parsed, subject)
        self.assertEqual(bound.outcome, RECEIPTS.MISS_LOCAL)
        self.assertNotIn("persistent_queue", mapping)
        self.assertNotIn("certificate_payload", mapping)
        for value in (local, mapping):
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(
                    RECEIPTS.TerminalReceiptValidationError
                ) as error:
                    RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                        value, subject, HEAD_SHA
                    )
                self.assertEqual(
                    error.exception.code,
                    RECEIPTS.TerminalReceiptRejectCode.LOCAL_AS_GLOBAL,
                )

    def test_local_receipt_binds_scheduler_input_not_only_subject(self) -> None:
        subject = source_binding()
        local = make_local(subject)
        source, changed_input = source_material()
        changed_input["terminal_policy_input_digest"] = digest("different-policy")
        same_subject_different_input = RECEIPTS.bind_source_subject_v1(
            source, changed_input
        )
        self.assertEqual(subject.subject_id, same_subject_different_input.subject_id)
        self.assertEqual(
            subject.subject_digest, same_subject_different_input.subject_digest
        )
        self.assertNotEqual(
            subject.scheduler_input_digest,
            same_subject_different_input.scheduler_input_digest,
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_local_terminal_miss_binding_v1(
                local, same_subject_different_input
            )
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
        )

    def test_legacy_terminal_miss_cannot_enter_complete_verifier(self) -> None:
        legacy = LEGACY_RUNTIME.TerminalMissV1(
            schedule_id="legacy", scope="local", evidence_id="self-asserted"
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                legacy, source_binding(), HEAD_SHA
            )
        self.assertEqual(
            error.exception.code, RECEIPTS.TerminalReceiptRejectCode.INPUT_NOT_MAPPING
        )

    def test_well_formed_forged_complete_mapping_always_fails_closed(self) -> None:
        subject = source_binding()
        forged = forged_complete_mapping(subject)
        parsed = RECEIPTS.parse_complete_terminal_miss_receipt_v1(forged)
        self.assertEqual(parsed.outcome, RECEIPTS.MISS_COMPLETE)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                forged, subject, HEAD_SHA
            )
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.SCHEDULE_NOT_COMPLETE,
        )

    def test_typed_complete_object_also_cannot_become_verified(self) -> None:
        subject = source_binding()
        typed = RECEIPTS.parse_complete_terminal_miss_receipt_v1(
            forged_complete_mapping(subject)
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                typed, subject, HEAD_SHA
            )
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.SCHEDULE_NOT_COMPLETE,
        )

    def test_receipt_subclasses_cannot_add_authority_fields(self) -> None:
        local = make_local()
        evil_local = EvilLocal(
            **{field.name: getattr(local, field.name) for field in fields(type(local))}
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.parse_local_terminal_miss_receipt_v1(evil_local)
        self.assertEqual(
            error.exception.code, RECEIPTS.TerminalReceiptRejectCode.INPUT_NOT_MAPPING
        )

        complete = RECEIPTS.parse_complete_terminal_miss_receipt_v1(
            forged_complete_mapping()
        )
        evil_complete = EvilComplete(
            **{
                field.name: getattr(complete, field.name)
                for field in fields(type(complete))
            }
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                evil_complete, source_binding(), HEAD_SHA
            )
        self.assertEqual(
            error.exception.code, RECEIPTS.TerminalReceiptRejectCode.INPUT_NOT_MAPPING
        )

    def test_test_only_authority_is_rejected_at_type_boundary(self) -> None:
        subject = source_binding()
        forged = forged_complete_mapping(subject)
        forged["authority_class"] = "TEST_ONLY"
        forged["registry_class"] = "TEST_ONLY"
        forged = reseal_receipt(forged)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                forged, subject, HEAD_SHA
            )
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.REGISTRY_BINDING_MISMATCH,
        )
        self.assertNotIn(
            "coordinator_registry",
            inspect.signature(
                RECEIPTS.verify_complete_terminal_miss_receipt_v1
            ).parameters,
        )
        self.assertFalse(hasattr(RECEIPTS, "TerminalArtifactManifestV1"))
        self.assertFalse(hasattr(RECEIPTS, "replay_complete_terminal_schedule_v1"))

    def test_source_and_projection_bindings_are_not_interchangeable(self) -> None:
        source = source_binding()
        target = target_binding()
        self.assertEqual(source.subject_kind, RECEIPTS.SOURCE_STATE)
        self.assertEqual(source.subject_id, source.source_state_id)
        self.assertEqual(target.subject_kind, RECEIPTS.TARGET_PROJECTION)
        self.assertEqual(target.subject_id, target.projection_id)
        self.assertNotEqual(target.subject_digest, target.source_state_digest)

        source_payload, projection, scheduler_input = target_material()
        changed_projection = dict(projection)
        changed_projection["chart_K"] += 1
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.bind_target_projection_subject_v1(
                source_payload, changed_projection, scheduler_input
            )
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
        )

        source_payload, scheduler_input = source_material()
        scheduler_input["subject_binding"]["subject_kind"] = (
            RECEIPTS.TARGET_PROJECTION
        )
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError):
            RECEIPTS.bind_source_subject_v1(source_payload, scheduler_input)

    def test_complete_binding_mutations_fail_before_schedule_lookup(self) -> None:
        subject = source_binding()
        cases = {
            "head": ("head_sha", "2" * 40),
            "registry": ("registry_digest", "3" * 64),
            "subject": ("subject_id", "state:other"),
            "scheduler_input": ("scheduler_input_digest", "4" * 64),
        }
        expected_codes = {
            "head": RECEIPTS.TerminalReceiptRejectCode.REGISTRY_BINDING_MISMATCH,
            "registry": RECEIPTS.TerminalReceiptRejectCode.REGISTRY_BINDING_MISMATCH,
            "subject": RECEIPTS.TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
            "scheduler_input": RECEIPTS.TerminalReceiptRejectCode.SUBJECT_BINDING_MISMATCH,
        }
        for case_id, (field_name, value) in cases.items():
            forged = forged_complete_mapping(subject)
            forged[field_name] = value
            forged = reseal_receipt(forged)
            with self.subTest(case_id=case_id):
                with self.assertRaises(
                    RECEIPTS.TerminalReceiptValidationError
                ) as error:
                    RECEIPTS.verify_complete_terminal_miss_receipt_v1(
                        forged, subject, HEAD_SHA
                    )
                self.assertEqual(error.exception.code, expected_codes[case_id])

    def test_registry_rejects_test_only_complete_bool_and_nonarrays(self) -> None:
        mutations = {}

        test_only = raw_registry()
        test_only["registry_class"] = "TEST_ONLY"
        mutations["test_only"] = RECEIPTS.seal_registry_mapping_v1(test_only)

        complete = raw_registry()
        complete["complete_schedules"] = [{"schedule_id": "forged"}]
        complete["invariants"]["complete_schedule_count"] = 1
        mutations["complete"] = RECEIPTS.seal_registry_mapping_v1(complete)

        bool_version = raw_registry()
        bool_version["schema_version"] = True
        mutations["bool_version"] = RECEIPTS.seal_registry_mapping_v1(bool_version)

        bool_count = raw_registry()
        bool_count["invariants"]["complete_schedule_count"] = False
        mutations["bool_count"] = RECEIPTS.seal_registry_mapping_v1(bool_count)

        nonarray = raw_registry()
        nonarray["local_schedules"] = tuple(nonarray["local_schedules"])
        unsigned = copy.deepcopy(nonarray)
        unsigned.pop("registry_digest")
        nonarray["registry_digest"] = RECEIPTS.canonical_digest_v1(unsigned)
        mutations["nonarray"] = nonarray

        nonmapping = raw_registry()
        nonmapping["local_schedules"][0] = "not-a-mapping"
        mutations["nonmapping"] = RECEIPTS.seal_registry_mapping_v1(nonmapping)

        for mutation_id, value in mutations.items():
            with self.subTest(mutation_id=mutation_id):
                with self.assertRaises(RECEIPTS.TerminalReceiptValidationError):
                    RECEIPTS.parse_production_registry_v1(value)

    def test_receipt_parser_is_bool_safe_and_rejects_extra_authority_fields(self) -> None:
        local = RECEIPTS.receipt_to_mapping_v1(make_local())
        bool_version = copy.deepcopy(local)
        bool_version["schema_version"] = True
        bool_version = reseal_receipt(bool_version)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError):
            RECEIPTS.parse_local_terminal_miss_receipt_v1(bool_version)

        bool_index = copy.deepcopy(local)
        bool_index["attempt_index"] = False
        bool_index = reseal_receipt(bool_index)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError):
            RECEIPTS.parse_local_terminal_miss_receipt_v1(bool_index)

        extra = copy.deepcopy(local)
        extra["persistent_queue"] = True
        extra = reseal_receipt(extra)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError) as error:
            RECEIPTS.parse_local_terminal_miss_receipt_v1(extra)
        self.assertEqual(
            error.exception.code,
            RECEIPTS.TerminalReceiptRejectCode.FIELD_SET_MISMATCH,
        )

        complete = forged_complete_mapping()
        complete["ordered_family_ids"] = tuple(complete["ordered_family_ids"])
        complete = reseal_receipt(complete)
        with self.assertRaises(RECEIPTS.TerminalReceiptValidationError):
            RECEIPTS.parse_complete_terminal_miss_receipt_v1(complete)

    def test_schema_and_parser_field_sets_remain_in_parity(self) -> None:
        schema = json.loads(
            (
                ROOT
                / "schemas"
                / "t6-complete-terminal-miss-receipt-v1.schema.json"
            ).read_text(encoding="utf-8")
        )
        pairs = (
            (
                RECEIPTS.LocalTerminalMissReceiptV1,
                schema["$defs"]["localTerminalMissReceiptV1"],
            ),
            (
                RECEIPTS.CompleteTerminalMissReceiptV1,
                schema["$defs"]["completeTerminalMissReceiptV1"],
            ),
        )
        for cls, definition in pairs:
            expected = {field.name for field in fields(cls)} | {
                "receipt_type",
                "schema_version",
            }
            with self.subTest(receipt_type=cls.RECEIPT_TYPE):
                self.assertEqual(set(definition["required"]), expected)
                self.assertEqual(set(definition["properties"]), expected)
                self.assertIs(definition["additionalProperties"], False)
                self.assertEqual(
                    definition["properties"]["schema_version"]["type"],
                    "integer",
                )

    def test_cross_import_uses_canonical_mapping_not_class_identity(self) -> None:
        other = load_module("t6_complete_terminal_receipts_v1_cross_import")
        local = make_local()
        mapping = RECEIPTS.receipt_to_mapping_v1(local)
        parsed = other.parse_local_terminal_miss_receipt_v1(
            json.loads(RECEIPTS.canonical_json_v1(mapping))
        )
        self.assertEqual(
            other.canonical_json_v1(other.receipt_to_mapping_v1(parsed)),
            RECEIPTS.canonical_json_v1(mapping),
        )
        with self.assertRaises(other.TerminalReceiptValidationError) as error:
            other.parse_local_terminal_miss_receipt_v1(local)
        self.assertEqual(
            error.exception.code, other.TerminalReceiptRejectCode.INPUT_NOT_MAPPING
        )


if __name__ == "__main__":
    unittest.main()
