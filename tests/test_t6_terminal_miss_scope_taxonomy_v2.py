from __future__ import annotations

import copy
from dataclasses import dataclass, fields
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
from types import MappingProxyType
import sys
import unittest

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_terminal_miss_scope_taxonomy_v2.py"
SCHEMA_PATH = ROOT / "schemas" / "t6-terminal-miss-scope-taxonomy-v2.schema.json"

SPEC = importlib.util.spec_from_file_location(
    "t6_terminal_miss_scope_taxonomy_v2_under_test", MODULE_PATH
)
assert SPEC and SPEC.loader
TAXONOMY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TAXONOMY
SPEC.loader.exec_module(TAXONOMY)


HEAD_SHA = "1" * 40


def digest(label: str) -> str:
    return TAXONOMY.canonical_digest_v2({"artifact": label, "version": 2})


def reseal(mapping: dict) -> dict:
    result = copy.deepcopy(mapping)
    result.pop("digest", None)
    result["digest"] = TAXONOMY.canonical_digest_v2(result)
    return result


def common_fields() -> dict:
    return {
        "head_sha": HEAD_SHA,
        "evidence_class": TAXONOMY.EVIDENCE_ONLY,
        "e1_authority": False,
        "queue_authority": False,
        "registry_id": TAXONOMY.COORDINATOR_ROLE_REGISTRY_ID_V2,
        "registry_version": 2,
        "registry_digest": digest("coordinator-role-registry"),
        "subject_kind": TAXONOMY.SOURCE_STATE,
        "subject_id": "state:q1-g:1201",
        "subject_digest": digest("state:q1-g:1201"),
        "scheduler_input_digest": digest("scheduler-input:q1-g:1201"),
        "owner_domain_id": "owner-domain:q1-g-root-source:v2",
        "owner_domain_digest": digest("owner-domain:q1-g-root-source:v2"),
        "domain_membership_replay_id": "domain-replay:q1-g-root-source:v2",
        "domain_membership_replay_artifact_digest": digest("domain-replay-artifact"),
        "domain_membership_replay_digest": digest("domain-replay-result:1201"),
    }


def prefix_mapping() -> dict:
    value = {
        "receipt_type": "RegisteredPriorityPrefixMissReceiptV2",
        "schema_version": 2,
        **common_fields(),
        "schedule_id": "q1_g_root_full_divisor_gap3_7_11_priority_prefix_v2",
        "schedule_digest": digest("schedule:gap3-7-11"),
        "ordered_gaps": [3, 7, 11],
        "ordered_family_ids": [
            "bradford_full_divisor_gap3_v2",
            "bradford_full_divisor_gap7_v2",
            "bradford_full_divisor_gap11_v2",
        ],
        "ordered_family_definition_digests": [
            digest("family:gap3"),
            digest("family:gap7"),
            digest("family:gap11"),
        ],
        "ordered_local_miss_digests": [
            digest("miss:gap3:1201"),
            digest("miss:gap7:1201"),
            digest("miss:gap11:1201"),
        ],
        "next_unchecked_gap": 15,
        "coverage_semantics": TAXONOMY.REGISTERED_PRIORITY_ONLY,
        "coverage_theorem_id": "claim:q1-gap3-7-11-prefix-coverage-v2",
        "coverage_theorem_digest": digest("coverage-theorem:prefix"),
        "coverage_reproduction_id": "reproduction:q1-gap3-7-11-prefix-v2",
        "coverage_reproduction_digest": digest("coverage-reproduction:prefix"),
        "coverage_verifier_id": "validator:q1-gap3-7-11-prefix-independent-v2",
        "coverage_verifier_digest": digest("coverage-verifier:prefix"),
        "coverage_replay_digest": digest("coverage-replay:prefix:1201"),
        "global_exhaustion": False,
        "outcome": TAXONOMY.MISS_REGISTERED_PRIORITY_COMPLETE,
    }
    return reseal(value)


