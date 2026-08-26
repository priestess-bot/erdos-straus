from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_t6_coordinator_role_registry_v3 import RepositoryFixture


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
    73: raw_q_one_g(73, [[19, 1]]),
    193: raw_q_one_g(193, [[7, 2]]),
    1_201: raw_q_one_g(1_201, [[7, 1], [43, 1]]),
    2_521: raw_q_one_g(2_521, [[631, 1]]),
    241_441: raw_q_one_g(241_441, [[7, 1], [8_623, 1]]),
}


DRIVER = r"""
import json
from dataclasses import fields
from pathlib import Path
import sys

root = Path(sys.argv[1])
head = sys.argv[2]
action = sys.argv[3]
sys.path.insert(0, str(root / "scripts"))
if action == "alternate_alias":
    import importlib.util
    issuer_path = root / "scripts" / "t6_q_one_terminal_issuer_v1.py"
    spec = importlib.util.spec_from_file_location("alternate_q1_terminal_issuer", issuer_path)
    issuer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = issuer
    spec.loader.exec_module(issuer)
else:
    import t6_q_one_terminal_issuer_v1 as issuer
import t6_q_one_terminal_receipt_verifier_v1 as verifier

payload = json.loads(sys.stdin.read())
raw = payload["raw"]
local_serializer_accepted = False
try:
    issued = issuer.issue_q_one_terminal_decision_v1(
        root=root, requested_head=head, raw_q_one_g=raw
    )
    receipt = issuer.production_terminal_receipt_to_mapping_v1(issued)
    if action == "hit_miss_swap":
        receipt["receipt_type"] = "ProductionQOneRegisteredPrefixMissReceiptV1"
    elif action == "global_flip":
        receipt["global_exhaustion"] = True
    elif action == "authority_flip":
        receipt["e1_authority"] = True
    elif action == "state_swap":
        receipt["state_id"] = "state:" + "0" * 64
    elif action == "grant_swap":
        receipt["initializer_grant_digest"] = "0" * 64
    elif action == "head_swap":
        receipt["head_sha"] = "0" * len(receipt["head_sha"])
    elif action == "coherent_source_reseal":
        import t6_q_one_root_initializer_envelope_v2 as root_envelope
        other_raw = {
            "schema_id": "q1_root_initializer_raw_v2", "schema_version": 2,
            "root_context": 1201, "equation_rank": 1201,
            "equation_numerator": 4, "equation_denominator": 1201, "q": 1,
            "gap_three_x": 301, "endpoint_fiber_code": 2, "major_phase_code": 3,
            "provenance_code": 1, "mark_kind_code": 1,
            "mark_root_context": 1201, "mark_equation_rank": 1201,
            "gap_three_factorization": [[7, 1], [43, 1]],
        }
        other_body = root_envelope.make_canonical_q_one_g_source_body_v2(other_raw)
        other_anchor = root_envelope.make_root_initializer_anchor_v2(other_body)
        other_state = root_envelope.make_raw_root_source_state_v2(other_body, other_anchor)
        body_map = root_envelope.artifact_to_mapping_v2(other_body)
        anchor_map = root_envelope.artifact_to_mapping_v2(other_anchor)
        state_map = root_envelope.artifact_to_mapping_v2(other_state)
        actual = issued.root_actualness
        branch = dict(actual.deterministic_initial_branch_replay)
        branch.update({
            "body_id": body_map["body_id"], "body_digest": body_map["digest"],
            "anchor_id": anchor_map["anchor_id"], "anchor_digest": anchor_map["digest"],
            "state_id": state_map["state_id"], "state_digest": state_map["digest"],
        })
        actual_values = {field.name: getattr(actual, field.name) for field in fields(type(actual))}
        actual_values.update({
            "body_id": body_map["body_id"], "body_digest": body_map["digest"],
            "anchor_id": anchor_map["anchor_id"], "anchor_digest": anchor_map["digest"],
            "state_id": state_map["state_id"], "state_digest": state_map["digest"],
            "deterministic_initial_branch_replay": branch,
            "deterministic_initial_branch_replay_digest": issuer.canonical_digest_v1(branch),
        })
        actual_unsigned = issuer._unsigned_artifact_mapping_v1(type(actual), actual_values)
        actual_digest = issuer.canonical_digest_v1(actual_unsigned)
        actual_values.update({
            "actualness_id": type(actual).ID_PREFIX + actual_digest,
            "digest": actual_digest,
        })
        forged_actual = issuer._construct_artifact_v1(type(actual), actual_values)
        issuer.actualness_receipt_to_mapping_v1(forged_actual)

        top_values = {field.name: getattr(issued, field.name) for field in fields(type(issued))}
        top_values.update({
            "root_actualness": forged_actual, "root_actualness_digest": actual_digest,
            "body_id": body_map["body_id"], "body_digest": body_map["digest"],
            "anchor_id": anchor_map["anchor_id"], "anchor_digest": anchor_map["digest"],
            "state_id": state_map["state_id"], "state_digest": state_map["digest"],
            "deterministic_initial_branch_replay_digest": issuer.canonical_digest_v1(branch),
        })
        top_unsigned = issuer._unsigned_artifact_mapping_v1(type(issued), top_values)
        top_digest = issuer.canonical_digest_v1(top_unsigned)
        top_values.update({"receipt_id": type(issued).ID_PREFIX + top_digest, "digest": top_digest})
        forged_top = issuer._construct_artifact_v1(type(issued), top_values)
        receipt = issuer.production_terminal_receipt_to_mapping_v1(forged_top)
        local_serializer_accepted = True
    verifier_root = root
    if action == "path_subclass":
        class PathSubclass(type(root)):
            pass
        verifier_root = PathSubclass(root)
    result = verifier.verify_q_one_production_terminal_receipt_v1(
        root=verifier_root, requested_head=head, raw_q_one_g=raw, receipt=receipt
    )
    print(json.dumps({
        "ok": True,
        "receipt": receipt,
        "verified": {
            "status": result.status,
            "receipt_type": result.receipt_type,
            "receipt_id": result.receipt_id,
            "receipt_digest": result.receipt_digest,
            "state_id": result.state_id,
            "outcome": result.outcome,
        },
        "local_serializer_accepted": local_serializer_accepted,
    }, sort_keys=True))
except (issuer.QOneTerminalIssuerError, verifier.ProductionReceiptReplayError) as exc:
    code = exc.code.value if hasattr(exc.code, "value") else str(exc.code)
    print(json.dumps({
        "ok": False, "code": code, "detail": exc.detail,
        "local_serializer_accepted": local_serializer_accepted,
    }, sort_keys=True))
"""


