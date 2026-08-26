from __future__ import annotations

import copy
import hashlib
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
MODULE_PATH = ROOT / "scripts" / "t6_coordinator_role_registry_v3.py"
DATA_PATH = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v3.json"
SCHEMA_PATH = ROOT / "schemas" / "t6-coordinator-role-registry-v3.schema.json"
SPEC = importlib.util.spec_from_file_location(
    "t6_coordinator_role_registry_v3_under_test", MODULE_PATH
)
assert SPEC and SPEC.loader
REGISTRY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = REGISTRY
SPEC.loader.exec_module(REGISTRY)
V2_FOR_REPIN = REGISTRY._fresh_module(
    ROOT / REGISTRY.V2_RESOLVER_PATH,
    (ROOT / REGISTRY.V2_RESOLVER_PATH).read_bytes(),
    "t6_coordinator_role_registry_v2_for_v3_tests",
)


def run_git(root: Path, *args: str) -> str:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    completed = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True, env=environment
    )
    return completed.stdout.strip()


def write_json(path: Path, value: object) -> None:
    path.write_bytes(
        json.dumps(value, ensure_ascii=True, indent=2, allow_nan=False).encode("ascii")
        + b"\n"
    )


def repin_dependency_manifest(source: dict, artifact_id: str) -> None:
    artifact = next(
        item for item in source["artifacts"] if item["artifact_id"] == artifact_id
    )
    dependency_digest = REGISTRY.canonical_digest_v3(
        {
            "schema_id": "t6_artifact_dependency_manifest_v3",
            **artifact["dependency_manifest"],
        }
    )
    artifact["expected_dependency_manifest_digest"] = dependency_digest
    semantic = REGISTRY.canonical_digest_v3(
        {
            "method": REGISTRY.SEMANTIC_DIGEST_METHOD,
            "path": artifact["path"],
            "blob_sha256": artifact["expected_blob_sha256"],
            "symbol_set_digest": artifact["expected_symbol_set_digest"],
            "local_import_closure_digest": artifact[
                "expected_local_import_closure_digest"
            ],
            "dependency_manifest_digest": dependency_digest,
            "python_ast_contract_digest": V2_FOR_REPIN.python_ast_contract_v2()[
                "digest"
            ],
        }
    )
    artifact["expected_semantic_sha256"] = semantic
    if artifact_id in {
        REGISTRY.SCHEDULER_ARTIFACT_ID,
        REGISTRY.COVERAGE_ARTIFACT_ID,
    }:
        artifact["expected_v3_semantic_sha256"] = semantic
    for grant in source["role_grants"]:
        if grant["artifact_id"] == artifact_id:
            grant["expected_artifact_semantic_sha256"] = semantic
            grant["expected_dependency_manifest_digest"] = dependency_digest


def repin_dependency_graph(source: dict) -> None:
    artifacts = {item["artifact_id"]: item for item in source["artifacts"]}
    visited: set[str] = set()

    def visit(artifact_id: str) -> None:
        if artifact_id in visited:
            return
        artifact = artifacts[artifact_id]
        manifest = artifact["dependency_manifest"]
        dependencies = set(manifest["execution_artifact_ids"]) | set(
            manifest["binding_artifact_ids"]
        )
        for dependency_id in sorted(dependencies):
            visit(dependency_id)
        manifest["artifact_semantic_pins"] = {
            dependency_id: artifacts[dependency_id]["expected_semantic_sha256"]
            for dependency_id in sorted(dependencies)
        }
        repin_dependency_manifest(source, artifact_id)
        visited.add(artifact_id)

    for artifact_id in sorted(artifacts):
        visit(artifact_id)