def universe_mapping(prime: int = 1201) -> dict:
    gap_count = (prime - 1) // 4
    value = {
        "receipt_type": "TerminalUniverseMissReceiptV2",
        "schema_version": 2,
        **common_fields(),
        "terminal_universe_id": "bradford_natural_terminal_universe_v2",
        "terminal_universe_digest": digest("terminal-universe"),
        "root_prime": prime,
        "root_primality_verifier_id": "validator:root-primality:v2",
        "root_primality_verifier_artifact_digest": digest("root-primality-verifier"),
        "root_primality_replay_digest": digest("root-primality-replay"),
        "natural_gap_start": 3,
        "natural_gap_stop": prime - 2,
        "natural_gap_step": 4,
        "natural_gap_count": gap_count,
        "checked_gap_count": gap_count,
        "checked_divisor_count": gap_count * 3,
        "hit_count": 0,
        "range_definition_id": "claim:core-natural-gap-range-v2",
        "range_definition_digest": digest("natural-range"),
        "scan_algorithm_id": "algorithm:full-bradford-divisor-universe-v2",
        "scan_algorithm_digest": digest("scan-algorithm"),
        "factorization_verifier_id": "validator:factorization-lattice-v2",
        "factorization_verifier_digest": digest("factorization-verifier"),
        "factorization_manifest_digest": digest("factorization-manifest"),
        "divisor_lattice_manifest_digest": digest("divisor-lattice-manifest"),
        "scan_transcript_digest": digest("scan-transcript"),
        "reverse_equivalence_claim_id": "claim:short-certificate-equivalence-v2",
        "reverse_equivalence_claim_digest": digest("reverse-equivalence-claim"),
        "reverse_equivalence_proof_id": "proof:short-certificate-reverse-v2",
        "reverse_equivalence_proof_digest": digest("reverse-equivalence-proof"),
        "reverse_equivalence_verifier_id": "validator:short-certificate-reverse-v2",
        "reverse_equivalence_verifier_digest": digest("reverse-equivalence-verifier"),
        "reverse_equivalence_replay_digest": digest("reverse-equivalence-replay"),
        "global_exhaustion": True,
        "outcome": TAXONOMY.TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY,
    }
    return reseal(value)


def positive_divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


@dataclass(frozen=True, slots=True)
class EvilPrefix(TAXONOMY.RegisteredPriorityPrefixMissReceiptV2):
    queue_gate: str = "ADMITTED_SUCCESSOR"


class StringSubclass(str):
    pass


class IntSubclass(int):
    pass