def execute(root: Path, head: str, raw: dict[str, object], action: str = "normal") -> dict:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, "-c", DRIVER, str(root), head, action],
        cwd=root,
        input=json.dumps({"raw": raw}),
        text=True,
        capture_output=True,
        check=True,
        env=environment,
    )
    return json.loads(completed.stdout)


class ProductionQOneTerminalIssuerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="q1-production-terminal-")
        self.fixture = RepositoryFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_real_head_hit_and_miss_issue_then_independent_replay(self):
        root, head = self.fixture.commit()
        expectations = {
            73: ("ProductionQOneRootTerminalReceiptV1", "ROOT_TERMINAL_HIT"),
            193: ("ProductionQOneRootTerminalReceiptV1", "ROOT_TERMINAL_HIT"),
            241_441: ("ProductionQOneRootTerminalReceiptV1", "ROOT_TERMINAL_HIT"),
            1_201: (
                "ProductionQOneRegisteredPrefixMissReceiptV1",
                "MISS_REGISTERED_PRIORITY_COMPLETE",
            ),
            2_521: (
                "ProductionQOneRegisteredPrefixMissReceiptV1",
                "MISS_REGISTERED_PRIORITY_COMPLETE",
            ),
        }
        for prime, expected in expectations.items():
            with self.subTest(prime=prime):
                result = execute(root, head, RAW[prime])
                self.assertTrue(result["ok"], result)
                receipt = result["receipt"]
                self.assertEqual((receipt["receipt_type"], receipt["outcome"]), expected)
                self.assertEqual(result["verified"]["status"], "PRODUCTION_Q1_TERMINAL_RECEIPT_VERIFIED")
                self.assertTrue(receipt["source_actualness"])
                self.assertTrue(receipt["root_initializer_authority"])
                self.assertTrue(receipt["issued_under_terminal_issuer"])
                self.assertFalse(receipt["persistent_admission"])
                self.assertFalse(receipt["common_owner_authority"])
                self.assertFalse(receipt["e1_authority"])
                self.assertFalse(receipt["queue_authority"])
                self.assertFalse(receipt["producer_continuation_allowed"])
                self.assertFalse(receipt["global_exhaustion"])

    def test_schema_and_outer_seal_reject_unresealed_mutations(self):
        for prime, actions in (
            (
                73,
                {
                    "hit_miss_swap": "SCHEMA_ERROR",
                    "authority_flip": "SCHEMA_ERROR",
                    "state_swap": "RECEIPT_SEAL_ERROR",
                    "grant_swap": "RECEIPT_SEAL_ERROR",
                    "head_swap": "RECEIPT_SEAL_ERROR",
                },
            ),
            (
                1_201,
                {
                    "global_flip": "SCHEMA_ERROR",
                    "authority_flip": "SCHEMA_ERROR",
                    "state_swap": "RECEIPT_SEAL_ERROR",
                    "grant_swap": "RECEIPT_SEAL_ERROR",
                    "head_swap": "RECEIPT_SEAL_ERROR",
                },
            ),
        ):
            for action, expected_code in actions.items():
                root, head = self.fixture.commit()
                with self.subTest(prime=prime, action=action):
                    result = execute(root, head, RAW[prime], action)
                    self.assertFalse(result["ok"], result)
                    self.assertEqual(result["code"], expected_code, result)

    def test_coherent_local_reseal_is_accepted_locally_but_replayer_rejects(self):
        root, head = self.fixture.commit()
        result = execute(root, head, RAW[73], "coherent_source_reseal")
        self.assertFalse(result["ok"], result)
        self.assertTrue(result["local_serializer_accepted"], result)
        self.assertIn(result["code"], {"SOURCE_MISMATCH", "WIRE_MISMATCH"})

    def test_import_alias_does_not_change_production_receipt(self):
        root, head = self.fixture.commit()
        canonical = execute(root, head, RAW[73])
        alternate = execute(root, head, RAW[73], "alternate_alias")
        self.assertTrue(canonical["ok"], canonical)
        self.assertTrue(alternate["ok"], alternate)
        self.assertEqual(canonical["receipt"], alternate["receipt"])

    def test_schema_uses_type_specific_id_prefixes(self):
        root, _head = self.fixture.commit()
        schema = json.loads(
            (root / "schemas/t6-q-one-production-terminal-receipts-v1.schema.json").read_text()
        )
        definitions = schema["$defs"]
        patterns = {
            "rootProblemId": "^q1-root-problem:",
            "bodyId": "^q1-source-body:",
            "anchorId": "^root-init-anchor:",
            "stateId": "^state:",
            "actualnessId": "^q1-root-source-actualness:",
            "hitReceiptId": "^production-q1-root-terminal:",
            "missReceiptId": "^production-q1-prefix-miss:",
        }
        for name, prefix in patterns.items():
            self.assertTrue(definitions[name]["pattern"].startswith(prefix), name)

    def test_independent_verifier_rejects_path_subclass(self):
        root, head = self.fixture.commit()
        result = execute(root, head, RAW[73], "path_subclass")
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["code"], "HEAD_ERROR")


if __name__ == "__main__":
    unittest.main()
