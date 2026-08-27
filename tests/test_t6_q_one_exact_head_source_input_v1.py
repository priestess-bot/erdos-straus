from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import jsonschema

from tests.test_t6_coordinator_role_registry_v5 import ActiveFixture as V5Fixture
from tests.test_t6_q_one_terminal_issuer_v1 import RAW


ROOT = Path(__file__).resolve().parents[1]
V5_DATA = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v5.json"
V6_DATA = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v6.json"
V6_REGISTRY_SCHEMA = ROOT / "schemas" / "t6-coordinator-role-registry-v6.schema.json"
SOURCE_INPUT_SCHEMA = ROOT / "schemas" / "t6-q-one-exact-head-source-input-v1.schema.json"
BINDER_PATH = ROOT / "scripts" / "t6_q_one_exact_head_source_input_v1.py"
_BINDER_SPEC = importlib.util.spec_from_file_location("t6_v6_public_binder_test", BINDER_PATH)
assert _BINDER_SPEC and _BINDER_SPEC.loader
BINDER = importlib.util.module_from_spec(_BINDER_SPEC)
sys.modules[_BINDER_SPEC.name] = BINDER
_BINDER_SPEC.loader.exec_module(BINDER)

V6_PATHS = {
    "data/t6-wave1/t6-coordinator-role-registry-v6.json",
    "schemas/t6-coordinator-role-registry-v6.schema.json",
    "schemas/t6-q-one-exact-head-source-input-v1.schema.json",
    "scripts/t6_coordinator_role_registry_v6.py",
    "scripts/t6_q_one_exact_head_source_input_v1.py",
    "scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py",
    "scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py",
    "scripts/t6_q_one_phase_root_prestate_v2.py",
    "scripts/t6_q_one_root_source_scoped_e1_rebind_v1.py",
}


def run_git(root: Path, *args: str) -> str:
    env = os.environ.copy()
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True, env=env
    )
    return result.stdout.strip()


class V6Fixture:
    """Minimal exact-HEAD tree covering the transitive V3--V6 source path."""

    def __init__(self, base: Path) -> None:
        self.base = base
        self.count = 0
        self.v5_source = json.loads(V5_DATA.read_text(encoding="ascii"))

    def commit(self) -> tuple[Path, str]:
        self.count += 1
        root = self.base / f"repo-{self.count}"
        root.mkdir(parents=True)
        paths = V5Fixture.paths(self.v5_source) | V6_PATHS
        for path in sorted(paths):
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, target)
        run_git(root, "init", "-q")
        run_git(root, "add", ".")
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=V6 source-input test",
                "-c",
                "user.email=v6@example.invalid",
                "commit",
                "-q",
                "-m",
                "fixture",
            ],
            cwd=root,
            check=True,
        )
        return root, run_git(root, "rev-parse", "HEAD")


ISSUE_DRIVER = r'''
import json
import sys
from pathlib import Path
import t6_q_one_terminal_issuer_v1 as issuer
raw = json.loads(sys.stdin.read())
receipt = issuer.issue_q_one_terminal_decision_v1(
    root=Path(sys.argv[1]), requested_head=sys.argv[2], raw_q_one_g=raw
)
print(json.dumps(issuer.production_terminal_receipt_to_mapping_v1(receipt), sort_keys=True))
'''

SOURCE_DRIVER = r'''
import importlib.util
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
head = sys.argv[2]
action = sys.argv[3]
def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, root / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

orchestrator = load("t6_v6_source_orchestrator_test", "scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py")
replayer = load("t6_v6_source_replayer_test", "scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py")
payload = json.loads(sys.stdin.read())
try:
    if action == "normal":
        output = orchestrator.assemble_exact_head_q_one_actual_source_input_v1(
            root=root,
            requested_head=head,
            raw_q_one_g=payload["raw"],
            production_miss_receipt=payload["production"],
        )
        replay = replayer.verify_exact_head_q_one_actual_source_input_v1(
            root=root,
            requested_head=head,
            raw_q_one_g=payload["raw"],
            production_miss_receipt=payload["production"],
            source_input=output["source_input"],
            external_source_binding=output["external_source_binding"],
        )
        print(json.dumps({
            "ok": True,
            "output": output,
            "replay": {
                "status": replay.status,
                "wire_match": replay.wire_match,
                "authority_verified": replay.authority_verified,
            },
        }, sort_keys=True))
    else:
        replay = replayer.verify_exact_head_q_one_actual_source_input_v1(
            root=root,
            requested_head=head,
            raw_q_one_g=payload["raw"],
            production_miss_receipt=payload["production"],
            source_input=payload["source_input"],
            external_source_binding=payload["external_source_binding"],
        )
        print(json.dumps({"ok": True, "status": replay.status}, sort_keys=True))
except (orchestrator.ExactHeadSourceInputOrchestratorError, replayer.ExactHeadSourceInputReceiptReplayError) as exc:
    code = exc.code.value if hasattr(exc.code, "value") else str(exc.code)
    print(json.dumps({"ok": False, "code": code, "detail": exc.detail}, sort_keys=True))
'''


def issue(root: Path, head: str, raw: dict[str, object]) -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = f"{root}:{root / 'scripts'}"
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


def run_source(root: Path, head: str, payload: dict[str, object], action: str = "normal") -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = f"{root}:{root / 'scripts'}"
    completed = subprocess.run(
        [sys.executable, "-c", SOURCE_DRIVER, str(root), head, action],
        cwd=root,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=True,
        env=env,
    )
    return json.loads(completed.stdout)


class ExactHeadQOneSourceInputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="q1-v6-source-input-")
        cls.root, cls.head = V6Fixture(Path(cls.temp.name)).commit()
        cls.raw = copy.deepcopy(RAW[1_201])
        cls.production = issue(cls.root, cls.head, cls.raw)
        cls.positive = run_source(
            cls.root,
            cls.head,
            {"raw": cls.raw, "production": cls.production},
        )
        if not cls.positive["ok"]:
            raise RuntimeError(cls.positive)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def test_registry_and_source_input_schema_fix_the_non_e1_boundary(self) -> None:
        registry_schema = json.loads(V6_REGISTRY_SCHEMA.read_text(encoding="ascii"))
        registry = json.loads(V6_DATA.read_text(encoding="ascii"))
        source_schema = json.loads(SOURCE_INPUT_SCHEMA.read_text(encoding="ascii"))
        jsonschema.Draft202012Validator.check_schema(registry_schema)
        jsonschema.Draft202012Validator(registry_schema).validate(registry)
        jsonschema.Draft202012Validator.check_schema(source_schema)
        source_input = self.positive["output"]["source_input"]
        jsonschema.Draft202012Validator(source_schema).validate(source_input)
        extra = copy.deepcopy(source_input)
        extra["unexpected_authority_field"] = False
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(source_schema).validate(extra)
        self.assertEqual(
            source_input["binding_scope"],
            "EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_REPLAY_CANDIDATE_NOT_E1",
        )
        for field in (
            "source_actualness_input", "v1_base_admission_evidence", "v6_rebind_evidence",
            "generic_e1", "successor_e1", "e1_authority", "producer_authority",
            "branch_authority", "admission_authority", "queue_authority", "enqueue_authority",
            "e2_authority", "e3_authority", "e4_authority", "e5_authority", "t5_authority",
            "reentry_authority", "global_exhaustion",
        ):
            self.assertFalse(source_input[field], field)
        self.assertEqual(
            self.positive["replay"]["status"],
            "EXACT_HEAD_Q_ONE_SOURCE_INPUT_CANDIDATE_REPLAY_VERIFIED",
        )
        self.assertTrue(self.positive["replay"]["wire_match"])
        self.assertTrue(self.positive["replay"]["authority_verified"])

    def test_private_candidate_factory_never_emits_evidence_or_a_publicly_parseable_wire(self) -> None:
        candidate = self.positive["output"]["source_input"]
        replay_candidate = BINDER._build_exact_head_q_one_source_input_replay_candidate_v1(
            registry_context={
                "head_sha": candidate["head_sha"],
                "head_tree_sha": candidate["head_tree_sha"],
                "registries": {
                    version: {
                        "registry_id": candidate[f"{version}_registry_id"],
                        "registry_digest": candidate[f"{version}_registry_digest"],
                        "role_manifest_digest": candidate[f"{version}_role_manifest_digest"],
                    }
                    for version in ("v3", "v4", "v5", "v6")
                },
            },
            v3_prefix_miss_receipt=copy.deepcopy(candidate["v3_prefix_miss_receipt"]),
            v4_consumer_receipt=copy.deepcopy(candidate["v4_consumer_receipt"]),
            v5_base_admission_receipt=copy.deepcopy(candidate["v5_base_admission_receipt"]),
            v6_rebind_receipt=copy.deepcopy(candidate["v6_rebind_receipt"]),
            role_grant=copy.deepcopy(candidate["role_grant"]),
        )
        replay_wire = BINDER.exact_head_q_one_actual_source_input_to_mapping_v1(replay_candidate)
        self.assertEqual(replay_wire["status"], BINDER.STATUS)
        for field in (
            "source_actualness_input",
            "v1_base_admission_evidence",
            "v6_rebind_evidence",
        ):
            self.assertFalse(replay_wire[field], field)
        with self.assertRaises(BINDER.ExactHeadQOneSourceInputError):
            BINDER.parse_exact_head_q_one_actual_source_input_v1(replay_wire)
        with self.assertRaises(BINDER.ExactHeadQOneSourceInputError):
            BINDER.external_binding_wire_from_exact_head_source_input_v1(replay_candidate)

    def test_tampered_authority_or_projection_is_rejected_by_independent_replay(self) -> None:
        forged = copy.deepcopy(self.positive["output"])
        forged["source_input"]["generic_e1"] = True
        result = run_source(
            self.root,
            self.head,
            {
                "raw": self.raw,
                "production": self.production,
                "source_input": forged["source_input"],
                "external_source_binding": forged["external_source_binding"],
            },
            action="replay",
        )
        self.assertFalse(result["ok"], result)
        self.assertIn(result["code"], {"RECEIPT_TYPE_ERROR", "WIRE_MISMATCH", "AUTHORITY_MISMATCH"})

    def test_v3_terminal_hit_preempts_before_v4_v5_v6_assembly(self) -> None:
        raw = copy.deepcopy(RAW[73])
        production = issue(self.root, self.head, raw)
        result = run_source(
            self.root,
            self.head,
            {"raw": raw, "production": production},
        )
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["code"], "TERMINAL_SOURCE_NOT_MISS")

    def test_worktree_drift_rejects_before_the_v6_registry_can_run(self) -> None:
        with tempfile.TemporaryDirectory(prefix="q1-v6-source-input-drift-") as temporary:
            root, head = V6Fixture(Path(temporary)).commit()
            raw = copy.deepcopy(RAW[1_201])
            production = issue(root, head, raw)
            registry_path = root / "scripts" / "t6_coordinator_role_registry_v6.py"
            registry_path.write_text(
                registry_path.read_text(encoding="ascii") + "\n# worktree drift\n",
                encoding="ascii",
            )
            result = run_source(
                root,
                head,
                {"raw": raw, "production": production},
            )
            self.assertFalse(result["ok"], result)
            self.assertEqual(result["code"], "WORKTREE_BINDING_ERROR")


if __name__ == "__main__":
    unittest.main()
