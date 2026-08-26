from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_t6_coordinator_role_registry_v3 import RepositoryFixture, run_git
from tests.test_t6_q_one_terminal_issuer_v1 import RAW


ROOT = Path(__file__).resolve().parents[1]
V4_SOURCE_PATH = ROOT / "data/t6-wave1/t6-coordinator-role-registry-v4.json"


ISSUE_DRIVER = r"""
import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
head = sys.argv[2]
sys.path.insert(0, str(root / "scripts"))
import t6_q_one_terminal_issuer_v1 as issuer

raw = json.loads(sys.stdin.read())
receipt = issuer.issue_q_one_terminal_decision_v1(
    root=root, requested_head=head, raw_q_one_g=raw
)
print(json.dumps(issuer.production_terminal_receipt_to_mapping_v1(receipt), sort_keys=True))
"""


ROLE_DRIVER = r"""
import importlib.util
import json
from pathlib import Path
import sys
from types import ModuleType

root = Path(sys.argv[1])
head = sys.argv[2]
action = sys.argv[3]
sys.path.insert(0, str(root / "scripts"))

if action == "preloaded_stale":
    for name in (
        f"_t6_owner_{head}", f"_t6_validator_{head}", f"_t6_consumer_{head}",
        f"_t6_owner_replay_{head}", f"_t6_validator_replay_{head}",
        f"_t6_consumer_replay_{head}",
    ):
        stale = ModuleType(name)
        stale.sentinel = "STALE_PRELOAD_MUST_NOT_EXECUTE"
        sys.modules[name] = stale

if action == "alternate_orchestrator_path":
    path = root / "scripts" / "alternate_q1_v4_orchestrator.py"
    spec = importlib.util.spec_from_file_location("alternate_q1_v4_orchestrator", path)
    orchestrator = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = orchestrator
    spec.loader.exec_module(orchestrator)
else:
    import t6_q_one_root_prefix_scoped_e1_orchestrator_v2 as orchestrator
import t6_q_one_root_prefix_scoped_e1_receipt_verifier_v2 as replayer

payload = json.loads(sys.stdin.read())
raw = payload["raw"]
production = payload["production"]
try:
    if action == "replay_supplied":
        receipt = payload["receipt"]
    else:
        receipt = orchestrator.assemble_q_one_root_prefix_scoped_e1_v2(
            root=root,
            requested_head=head,
            raw_q_one_g=raw,
            production_miss_receipt=production,
        )
    if action == "authority_flip":
        receipt["global_exhaustion"] = True
    replayed = replayer.verify_q_one_root_prefix_scoped_e1_receipt_v2(
        root=root,
        requested_head=head,
        raw_q_one_g=raw,
        production_miss_receipt=production,
        receipt=receipt,
    )
    print(json.dumps({
        "ok": True,
        "receipt": receipt,
        "replay": {
            "status": replayed.status,
            "receipt_id": replayed.receipt_id,
            "state_id": replayed.state_id,
            "root_context": replayed.root_context,
            "wire_match": replayed.wire_match,
            "authority_verified": replayed.authority_verified,
        },
    }, sort_keys=True))
except (orchestrator.OrchestratorError, replayer.ReceiptVerifierError) as exc:
    code = exc.code.value if hasattr(exc.code, "value") else str(exc.code)
    print(json.dumps({"ok": False, "code": code, "detail": exc.detail}, sort_keys=True))
"""


def _run_driver(
    root: Path,
    head: str,
    raw: dict[str, object],
    production: dict[str, object],
    *,
    action: str = "normal",
    receipt: dict[str, object] | None = None,
) -> dict[str, object]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    payload: dict[str, object] = {"raw": raw, "production": production}
    if receipt is not None:
        payload["receipt"] = receipt
    completed = subprocess.run(
        [sys.executable, "-c", ROLE_DRIVER, str(root), head, action],
        cwd=root,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=True,
        env=environment,
    )
    return json.loads(completed.stdout)


