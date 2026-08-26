from __future__ import annotations

import copy
import importlib.util
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_coordinator_role_registry_v1.py"
DATA_PATH = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v1.json"
SCHEMA_PATH = ROOT / "schemas" / "t6-coordinator-role-registry-v1.schema.json"
SPEC = importlib.util.spec_from_file_location(
    "t6_coordinator_role_registry_v1_under_test", MODULE_PATH
)
assert SPEC and SPEC.loader
registry_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = registry_module
SPEC.loader.exec_module(registry_module)
RECEIPTS_PATH = ROOT / "scripts" / "t6_structured_transition_receipts_v1.py"
RECEIPTS_SPEC = importlib.util.spec_from_file_location(
    "t6_structured_transition_receipts_v1_inventory_boundary_test", RECEIPTS_PATH
)
assert RECEIPTS_SPEC and RECEIPTS_SPEC.loader
receipts_module = importlib.util.module_from_spec(RECEIPTS_SPEC)
sys.modules[RECEIPTS_SPEC.name] = receipts_module
RECEIPTS_SPEC.loader.exec_module(receipts_module)


def run_git(root: Path, *args: str) -> str:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    return completed.stdout.strip()


def write_json(path: Path, value: object) -> None:
    path.write_bytes(
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=False,
            indent=2,
            allow_nan=False,
        ).encode("ascii")
        + b"\n"
    )


class RepositoryFixture:
    def __init__(self, base: Path):
        self.base = base
        self.counter = 0
        self.source = json.loads(DATA_PATH.read_text(encoding="ascii"))

    def commit(
        self,
        source: dict | None = None,
        *,
        raw_registry: bytes | None = None,
        overrides: dict[str, bytes] | None = None,
    ) -> tuple[Path, str]:
        self.counter += 1
        root = self.base / f"repo-{self.counter}"
        root.mkdir()
        document = copy.deepcopy(source if source is not None else self.source)
        files = {
            item["path"]
            for item in document.get("artifacts", [])
            if isinstance(item, dict) and isinstance(item.get("path"), str)
        }
        files.update(
            item["path"]
            for item in document.get("blocked_candidates", [])
            if isinstance(item, dict) and isinstance(item.get("path"), str)
        )
        files.update(registry_module.TOOLCHAIN_PATHS)
        overrides = overrides or {}
        for path in sorted(files | set(overrides)):
            if path.startswith("../"):
                continue
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            if path in overrides:
                target.write_bytes(overrides[path])
            elif (ROOT / path).is_file():
                target.write_bytes((ROOT / path).read_bytes())
        registry_path = root / registry_module.REGISTRY_PATH
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        if raw_registry is not None:
            registry_path.write_bytes(raw_registry)
        else:
            write_json(registry_path, document)
        run_git(root, "init", "-q")
        run_git(root, "add", ".")
        run_git(
            root,
            "-c",
            "user.name=Registry Test",
            "-c",
            "user.email=registry-test@example.invalid",
            "commit",
            "-q",
            "-m",
            "fixture",
        )
        return root, run_git(root, "rev-parse", "HEAD")

    @staticmethod
    def commit_current(root: Path, message: str) -> str:
        run_git(root, "add", ".")
        run_git(
            root,
            "-c",
            "user.name=Registry Test",
            "-c",
            "user.email=registry-test@example.invalid",
            "commit",
            "-q",
            "-m",
            message,
        )
        return run_git(root, "rev-parse", "HEAD")


class CoordinatorEvidenceInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-role-inventory-test-")
        self.fixture = RepositoryFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def resolve(self, root: Path, head: str) -> dict:
        return registry_module.resolve_registry_v1(root=root, requested_head=head)

    def assert_rejects(
        self, root: Path, head: str, code: str
    ) -> registry_module.RegistryError:
        with self.assertRaises(registry_module.RegistryError) as raised:
            self.resolve(root, head)
        self.assertEqual(raised.exception.code, code)
        return raised.exception

    def test_baseline_is_deterministic_and_grants_no_role(self):
        root, head = self.fixture.commit()
        first = self.resolve(root, head)
        second = self.resolve(root, head)
        self.assertEqual(first, second)
        self.assertEqual(first["head_sha"], head)
        self.assertEqual(first["status"], registry_module.RESOLVED_STATUS)
        self.assertEqual(first["resolved_role_grants"], [])
        self.assertEqual(first["active_role_grant_count"], 0)
        self.assertEqual(first["authorized_branches"], [])
        self.assertEqual(first["complete_terminal_schedules"], [])
        self.assertTrue(all(value == 0 for value in first["role_grant_counts"].values()))
        self.assertEqual(
            set(first["role_subdigests"]),
            set(registry_module.ROLE_DIGEST_KEYS.values()),
        )
        unsigned = dict(first)
        observed_digest = unsigned.pop("registry_digest")
        self.assertEqual(observed_digest, registry_module.canonical_digest_v1(unsigned))
        self.assertEqual(
            first["execution_binding"]["status"], "BOUND_TO_CLEAN_REQUESTED_HEAD"
        )
        self.assertNotIn("artifact_digest_manifest", first)
        evidence = first["artifact_evidence_inventory"]
        self.assertEqual(
            evidence["schema_id"], "t6_evidence_artifact_digest_inventory_v1"
        )
        self.assertEqual(evidence["status"], "EVIDENCE_ONLY_NOT_AUTHORIZED")
        self.assertIs(evidence["role_authority"], False)
        self.assertTrue(
            {
                "coordinator_prefix_schedule_role_registry_resolver_v2",
                "coordinator_prefix_schedule_role_registry_schema_v2",
                "coordinator_prefix_schedule_role_registry_source_v2",
                "coordinator_q1_root_terminal_authority_registry_resolver_v3",
                "coordinator_q1_root_terminal_authority_registry_schema_v3",
                "coordinator_q1_root_terminal_authority_registry_source_v3",
                "coordinator_q1_root_v1_base_admission_authority_registry_resolver_v5",
                "coordinator_q1_root_v1_base_admission_authority_registry_schema_v5",
                "coordinator_q1_root_v1_base_admission_authority_registry_source_v5",
                "q1_root_v1_base_admission_orchestrator_v1",
                "q1_root_v1_base_admission_receipt_verifier_v1",
                "q1_root_v1_base_admission_verifier_v1",
                "q1_root_v1_base_materializer_v1",
                "q1_root_v1_terminal_adapter_v1",
                "coordinator_q1_root_prefix_scoped_e1_authority_registry_resolver_v4",
                "coordinator_q1_root_prefix_scoped_e1_authority_registry_schema_v4",
                "coordinator_q1_root_prefix_scoped_e1_authority_registry_source_v4",
                "q_one_priority_prefix_coverage_verifier_v1",
                "q_one_priority_prefix_scheduler_v1",
                "q_one_registered_prefix_e1_consumer_v2",
                "q_one_production_terminal_issuer_v1",
                "q_one_production_terminal_receipt_schema_v1",
                "q_one_production_terminal_receipt_verifier_v1",
                "q_one_root_initializer_envelope_v2",
                "q_one_root_owner_classifier_v2",
                "q_one_root_prefix_scoped_e1_orchestrator_v2",
                "q_one_root_prefix_scoped_e1_receipt_schema_v2",
                "q_one_root_prefix_scoped_e1_receipt_verifier_v2",
                "q_one_scope_aware_e1_validator_v2",
                "q_one_terminal_decision_assembler_v2",
                "terminal_miss_scope_taxonomy_schema_v2",
                "terminal_miss_scope_taxonomy_v2",
            }
            <= set(evidence["digests"])
        )
        unsigned_evidence = dict(evidence)
        evidence_digest = unsigned_evidence.pop("digest")
        self.assertEqual(
            evidence_digest, registry_module.canonical_digest_v1(unsigned_evidence)
        )
        ast_contract = first["python_ast_contract"]
        self.assertEqual(
            ast_contract["python_major_minor"],
            f"{sys.version_info.major}.{sys.version_info.minor}",
        )
        unsigned_ast = dict(ast_contract)
        ast_digest = unsigned_ast.pop("digest")
        self.assertEqual(ast_digest, registry_module.canonical_digest_v1(unsigned_ast))

    def test_evidence_inventory_cannot_masquerade_as_trusted_artifact_manifest(self):
        root, head = self.fixture.commit()
        payload = self.resolve(root, head)
        evidence = payload["artifact_evidence_inventory"]
        self.assertFalse(evidence["role_authority"])
        with self.assertRaises(receipts_module.ReceiptValidationError):
            receipts_module.ArtifactDigestManifestV1(evidence)

    def test_q1_reason_codes_are_exact_declared_blockers(self):
        root, head = self.fixture.commit()
        q1 = self.resolve(root, head)["blocked_candidates"][0]
        self.assertEqual(q1["candidate_id"], registry_module.Q1_BLOCKED_ID)
        self.assertEqual(set(q1["reason_codes"]), registry_module.Q1_BLOCK_REASONS)
        self.assertIn("_phase_root_executor", q1["symbol_semantic_sha256"])
        self.assertIn("_contraction_validator", q1["symbol_semantic_sha256"])

    def test_schema_freezes_evidence_only_zero_role_surface(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        self.assertEqual(set(schema["required"]), registry_module.SOURCE_KEYS)
        self.assertEqual(
            schema["properties"]["status"]["const"], registry_module.RESOLVED_STATUS
        )
        self.assertEqual(schema["properties"]["role_grants"]["maxItems"], 0)
        self.assertEqual(schema["properties"]["branch_bindings"]["maxItems"], 0)
        self.assertEqual(
            schema["properties"]["complete_terminal_schedules"]["maxItems"], 0
        )
        policy_properties = schema["$defs"]["authorityPolicy"]["properties"]
        schema_policy = {
            key: value["const"] for key, value in policy_properties.items()
        }
        self.assertEqual(schema_policy, registry_module.EXPECTED_AUTHORITY_POLICY)
        reason_enum = schema["$defs"]["blockedCandidate"]["properties"][
            "reason_codes"
        ]["items"]["enum"]
        self.assertEqual(set(reason_enum), registry_module.Q1_BLOCK_REASONS)

    def test_api_offers_no_registry_or_callable_override(self):
        parameters = inspect.signature(registry_module.resolve_registry_v1).parameters
        self.assertEqual(tuple(parameters), ("root", "requested_head"))
        self.assertTrue(
            all(item.kind is inspect.Parameter.KEYWORD_ONLY for item in parameters.values())
        )

    def test_symbolic_head_is_rejected(self):
        root, _ = self.fixture.commit()
        self.assert_rejects(root, "HEAD", "INVALID_HEAD")

    def test_dirty_registry_worktree_has_no_authority(self):
        root, head = self.fixture.commit()
        expected = self.resolve(root, head)
        (root / registry_module.REGISTRY_PATH).write_bytes(b'{"schema_id": NaN}\n')
        self.assertEqual(self.resolve(root, head), expected)

    def test_duplicate_json_key_is_rejected(self):
        raw = DATA_PATH.read_bytes().replace(
            b'{\n  "schema_id":',
            b'{\n  "schema_id": "duplicate",\n  "schema_id":',
            1,
        )
        root, head = self.fixture.commit(raw_registry=raw)
        self.assert_rejects(root, head, "DUPLICATE_JSON_KEY")

    def test_nonfinite_json_is_rejected(self):
        raw = DATA_PATH.read_bytes().replace(
            b'"schema_version": 1', b'"schema_version": NaN', 1
        )
        root, head = self.fixture.commit(raw_registry=raw)
        self.assert_rejects(root, head, "NONFINITE_JSON")

    def test_role_grant_mutation_is_rejected_by_head_schema(self):
        source = copy.deepcopy(self.fixture.source)
        source["role_grants"] = [{"grant_id": "caller.injected"}]
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_branch_and_complete_schedule_mutations_are_rejected(self):
        for key, value in (
            ("branch_bindings", [{"branch_id": "caller.injected"}]),
            ("complete_terminal_schedules", [{"schedule_id": "local.miss"}]),
        ):
            with self.subTest(key=key):
                source = copy.deepcopy(self.fixture.source)
                source[key] = value
                root, head = self.fixture.commit(source)
                self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_duplicate_artifact_id_is_rejected(self):
        source = copy.deepcopy(self.fixture.source)
        source["artifacts"].append(copy.deepcopy(source["artifacts"][0]))
        source["artifacts"].sort(key=lambda item: item["artifact_id"])
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "DUPLICATE_ID")

    def test_unsafe_and_forbidden_evidence_paths_are_rejected(self):
        source = copy.deepcopy(self.fixture.source)
        source["artifacts"][0]["path"] = "../outside.json"
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "UNSAFE_PATH")

        source = copy.deepcopy(self.fixture.source)
        artifact = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == "structured_transition_verifier_v1"
        )
        artifact["path"] = "tests/authority.py"
        root, head = self.fixture.commit(
            source,
            overrides={
                "tests/authority.py": (
                    b"def verify_structured_transition_evidence_v1():\n    pass\n"
                )
            },
        )
        self.assert_rejects(root, head, "FORBIDDEN_EXECUTABLE_ROOT")

    def test_ambiguous_python_symbol_is_rejected(self):
        path = "scripts/t6_structured_transition_receipts_v1.py"
        altered = (ROOT / path).read_bytes() + (
            b"\ndef verify_structured_transition_evidence_v1():\n    return None\n"
        )
        root, head = self.fixture.commit(overrides={path: altered})
        self.assert_rejects(root, head, "SYMBOL_AMBIGUITY")

    def test_unreferenced_unicode_and_space_paths_do_not_break_tree_read(self):
        unicode_path = (
            "docs/"
            + chr(0x8DEF)
            + chr(0x7EBF)
            + " "
            + chr(0x590D)
            + chr(0x67E5)
            + ".md"
        )
        root, head = self.fixture.commit(overrides={unicode_path: b"unreferenced\n"})
        self.assertEqual(self.resolve(root, head)["head_sha"], head)

    def test_requested_head_schema_actually_governs_source(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        schema["properties"]["status"]["const"] = "IMPOSSIBLE_TEST_STATUS"
        root, head = self.fixture.commit(
            overrides={
                registry_module.SCHEMA_PATH: (
                    json.dumps(schema, ensure_ascii=True, indent=2).encode("ascii") + b"\n"
                )
            }
        )
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_dirty_resolver_and_schema_worktree_are_rejected(self):
        for path in registry_module.TOOLCHAIN_PATHS:
            with self.subTest(path=path):
                root, head = self.fixture.commit()
                target = root / path
                target.write_bytes(target.read_bytes() + b"\n")
                self.assert_rejects(root, head, "DIRTY_TOOLCHAIN")

    def test_untracked_resolver_is_rejected(self):
        root, _ = self.fixture.commit()
        run_git(root, "rm", "--cached", registry_module.RESOLVER_PATH)
        run_git(
            root,
            "-c",
            "user.name=Registry Test",
            "-c",
            "user.email=registry-test@example.invalid",
            "commit",
            "-q",
            "-m",
            "untrack resolver",
        )
        head = run_git(root, "rev-parse", "HEAD")
        self.assert_rejects(root, head, "DIRTY_TOOLCHAIN")

    def test_executing_resolver_must_match_requested_head_blob(self):
        altered = MODULE_PATH.read_bytes() + b"\n# different resolver bytes\n"
        root, head = self.fixture.commit(
            overrides={registry_module.RESOLVER_PATH: altered}
        )
        self.assert_rejects(root, head, "EXECUTING_RESOLVER_HEAD_MISMATCH")

    def test_commit_replace_ref_cannot_change_requested_commit(self):
        root, original_head = self.fixture.commit()
        expected = self.resolve(root, original_head)
        changed = copy.deepcopy(self.fixture.source)
        changed["proof_boundary"] += " Replacement target only."
        write_json(root / registry_module.REGISTRY_PATH, changed)
        replacement_head = self.fixture.commit_current(root, "replacement commit")
        run_git(root, "replace", original_head, replacement_head)
        with mock.patch.dict(os.environ, {"GIT_NO_REPLACE_OBJECTS": "0"}):
            observed = self.resolve(root, original_head)
        self.assertEqual(observed, expected)

    def test_blob_replace_ref_cannot_change_registry_blob(self):
        root, head = self.fixture.commit()
        expected = self.resolve(root, head)
        original_blob = run_git(
            root, "rev-parse", f"{head}:{registry_module.REGISTRY_PATH}"
        )
        malicious = root / "malicious-registry.json"
        malicious.write_bytes(b'{"schema_id": NaN}\n')
        replacement_blob = run_git(root, "hash-object", "-w", str(malicious))
        run_git(root, "replace", original_blob, replacement_blob)
        with mock.patch.dict(os.environ, {"GIT_NO_REPLACE_OBJECTS": "0"}):
            observed = self.resolve(root, head)
        self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
