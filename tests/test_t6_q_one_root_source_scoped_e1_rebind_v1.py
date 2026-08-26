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

from tests.test_t6_coordinator_role_registry_v5 import ActiveFixture  # noqa: E402
from tests.test_t6_q_one_root_prefix_scoped_e1_orchestrator_v2 import _run_driver  # noqa: E402
from tests.test_t6_q_one_root_v1_base_admission_orchestrator_v1 import run_v5  # noqa: E402
from tests.test_t6_q_one_terminal_issuer_v1 import RAW  # noqa: E402

import t6_q_one_root_source_scoped_e1_rebind_v1 as rebind  # noqa: E402
import t6_structured_transition_receipts_v1 as structured  # noqa: E402


SCHEMA = json.loads(
    (ROOT / "schemas/t6-q-one-root-source-scoped-e1-rebind-v1.schema.json").read_text(
        encoding="ascii"
    )
)


ISSUE_DRIVER = r"""
import json
import sys
from pathlib import Path
import t6_q_one_terminal_issuer_v1 as issuer
raw = json.loads(sys.stdin.read())
receipt = issuer.issue_q_one_terminal_decision_v1(
    root=Path(sys.argv[1]), requested_head=sys.argv[2], raw_q_one_g=raw
)
print(json.dumps(issuer.production_terminal_receipt_to_mapping_v1(receipt), sort_keys=True))
"""


def issue(root: Path, head: str, raw: dict[str, object]) -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root / "scripts")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, "-c", ISSUE_DRIVER, str(root), head],
        cwd=root,
        input=json.dumps(raw),
        text=True,
        capture_output=True,
        check=True,
        env=env,
    )
    return json.loads(completed.stdout)


def grant() -> dict[str, object]:
    return {
        "grant_id": rebind.GRANT_ID,
        "role": rebind.ROLE,
        "artifact_id": rebind.ARTIFACT_ID,
        "artifact_path": rebind.ARTIFACT_PATH,
        "artifact_symbols": list(rebind.ARTIFACT_SYMBOLS),
        "capabilities": list(rebind.CAPABILITIES),
        "authority_class": rebind.AUTHORITY_CLASS,
        "artifact_semantic_sha256": "a" * 64,
    }


def reseal(value: dict[str, object], prefix: str) -> dict[str, object]:
    result = copy.deepcopy(value)
    result.pop("receipt_id", None)
    result.pop("digest", None)
    digest = rebind.canonical_digest_v1(result)
    result["receipt_id"] = prefix + digest
    result["digest"] = digest
    return result


def forge_receipt(receipt, **updates):
    values = {field.name: getattr(receipt, field.name) for field in fields(type(receipt))}
    values.update(updates)
    values["digest"] = rebind.canonical_digest_v1(rebind._unsigned(values))
    values["receipt_id"] = rebind.RECEIPT_ID_PREFIX + values["digest"]
    forged = object.__new__(type(receipt))
    for field in fields(type(receipt)):
        object.__setattr__(forged, field.name, values[field.name])
    return forged


