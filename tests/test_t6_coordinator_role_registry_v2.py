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
MODULE_PATH = ROOT / "scripts" / "t6_coordinator_role_registry_v2.py"
DATA_PATH = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v2.json"
SCHEMA_PATH = ROOT / "schemas" / "t6-coordinator-role-registry-v2.schema.json"
SPEC = importlib.util.spec_from_file_location(
    "t6_coordinator_role_registry_v2_under_test", MODULE_PATH
)
assert SPEC and SPEC.loader
REGISTRY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = REGISTRY
SPEC.loader.exec_module(REGISTRY)


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
            if type(item) is dict and type(item.get("path")) is str
        }
        files.update(REGISTRY.TOOLCHAIN_PATHS)
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
        registry_path = root / REGISTRY.REGISTRY_PATH
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
            "user.name=Registry V2 Test",
            "-c",
            "user.email=registry-v2-test@example.invalid",
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
            "user.name=Registry V2 Test",
            "-c",
            "user.email=registry-v2-test@example.invalid",
            "commit",
            "-q",
            "-m",
            message,
        )
        return run_git(root, "rev-parse", "HEAD")


class CoordinatorRoleRegistryV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-role-registry-v2-")
        self.fixture = RepositoryFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def resolve(self, root: Path, head: str) -> dict:
        return REGISTRY.resolve_registry_v2(root=root, requested_head=head)

    def assert_rejects(self, root: Path, head: str, code: str) -> None:
        with self.assertRaises(REGISTRY.RegistryV2Error) as raised:
            self.resolve(root, head)
        self.assertEqual(raised.exception.code, code)

    def test_baseline_grants_only_two_head_bound_capabilities(self) -> None:
        root, head = self.fixture.commit()
        first = self.resolve(root, head)
        second = self.resolve(root, head)
        self.assertEqual(first, second)
        self.assertEqual(first["head_sha"], head)
        self.assertEqual(first["status"], REGISTRY.STATUS)
        self.assertNotIn("python_major_minor", first["python_ast_contract"])
        self.assertNotIn("python_implementation", first["python_ast_contract"])
        self.assertEqual(first["active_role_grant_count"], 2)
        self.assertEqual(
            first["role_grant_counts"],
            {"INDEPENDENT_COVERAGE_VERIFIER": 1, "TERMINAL_SCHEDULER": 1},
        )
        self.assertEqual(first["authorized_branches"], [])
        self.assertEqual(first["terminal_prefix_authority_count"], 1)
        self.assertEqual(len(first["authorized_terminal_prefixes"]), 1)
        prefix = first["authorized_terminal_prefixes"][0]
        self.assertEqual(prefix["schedule_id"], REGISTRY.SCHEDULE_ID)
        self.assertEqual(prefix["ordered_gaps"], [3, 7, 11])
        self.assertEqual(prefix["next_unchecked_gap"], 15)
        self.assertEqual(prefix["coverage_semantics"], "REGISTERED_PRIORITY_ONLY")
        self.assertIs(prefix["global_exhaustion"], False)
        self.assertEqual(
            prefix["outcomes"], ["PREFIX_MISS_EVIDENCE_ONLY", "ROOT_TERMINAL_HIT"]
        )
        self.assertEqual(first["issuer_count"], 0)
        for key in (
            "issuer_authority",
            "e1_authority",
            "queue_authority",
            "producer_authority",
            "initializer_authority",
            "t5_authority",
        ):
            self.assertIs(first[key], False)
        unsigned = dict(first)
        observed = unsigned.pop("registry_digest")
        self.assertEqual(observed, REGISTRY.canonical_digest_v2(unsigned))

    def test_scheduler_and_verifier_are_distinct_and_import_independent(self) -> None:
        root, head = self.fixture.commit()
        artifacts = {
            item["artifact_id"]: item for item in self.resolve(root, head)["resolved_artifacts"]
        }
        scheduler = artifacts[REGISTRY.SCHEDULER_ARTIFACT_ID]
        verifier = artifacts[REGISTRY.VERIFIER_ARTIFACT_ID]
        for artifact in artifacts.values():
            self.assertEqual(artifact["expected_blob_sha256"], artifact["blob_sha256"])
            self.assertEqual(
                artifact["expected_symbol_ast_sha256"], artifact["symbol_ast_sha256"]
            )
            self.assertEqual(
                artifact["expected_local_import_closure_digest"],
                artifact["local_import_closure_digest"],
            )
            self.assertEqual(
                artifact["expected_semantic_sha256"], artifact["semantic_sha256"]
            )
        self.assertNotEqual(scheduler["path"], verifier["path"])
        self.assertNotEqual(scheduler["blob_sha256"], verifier["blob_sha256"])
        self.assertNotEqual(scheduler["semantic_sha256"], verifier["semantic_sha256"])
        self.assertEqual(
            [item["path"] for item in scheduler["local_import_closure_files"]],
            [REGISTRY.SCHEDULER_PATH],
        )
        self.assertEqual(
            [item["path"] for item in verifier["local_import_closure_files"]],
            [REGISTRY.VERIFIER_PATH],
        )
        self.assertNotIn(
            REGISTRY.SCHEDULER_PATH,
            [item["path"] for item in verifier["local_import_closure_files"]],
        )
        self.assertNotIn(
            REGISTRY.LEGACY_RUNTIME_PATH,
            [item["path"] for item in verifier["local_import_closure_files"]],
        )

    def test_verifier_capabilities_do_not_create_more_roles(self) -> None:
        root, head = self.fixture.commit()
        grants = {
            item["role"]: item for item in self.resolve(root, head)["resolved_role_grants"]
        }
        self.assertEqual(set(grants), set(REGISTRY.ALLOWED_ROLES))
        self.assertEqual(
            grants["INDEPENDENT_COVERAGE_VERIFIER"]["capabilities"],
            list(REGISTRY.VERIFIER_CAPABILITIES),
        )
        self.assertEqual(
            grants["TERMINAL_SCHEDULER"]["capabilities"],
            list(REGISTRY.SCHEDULER_CAPABILITIES),
        )
        for grant in grants.values():
            self.assertEqual(
                grant["expected_artifact_semantic_sha256"],
                grant["artifact_semantic_sha256"],
            )
        self.assertNotIn("PRODUCER", grants)
        self.assertNotIn("E1", grants)
        self.assertNotIn("T5_TICKET", grants)

    def test_source_registry_contains_no_head_and_schema_freezes_surface(self) -> None:
        source = json.loads(DATA_PATH.read_text(encoding="ascii"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        self.assertNotIn("head_sha", source)
        self.assertNotIn("head_sha", schema["properties"])
        self.assertEqual(set(schema["required"]), REGISTRY.EXPECTED_SOURCE_KEYS)
        self.assertEqual(schema["properties"]["status"]["const"], REGISTRY.STATUS)
        self.assertEqual(schema["properties"]["branch_bindings"]["maxItems"], 0)
        self.assertEqual(source["authority_denials"], REGISTRY.EXPECTED_DENIALS)
        artifact_required = set(schema["$defs"]["pythonArtifactBase"]["required"])
        self.assertTrue(set(REGISTRY.ARTIFACT_PIN_KEYS) <= artifact_required)
        grant_required = set(schema["$defs"]["grantBase"]["required"])
        self.assertIn(REGISTRY.GRANT_PIN_KEY, grant_required)

    def test_api_accepts_no_registry_callable_or_role_override(self) -> None:
        parameters = inspect.signature(REGISTRY.resolve_registry_v2).parameters
        self.assertEqual(tuple(parameters), ("root", "requested_head"))
        self.assertTrue(
            all(item.kind is inspect.Parameter.KEYWORD_ONLY for item in parameters.values())
        )
        for name in (
            "issue_terminal_prefix_receipt_v2",
            "register_producer_v2",
            "enqueue_v2",
            "authorize_e1_v2",
        ):
            self.assertFalse(hasattr(REGISTRY, name))

    def test_symbolic_and_abbreviated_heads_are_rejected(self) -> None:
        root, head = self.fixture.commit()
        self.assert_rejects(root, "HEAD", "INVALID_HEAD")
        self.assert_rejects(root, head[:12], "INVALID_HEAD")

    def test_self_schema_and_registry_must_match_requested_head_worktree(self) -> None:
        for path in REGISTRY.TOOLCHAIN_PATHS:
            with self.subTest(path=path):
                root, head = self.fixture.commit()
                target = root / path
                target.write_bytes(target.read_bytes() + b"\n")
                self.assert_rejects(root, head, "TOOLCHAIN_WORKTREE_MISMATCH")

    def test_executing_resolver_must_match_requested_head_blob(self) -> None:
        root, head = self.fixture.commit(
            overrides={REGISTRY.RESOLVER_PATH: MODULE_PATH.read_bytes() + b"\n"}
        )
        self.assert_rejects(root, head, "EXECUTING_RESOLVER_HEAD_MISMATCH")

    def test_duplicate_and_noninteger_json_are_rejected(self) -> None:
        duplicate = DATA_PATH.read_bytes().replace(
            b'{\n  "schema_id":',
            b'{\n  "schema_id": "duplicate",\n  "schema_id":',
            1,
        )
        root, head = self.fixture.commit(raw_registry=duplicate)
        self.assert_rejects(root, head, "DUPLICATE_JSON_KEY")

        noninteger = DATA_PATH.read_bytes().replace(b'"schema_version": 2', b'"schema_version": 2.0')
        root, head = self.fixture.commit(raw_registry=noninteger)
        self.assert_rejects(root, head, "NONINTEGER_JSON")

    def test_head_field_unknown_role_branch_and_forbidden_authority_fail(self) -> None:
        mutations: list[dict] = []
        with_head = copy.deepcopy(self.fixture.source)
        with_head["head_sha"] = "0" * 40
        mutations.append(with_head)

        unknown_role = copy.deepcopy(self.fixture.source)
        unknown_role["role_grants"][0]["role"] = "PRODUCER"
        mutations.append(unknown_role)

        branch = copy.deepcopy(self.fixture.source)
        branch["branch_bindings"] = [{"branch_id": "caller.injected"}]
        mutations.append(branch)

        producer = copy.deepcopy(self.fixture.source)
        producer["authority_denials"]["producer_authority"] = True
        mutations.append(producer)

        for index, source in enumerate(mutations):
            with self.subTest(index=index):
                root, head = self.fixture.commit(source)
                self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_fixed_artifact_grant_and_schedule_mutations_fail(self) -> None:
        mutations: list[dict] = []
        artifact = copy.deepcopy(self.fixture.source)
        artifact["artifacts"][0]["symbol"] = "forged_verifier"
        mutations.append(artifact)

        grant = copy.deepcopy(self.fixture.source)
        grant["role_grants"][0]["capabilities"].append("PRODUCER")
        mutations.append(grant)

        for key, value in (
            ("ordered_gaps", [3, 7]),
            ("next_unchecked_gap", 19),
            ("coverage_semantics", "GLOBAL"),
            ("global_exhaustion", True),
            ("outcomes", ["ROOT_COUNTEREXAMPLE_CERTIFIED"]),
            ("issuer_authorized", True),
        ):
            source = copy.deepcopy(self.fixture.source)
            source["terminal_prefix_authority"][key] = value
            mutations.append(source)

        for index, source in enumerate(mutations):
            with self.subTest(index=index):
                root, head = self.fixture.commit(source)
                self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_artifact_and_grant_pins_are_mandatory(self) -> None:
        for pin_name in REGISTRY.ARTIFACT_PIN_KEYS:
            with self.subTest(pin_name=pin_name):
                source = copy.deepcopy(self.fixture.source)
                source["artifacts"][0][pin_name] = "0" * 64
                root, head = self.fixture.commit(source)
                self.assert_rejects(root, head, "ARTIFACT_PIN_MISMATCH")

        source = copy.deepcopy(self.fixture.source)
        source["role_grants"][0]["expected_artifact_semantic_sha256"] = "0" * 64
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "GRANT_PIN_MISMATCH")

    def test_code_change_does_not_inherit_role_without_registry_pin_update(self) -> None:
        altered = (ROOT / REGISTRY.SCHEDULER_PATH).read_bytes() + b"\n# harmless drift\n"
        root, head = self.fixture.commit(overrides={REGISTRY.SCHEDULER_PATH: altered})
        self.assert_rejects(root, head, "ARTIFACT_PIN_MISMATCH")

    def test_tests_docs_archive_and_reproductions_cannot_be_executable(self) -> None:
        for path in (
            "tests/authority.py",
            "docs/authority.py",
            "docs/archive/authority.py",
            "reproductions/authority.py",
        ):
            with self.subTest(path=path):
                with self.assertRaises(REGISTRY.RegistryV2Error) as raised:
                    REGISTRY._safe_path(path, executable=True)
                self.assertEqual(raised.exception.code, "FORBIDDEN_EXECUTABLE_ROOT")

    def test_identical_scheduler_and_verifier_blobs_are_rejected(self) -> None:
        root, head = self.fixture.commit(
            overrides={REGISTRY.VERIFIER_PATH: (ROOT / REGISTRY.SCHEDULER_PATH).read_bytes()}
        )
        self.assert_rejects(root, head, "ROLE_BLOB_COLLISION")

    def test_verifier_cannot_import_scheduler(self) -> None:
        altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + (
            b"\nimport t6_q_one_priority_prefix_scheduler_v1\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: altered})
        self.assert_rejects(root, head, "VERIFIER_IMPORTS_SCHEDULER")

    def test_scheduler_cannot_import_verifier(self) -> None:
        altered = (ROOT / REGISTRY.SCHEDULER_PATH).read_bytes() + (
            b"\nimport t6_q_one_priority_prefix_coverage_verifier_v1\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.SCHEDULER_PATH: altered})
        self.assert_rejects(root, head, "ROLE_IMPORT_CYCLE")

    def test_verifier_cannot_import_legacy_runtime_or_reproduction(self) -> None:
        verifier = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes()
        root, head = self.fixture.commit(
            overrides={
                REGISTRY.VERIFIER_PATH: verifier + b"\nimport t6_persistent_selector_runtime_v1\n",
                REGISTRY.LEGACY_RUNTIME_PATH: b"VALUE = 1\n",
            }
        )
        self.assert_rejects(root, head, "FORBIDDEN_AUTHORIZED_IMPORT")

        root, head = self.fixture.commit(
            overrides={
                REGISTRY.VERIFIER_PATH: verifier + b"\nimport reproductions.authority\n",
                "reproductions/authority.py": b"VALUE = 1\n",
            }
        )
        self.assert_rejects(root, head, "FORBIDDEN_IMPORT_ROOT")

    def test_nonliteral_dynamic_import_is_rejected(self) -> None:
        altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + (
            b"\n_DYNAMIC_TARGET = 'json'\n__import__(_DYNAMIC_TARGET)\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: altered})
        self.assert_rejects(root, head, "DYNAMIC_IMPORT_FORBIDDEN")

    def test_importlib_aliases_builtins_loader_and_dynamic_code_are_rejected(self) -> None:
        suffixes = (
            b"\nimport importlib as il\n",
            b"\nfrom importlib import import_module as load\n",
            b"\nfrom builtins import __import__ as load\n",
            b"\nexec('pass')\n",
            b"\neval('1')\n",
            b"\ncompile('1', '<x>', 'eval')\n",
        )
        for suffix in suffixes:
            with self.subTest(suffix=suffix):
                altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + suffix
                root, head = self.fixture.commit(
                    overrides={REGISTRY.VERIFIER_PATH: altered}
                )
                self.assert_rejects(root, head, "DYNAMIC_IMPORT_FORBIDDEN")

    def test_unresolved_forbidden_root_import_is_rejected(self) -> None:
        altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + (
            b"\nimport tests.untracked_authority\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: altered})
        self.assert_rejects(root, head, "FORBIDDEN_IMPORT_ROOT")

    def test_scheduler_and_verifier_cannot_share_a_local_helper(self) -> None:
        helper_path = "scripts/shared_prefix_authority_helper_v2.py"
        root, head = self.fixture.commit(
            overrides={
                REGISTRY.SCHEDULER_PATH: (
                    (ROOT / REGISTRY.SCHEDULER_PATH).read_bytes()
                    + b"\nimport shared_prefix_authority_helper_v2\n"
                ),
                REGISTRY.VERIFIER_PATH: (
                    (ROOT / REGISTRY.VERIFIER_PATH).read_bytes()
                    + b"\nimport shared_prefix_authority_helper_v2\n"
                ),
                helper_path: b"VALUE = 1\n",
            }
        )
        self.assert_rejects(root, head, "SHARED_LOCAL_IMPORT_CLOSURE")

    def test_authorized_symbol_import_alias_and_tuple_lambda_rebinding_fail(self) -> None:
        symbol = REGISTRY.VERIFIER_SYMBOL.encode("ascii")
        mutations = (
            b"\nfrom json import dumps as " + symbol + b"\n",
            b"\n(" + symbol + b", _other) = (lambda: None, lambda: None)\n",
        )
        for suffix in mutations:
            with self.subTest(suffix=suffix):
                altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + suffix
                root, head = self.fixture.commit(
                    overrides={REGISTRY.VERIFIER_PATH: altered}
                )
                self.assert_rejects(root, head, "SYMBOL_AMBIGUITY")

    def test_other_module_scope_store_and_delete_rebindings_fail(self) -> None:
        symbol = REGISTRY.VERIFIER_SYMBOL.encode("ascii")
        suffixes = (
            b"\n" + symbol + b" += 1\n",
            b"\n" + symbol + b": object\n",
            b"\nfor " + symbol + b" in ():\n    pass\n",
            (
                b"\nfrom contextlib import nullcontext\nwith nullcontext() as "
                + symbol
                + b":\n    pass\n"
            ),
            (
                b"\ntry:\n    raise ValueError\nexcept ValueError as "
                + symbol
                + b":\n    pass\n"
            ),
            b"\n(" + symbol + b" := 1)\n",
            b"\ndel " + symbol + b"\n",
            b"\nmatch 1:\n    case " + symbol + b":\n        pass\n",
        )
        for suffix in suffixes:
            with self.subTest(suffix=suffix):
                altered = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + suffix
                root, head = self.fixture.commit(
                    overrides={REGISTRY.VERIFIER_PATH: altered}
                )
                self.assert_rejects(root, head, "SYMBOL_AMBIGUITY")

    def test_decorated_or_conditional_authorized_function_is_rejected(self) -> None:
        original = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes()
        marker = b"def verify_q_one_priority_prefix_coverage_v1("
        decorated = original.replace(marker, b"@staticmethod\n" + marker, 1)
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: decorated})
        self.assert_rejects(root, head, "AUTHORIZED_SYMBOL_DECORATED")

        renamed = original.replace(
            marker, b"def renamed_q_one_priority_prefix_coverage_v1(", 1
        )
        conditional = renamed + (
            b"\nif True:\n    def verify_q_one_priority_prefix_coverage_v1(*args):\n"
            b"        return args\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: conditional})
        self.assert_rejects(root, head, "SYMBOL_NOT_FUNCTION")

    def test_ast_authority_digest_is_stable_across_supported_python_minors(self) -> None:
        py312 = REGISTRY._python_ast_contract_diagnostic_v2("cpython", "3.12")
        py313 = REGISTRY._python_ast_contract_diagnostic_v2("cpython", "3.13")
        self.assertNotEqual(py312["python_major_minor"], py313["python_major_minor"])
        self.assertEqual(py312["digest"], py313["digest"])
        changed_contract = REGISTRY._ast_authority_contract_digest_v2(
            REGISTRY.AST_DUMP_CONTRACT_VERSION + "_CHANGED"
        )
        self.assertNotEqual(py312["digest"], changed_contract)

    def test_missing_and_ambiguous_authorized_symbols_are_rejected(self) -> None:
        missing = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes().replace(
            b"def verify_q_one_priority_prefix_coverage_v1(",
            b"def renamed_q_one_priority_prefix_coverage_v1(",
            1,
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: missing})
        self.assert_rejects(root, head, "SYMBOL_MISSING")

        ambiguous = (ROOT / REGISTRY.VERIFIER_PATH).read_bytes() + (
            b"\ndef verify_q_one_priority_prefix_coverage_v1():\n    return None\n"
        )
        root, head = self.fixture.commit(overrides={REGISTRY.VERIFIER_PATH: ambiguous})
        self.assert_rejects(root, head, "SYMBOL_AMBIGUITY")

    def test_requested_head_schema_actually_governs_source(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        schema["properties"]["status"]["const"] = "IMPOSSIBLE_STATUS"
        root, head = self.fixture.commit(
            overrides={
                REGISTRY.SCHEMA_PATH: json.dumps(schema, indent=2).encode("ascii") + b"\n"
            }
        )
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_replace_refs_cannot_change_commit_or_registry_blob(self) -> None:
        root, original_head = self.fixture.commit()
        expected = self.resolve(root, original_head)
        changed = copy.deepcopy(self.fixture.source)
        changed["proof_boundary"] += " replacement target"
        write_json(root / REGISTRY.REGISTRY_PATH, changed)
        replacement_head = self.fixture.commit_current(root, "replacement")
        run_git(root, "replace", original_head, replacement_head)
        (root / REGISTRY.REGISTRY_PATH).write_bytes(DATA_PATH.read_bytes())
        with mock.patch.dict(os.environ, {"GIT_NO_REPLACE_OBJECTS": "0"}):
            self.assertEqual(self.resolve(root, original_head), expected)

        root, head = self.fixture.commit()
        expected = self.resolve(root, head)
        original_blob = run_git(root, "rev-parse", f"{head}:{REGISTRY.REGISTRY_PATH}")
        malicious = root / "malicious-registry.json"
        malicious.write_bytes(b'{"schema_id": NaN}\n')
        replacement_blob = run_git(root, "hash-object", "-w", str(malicious))
        run_git(root, "replace", original_blob, replacement_blob)
        with mock.patch.dict(os.environ, {"GIT_NO_REPLACE_OBJECTS": "0"}):
            self.assertEqual(self.resolve(root, head), expected)


if __name__ == "__main__":
    unittest.main()