class QOneRootPrefixScopedE1ExactHeadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="q1-v4-exact-head-")
        cls.v3_fixture = RepositoryFixture(Path(cls.temp.name))
        cls.root, _base_head = cls.v3_fixture.commit()
        source = json.loads(V4_SOURCE_PATH.read_text(encoding="ascii"))
        if source.get("activation_status") != "ACTIVE_EXACT_HEAD_AUTHORITY":
            raise RuntimeError("V4 registry must be active and pinned before exact-HEAD tests")
        paths = {
            "data/t6-wave1/t6-coordinator-role-registry-v4.json",
            "schemas/t6-coordinator-role-registry-v4.schema.json",
            "schemas/t6-q-one-root-prefix-scoped-e1-v2.schema.json",
            "scripts/t6_coordinator_role_registry_v4.py",
            "claims/t6-coordinator-q1-root-prefix-scoped-e1-authority-v4.md",
            "claims/t6-q-one-root-prefix-scoped-e1-roles-v2.md",
        }
        cross = source["v3_cross_registry_binding"]
        paths.update(
            {
                cross["registry_path"],
                cross["schema_path"],
                cross["resolver_path"],
            }
        )
        paths.update(item["path"] for item in source["artifacts"])
        paths.update(item["path"] for item in source["pinned_documents"])
        for relative in sorted(paths):
            target = cls.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())
        cls.head = RepositoryFixture.commit_current(cls.root, "add active V4 role layer")
        cls.production: dict[int, dict[str, object]] = {}
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONPATH"] = str(cls.root / "scripts")
        for prime in (73, 1_201, 2_521):
            completed = subprocess.run(
                [sys.executable, "-c", ISSUE_DRIVER, str(cls.root), cls.head],
                cwd=cls.root,
                input=json.dumps(RAW[prime]),
                text=True,
                capture_output=True,
                check=True,
                env=environment,
            )
            cls.production[prime] = json.loads(completed.stdout)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def test_p1201_and_p2521_assemble_then_independent_replay(self) -> None:
        expected = {1_201: (803, 241_101), 2_521: (1_683, 1_060_711)}
        for prime, (chart_r, chart_k) in expected.items():
            with self.subTest(prime=prime):
                result = _run_driver(
                    self.root,
                    self.head,
                    RAW[prime],
                    self.production[prime],
                )
                self.assertTrue(result["ok"], result)
                receipt = result["receipt"]
                self.assertEqual(receipt["math_replay"]["chart_r"], chart_r)
                self.assertEqual(receipt["math_replay"]["chart_k"], chart_k)
                self.assertTrue(receipt["root_source_scoped_e1"])
                self.assertFalse(receipt["generic_e1"])
                self.assertFalse(receipt["successor_e1"])
                self.assertFalse(receipt["persistent_admission"])
                self.assertFalse(receipt["queue_authority"])
                self.assertFalse(receipt["global_exhaustion"])
                self.assertEqual(
                    result["replay"]["status"],
                    "Q1_ROOT_PREFIX_SCOPED_E1_RECEIPT_REPLAY_VERIFIED",
                )
                self.assertTrue(result["replay"]["wire_match"])

    def test_root_terminal_hit_is_rejected_before_e1(self) -> None:
        result = _run_driver(
            self.root,
            self.head,
            RAW[73],
            self.production[73],
        )
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["code"], "TERMINAL_SOURCE_NOT_MISS")

    def test_cross_source_and_cross_head_receipts_reject(self) -> None:
        source_swap = _run_driver(
            self.root,
            self.head,
            RAW[2_521],
            self.production[1_201],
        )
        self.assertFalse(source_swap["ok"], source_swap)
        self.assertIn(source_swap["code"], {"V3_RECEIPT_ERROR", "SOURCE_MISMATCH"})

        marker = self.root / "V4_CROSS_HEAD_MARKER"
        marker.write_text("cross-head control\n", encoding="ascii")
        cross_head = RepositoryFixture.commit_current(self.root, "cross-head control")
        try:
            result = _run_driver(
                self.root,
                cross_head,
                RAW[1_201],
                self.production[1_201],
            )
            self.assertFalse(result["ok"], result)
            self.assertIn(result["code"], {"V3_RECEIPT_ERROR", "SOURCE_MISMATCH"})
        finally:
            run_git(self.root, "reset", "--soft", self.head)
            marker.unlink(missing_ok=True)
            run_git(self.root, "reset", "--mixed", self.head)

    def test_replayer_rejects_consumer_authority_flip(self) -> None:
        baseline = _run_driver(
            self.root,
            self.head,
            RAW[1_201],
            self.production[1_201],
        )
        self.assertTrue(baseline["ok"], baseline)
        receipt = copy.deepcopy(baseline["receipt"])
        receipt["global_exhaustion"] = True
        result = _run_driver(
            self.root,
            self.head,
            RAW[1_201],
            self.production[1_201],
            action="replay_supplied",
            receipt=receipt,
        )
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["code"], "WIRE_MISMATCH")

    def test_preloaded_stale_modules_do_not_replace_fresh_head_modules(self) -> None:
        result = _run_driver(
            self.root,
            self.head,
            RAW[1_201],
            self.production[1_201],
            action="preloaded_stale",
        )
        self.assertTrue(result["ok"], result)
        self.assertTrue(result["replay"]["authority_verified"])

    def test_worktree_drift_and_alternate_self_path_reject(self) -> None:
        owner_path = self.root / "scripts/t6_q_one_root_owner_classifier_v2.py"
        original = owner_path.read_bytes()
        owner_path.write_bytes(original + b"\n# uncommitted drift\n")
        try:
            drift = _run_driver(
                self.root,
                self.head,
                RAW[1_201],
                self.production[1_201],
            )
            self.assertFalse(drift["ok"], drift)
            self.assertIn(drift["code"], {"REGISTRY_ERROR", "WORKTREE_BINDING_ERROR"})
        finally:
            owner_path.write_bytes(original)

        alternate = self.root / "scripts/alternate_q1_v4_orchestrator.py"
        alternate.write_bytes(
            (self.root / "scripts/t6_q_one_root_prefix_scoped_e1_orchestrator_v2.py").read_bytes()
        )
        try:
            wrong_path = _run_driver(
                self.root,
                self.head,
                RAW[1_201],
                self.production[1_201],
                action="alternate_orchestrator_path",
            )
            self.assertFalse(wrong_path["ok"], wrong_path)
            self.assertEqual(wrong_path["code"], "WORKTREE_BINDING_ERROR")
        finally:
            alternate.unlink(missing_ok=True)

    def test_git_replace_does_not_change_requested_head_objects(self) -> None:
        fake_tree = run_git(self.root, "rev-parse", f"{self.head}^{{tree}}")
        fake_commit = run_git(
            self.root,
            "-c",
            "user.name=V4 replace test",
            "-c",
            "user.email=v4-replace@example.invalid",
            "commit-tree",
            fake_tree,
            "-m",
            "replace control",
        )
        run_git(self.root, "replace", self.head, fake_commit)
        try:
            result = _run_driver(
                self.root,
                self.head,
                RAW[1_201],
                self.production[1_201],
            )
            self.assertTrue(result["ok"], result)
        finally:
            run_git(self.root, "replace", "-d", self.head)


if __name__ == "__main__":
    unittest.main()
