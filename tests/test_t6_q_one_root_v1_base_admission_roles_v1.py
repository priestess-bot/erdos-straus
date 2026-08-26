from __future__ import annotations

import copy
from dataclasses import fields
import inspect
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

import t6_persistent_selector_state_v1 as persistent_state  # noqa: E402
import t6_q_one_root_initializer_envelope_v2 as root_envelope  # noqa: E402
import t6_q_one_root_owner_classifier_v2 as owner  # noqa: E402
import t6_q_one_root_v1_base_admission_verifier_v1 as admission  # noqa: E402
import t6_q_one_root_v1_base_materializer_v1 as materializer  # noqa: E402
import t6_q_one_root_v1_terminal_adapter_v1 as terminal_adapter  # noqa: E402
import t6_q_one_scope_aware_e1_validator_v2 as scope_validator  # noqa: E402


SCHEMA = json.loads(
    (ROOT / "schemas/t6-q-one-root-v1-base-admission-v1.schema.json").read_text(
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


def issue(root: Path, head: str, raw: dict[str, object]) -> dict[str, object]:
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


def grant(module: object) -> dict[str, object]:
    return {
        "grant_id": module.GRANT_ID,
        "role": module.ROLE,
        "artifact_id": module.ARTIFACT_ID,
        "artifact_path": module.ARTIFACT_PATH,
        "artifact_symbols": list(module.ARTIFACT_SYMBOLS),
        "capabilities": list(module.CAPABILITIES),
        "authority_class": module.AUTHORITY_CLASS,
        "artifact_semantic_sha256": "a" * 64,
    }


def reseal_mapping(value: dict[str, object], prefix: str) -> dict[str, object]:
    result = copy.deepcopy(value)
    result.pop("receipt_id", None)
    result.pop("digest", None)
    digest = admission.canonical_digest_v1(result)
    result["receipt_id"] = prefix + digest
    result["digest"] = digest
    return result


def forge_admission_receipt(receipt, **updates):
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    values.update(updates)
    digest = admission.canonical_digest_v1(admission._unsigned(values))
    values.update({"receipt_id": admission.RECEIPT_ID_PREFIX + digest, "digest": digest})
    forged = object.__new__(type(receipt))
    for field in fields(type(receipt)):
        object.__setattr__(forged, field.name, values[field.name])
    return forged


class QOneRootV1BaseAdmissionRoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="q1-v1-base-")
        cls.fixture = RepositoryFixture(Path(cls.temp.name))
        cls.repo, cls.head = cls.fixture.commit()
        cls.cache: dict[int, dict[str, object]] = {}

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    @classmethod
    def case(cls, prime: int) -> dict[str, object]:
        cached = cls.cache.get(prime)
        if cached is not None:
            return cached
        raw = copy.deepcopy(RAW[prime])
        issued = issue(cls.repo, cls.head, raw)
        body = root_envelope.make_canonical_q_one_g_source_body_v2(raw)
        anchor = root_envelope.make_root_initializer_anchor_v2(body)
        state = root_envelope.make_raw_root_source_state_v2(body, anchor)
        result = {
            "raw": raw,
            "body": root_envelope.artifact_to_mapping_v2(body),
            "anchor": root_envelope.artifact_to_mapping_v2(anchor),
            "state": root_envelope.artifact_to_mapping_v2(state),
            "actualness": issued["actualness"],
            "terminal": issued["terminal"],
        }
        cls.cache[prime] = result
        return result

    @classmethod
    def owner_for(cls, prime: int) -> dict[str, object]:
        value = cls.case(prime)
        receipt = owner.classify_q_one_root_owner_v2(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            role_grant=grant(owner),
        )
        return owner.root_owner_receipt_to_mapping_v2(receipt)

    @classmethod
    def scope_for(cls, prime: int) -> dict[str, object]:
        value = cls.case(prime)
        receipt = scope_validator.validate_q_one_registered_prefix_e1_scope_v2(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            owner_receipt=cls.owner_for(prime),
            terminal_receipt=value["terminal"],
            role_grant=grant(scope_validator),
        )
        return scope_validator.scope_validation_receipt_to_mapping_v2(receipt)

    @classmethod
    def materialization_for(cls, prime: int):
        value = cls.case(prime)
        return materializer.materialize_q_one_root_v1_base_state_v1(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            terminal_receipt=value["terminal"],
            role_grant=grant(materializer),
        )

    @classmethod
    def admission_for(cls, prime: int):
        value = cls.case(prime)
        materialization = materializer.base_materialization_receipt_to_mapping_v1(
            cls.materialization_for(prime)
        )
        return admission.verify_and_admit_q_one_root_v1_base_v1(
            raw_q_one_g=value["raw"],
            source_body=value["body"],
            root_anchor=value["anchor"],
            source_state=value["state"],
            root_actualness=value["actualness"],
            terminal_receipt=value["terminal"],
            materialization_receipt=materialization,
            v4_owner_receipt=cls.owner_for(prime),
            v4_scope_receipt=cls.scope_for(prime),
            role_grant=grant(admission),
        )

    def test_positive_controls_materialize_and_admit_without_queue(self) -> None:
        state_ids = []
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                materialized = self.materialization_for(prime)
                materialized_wire = materializer.base_materialization_receipt_to_mapping_v1(
                    materialized
                )
                self.assertTrue(materialized_wire["root_base_materialization_authority"])
                self.assertFalse(materialized_wire["persistent_admission"])
                state = materialized_wire["v1_state"]
                self.assertEqual(state["queue_gate"], persistent_state.ROOT_INITIALIZER_OUTPUT)
                self.assertIsNone(state["parent_state_id"])
                self.assertNotIn("owner", state)
                self.assertNotIn("owner_digest", json.dumps(state, sort_keys=True))

                receipt = self.admission_for(prime)
                wire = admission.base_admission_receipt_to_mapping_v1(receipt)
                jsonschema.Draft202012Validator(SCHEMA).validate(materialized_wire)
                jsonschema.Draft202012Validator(SCHEMA).validate(wire)
                self.assertTrue(wire["persistent_admission"])
                self.assertTrue(wire["root_base_admission_authority"])
                self.assertTrue(wire["v1_base_owner_authority"])
                self.assertFalse(wire["queue_authority"])
                self.assertFalse(wire["enqueue_authority"])
                self.assertFalse(wire["enqueue_performed"])
                self.assertFalse(wire["successor_admission"])
                self.assertEqual(
                    wire["canonical_root_potential_evidence"],
                    [prime, 3, 0, 0, 0, 0, 0],
                )
                self.assertFalse(wire["t5_potential_authority"])
                self.assertEqual(wire["owner"], admission.TARGET_OWNER)
                self.assertEqual(wire["matched_families"], [admission.TARGET_OWNER])
                self.assertEqual(wire["precedence_index"], 2)
                state_ids.append(wire["v1_state_id"])
        self.assertEqual(len(state_ids), 2)
        self.assertNotEqual(state_ids[0], state_ids[1])

    def test_actual_frozen_v1_gate_replays_the_admitted_wire(self) -> None:
        receipt = admission.base_admission_receipt_to_mapping_v1(self.admission_for(1_201))
        rule = persistent_state.ProducerRuleV1(
            producer_id=admission.PRODUCER_ID,
            queue_gate=persistent_state.ROOT_INITIALIZER_OUTPUT,
            branch_ids=frozenset({admission.BRANCH_ID}),
            source_owners=frozenset(),
            target_owners=frozenset({admission.TARGET_OWNER}),
        )
        decision = persistent_state.reject_before_persistent_queue_v1(
            receipt["v1_state"], {admission.PRODUCER_ID: rule}
        )
        self.assertTrue(decision.accepted)
        self.assertEqual(decision.owner, admission.TARGET_OWNER)
        self.assertEqual(decision.owner_digest, receipt["v1_owner_digest"])

    def test_terminal_adapter_is_nonrole_and_hit_cases_reject_early(self) -> None:
        self.assertFalse(hasattr(terminal_adapter, "ROLE"))
        for prime in (73, 193, 241_441):
            with self.subTest(prime=prime):
                value = self.case(prime)
                with self.assertRaises(terminal_adapter.TerminalProjectionError) as raised:
                    terminal_adapter.project_q_one_v3_miss_to_v1_terminal_first_v1(
                        source_state=value["state"],
                        root_actualness=value["actualness"],
                        terminal_receipt=value["terminal"],
                    )
                self.assertEqual(
                    raised.exception.code,
                    terminal_adapter.TerminalProjectionRejectCode.TERMINAL_SOURCE_NOT_MISS,
                )
                with self.assertRaises(materializer.BaseMaterializationError):
                    self.materialization_for(prime)

    def test_cross_source_and_prefix_global_mutations_reject(self) -> None:
        first = self.case(1_201)
        second = self.case(2_521)
        with self.assertRaises(materializer.BaseMaterializationError):
            materializer.materialize_q_one_root_v1_base_state_v1(
                raw_q_one_g=first["raw"],
                source_body=first["body"],
                root_anchor=first["anchor"],
                source_state=first["state"],
                root_actualness=second["actualness"],
                terminal_receipt=first["terminal"],
                role_grant=grant(materializer),
            )
        bad_terminal = copy.deepcopy(first["terminal"])
        bad_terminal["global_exhaustion"] = True
        bad_terminal = reseal_mapping(bad_terminal, "production-q1-prefix-miss:")
        with self.assertRaises(terminal_adapter.TerminalProjectionError) as raised:
            terminal_adapter.project_q_one_v3_miss_to_v1_terminal_first_v1(
                source_state=first["state"],
                root_actualness=first["actualness"],
                terminal_receipt=bad_terminal,
            )
        self.assertIn(
            raised.exception.code,
            {
                terminal_adapter.TerminalProjectionRejectCode.SCOPE_WIDENING,
                terminal_adapter.TerminalProjectionRejectCode.DIGEST_MISMATCH,
            },
        )

    def test_v4_owner_scope_and_v4_digest_as_v1_digest_reject(self) -> None:
        prime = 1_201
        value = self.case(prime)
        materialization_wire = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(prime)
        )
        bad_owner = copy.deepcopy(self.owner_for(prime))
        bad_owner["owner"] = "type_ii_relation_f_endpoint"
        bad_owner = reseal_mapping(bad_owner, "q1-common-root-owner:")
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"],
                source_body=value["body"],
                root_anchor=value["anchor"],
                source_state=value["state"],
                root_actualness=value["actualness"],
                terminal_receipt=value["terminal"],
                materialization_receipt=materialization_wire,
                v4_owner_receipt=bad_owner,
                v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )
        receipt = self.admission_for(prime)
        forged = forge_admission_receipt(receipt, v1_owner_digest=receipt.v4_owner_digest)
        with self.assertRaises(admission.BaseAdmissionError):
            admission.base_admission_receipt_to_mapping_v1(forged)

    def test_resealed_state_gate_parent_producer_mark_and_facts_mutations_reject(self) -> None:
        prime = 1_201
        value = self.case(prime)
        original = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(prime)
        )
        mutations = []
        for label in ("gate", "parent", "producer", "mark", "facts"):
            candidate = copy.deepcopy(original)
            state = candidate["v1_state"]
            if label == "gate":
                state["queue_gate"] = persistent_state.ADMITTED_SUCCESSOR
            elif label == "parent":
                state["parent_state_id"] = "state:" + "f" * 64
            elif label == "producer":
                state["producer_id"] = "caller_supplied_initializer"
            elif label == "mark":
                state["mark"]["kind"] = persistent_state.NONTRIVIAL_MARK
                state["mark"] = persistent_state.seal_receipt_v1(
                    {k: v for k, v in state["mark"].items() if k != "digest"}
                )
            else:
                state["facts"]["relation_q"] = 2
            state["state_id"] = persistent_state.build_state_id_v1(state)
            candidate["v1_state_id"] = state["state_id"]
            candidate["v1_state_wire_digest"] = admission.canonical_digest_v1(state)
            candidate = reseal_mapping(candidate, materializer.RECEIPT_ID_PREFIX)
            mutations.append((label, candidate))
        for label, candidate in mutations:
            with self.subTest(label=label):
                with self.assertRaises(admission.BaseAdmissionError):
                    admission.verify_and_admit_q_one_root_v1_base_v1(
                        raw_q_one_g=value["raw"],
                        source_body=value["body"],
                        root_anchor=value["anchor"],
                        source_state=value["state"],
                        root_actualness=value["actualness"],
                        terminal_receipt=value["terminal"],
                        materialization_receipt=candidate,
                        v4_owner_receipt=self.owner_for(prime),
                        v4_scope_receipt=self.scope_for(prime),
                        role_grant=grant(admission),
                    )

    def test_authority_flips_and_caller_controlled_inputs_are_rejected(self) -> None:
        receipt = self.admission_for(1_201)
        for name in (
            "queue_authority",
            "enqueue_authority",
            "successor_admission",
            "e1_authority",
            "e5_authority",
            "t5_ticket_authority",
        ):
            with self.subTest(name=name):
                forged = forge_admission_receipt(receipt, **{name: True})
                with self.assertRaises(admission.BaseAdmissionError):
                    admission.base_admission_receipt_to_mapping_v1(forged)
        parameters = inspect.signature(
            materializer.materialize_q_one_root_v1_base_state_v1
        ).parameters
        for forbidden in ("facts", "state", "owner", "producer_rule", "authority"):
            self.assertNotIn(forbidden, parameters)

    def test_coherently_resealed_hit_cannot_be_relabeled_miss_or_rebound_to_scope(self) -> None:
        hit = self.case(73)
        fake_terminal = copy.deepcopy(hit["terminal"])
        for name in ("root_outcome_kind", "root_equation", "root_equation_digest"):
            fake_terminal.pop(name, None)
        fake_terminal.update(
            {
                "receipt_type": "ProductionQOneRegisteredPrefixMissReceiptV1",
                "outcome": "MISS_REGISTERED_PRIORITY_COMPLETE",
                "coverage_semantics": "REGISTERED_PRIORITY_ONLY",
                "ordered_gaps": [3, 7, 11],
                "next_unchecked_gap": 15,
                "selected_certificate": None,
                "selected_certificate_digest": None,
                "terminal_leaf_authority": False,
                "registered_prefix_miss_authority": True,
                "root_proof_close_authority": False,
            }
        )
        fake_terminal = reseal_mapping(fake_terminal, "production-q1-prefix-miss:")
        fake_scope = copy.deepcopy(self.scope_for(1_201))
        hit_owner = self.owner_for(73)
        for name in ("raw_q_one_g", "source_body", "root_anchor", "source_state", "root_actualness"):
            fake_scope[name] = copy.deepcopy(hit[{"raw_q_one_g": "raw", "source_body": "body", "root_anchor": "anchor", "source_state": "state", "root_actualness": "actualness"}[name]])
        fake_scope.update(
            {
                "raw_q_one_g_digest": admission.canonical_digest_v1(hit["raw"]),
                "body_id": hit["body"]["body_id"],
                "body_digest": hit["body"]["digest"],
                "anchor_id": hit["anchor"]["anchor_id"],
                "anchor_digest": hit["anchor"]["digest"],
                "state_id": hit["state"]["state_id"],
                "state_digest": hit["state"]["digest"],
                "root_actualness_id": hit["actualness"]["actualness_id"],
                "root_actualness_digest": hit["actualness"]["digest"],
                "owner_receipt": hit_owner,
                "owner_receipt_id": hit_owner["receipt_id"],
                "owner_receipt_digest": hit_owner["digest"],
                "terminal_receipt": fake_terminal,
                "terminal_receipt_id": fake_terminal["receipt_id"],
                "terminal_receipt_digest": fake_terminal["digest"],
            }
        )
        fake_scope = reseal_mapping(fake_scope, "q1-prefix-scope-validation:")
        materialization = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(1_201)
        )
        with self.assertRaises(admission.BaseAdmissionError) as raised:
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=hit["raw"],
                source_body=hit["body"],
                root_anchor=hit["anchor"],
                source_state=hit["state"],
                root_actualness=hit["actualness"],
                terminal_receipt=fake_terminal,
                materialization_receipt=materialization,
                v4_owner_receipt=hit_owner,
                v4_scope_receipt=fake_scope,
                role_grant=grant(admission),
            )
        self.assertEqual(
            raised.exception.code,
            admission.BaseAdmissionRejectCode.TERMINAL_SOURCE_NOT_MISS,
        )

    def test_actualness_head_and_v3_scheduler_semantic_pin_reseals_reject(self) -> None:
        prime = 1_201
        value = self.case(prime)
        materialization = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(prime)
        )
        bad_actualness = copy.deepcopy(value["actualness"])
        bad_actualness["head_sha"] = "0" * len(bad_actualness["head_sha"])
        bad_actualness = reseal_mapping(bad_actualness, "q1-root-source-actualness:")
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=bad_actualness,
                terminal_receipt=value["terminal"], materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )
        old_head_actualness = copy.deepcopy(value["actualness"])
        old_head_actualness["head_sha"] = "f" * len(old_head_actualness["head_sha"])
        old_head_actualness = reseal_mapping(
            old_head_actualness, "q1-root-source-actualness:"
        )
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=old_head_actualness,
                terminal_receipt=value["terminal"], materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )
        bad_terminal = copy.deepcopy(value["terminal"])
        bad_terminal["scheduler_artifact_semantic_sha256"] = "0" * 64
        bad_terminal = reseal_mapping(bad_terminal, "production-q1-prefix-miss:")
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=bad_terminal, materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )

    def test_terminal_root_context_and_scope_replay_digest_reseals_reject(self) -> None:
        prime = 1_201
        value = self.case(prime)
        materialization = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(prime)
        )
        bad_terminal = copy.deepcopy(value["terminal"])
        bad_terminal["root_context"] = 2_521
        bad_terminal = reseal_mapping(bad_terminal, "production-q1-prefix-miss:")
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=bad_terminal, materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )
        bad_scope = copy.deepcopy(self.scope_for(prime))
        bad_scope["registered_prefix_replay_digest"] = "0" * 64
        bad_scope = reseal_mapping(bad_scope, "q1-prefix-scope-validation:")
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=value["terminal"], materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=bad_scope,
                role_grant=grant(admission),
            )

    def test_v4_owner_and_scope_deep_coherent_reseals_reject(self) -> None:
        prime = 1_201
        value = self.case(prime)
        materialization = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(prime)
        )
        bad_owner = copy.deepcopy(self.owner_for(prime))
        bad_owner["owner_id"] = "owner:" + "0" * 64
        bad_owner["owner_digest"] = "0" * 64
        bad_owner = reseal_mapping(bad_owner, "q1-common-root-owner:")
        with self.assertRaises(admission.BaseAdmissionError) as raised:
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=value["terminal"], materialization_receipt=materialization,
                v4_owner_receipt=bad_owner, v4_scope_receipt=self.scope_for(prime),
                role_grant=grant(admission),
            )
        self.assertEqual(raised.exception.code, admission.BaseAdmissionRejectCode.V4_OWNER_MISMATCH)
        bad_scope = copy.deepcopy(self.scope_for(prime))
        bad_scope["registered_gap_scans"] = []
        bad_scope["registered_prefix_replay_digest"] = "0" * 64
        bad_scope = reseal_mapping(bad_scope, "q1-prefix-scope-validation:")
        with self.assertRaises(admission.BaseAdmissionError) as raised:
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=value["terminal"], materialization_receipt=materialization,
                v4_owner_receipt=self.owner_for(prime), v4_scope_receipt=bad_scope,
                role_grant=grant(admission),
            )
        self.assertEqual(raised.exception.code, admission.BaseAdmissionRejectCode.V4_SCOPE_MISMATCH)

    def test_local_grant_is_not_repository_authority_and_canonical_json_rejects_float(self) -> None:
        materialized = materializer.base_materialization_receipt_to_mapping_v1(
            self.materialization_for(1_201)
        )
        admitted = admission.base_admission_receipt_to_mapping_v1(self.admission_for(1_201))
        self.assertFalse(materialized["local_grant_authenticates_head"])
        self.assertFalse(materialized["repository_authority"])
        self.assertFalse(admitted["local_grant_authenticates_head"])
        self.assertFalse(admitted["repository_authority"])
        with self.assertRaises(admission.BaseAdmissionError):
            admission.canonical_json_v1({"float": 1.0})
        forged = forge_admission_receipt(
            self.admission_for(1_201),
            canonical_root_potential_evidence=(1_201, 3, False, 0, 0, 0, 0),
        )
        with self.assertRaises(admission.BaseAdmissionError):
            admission.base_admission_receipt_to_mapping_v1(forged)
        bad_materialization = copy.deepcopy(materialized)
        bad_materialization["schema_version"] = True
        bad_materialization = reseal_mapping(
            bad_materialization, materializer.RECEIPT_ID_PREFIX
        )
        value = self.case(1_201)
        with self.assertRaises(admission.BaseAdmissionError):
            admission.verify_and_admit_q_one_root_v1_base_v1(
                raw_q_one_g=value["raw"], source_body=value["body"], root_anchor=value["anchor"],
                source_state=value["state"], root_actualness=value["actualness"],
                terminal_receipt=value["terminal"], materialization_receipt=bad_materialization,
                v4_owner_receipt=self.owner_for(1_201), v4_scope_receipt=self.scope_for(1_201),
                role_grant=grant(admission),
            )

    def test_verifier_is_independent_and_has_no_runtime_queue_dependency(self) -> None:
        source = inspect.getsource(admission)
        self.assertNotIn("import t6_q_one_root_v1_terminal_adapter_v1", source)
        self.assertNotIn("import t6_q_one_root_v1_base_materializer_v1", source)
        self.assertNotIn("t6_persistent_selector_runtime", source)
        self.assertNotIn("bootstrap_nonterminal_v1", source)
        self.assertNotIn("RuntimeQueueItemV1", source)


if __name__ == "__main__":
    unittest.main()
