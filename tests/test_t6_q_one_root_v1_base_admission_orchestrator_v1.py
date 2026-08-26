from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_t6_coordinator_role_registry_v5 import ActiveFixture, run_git
from tests.test_t6_q_one_terminal_issuer_v1 import RAW


ROOT = Path(__file__).resolve().parents[1]

ISSUE_DRIVER = r"""
import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
head = sys.argv[2]
sys.path.insert(0, str(root / "scripts"))
import t6_q_one_terminal_issuer_v1 as issuer

raw = json.loads(sys.stdin.read())
issued = issuer.issue_q_one_terminal_decision_v1(
    root=root, requested_head=head, raw_q_one_g=raw
)
print(json.dumps(issuer.production_terminal_receipt_to_mapping_v1(issued), sort_keys=True))
"""

V5_DRIVER = r"""
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
        f"_t6_v5_orchestrator_{head}",
        f"_t6_v4_for_v5_{head}",
        f"_t6_v3_for_v5_{head}",
        f"_t6_v4_owner_for_v5_{head}",
        f"_t6_v4_scope_for_v5_{head}",
        "t6_persistent_selector_state_v1",
        "t6_q_one_root_initializer_envelope_v2",
        "t6_q_one_root_v1_terminal_adapter_v1",
    ):
        stale = ModuleType(name)
        stale.sentinel = "STALE_PRELOAD_MUST_NOT_EXECUTE"
        sys.modules[name] = stale

if action == "alternate_orchestrator_path":
    path = root / "scripts" / "alternate_q1_v5_orchestrator.py"
    spec = importlib.util.spec_from_file_location("alternate_q1_v5_orchestrator", path)
    orchestrator = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = orchestrator
    spec.loader.exec_module(orchestrator)
else:
    import t6_q_one_root_v1_base_admission_orchestrator_v1 as orchestrator
import t6_q_one_root_v1_base_admission_receipt_verifier_v1 as replayer

payload = json.loads(sys.stdin.read())
raw = payload["raw"]
production = payload["production"]
try:
    if action == "replay_supplied":
        receipt = payload["receipt"]
    elif action == "caller_coerced_grant":
        orchestrator.assemble_q_one_root_v1_base_admission_v1(
            root=root,
            requested_head=head,
            raw_q_one_g=raw,
            production_miss_receipt=production,
            role_grant={"forged": True},
        )
        raise RuntimeError("coerced grant was unexpectedly accepted")
    else:
        receipt = orchestrator.assemble_q_one_root_v1_base_admission_v1(
            root=root,
            requested_head=head,
            raw_q_one_g=raw,
            production_miss_receipt=production,
        )
    replayed = replayer.verify_q_one_root_v1_base_admission_receipt_v1(
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
except TypeError as exc:
    if action == "caller_coerced_grant":
        print(json.dumps({"ok": False, "code": "CALLER_GRANT_REJECTED", "detail": str(exc)}, sort_keys=True))
    else:
        raise
except (orchestrator.OrchestratorError, replayer.ReceiptVerifierError) as exc:
    code = exc.code.value if hasattr(exc.code, "value") else str(exc.code)
    print(json.dumps({"ok": False, "code": code, "detail": exc.detail}, sort_keys=True))
"""


def issue(root: Path, head: str, raw: dict[str, object]) -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(root / "scripts")
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


def run_v5(
    root: Path,
    head: str,
    raw: dict[str, object],
    production: dict[str, object],
    *,
    action: str = "normal",
    receipt: dict[str, object] | None = None,
    git_environment: dict[str, str] | None = None,
) -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    if git_environment is not None:
        env.update(git_environment)
    payload: dict[str, object] = {"raw": raw, "production": production}
    if receipt is not None:
        payload["receipt"] = receipt
    completed = subprocess.run(
        [sys.executable, "-c", V5_DRIVER, str(root), head, action],
        cwd=root,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=True,
        env=env,
    )
    return json.loads(completed.stdout)


def commit_current(root: Path, message: str) -> str:
    run_git(root, "add", ".")
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=V5 exact-head test",
            "-c",
            "user.email=v5@example.invalid",
            "commit",
            "-q",
            "-m",
            message,
        ],
        cwd=root,
        check=True,
    )
    return run_git(root, "rev-parse", "HEAD")


class QOneRootV1BaseAdmissionExactHeadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="q1-v5-exact-head-")
        cls.fixture = ActiveFixture(Path(cls.temp.name))
        cls.root, cls.head = cls.fixture.commit()
        cls.production = {
            prime: issue(cls.root, cls.head, copy.deepcopy(RAW[prime]))
            for prime in (73, 193, 1_201, 2_521, 241_441)
        }

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def test_prefix_miss_p1201_and_p2521_assemble_and_replay(self) -> None:
        for prime in (1_201, 2_521):
            with self.subTest(prime=prime):
                result = run_v5(
                    self.root,
                    self.head,
                    copy.deepcopy(RAW[prime]),
                    copy.deepcopy(self.production[prime]),
                )
                self.assertTrue(result["ok"], result)
                receipt = result["receipt"]
                self.assertEqual(receipt["admission_decision"], "ACCEPT")
                self.assertTrue(receipt["persistent_admission"])
                self.assertTrue(receipt["v1_base_owner_authority"])
                self.assertTrue(receipt["root_base_admission_authority"])
                for field in (
                    "queue_authority",
                    "enqueue_authority",
                    "successor_admission",
                    "producer_authority",
                    "e1_authority",
                    "e2_authority",
                    "e3_authority",
                    "e4_authority",
                    "e5_authority",
                    "t5_ticket_authority",
                    "global_exhaustion",
                ):
                    self.assertFalse(receipt[field], field)
                self.assertEqual(
                    receipt["v1_state"]["queue_gate"], "ROOT_INITIALIZER_OUTPUT"
                )
                self.assertEqual(
                    result["replay"]["status"],
                    "Q1_ROOT_V1_BASE_ADMISSION_RECEIPT_REPLAY_VERIFIED",
                )
                self.assertTrue(result["replay"]["wire_match"])

    def test_terminal_hits_reject_before_base_admission(self) -> None:
        for prime in (73, 193, 241_441):
            with self.subTest(prime=prime):
                result = run_v5(
                    self.root,
                    self.head,
                    copy.deepcopy(RAW[prime]),
                    copy.deepcopy(self.production[prime]),
                )
                self.assertFalse(result["ok"], result)
                self.assertEqual(result["code"], "TERMINAL_SOURCE_NOT_MISS")

    def test_cross_source_and_cross_head_miss_cannot_enter(self) -> None:
        swapped = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[2_521]),
            copy.deepcopy(self.production[1_201]),
        )
        self.assertFalse(swapped["ok"], swapped)
        self.assertIn(swapped["code"], {"V3_RECEIPT_ERROR", "SOURCE_MISMATCH"})

        isolated = ActiveFixture(Path(self.temp.name) / "cross-head").commit()
        root, old_head = isolated
        old_terminal = issue(root, old_head, copy.deepcopy(RAW[1_201]))
        (root / "cross-head-marker").write_text("changed\n", encoding="ascii")
        new_head = commit_current(root, "cross head")
        crossed = run_v5(root, new_head, copy.deepcopy(RAW[1_201]), old_terminal)
        self.assertFalse(crossed["ok"], crossed)
        self.assertIn(crossed["code"], {"V3_RECEIPT_ERROR", "SOURCE_MISMATCH"})

    def test_stale_preload_and_git_replace_cannot_change_exact_execution(self) -> None:
        baseline = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[1_201]),
            copy.deepcopy(self.production[1_201]),
            action="preloaded_stale",
        )
        self.assertTrue(baseline["ok"], baseline)

        registry_path = self.root / "data/t6-wave1/t6-coordinator-role-registry-v5.json"
        original_registry = registry_path.read_bytes()
        replacement_registry = json.loads(original_registry)
        replacement_registry["authority_denials"]["queue_authority"] = True
        registry_path.write_text(
            json.dumps(replacement_registry, ensure_ascii=True, indent=2) + "\n",
            encoding="ascii",
        )
        replacement = commit_current(self.root, "replace target")
        # Restore the requested tree's artifact in the worktree.  If Git
        # replace were honored, replacement's changed registry blob would no
        # longer agree with this restored old-tree worktree binding.
        registry_path.write_bytes(original_registry)
        subprocess.run(
            ["git", "replace", self.head, replacement], cwd=self.root, check=True
        )
        try:
            replaced = run_v5(
                self.root,
                self.head,
                copy.deepcopy(RAW[1_201]),
                copy.deepcopy(self.production[1_201]),
            )
            self.assertTrue(replaced["ok"], replaced)
        finally:
            subprocess.run(
                ["git", "replace", "-d", self.head], cwd=self.root, check=True
            )

    def test_git_routing_environment_cannot_redirect_v3_v4_or_v5(self) -> None:
        foreign = self.root.parent / "foreign-git-routing"
        foreign.mkdir()
        run_git(foreign, "init", "-q")
        foreign_git = foreign / ".git"
        result = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[1_201]),
            copy.deepcopy(self.production[1_201]),
            git_environment={
                "GIT_DIR": str(foreign_git),
                "GIT_WORK_TREE": str(foreign),
                "GIT_INDEX_FILE": str(foreign_git / "index"),
                "GIT_OBJECT_DIRECTORY": str(foreign_git / "objects"),
                "GIT_ALTERNATE_OBJECT_DIRECTORIES": str(foreign_git / "objects"),
                "GIT_CONFIG_NOSYSTEM": "1",
            },
        )
        self.assertTrue(result["ok"], result)

    def test_caller_grant_and_authority_or_pin_mutations_reject(self) -> None:
        coerced = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[1_201]),
            copy.deepcopy(self.production[1_201]),
            action="caller_coerced_grant",
        )
        self.assertFalse(coerced["ok"], coerced)
        self.assertEqual(coerced["code"], "CALLER_GRANT_REJECTED")

        for name, mutate in (
            ("authority", lambda source: source["authority_denials"].__setitem__("queue_authority", True)),
            (
                "pin",
                lambda source: source["artifacts"][0].__setitem__(
                    "expected_blob_sha256", "0" * 64
                ),
            ),
        ):
            with self.subTest(name=name):
                fixture = ActiveFixture(Path(self.temp.name) / f"mutation-{name}")
                source = copy.deepcopy(fixture.source)
                mutate(source)
                root, head = fixture.commit(source)
                terminal = issue(root, head, copy.deepcopy(RAW[1_201]))
                result = run_v5(root, head, copy.deepcopy(RAW[1_201]), terminal)
                self.assertFalse(result["ok"], result)
                self.assertEqual(result["code"], "REGISTRY_ERROR")

    def test_replayer_and_worktree_tampering_reject(self) -> None:
        baseline = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[1_201]),
            copy.deepcopy(self.production[1_201]),
        )
        self.assertTrue(baseline["ok"], baseline)
        forged = copy.deepcopy(baseline["receipt"])
        forged["queue_authority"] = True
        rejected = run_v5(
            self.root,
            self.head,
            copy.deepcopy(RAW[1_201]),
            copy.deepcopy(self.production[1_201]),
            action="replay_supplied",
            receipt=forged,
        )
        self.assertFalse(rejected["ok"], rejected)
        self.assertEqual(rejected["code"], "WIRE_MISMATCH")

        root, head = ActiveFixture(Path(self.temp.name) / "worktree-drift").commit()
        terminal = issue(root, head, copy.deepcopy(RAW[1_201]))
        path = root / "scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py"
        path.write_bytes(path.read_bytes() + b"\n# worktree drift\n")
        drifted = run_v5(root, head, copy.deepcopy(RAW[1_201]), terminal)
        self.assertFalse(drifted["ok"], drifted)
        self.assertEqual(drifted["code"], "WORKTREE_BINDING_ERROR")

        alternate_root, alternate_head = ActiveFixture(
            Path(self.temp.name) / "alternate-loader"
        ).commit()
        alternate_terminal = issue(
            alternate_root, alternate_head, copy.deepcopy(RAW[1_201])
        )
        source = alternate_root / "scripts/t6_q_one_root_v1_base_admission_orchestrator_v1.py"
        alternate = alternate_root / "scripts/alternate_q1_v5_orchestrator.py"
        alternate.write_bytes(source.read_bytes())
        alternate_result = run_v5(
            alternate_root,
            alternate_head,
            copy.deepcopy(RAW[1_201]),
            alternate_terminal,
            action="alternate_orchestrator_path",
        )
        self.assertFalse(alternate_result["ok"], alternate_result)
        self.assertEqual(alternate_result["code"], "WORKTREE_BINDING_ERROR")


if __name__ == "__main__":
    unittest.main()