class TerminalMissScopeTaxonomyV2Tests(unittest.TestCase):
    def test_prefix_round_trip_is_explicitly_non_global(self) -> None:
        parsed = TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
            prefix_mapping()
        )
        self.assertEqual(parsed.ordered_gaps, (3, 7, 11))
        self.assertEqual(parsed.next_unchecked_gap, 15)
        self.assertIs(parsed.global_exhaustion, False)
        self.assertIs(parsed.e1_authority, False)
        self.assertEqual(
            TAXONOMY.receipt_to_mapping_v2(parsed), prefix_mapping()
        )

    def test_universe_round_trip_remains_shape_only(self) -> None:
        parsed = TAXONOMY.parse_terminal_universe_miss_receipt_v2(
            universe_mapping()
        )
        self.assertEqual(parsed.natural_gap_count, 300)
        self.assertEqual(parsed.natural_gap_stop, 1199)
        self.assertIs(parsed.global_exhaustion, True)
        self.assertEqual(
            parsed.outcome, TAXONOMY.TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY
        )

    def test_p1201_separates_prefix_miss_from_global_gap23_hit(self) -> None:
        prime = 1201
        for gap in (3, 7, 11):
            x_value = (prime + gap) // 4
            hits = [
                divisor
                for divisor in positive_divisors(x_value * x_value)
                if (prime * x_value + divisor) % gap == 0
                or (divisor <= x_value and (x_value + divisor) % gap == 0)
            ]
            self.assertEqual(hits, [])
        gap = 23
        divisor = 34
        x_value = (prime + gap) // 4
        y_value = (prime * x_value + divisor) // gap
        z_value = prime * (x_value + prime * x_value * x_value // divisor) // gap
        self.assertEqual((x_value, y_value, z_value), (306, 15980, 172727820))
        self.assertEqual(
            Fraction(1, x_value) + Fraction(1, y_value) + Fraction(1, z_value),
            Fraction(4, prime),
        )
        self.assertFalse(
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
                prefix_mapping()
            ).global_exhaustion
        )
        shape_only = TAXONOMY.parse_terminal_universe_miss_receipt_v2(
            universe_mapping(prime)
        )
        self.assertEqual(
            shape_only.outcome, TAXONOMY.TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY
        )
        self.assertEqual(shape_only.hit_count, 0)
        self.assertIs(shape_only.e1_authority, False)

    def test_each_parser_rejects_the_other_exact_type(self) -> None:
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as first:
            TAXONOMY.parse_terminal_universe_miss_receipt_v2(prefix_mapping())
        self.assertEqual(
            first.exception.code, TAXONOMY.TerminalMissScopeRejectCode.RECEIPT_TYPE_MISMATCH
        )
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as second:
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
                universe_mapping()
            )
        self.assertEqual(
            second.exception.code, TAXONOMY.TerminalMissScopeRejectCode.RECEIPT_TYPE_MISMATCH
        )

    def test_local_and_v1_receipts_cannot_enter_v2(self) -> None:
        for receipt_type in (
            "TerminalMissV1",
            "LocalTerminalMissReceiptV1",
            "CompleteTerminalMissReceiptV1",
        ):
            with self.subTest(receipt_type=receipt_type):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
                    TAXONOMY.parse_terminal_miss_scope_receipt_v2(
                        {"receipt_type": receipt_type}
                    )
                self.assertEqual(
                    raised.exception.code,
                    TAXONOMY.TerminalMissScopeRejectCode.LEGACY_OR_LOCAL_RECEIPT,
                )

    def test_subclass_cannot_add_queue_authority(self) -> None:
        parsed = TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
            prefix_mapping()
        )
        evil = EvilPrefix(
            **{field.name: getattr(parsed, field.name) for field in fields(type(parsed))}
        )
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
            TAXONOMY.parse_terminal_miss_scope_receipt_v2(evil)
        self.assertEqual(
            raised.exception.code, TAXONOMY.TerminalMissScopeRejectCode.SUBCLASS_REJECTED
        )

    def test_direct_dataclass_cannot_smuggle_list_into_tuple_field(self) -> None:
        parsed = TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
            prefix_mapping()
        )
        values = {field.name: getattr(parsed, field.name) for field in fields(type(parsed))}
        values["ordered_gaps"] = [3, 7, 11]
        malformed = TAXONOMY.RegisteredPriorityPrefixMissReceiptV2(**values)
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(malformed)
        self.assertEqual(
            raised.exception.code,
            TAXONOMY.TerminalMissScopeRejectCode.MALFORMED_FIELD,
        )

    def test_bool_cannot_spoof_integer_fields(self) -> None:
        mutations = []
        for field_name in ("schema_version", "registry_version", "next_unchecked_gap"):
            value = prefix_mapping()
            value[field_name] = True
            mutations.append(reseal(value))
        for field_name in ("root_prime", "natural_gap_count", "checked_divisor_count"):
            value = universe_mapping()
            value[field_name] = True
            mutations.append(reseal(value))
        for value in mutations:
            with self.subTest(receipt_type=value["receipt_type"]):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
                    TAXONOMY.parse_terminal_miss_scope_receipt_v2(value)

    def test_builtin_subclasses_are_rejected_for_keys_and_scalar_fields(self) -> None:
        mutations = []

        text_value = prefix_mapping()
        text_value["schedule_id"] = StringSubclass(text_value["schedule_id"])
        mutations.append(text_value)

        digest_value = prefix_mapping()
        digest_value["schedule_digest"] = StringSubclass(digest_value["schedule_digest"])
        mutations.append(digest_value)

        head_value = prefix_mapping()
        head_value["head_sha"] = StringSubclass(head_value["head_sha"])
        mutations.append(head_value)

        int_value = prefix_mapping()
        int_value["next_unchecked_gap"] = IntSubclass(15)
        mutations.append(int_value)

        gap_value = prefix_mapping()
        gap_value["ordered_gaps"][0] = IntSubclass(3)
        mutations.append(gap_value)

        key_value = prefix_mapping()
        schedule_id = key_value.pop("schedule_id")
        key_value[StringSubclass("schedule_id")] = schedule_id
        mutations.append(key_value)

        for index, value in enumerate(mutations):
            with self.subTest(index=index):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
                    TAXONOMY.parse_terminal_miss_scope_receipt_v2(value)
                self.assertEqual(
                    raised.exception.code,
                    TAXONOMY.TerminalMissScopeRejectCode.MALFORMED_FIELD,
                )

    def test_attacker_reseal_cannot_add_e1_or_queue_authority(self) -> None:
        for field_name in ("e1_authority", "queue_authority"):
            value = prefix_mapping()
            value[field_name] = True
            value = reseal(value)
            with self.subTest(field_name=field_name):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
                    TAXONOMY.parse_terminal_miss_scope_receipt_v2(value)
                self.assertEqual(
                    raised.exception.code,
                    TAXONOMY.TerminalMissScopeRejectCode.SCOPE_SEMANTICS_MISMATCH,
                )

    def test_resealed_scope_swap_is_only_rejected_by_shape_constants(self) -> None:
        prefix = prefix_mapping()
        prefix["global_exhaustion"] = True
        prefix["outcome"] = TAXONOMY.TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(reseal(prefix))

        universe = universe_mapping()
        universe["global_exhaustion"] = False
        universe["outcome"] = TAXONOMY.MISS_REGISTERED_PRIORITY_COMPLETE
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
            TAXONOMY.parse_terminal_universe_miss_receipt_v2(reseal(universe))

    def test_prefix_must_be_contiguous_and_name_next_gap(self) -> None:
        for gaps, next_gap in (([3, 11], 15), ([3, 7, 11], 19)):
            value = prefix_mapping()
            value["ordered_gaps"] = gaps
            value["next_unchecked_gap"] = next_gap
            if len(gaps) == 2:
                for name in (
                    "ordered_family_ids",
                    "ordered_family_definition_digests",
                    "ordered_local_miss_digests",
                ):
                    value[name] = value[name][:2]
            with self.subTest(gaps=gaps, next_gap=next_gap):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
                    TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(
                        reseal(value)
                    )

    def test_universe_range_and_zero_hit_are_derived_from_root_prime(self) -> None:
        mutations = {
            "stop": ("natural_gap_stop", 1195),
            "count": ("natural_gap_count", 299),
            "checked": ("checked_gap_count", 299),
            "hit": ("hit_count", 1),
        }
        for name, (field_name, replacement) in mutations.items():
            value = universe_mapping()
            value[field_name] = replacement
            with self.subTest(name=name):
                with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
                    TAXONOMY.parse_terminal_universe_miss_receipt_v2(reseal(value))

    def test_unknown_field_tuple_and_mapping_subclass_fail(self) -> None:
        extra = prefix_mapping()
        extra["queue_gate"] = "ADMITTED_SUCCESSOR"
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(reseal(extra))

        tuple_value = prefix_mapping()
        tuple_value["ordered_gaps"] = tuple(tuple_value["ordered_gaps"])
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(tuple_value)

        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError):
            TAXONOMY.parse_terminal_miss_scope_receipt_v2(
                MappingProxyType(prefix_mapping())
            )

    def test_digest_tamper_fails(self) -> None:
        value = prefix_mapping()
        value["coverage_replay_digest"] = digest("tampered")
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as raised:
            TAXONOMY.parse_registered_priority_prefix_miss_receipt_v2(value)
        self.assertEqual(
            raised.exception.code, TAXONOMY.TerminalMissScopeRejectCode.DIGEST_MISMATCH
        )

    def test_both_current_outcomes_fail_closed_for_producer_continuation(self) -> None:
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as prefix:
            TAXONOMY.reject_producer_continuation_v2(prefix_mapping())
        self.assertEqual(
            prefix.exception.code,
            TAXONOMY.TerminalMissScopeRejectCode.REGISTRY_V2_AUTHORIZATION_REQUIRED,
        )
        with self.assertRaises(TAXONOMY.TerminalMissScopeValidationError) as universe:
            TAXONOMY.reject_producer_continuation_v2(universe_mapping())
        self.assertEqual(
            universe.exception.code,
            TAXONOMY.TerminalMissScopeRejectCode.TERMINAL_UNIVERSE_FORBIDS_PRODUCER,
        )

    def test_schema_field_sets_and_examples_match_parser(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        validator = Draft202012Validator(schema)
        for receipt_class, mapping in (
            (TAXONOMY.RegisteredPriorityPrefixMissReceiptV2, prefix_mapping()),
            (TAXONOMY.TerminalUniverseMissReceiptV2, universe_mapping()),
        ):
            with self.subTest(receipt_type=receipt_class.RECEIPT_TYPE):
                required = set(schema["$defs"][receipt_class.RECEIPT_TYPE]["required"])
                expected = {field.name for field in fields(receipt_class)} | {
                    "receipt_type",
                    "schema_version",
                }
                self.assertEqual(required, expected)
                self.assertEqual(list(validator.iter_errors(mapping)), [])

    def test_module_exposes_no_issuer_or_queue_api(self) -> None:
        summary = TAXONOMY.scope_taxonomy_summary_v2()
        self.assertIs(summary["production_issuer_present"], False)
        self.assertIs(summary["semantic_verifier_present"], False)
        self.assertIs(summary["declared_artifacts_executed"], False)
        self.assertIs(summary["shape_only"], True)
        self.assertIs(summary["e1_authority_present"], False)
        self.assertIs(summary["queue_authority_present"], False)
        for name in (
            "issue_registered_priority_prefix_miss_v2",
            "issue_terminal_universe_miss_v2",
            "enqueue_from_terminal_miss_v2",
            "authorize_e1_from_prefix_miss_v2",
        ):
            self.assertFalse(hasattr(TAXONOMY, name))


if __name__ == "__main__":
    unittest.main()