def repin_single_file_artifact(source: dict, artifact_id: str, raw: bytes) -> None:
    artifact = next(
        item for item in source["artifacts"] if item["artifact_id"] == artifact_id
    )
    blob_sha256 = hashlib.sha256(raw).hexdigest()
    symbol_ast = {
        symbol: V2_FOR_REPIN._symbol_receipt(
            artifact["path"], symbol, raw, blob_sha256
        )["symbol_ast_sha256"]
        for symbol in artifact["symbols"]
    }
    artifact["expected_blob_sha256"] = blob_sha256
    artifact["expected_symbol_ast_sha256"] = symbol_ast
    artifact["expected_symbol_set_digest"] = REGISTRY.canonical_digest_v3(
        {
            "schema_id": "t6_python_symbol_set_v3",
            "symbols": {
                symbol: {"symbol_ast_sha256": digest}
                for symbol, digest in symbol_ast.items()
            },
        }
    )
    git_object_id = hashlib.sha1(
        b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw,
        usedforsecurity=False,
    ).hexdigest()
    artifact["expected_local_import_closure_digest"] = REGISTRY.canonical_digest_v3(
        {
            "schema_id": "t6_local_import_closure_v3",
            "files": [
                {
                    "path": artifact["path"],
                    "git_mode": "100644",
                    "git_object_id": git_object_id,
                    "blob_sha256": blob_sha256,
                }
            ],
        }
    )
    repin_dependency_manifest(source, artifact_id)


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
        cross = document.get("v2_cross_registry_binding", {})
        files.update(
            value
            for key, value in cross.items()
            if key in {"registry_path", "schema_path", "resolver_path"}
            and type(value) is str
        )
        files.update(
            item["path"]
            for item in document.get("pinned_documents", [])
            if type(item) is dict and type(item.get("path")) is str
        )
        overrides = overrides or {}
        for path in sorted(files | set(overrides)):
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
            "user.name=Registry V3 Test",
            "-c",
            "user.email=registry-v3-test@example.invalid",
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
            "user.name=Registry V3 Test",
            "-c",
            "user.email=registry-v3-test@example.invalid",
            "commit",
            "-q",
            "-m",
            message,
        )
        return run_git(root, "rev-parse", "HEAD")