class QOneRootSourceScopedE1RebindTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="q1-v6-rebind-")
        cls.fixture = ActiveFixture(Path(cls.temp.name))
        cls.root, cls.head = cls.fixture.commit()
        cls.production: dict[int, dict[str, object]] = {
            p: issue(cls.root, cls.head, copy.deepcopy(RAW[p]))
            for p in (73, 193, 1_201, 2_521, 241_441)
        }
        cls.v4: dict[int, dict[str, object]] = {}
        cls.v5: dict[int, dict[str, object]] = {}
        for p in (1_201, 2_521):
            v4_result = _run_driver(
                cls.root, cls.head, copy.deepcopy(RAW[p]), cls.production[p]
            )
            if not v4_result["ok"]:
                raise RuntimeError(v4_result)
            cls.v4[p] = v4_result["receipt"]
            v5_result = run_v5(
                cls.root,
                cls.head,
                copy.deepcopy(RAW[p]),
                copy.deepcopy(cls.production[p]),
            )
            if not v5_result["ok"]:
                raise RuntimeError(v5_result)
            cls.v5[p] = v5_result["receipt"]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    @classmethod
    def make(cls, prime: int):
        v4 = cls.v4[prime]
        v5 = cls.v5[prime]
        return rebind.rebind_q_one_root_source_scoped_e1_v1(
            v4_consumer_receipt=copy.deepcopy(v4),
            v5_admission_receipt=copy.deepcopy(v5),
            raw_q_one_g=copy.deepcopy(v4["raw_q_one_g"]),
            source_body=copy.deepcopy(v4["source_body"]),
            root_anchor=copy.deepcopy(v4["root_anchor"]),
            source_state=copy.deepcopy(v4["source_state"]),
            v1_state=copy.deepcopy(v5["v1_state"]),
            role_grant=grant(),
        )

    def test_positive_controls_rebind_to_new_v1_source_without_recursive_authority(self):
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                wire = rebind.root_source_scoped_e1_rebind_receipt_to_mapping_v1(
                    self.make(prime)
                )
                jsonschema.Draft202012Validator(SCHEMA).validate(wire)
                self.assertEqual(wire["v2_source_state_id"], self.v4[prime]["state_id"])
                self.assertEqual(wire["v1_source_state_id"], self.v5[prime]["v1_state_id"])
                self.assertNotEqual(wire["v2_source_state_id"], wire["v1_source_state_id"])
                self.assertEqual(wire["v1_state"], self.v5[prime]["v1_state"])
                self.assertEqual(wire["source_owner"], "type_ii_relation_g_endpoint")
                self.assertEqual(wire["source_owner_digest"], wire["v1_owner_digest"][len("owner:"):])
                self.assertTrue(wire["root_source_scoped_e1_rebound"])
                self.assertTrue(wire["source_rebind_authority"])
                self.assertEqual(wire["representation_namespace"], rebind.REPRESENTATION_NAMESPACE)
                self.assertEqual(wire["path_semantics"], rebind.PATH_SEMANTICS)
                self.assertTrue(wire["not_transition"])
                self.assertEqual(
                    wire["rebound_candidate_witness"]["source_state_digest_domain"],
                    rebind.DIGEST_DOMAIN_STATE_ID_SUFFIX,
                )
                self.assertEqual(
                    wire["rebound_candidate_witness"]["source_state_wire_digest_domain"],
                    rebind.DIGEST_DOMAIN_STATE_WIRE,
                )
                self.assertEqual(
                    wire["rebound_candidate_witness"]["path_semantics"],
                    rebind.PATH_SEMANTICS,
                )
                for name in (
                    "e1_authority", "generic_e1", "successor_e1", "producer_authority",
                    "admission_authority", "persistent_admission", "queue_authority",
                    "e2_authority", "e3_authority", "e4_authority", "e5_authority",
                    "t5_ticket_authority", "t5_potential_authority", "global_exhaustion",
                    "reentry_authority",
                ):
                    self.assertFalse(wire[name], name)
                self.assertNotIn("candidate_witness", json.dumps(wire["v1_state"], sort_keys=True))
                self.assertNotIn("math_replay", json.dumps(wire["v1_state"], sort_keys=True))

    def test_v4_and_v5_source_swaps_fail_closed(self):
        v4 = copy.deepcopy(self.v4[1_201])
        v5 = copy.deepcopy(self.v5[2_521])
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            rebind.rebind_q_one_root_source_scoped_e1_v1(
                v4_consumer_receipt=v4,
                v5_admission_receipt=v5,
                raw_q_one_g=v4["raw_q_one_g"],
                source_body=v4["source_body"],
                root_anchor=v4["root_anchor"],
                source_state=v4["source_state"],
                v1_state=v5["v1_state"],
                role_grant=grant(),
            )
        self.assertIn(raised.exception.code, {rebind.RebindRejectCode.V5_RECEIPT_MISMATCH, rebind.RebindRejectCode.SOURCE_BINDING_MISMATCH, rebind.RebindRejectCode.V1_STATE_MISMATCH})

    def test_namespaced_rebind_is_rejected_by_legacy_structured_e1_parser(self):
        wire = rebind.root_source_scoped_e1_rebind_receipt_to_mapping_v1(
            self.make(1_201)
        )
        with self.assertRaises(structured.ReceiptValidationError) as raised:
            structured._parse_leaf_v1(wire, structured.E1OccurrenceReceiptV1)
        self.assertEqual(
            raised.exception.code,
            structured.ReceiptRejectCode.FIELD_SET_MISMATCH,
        )

    def test_v4_and_v5_role_grants_are_registry_pinned(self):
        bad_v4 = copy.deepcopy(self.v4[1_201])
        bad_v4["role_grant"]["role"] = "EVIL"
        bad_v4 = reseal(bad_v4, rebind.V4_RECEIPT_ID_PREFIX)
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(bad_v4, self.v5[1_201])
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.V4_RECEIPT_MISMATCH)

        bad_v5 = copy.deepcopy(self.v5[1_201])
        bad_v5["role_grant"]["role"] = "EVIL"
        bad_v5 = reseal(bad_v5, rebind.V5_RECEIPT_ID_PREFIX)
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(self.v4[1_201], bad_v5)
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.V5_RECEIPT_MISMATCH)

    def test_candidate_injection_and_miss_complete_relabel_fail(self):
        bad_v4 = copy.deepcopy(self.v4[1_201])
        bad_v4["candidate_witness"]["injected"] = True
        bad_v4 = reseal(bad_v4, rebind.V4_RECEIPT_ID_PREFIX)
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(bad_v4, self.v5[1_201])
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.FIELD_SET_MISMATCH)

        bad_v4 = copy.deepcopy(self.v4[1_201])
        terminal = copy.deepcopy(bad_v4["terminal_receipt"])
        terminal["outcome"] = "MISS_COMPLETE"
        terminal = reseal(terminal, rebind.V3_MISS_ID_PREFIX)
        bad_v4["terminal_receipt"] = terminal
        bad_v4["terminal_receipt_id"] = terminal["receipt_id"]
        bad_v4["terminal_receipt_digest"] = terminal["digest"]
        bad_v4 = reseal(bad_v4, rebind.V4_RECEIPT_ID_PREFIX)
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(bad_v4, self.v5[1_201])
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.TERMINAL_SOURCE_NOT_MISS)

    def test_authority_and_state_mutations_fail_after_reseal(self):
        bad_v4 = copy.deepcopy(self.v4[1_201])
        bad_v4["generic_e1"] = True
        bad_v4 = reseal(bad_v4, rebind.V4_RECEIPT_ID_PREFIX)
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(bad_v4, self.v5[1_201])
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.V4_RECEIPT_MISMATCH)

        bad_state = copy.deepcopy(self.v5[1_201]["v1_state"])
        bad_state["candidate_witness"] = {"forged": True}
        with self.assertRaises(rebind.RootSourceScopedE1RebindError) as raised:
            self._call_with(self.v4[1_201], self.v5[1_201], v1_state=bad_state)
        self.assertEqual(raised.exception.code, rebind.RebindRejectCode.SEMANTIC_ORIGIN_MISMATCH)

    def test_serializer_replays_cross_receipt_ids_and_derived_maps(self):
        original = self.make(1_201)
        mutations = []
        mutations.append(("v4_receipt_id", forge_receipt(original, v4_receipt_id=rebind.V4_RECEIPT_ID_PREFIX + "f" * 64)))
        candidate = copy.deepcopy(dict(original.rebound_candidate_witness))
        candidate["source_state_id"] = "state:" + "f" * 64
        mutations.append(("candidate_source", forge_receipt(original, rebound_candidate_witness=candidate)))
        mapping = copy.deepcopy(dict(original.source_rebind_map))
        mapping["old_source_state_id"] = "state:" + "f" * 64
        mutations.append(("rebind_map", forge_receipt(original, source_rebind_map=mapping)))
        mutations.append(("v1_wire_digest", forge_receipt(original, v1_state_wire_digest="f" * 64)))
        for label, forged in mutations:
            with self.subTest(label=label):
                with self.assertRaises(rebind.RootSourceScopedE1RebindError):
                    rebind.root_source_scoped_e1_rebind_receipt_to_mapping_v1(forged)

    def test_boolean_and_float_source_controls_fail(self):
        bad_raw = copy.deepcopy(self.v4[1_201]["raw_q_one_g"])
        bad_raw["q"] = True
        with self.assertRaises(rebind.RootSourceScopedE1RebindError):
            self._call_with(self.v4[1_201], self.v5[1_201], raw_q_one_g=bad_raw)
        bad_raw = copy.deepcopy(self.v4[1_201]["raw_q_one_g"])
        bad_raw["q"] = 1.0
        with self.assertRaises(rebind.RootSourceScopedE1RebindError):
            self._call_with(self.v4[1_201], self.v5[1_201], raw_q_one_g=bad_raw)

    def test_terminal_hits_preempt_before_any_rebind(self):
        # The V4 and V5 producers refuse these inputs at the terminal-first gate;
        # consequently there is no valid V4/V5 pair that the rebind can accept.
        for prime in (73, 193, 241_441):
            with self.subTest(prime=prime):
                v4_result = _run_driver(self.root, self.head, RAW[prime], self.production[prime])
                self.assertFalse(v4_result["ok"])
                self.assertEqual(v4_result["code"], "TERMINAL_SOURCE_NOT_MISS")

    def _call_with(self, v4, v5, **overrides):
        source = self.v4[1_201]
        base = {
            "v4_consumer_receipt": copy.deepcopy(v4),
            "v5_admission_receipt": copy.deepcopy(v5),
            "raw_q_one_g": copy.deepcopy(overrides.get("raw_q_one_g", source["raw_q_one_g"])),
            "source_body": copy.deepcopy(overrides.get("source_body", source["source_body"])),
            "root_anchor": copy.deepcopy(overrides.get("root_anchor", source["root_anchor"])),
            "source_state": copy.deepcopy(overrides.get("source_state", source["source_state"])),
            "v1_state": copy.deepcopy(overrides.get("v1_state", v5["v1_state"])),
            "role_grant": grant(),
        }
        return rebind.rebind_q_one_root_source_scoped_e1_v1(**base)


if __name__ == "__main__":
    unittest.main()