class CoordinatorRoleRegistryV3Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-role-registry-v3-")
        self.fixture = RepositoryFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def resolve(self, root: Path, head: str) -> dict:
        return REGISTRY.resolve_registry_v3(root=root, requested_head=head)

    def assert_rejects(self, root: Path, head: str, code: str) -> None:
        with self.assertRaises(REGISTRY.RegistryV3Error) as raised:
            self.resolve(root, head)
        self.assertEqual(raised.exception.code, code)

    def test_baseline_has_exact_four_roles_and_no_recursive_authority(self) -> None:
        root, head = self.fixture.commit()
        first = self.resolve(root, head)
        self.assertEqual(first, self.resolve(root, head))
        self.assertEqual(first["status"], REGISTRY.STATUS)
        self.assertEqual(first["head_sha"], head)
        self.assertEqual(first["active_role_grant_count"], 4)
        self.assertEqual(first["root_initializer_count"], 1)
        self.assertEqual(first["terminal_issuer_count"], 1)
        self.assertEqual(first["terminal_scheduler_count"], 1)
        self.assertEqual(first["independent_coverage_verifier_count"], 1)
        self.assertEqual(first["assembler_role_count"], 0)
        self.assertEqual(first["receipt_verifier_role_count"], 0)
        self.assertEqual(first["authorized_branches"], [])
        self.assertEqual(first["authority_denials"], REGISTRY.AUTHORITY_DENIALS)
        unsigned = dict(first)
        observed = unsigned.pop("registry_digest")
        self.assertEqual(observed, REGISTRY.canonical_digest_v3(unsigned))

    def test_roles_are_distinct_and_nonroles_remain_dependencies(self) -> None:
        root, head = self.fixture.commit()
        resolved = self.resolve(root, head)
        artifacts = {item["artifact_id"]: item for item in resolved["resolved_artifacts"]}
        grants = {item["role"]: item for item in resolved["resolved_role_grants"]}
        self.assertEqual(set(grants), set(REGISTRY.ALLOWED_ROLES))
        role_artifacts = [artifacts[grant["artifact_id"]] for grant in grants.values()]
        self.assertEqual(len({item["path"] for item in role_artifacts}), 4)
        self.assertEqual(len({item["blob_sha256"] for item in role_artifacts}), 4)
        self.assertEqual(len({item["semantic_sha256"] for item in role_artifacts}), 4)
        self.assertNotIn(REGISTRY.ASSEMBLER_ARTIFACT_ID, {g["artifact_id"] for g in grants.values()})
        self.assertNotIn(
            REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID,
            {g["artifact_id"] for g in grants.values()},
        )
        self.assertEqual(
            artifacts[REGISTRY.ASSEMBLER_ARTIFACT_ID]["artifact_class"],
            REGISTRY.ARTIFACT_CLASS_ASSEMBLER,
        )
        self.assertEqual(
            artifacts[REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID]["artifact_class"],
            REGISTRY.ARTIFACT_CLASS_REPLAYER,
        )

    def test_every_artifact_and_grant_pin_replays(self) -> None:
        root, head = self.fixture.commit()
        resolved = self.resolve(root, head)
        artifacts_by_id = {
            item["artifact_id"]: item for item in resolved["resolved_artifacts"]
        }
        for artifact in resolved["resolved_artifacts"]:
            self.assertEqual(artifact["expected_blob_sha256"], artifact["blob_sha256"])
            self.assertEqual(
                artifact["expected_symbol_set_digest"], artifact["symbol_set_digest"]
            )
            self.assertEqual(
                artifact["expected_local_import_closure_digest"],
                artifact["local_import_closure_digest"],
            )
            self.assertEqual(
                artifact["expected_dependency_manifest_digest"],
                artifact["dependency_manifest_digest"],
            )
            self.assertEqual(
                artifact["expected_semantic_sha256"], artifact["semantic_sha256"]
            )
            dependency_ids = set(
                artifact["dependency_manifest"]["execution_artifact_ids"]
            ) | set(artifact["dependency_manifest"]["binding_artifact_ids"])
            self.assertEqual(
                set(artifact["dependency_manifest"]["artifact_semantic_pins"]),
                dependency_ids,
            )
            for dependency_id, semantic in artifact["dependency_manifest"][
                "artifact_semantic_pins"
            ].items():
                self.assertEqual(
                    semantic, artifacts_by_id[dependency_id]["semantic_sha256"]
                )
        for grant in resolved["resolved_role_grants"]:
            self.assertEqual(
                grant["expected_artifact_semantic_sha256"],
                grant["artifact_semantic_sha256"],
            )

    def test_initializer_actualness_is_external_and_issuer_attested(self) -> None:
        root, head = self.fixture.commit()
        policy = self.resolve(root, head)["root_initializer_authority"]
        self.assertEqual(policy, REGISTRY.ROOT_INITIALIZER_POLICY)
        self.assertIs(policy["initializer_output_self_authorizing"], False)
        self.assertEqual(policy["actualness_attestor_role"], REGISTRY.ROLE_ISSUER)
        initializer_grant = next(
            item
            for item in self.resolve(root, head)["resolved_role_grants"]
            if item["role"] == REGISTRY.ROLE_INITIALIZER
        )
        self.assertNotIn("ISSUE_ROOT_ACTUALNESS_SIDECAR", initializer_grant["capabilities"])

    def test_hit_and_prefix_miss_authority_matrix_is_exact(self) -> None:
        root, head = self.fixture.commit()
        resolved = self.resolve(root, head)
        self.assertEqual(
            resolved["terminal_issuance_policy"], REGISTRY.TERMINAL_ISSUANCE_POLICY
        )
        matrix = resolved["terminal_issuance_policy"]["authority_matrix"]
        self.assertIs(matrix["common"]["e1_authority"], False)
        self.assertIs(matrix["common"]["queue_authority"], False)
        self.assertIs(matrix[REGISTRY.HIT_OUTCOME]["root_proof_close_authority"], True)
        self.assertIs(matrix[REGISTRY.MISS_OUTCOME]["root_proof_close_authority"], False)
        prefix = resolved["authorized_terminal_prefixes"][0]
        self.assertEqual(prefix["ordered_gaps"], [3, 7, 11])
        self.assertEqual(prefix["next_unchecked_gap"], 15)
        self.assertIs(prefix["global_exhaustion"], False)

    def test_issuer_and_replayer_dependency_dag_has_no_direct_role_bypass(self) -> None:
        root, head = self.fixture.commit()
        resolved = self.resolve(root, head)
        artifacts = {item["artifact_id"]: item for item in resolved["resolved_artifacts"]}
        issuer_dependencies = set(
            artifacts[REGISTRY.ISSUER_ARTIFACT_ID]["dependency_manifest"][
                "execution_artifact_ids"
            ]
        )
        self.assertFalse(
            issuer_dependencies
            & {
                REGISTRY.SCHEDULER_ARTIFACT_ID,
                REGISTRY.COVERAGE_ARTIFACT_ID,
                REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID,
            }
        )
        replayer_dependencies = set(
            artifacts[REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID]["dependency_manifest"][
                "execution_artifact_ids"
            ]
        )
        self.assertNotIn(REGISTRY.ISSUER_ARTIFACT_ID, replayer_dependencies)
        self.assertEqual(
            resolved["post_issuance_replay_policy"],
            REGISTRY.POST_ISSUANCE_REPLAY_POLICY,
        )

    def test_v2_cross_registry_role_digests_are_bound_separately(self) -> None:
        root, head = self.fixture.commit()
        cross = self.resolve(root, head)["v2_cross_registry_binding"]
        self.assertEqual(cross["v2_registry_id"], REGISTRY.V2_REGISTRY_ID)
        self.assertTrue(cross["v2_registry_digest"])
        self.assertTrue(cross["v2_role_manifest_digest"])
        self.assertEqual(
            set(cross["v2_role_subdigests"]),
            {
                "independent_coverage_verifier_registry",
                "terminal_prefix_registry",
                "terminal_scheduler_registry",
            },
        )

    def test_source_has_no_head_and_api_has_no_authority_override(self) -> None:
        source = json.loads(DATA_PATH.read_text(encoding="ascii"))
        self.assertNotIn("head_sha", source)
        parameters = inspect.signature(REGISTRY.resolve_registry_v3).parameters
        self.assertEqual(tuple(parameters), ("root", "requested_head"))
        self.assertTrue(
            all(item.kind is inspect.Parameter.KEYWORD_ONLY for item in parameters.values())
        )
        for name in ("register_branch_v3", "enqueue_v3", "authorize_e1_v3"):
            self.assertFalse(hasattr(REGISTRY, name))

    def test_exact_builtin_types_and_fixed_role_grants_are_required(self) -> None:
        class StringSubclass(str):
            pass

        class IntegerSubclass(int):
            pass

        for value in (
            {StringSubclass("key"): "value"},
            {"key": StringSubclass("value")},
            {"key": IntegerSubclass(1)},
        ):
            with self.subTest(value=value):
                with self.assertRaises(REGISTRY.RegistryV3Error) as raised:
                    REGISTRY.canonical_digest_v3(value)
                self.assertEqual(raised.exception.code, "NONCANONICAL_VALUE")

        root, head = self.fixture.commit()
        self.assert_rejects(root, StringSubclass(head), "INVALID_HEAD")

        unknown_role = copy.deepcopy(self.fixture.source)
        unknown_role["role_grants"][0]["role"] = "UNKNOWN_ROLE"
        root, head = self.fixture.commit(unknown_role)
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

        changed_capability = copy.deepcopy(self.fixture.source)
        changed_capability["role_grants"][0]["capabilities"] = ["MINT_AUTHORITY"]
        root, head = self.fixture.commit(changed_capability)
        self.assert_rejects(root, head, "FIXED_GRANT_MISMATCH")

    def test_symbolic_short_head_and_toolchain_drift_fail(self) -> None:
        root, head = self.fixture.commit()
        self.assert_rejects(root, "HEAD", "INVALID_HEAD")
        self.assert_rejects(root, head[:12], "INVALID_HEAD")
        for path in REGISTRY.TOOLCHAIN_PATHS:
            root, head = self.fixture.commit()
            target = root / path
            target.write_bytes(target.read_bytes() + b"\n")
            self.assert_rejects(root, head, "TOOLCHAIN_WORKTREE_MISMATCH")

    def test_code_and_pin_drift_do_not_inherit_authority(self) -> None:
        altered = (ROOT / REGISTRY.ISSUER_PATH).read_bytes() + b"\n# drift\n"
        root, head = self.fixture.commit(overrides={REGISTRY.ISSUER_PATH: altered})
        self.assert_rejects(root, head, "ARTIFACT_PIN_MISMATCH")

        for pin in REGISTRY.ARTIFACT_PIN_FIELDS:
            source = copy.deepcopy(self.fixture.source)
            source["artifacts"][0][pin] = "0" * 64
            root, head = self.fixture.commit(source)
            expected = (
                "DEPENDENCY_MANIFEST_PIN_MISMATCH"
                if pin == "expected_dependency_manifest_digest"
                else "ARTIFACT_PIN_MISMATCH"
            )
            self.assert_rejects(root, head, expected)

        source = copy.deepcopy(self.fixture.source)
        source["role_grants"][0]["expected_artifact_semantic_sha256"] = "0" * 64
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "GRANT_PIN_MISMATCH")

    def test_policy_authority_and_branch_mutations_fail_closed(self) -> None:
        mutations: list[dict] = []
        matrix = copy.deepcopy(self.fixture.source)
        matrix["terminal_issuance_policy"]["authority_matrix"]["common"][
            "e1_authority"
        ] = True
        mutations.append(matrix)
        actualness = copy.deepcopy(self.fixture.source)
        actualness["root_initializer_authority"]["initializer_output_self_authorizing"] = True
        mutations.append(actualness)
        assembler = copy.deepcopy(self.fixture.source)
        artifact = next(
            item
            for item in assembler["artifacts"]
            if item["artifact_id"] == REGISTRY.ASSEMBLER_ARTIFACT_ID
        )
        artifact["artifact_class"] = REGISTRY.ARTIFACT_CLASS_ROLE
        mutations.append(assembler)
        branch = copy.deepcopy(self.fixture.source)
        branch["branch_bindings"] = [{"branch_id": "forged"}]
        mutations.append(branch)
        denial = copy.deepcopy(self.fixture.source)
        denial["authority_denials"]["producer_authority"] = True
        mutations.append(denial)
        for index, source in enumerate(mutations):
            with self.subTest(index=index):
                root, head = self.fixture.commit(source)
                with self.assertRaises(REGISTRY.RegistryV3Error):
                    self.resolve(root, head)

    def test_dependency_manifest_direct_bypass_and_cycle_mutations_fail(self) -> None:
        source = copy.deepcopy(self.fixture.source)
        issuer = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == REGISTRY.ISSUER_ARTIFACT_ID
        )
        issuer["dependency_manifest"]["execution_artifact_ids"].append(
            REGISTRY.SCHEDULER_ARTIFACT_ID
        )
        scheduler = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == REGISTRY.SCHEDULER_ARTIFACT_ID
        )
        issuer["dependency_manifest"]["artifact_semantic_pins"][
            REGISTRY.SCHEDULER_ARTIFACT_ID
        ] = scheduler["expected_semantic_sha256"]
        repin_dependency_manifest(source, REGISTRY.ISSUER_ARTIFACT_ID)
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "ISSUER_DIRECT_ROLE_BYPASS")

        source = copy.deepcopy(self.fixture.source)
        replayer = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID
        )
        replayer["dependency_manifest"]["execution_artifact_ids"].append(
            REGISTRY.ISSUER_ARTIFACT_ID
        )
        repin_dependency_manifest(source, REGISTRY.RECEIPT_VERIFIER_ARTIFACT_ID)
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "RECEIPT_VERIFIER_IMPORTS_ISSUER")

        source = copy.deepcopy(self.fixture.source)
        assembler = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == REGISTRY.ASSEMBLER_ARTIFACT_ID
        )
        assembler["dependency_manifest"]["execution_artifact_ids"].append(
            REGISTRY.ISSUER_ARTIFACT_ID
        )
        issuer = next(
            item
            for item in source["artifacts"]
            if item["artifact_id"] == REGISTRY.ISSUER_ARTIFACT_ID
        )
        assembler["dependency_manifest"]["artifact_semantic_pins"][
            REGISTRY.ISSUER_ARTIFACT_ID
        ] = issuer["expected_semantic_sha256"]
        repin_dependency_manifest(source, REGISTRY.ASSEMBLER_ARTIFACT_ID)
        root, head = self.fixture.commit(source)
        self.assert_rejects(root, head, "DEPENDENCY_CYCLE")

    def test_dependency_code_update_requires_consumer_semantic_repin(self) -> None:
        altered_initializer = (
            (ROOT / REGISTRY.INITIALIZER_PATH).read_bytes()
            + b"\n# dependency semantic pin control\n"
        )
        stale = copy.deepcopy(self.fixture.source)
        repin_single_file_artifact(
            stale, REGISTRY.INITIALIZER_ARTIFACT_ID, altered_initializer
        )
        root, head = self.fixture.commit(
            stale, overrides={REGISTRY.INITIALIZER_PATH: altered_initializer}
        )
        self.assert_rejects(root, head, "DEPENDENCY_SEMANTIC_PIN_MISMATCH")

        updated = copy.deepcopy(stale)
        repin_dependency_graph(updated)
        root, head = self.fixture.commit(
            updated, overrides={REGISTRY.INITIALIZER_PATH: altered_initializer}
        )
        self.resolve(root, head)

    def test_dependency_semantic_pin_key_set_is_exact(self) -> None:
        for add_extra in (False, True):
            source = copy.deepcopy(self.fixture.source)
            issuer = next(
                item
                for item in source["artifacts"]
                if item["artifact_id"] == REGISTRY.ISSUER_ARTIFACT_ID
            )
            pins = issuer["dependency_manifest"]["artifact_semantic_pins"]
            if add_extra:
                pins[REGISTRY.SCHEDULER_ARTIFACT_ID] = next(
                    item["expected_semantic_sha256"]
                    for item in source["artifacts"]
                    if item["artifact_id"] == REGISTRY.SCHEDULER_ARTIFACT_ID
                )
            else:
                pins.pop(REGISTRY.INITIALIZER_ARTIFACT_ID)
            repin_dependency_manifest(source, REGISTRY.ISSUER_ARTIFACT_ID)
            root, head = self.fixture.commit(source)
            self.assert_rejects(
                root, head, "DEPENDENCY_SEMANTIC_PIN_SET_MISMATCH"
            )

    def test_nonloader_dynamic_loading_aliases_and_code_are_rejected(self) -> None:
        suffixes = (
            b"\nimport importlib as il\n",
            b"\nfrom importlib import import_module as load\n",
            b"\nfrom builtins import __import__ as load\n",
            b"\n__import__('json')\n",
            b"\nexec('pass')\n",
            b"\neval('1')\n",
            b"\ncompile('1', '<x>', 'eval')\n",
        )
        original = (ROOT / REGISTRY.INITIALIZER_PATH).read_bytes()
        for suffix in suffixes:
            with self.subTest(suffix=suffix):
                root, head = self.fixture.commit(
                    overrides={REGISTRY.INITIALIZER_PATH: original + suffix}
                )
                self.assert_rejects(root, head, "DYNAMIC_LOADER_FORBIDDEN")

    def test_fully_repinned_extra_compile_exec_loader_is_rejected(self) -> None:
        original = (ROOT / REGISTRY.ISSUER_PATH).read_bytes()
        marker = (
            b'    """Issue one exact-HEAD q=1 root terminal or registered-prefix '
            b'miss receipt."""\n'
        )
        self.assertIn(marker, original)
        escaped = original.replace(
            marker,
            marker
            + b"    undeclared = 'pass'\n"
            + b"    exec(compile(undeclared, "
            + b"'scripts/t6_q_one_priority_prefix_scheduler_v1.py', 'exec'))\n",
            1,
        )
        source = copy.deepcopy(self.fixture.source)
        repin_single_file_artifact(source, REGISTRY.ISSUER_ARTIFACT_ID, escaped)
        repin_dependency_graph(source)
        root, head = self.fixture.commit(
            source, overrides={REGISTRY.ISSUER_PATH: escaped}
        )
        self.assert_rejects(
            root, head, "CONTROLLED_EXECUTABLE_LITERAL_MISMATCH"
        )

    def test_authorized_symbol_rebinding_and_forbidden_root_import_fail(self) -> None:
        symbol = REGISTRY.COVERAGE_SYMBOL.encode("ascii")
        original = (ROOT / REGISTRY.COVERAGE_PATH).read_bytes()
        suffixes = (
            b"\nfrom json import dumps as " + symbol + b"\n",
            b"\n(" + symbol + b", _other) = (lambda: None, lambda: None)\n",
            b"\ndel " + symbol + b"\n",
        )
        for suffix in suffixes:
            with self.subTest(suffix=suffix):
                root, head = self.fixture.commit(
                    overrides={REGISTRY.COVERAGE_PATH: original + suffix}
                )
                self.assert_rejects(root, head, "SYMBOL_AMBIGUITY")

        root, head = self.fixture.commit(
            overrides={
                REGISTRY.COVERAGE_PATH: original
                + b"\nimport tests.untracked_authority\n"
            }
        )
        self.assert_rejects(root, head, "FORBIDDEN_IMPORT_ROOT")

    def test_cross_role_pins_are_required_only_for_v2_roles(self) -> None:
        missing = copy.deepcopy(self.fixture.source)
        scheduler = next(
            item
            for item in missing["artifacts"]
            if item["artifact_id"] == REGISTRY.SCHEDULER_ARTIFACT_ID
        )
        del scheduler["expected_v2_semantic_sha256"]
        root, head = self.fixture.commit(missing)
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

        extra = copy.deepcopy(self.fixture.source)
        issuer = next(
            item
            for item in extra["artifacts"]
            if item["artifact_id"] == REGISTRY.ISSUER_ARTIFACT_ID
        )
        issuer["expected_v2_semantic_sha256"] = "0" * 64
        root, head = self.fixture.commit(extra)
        self.assert_rejects(root, head, "SOURCE_SCHEMA_INVALID")

    def test_ast_authority_digest_is_stable_across_supported_python_minors(self) -> None:
        py312 = V2_FOR_REPIN._python_ast_contract_diagnostic_v2("cpython", "3.12")
        py313 = V2_FOR_REPIN._python_ast_contract_diagnostic_v2("cpython", "3.13")
        self.assertNotEqual(py312["python_major_minor"], py313["python_major_minor"])
        self.assertEqual(py312["digest"], py313["digest"])
        changed = V2_FOR_REPIN._ast_authority_contract_digest_v2(
            V2_FOR_REPIN.AST_DUMP_CONTRACT_VERSION + "_CHANGED"
        )
        self.assertNotEqual(py312["digest"], changed)

    def test_cross_registry_pin_mutation_fails(self) -> None:
        for key in (
            "expected_v2_registry_source_sha256",
            "expected_v2_schema_sha256",
            "expected_v2_resolver_blob_sha256",
            "expected_v2_scheduler_semantic_sha256",
            "expected_v2_coverage_verifier_semantic_sha256",
        ):
            source = copy.deepcopy(self.fixture.source)
            source["v2_cross_registry_binding"][key] = "0" * 64
            root, head = self.fixture.commit(source)
            with self.assertRaises(REGISTRY.RegistryV3Error):
                self.resolve(root, head)

    def test_invalid_but_rehashed_production_schema_is_rejected(self) -> None:
        invalid = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": (
                "https://priestess-bot.github.io/erdos-straus/schemas/"
                "t6-q-one-production-terminal-receipts-v1.schema.json"
            ),
            "type": "not-a-json-schema-type"
        }
        raw = json.dumps(invalid, ensure_ascii=True, indent=2).encode("ascii") + b"\n"
        source = copy.deepcopy(self.fixture.source)
        document = source["pinned_documents"][0]
        document["expected_blob_sha256"] = hashlib.sha256(raw).hexdigest()
        document["expected_canonical_sha256"] = REGISTRY.canonical_digest_v3(invalid)
        root, head = self.fixture.commit(
            source, overrides={REGISTRY.PRODUCTION_RECEIPT_SCHEMA_PATH: raw}
        )
        self.assert_rejects(root, head, "PINNED_DOCUMENT_SCHEMA_INVALID")

    def test_duplicate_json_and_replace_ref_fail_closed(self) -> None:
        raw = DATA_PATH.read_bytes().replace(
            b'{\n  "schema_id":',
            b'{\n  "schema_id": "duplicate",\n  "schema_id":',
            1,
        )
        root, head = self.fixture.commit(raw_registry=raw)
        self.assert_rejects(root, head, "DUPLICATE_JSON_KEY")

        root, original_head = self.fixture.commit()
        original_registry = (root / REGISTRY.REGISTRY_PATH).read_bytes()
        expected = self.resolve(root, original_head)
        changed = copy.deepcopy(self.fixture.source)
        changed["proof_boundary"] += " replacement"
        write_json(root / REGISTRY.REGISTRY_PATH, changed)
        replacement = self.fixture.commit_current(root, "replacement")
        run_git(root, "replace", original_head, replacement)
        (root / REGISTRY.REGISTRY_PATH).write_bytes(original_registry)
        with mock.patch.dict(os.environ, {"GIT_NO_REPLACE_OBJECTS": "0"}):
            self.assertEqual(self.resolve(root, original_head), expected)


if __name__ == "__main__":
    unittest.main()
