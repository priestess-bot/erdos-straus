from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_coordinator_role_registry_v4.py"
DATA_PATH = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v4.json"
SCHEMA_PATH = ROOT / "schemas" / "t6-coordinator-role-registry-v4.schema.json"
CLAIM_PATH = ROOT / "claims" / "t6-coordinator-q1-root-prefix-scoped-e1-authority-v4.md"
RECEIPT_SCHEMA_PATH = ROOT / "schemas" / "t6-q-one-root-prefix-scoped-e1-v2.schema.json"
SPEC = importlib.util.spec_from_file_location("t6_registry_v4_tests_module", MODULE_PATH)
assert SPEC and SPEC.loader
REGISTRY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = REGISTRY
SPEC.loader.exec_module(REGISTRY)


def git(root: Path, *args: str) -> str:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    return result.stdout.strip()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        json.dumps(value, ensure_ascii=True, indent=2, allow_nan=False).encode("ascii")
        + b"\n"
    )


class PendingRepository:
    def __init__(self, base: Path) -> None:
        self.base = base
        self.count = 0
        self.source = json.loads(DATA_PATH.read_text(encoding="ascii"))

    def commit(self, source: dict | None = None) -> tuple[Path, str]:
        self.count += 1
        root = self.base / f"repo-{self.count}"
        root.mkdir()
        document = copy.deepcopy(source if source is not None else self.source)
        paths = {
            REGISTRY.REGISTRY_PATH,
            REGISTRY.RESOLVER_PATH,
            REGISTRY.SCHEMA_PATH,
            REGISTRY.V3_REGISTRY_PATH,
            REGISTRY.V3_SCHEMA_PATH,
            REGISTRY.V3_RESOLVER_PATH,
            REGISTRY.V3_REGISTRY_PATH,
            REGISTRY.V3_SCHEMA_PATH,
            REGISTRY.V3_RESOLVER_PATH,
            REGISTRY.V3_PRODUCTION_VERIFIER_PATH,
            REGISTRY.V3_PRODUCTION_SCHEMA_PATH,
            "scripts/t6_q_one_root_initializer_envelope_v2.py",
            REGISTRY.V3_REGISTRY_PATH.replace("-v3", "-v2"),
            REGISTRY.V3_SCHEMA_PATH.replace("-v3", "-v2"),
            REGISTRY.V3_RESOLVER_PATH.replace("_v3", "_v2"),
        }
        paths.update(item["path"] for item in document["artifacts"])
        paths.update(item["path"] for item in document["pinned_documents"])
        v3_source = json.loads(
            (ROOT / REGISTRY.V3_REGISTRY_PATH).read_text(encoding="ascii")
        )
        paths.update(item["path"] for item in v3_source["artifacts"])
        paths.update(item["path"] for item in v3_source["pinned_documents"])
        for path in sorted(paths):
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / path).read_bytes())
        write_json(root / REGISTRY.REGISTRY_PATH, document)
        git(root, "init", "-q")
        git(root, "add", ".")
        git(
            root,
            "-c",
            "user.name=V4 test",
            "-c",
            "user.email=v4-test@example.invalid",
            "commit",
            "-q",
            "-m",
            "fixture",
        )
        return root, git(root, "rev-parse", "HEAD")


class CoordinatorRoleRegistryV4Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-registry-v4-")
        self.fixture = PendingRepository(Path(self.temp.name))
        self.source = copy.deepcopy(self.fixture.source)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def assert_rejects(self, source: dict, code: str) -> None:
        root, head = self.fixture.commit(source)
        with self.assertRaises(REGISTRY.RegistryV4Error) as raised:
            REGISTRY.resolve_registry_v4(root=root, requested_head=head)
        self.assertEqual(raised.exception.code, code)

    def test_schema_and_active_source_are_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(self.source)
        self.assertEqual(self.source["activation_status"], REGISTRY.ACTIVE)
        self.assertTrue(
            all(item["pin_status"] == "PINNED" for item in self.source["artifacts"])
        )

    def test_active_exact_head_registry_resolves_narrow_authority(self) -> None:
        root, head = self.fixture.commit()
        resolved = REGISTRY.resolve_registry_v4(root=root, requested_head=head)
        self.assertEqual(resolved["head_sha"], head)
        self.assertEqual(resolved["status"], REGISTRY.STATUS)
        self.assertEqual(resolved["new_role_grant_count"], 3)
        self.assertEqual(resolved["inherited_v3_role_grant_count"], 4)
        self.assertEqual(resolved["effective_role_capability_count"], 7)
        self.assertEqual(len(resolved["resolved_artifacts"]), 9)
        self.assertEqual(resolved["authorized_branches"], [])
        self.assertEqual(resolved["authority_denials"], REGISTRY.AUTHORITY_DENIALS)
        artifacts = {
            item["artifact_id"]: item for item in resolved["resolved_artifacts"]
        }
        for artifact_id in (
            REGISTRY.ORCHESTRATOR_ARTIFACT_ID,
            REGISTRY.REPLAYER_ARTIFACT_ID,
        ):
            self.assertEqual(
                artifacts[artifact_id]["controlled_loader_contract"]["status"],
                "FIXED_LOADER_CALL_TABLE_MATCHES_V4_DEPENDENCY_DAG",
            )
        unsigned = dict(resolved)
        digest = unsigned.pop("registry_digest")
        self.assertEqual(digest, REGISTRY.canonical_digest_v4(unsigned))

    def test_pending_registry_has_no_authority(self) -> None:
        source = copy.deepcopy(self.source)
        source["activation_status"] = REGISTRY.PENDING
        source["artifacts"][0]["pin_status"] = "PLACEHOLDER_UNRESOLVED"
        self.assert_rejects(source, "REGISTRY_NOT_ACTIVE")

    def test_pending_status_without_placeholder_fails_closed(self) -> None:
        source = copy.deepcopy(self.source)
        source["activation_status"] = REGISTRY.PENDING
        for artifact in source["artifacts"]:
            artifact["pin_status"] = "PINNED"
        source["pinned_documents"][0]["pin_status"] = "PINNED"
        self.assert_rejects(source, "ACTIVATION_STATUS_MISMATCH")

    def test_active_status_with_placeholder_fails_closed(self) -> None:
        source = copy.deepcopy(self.source)
        source["activation_status"] = REGISTRY.ACTIVE
        source["artifacts"][0]["pin_status"] = "PLACEHOLDER_UNRESOLVED"
        self.assert_rejects(source, "ACTIVATION_STATUS_MISMATCH")

    def test_exact_three_roles_and_two_nonroles_are_frozen(self) -> None:
        self.assertEqual(
            tuple(item["role"] for item in self.source["role_grants"]),
            (REGISTRY.ROLE_OWNER, REGISTRY.ROLE_CONSUMER, REGISTRY.ROLE_VALIDATOR),
        )
        artifacts = {item["artifact_id"]: item for item in self.source["artifacts"]}
        self.assertEqual(
            artifacts[REGISTRY.OWNER_ARTIFACT_ID]["symbols"],
            list(REGISTRY.OWNER_SYMBOLS),
        )
        self.assertEqual(
            artifacts[REGISTRY.VALIDATOR_ARTIFACT_ID]["symbols"],
            list(REGISTRY.VALIDATOR_SYMBOLS),
        )
        self.assertEqual(
            artifacts[REGISTRY.CONSUMER_ARTIFACT_ID]["symbols"],
            list(REGISTRY.CONSUMER_SYMBOLS),
        )
        self.assertEqual(
            artifacts[REGISTRY.ORCHESTRATOR_ARTIFACT_ID]["artifact_class"],
            REGISTRY.ARTIFACT_CLASS_ORCHESTRATOR,
        )
        self.assertEqual(
            artifacts[REGISTRY.REPLAYER_ARTIFACT_ID]["artifact_class"],
            REGISTRY.ARTIFACT_CLASS_REPLAYER,
        )

    def test_owner_does_not_depend_on_terminal_miss(self) -> None:
        owner_execution, owner_binding, _ = REGISTRY.DEPENDENCIES[REGISTRY.OWNER_ARTIFACT_ID]
        self.assertEqual(owner_execution, ())
        self.assertEqual(
            owner_binding,
            tuple(sorted((REGISTRY.OWNER_REFERENCE_ID, REGISTRY.V3_ROOT_INITIALIZER_ARTIFACT_ID))),
        )
        self.assertNotIn(REGISTRY.V3_PRODUCTION_VERIFIER_ARTIFACT_ID, owner_binding)
        validator = REGISTRY.DEPENDENCIES[REGISTRY.VALIDATOR_ARTIFACT_ID][1]
        consumer = REGISTRY.DEPENDENCIES[REGISTRY.CONSUMER_ARTIFACT_ID][1]
        self.assertIn(REGISTRY.V3_PRODUCTION_VERIFIER_ARTIFACT_ID, validator)
        self.assertIn(REGISTRY.V3_PRODUCTION_VERIFIER_ARTIFACT_ID, consumer)

    def test_scope_is_prefix_only_and_not_global(self) -> None:
        scope = self.source["authorized_consumer_scopes"][0]
        self.assertEqual(scope, REGISTRY.CONSUMER_SCOPE)
        self.assertEqual(scope["ordered_gaps"], [3, 7, 11])
        self.assertEqual(scope["next_unchecked_gap"], 15)
        self.assertIs(scope["global_exhaustion"], False)
        self.assertIs(scope["remaining_domain_unchecked"], True)
        self.assertIs(scope["same_head_consumption_required"], True)

    def test_authority_matrix_and_denials_are_exactly_nonrecursive(self) -> None:
        self.assertEqual(
            self.source["receipt_authority_matrix"], REGISTRY.RECEIPT_AUTHORITY_MATRIX
        )

    def test_normative_receipt_schema_matches_authority_matrix(self) -> None:
        receipt_schema = json.loads(RECEIPT_SCHEMA_PATH.read_text(encoding="utf-8"))
        definitions = receipt_schema["$defs"]
        receipt_definitions = {
            "COMMON_Q1_ROOT_OWNER_RECEIPT_V2": "ownerReceipt",
            "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2": "validationReceipt",
            "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2": "consumerReceipt",
        }
        for receipt_type, definition_name in receipt_definitions.items():
            with self.subTest(receipt_type=receipt_type):
                definition = definitions[definition_name]
                required = set(definition["required"])
                properties = definition["properties"]
                for field, value in REGISTRY.RECEIPT_AUTHORITY_MATRIX[
                    receipt_type
                ].items():
                    self.assertIn(field, required)
                    self.assertEqual(properties[field], {"const": value})
        owner = definitions["ownerReceipt"]
        self.assertIn("owner_id", owner["required"])
        self.assertEqual(
            owner["properties"]["owner_id"],
            {"type": "string", "pattern": "^owner:[0-9a-f]{64}$"},
        )
        validator = self.source["receipt_authority_matrix"][
            "Q1_REGISTERED_PREFIX_SCOPE_VALIDATION_RECEIPT_V2"
        ]
        consumer = self.source["receipt_authority_matrix"][
            "Q1_REGISTERED_PREFIX_ROOT_SOURCE_E1_RECEIPT_V2"
        ]
        self.assertIs(validator["common_owner_authority"], False)
        self.assertIs(validator["scope_validation_authority"], True)
        self.assertIs(consumer["common_owner_authority"], True)
        self.assertIs(consumer["root_source_scoped_e1"], True)
        self.assertEqual(self.source["authority_denials"], REGISTRY.AUTHORITY_DENIALS)
        self.assertTrue(
            all(value is False for value in self.source["authority_denials"].values())
        )
        matrix_keys = {
            frozenset(value) for value in self.source["receipt_authority_matrix"].values()
        }
        self.assertEqual(len(matrix_keys), 1)
        self.assertEqual(
            next(iter(matrix_keys)),
            frozenset(
                {
                    "source_actualness",
                    "common_owner_authority",
                    "registered_prefix_miss_authority",
                    "scope_validation_authority",
                    "root_source_scoped_e1",
                    "scope_aware_consumer_authority",
                    "root_source_occurrence_authority",
                    "terminal_receipt_direct_continuation_authority",
                    "e1_authority",
                    "generic_e1",
                    "successor_e1",
                    "producer_authority",
                    "producer_continuation_allowed",
                    "persistent_admission",
                    "queue_authority",
                    "e2_authority",
                    "e3_authority",
                    "e4_authority",
                    "e5_authority",
                    "global_exhaustion",
                    "terminal_leaf_authority",
                    "root_proof_close_authority",
                }
            ),
        )

    def test_v3_cross_binding_is_same_head_and_static(self) -> None:
        cross = self.source["v3_cross_registry_binding"]
        self.assertEqual(cross["registry_id"], REGISTRY.V3_REGISTRY_ID)
        self.assertIs(cross["same_head_required"], True)
        self.assertIs(cross["cross_head_receipts_allowed"], False)
        for key, path in (
            ("expected_v3_registry_source_sha256", REGISTRY.V3_REGISTRY_PATH),
            ("expected_v3_schema_sha256", REGISTRY.V3_SCHEMA_PATH),
            ("expected_v3_resolver_blob_sha256", REGISTRY.V3_RESOLVER_PATH),
        ):
            self.assertEqual(
                cross[key], hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            )

    def test_dependency_graph_is_acyclic_and_pin_keys_are_exact(self) -> None:
        REGISTRY._prevalidate_dependency_graph(self.source["artifacts"])
        for artifact in self.source["artifacts"]:
            manifest = artifact["dependency_manifest"]
            expected = set(manifest["execution_artifact_ids"]) | set(
                manifest["binding_artifact_ids"]
            )
            self.assertEqual(set(manifest["artifact_semantic_pins"]), expected)

    def test_source_mutations_fail_schema_or_fixed_policy(self) -> None:
        mutations = []
        role = copy.deepcopy(self.source)
        role["authority_policy"]["new_roles"].append("FORGED_ROLE")
        mutations.append(role)
        scope = copy.deepcopy(self.source)
        scope["authorized_consumer_scopes"][0]["next_unchecked_gap"] = 23
        mutations.append(scope)
        denials = copy.deepcopy(self.source)
        denials["authority_denials"]["successor_e1_authority"] = True
        mutations.append(denials)
        for source in mutations:
            with self.subTest(source=source):
                self.assert_rejects(source, "SOURCE_SCHEMA_INVALID")

    def test_exact_types_are_required_for_canonical_inputs(self) -> None:
        class StringSubclass(str):
            pass

        class IntegerSubclass(int):
            pass

        for value in ({StringSubclass("key"): "value"}, {"key": StringSubclass("value")}, {"key": IntegerSubclass(1)}):
            with self.subTest(value=value):
                with self.assertRaises(REGISTRY.RegistryV4Error) as raised:
                    REGISTRY.canonical_digest_v4(value)
                self.assertEqual(raised.exception.code, "NONCANONICAL_VALUE")

        class PathSubclass(type(Path())):
            pass

        root, head = self.fixture.commit()
        with self.assertRaises(REGISTRY.RegistryV4Error) as raised:
            REGISTRY.resolve_registry_v4(root=PathSubclass(root), requested_head=head)
        self.assertEqual(raised.exception.code, "INVALID_ROOT")

    def test_claim_states_serializer_and_future_boundary(self) -> None:
        claim = CLAIM_PATH.read_text(encoding="utf-8")
        self.assertIn("claim_status: established", claim)
        self.assertIn("review_status: independent_review", claim)
        self.assertIn("active registry requires", claim.lower())
        self.assertIn("local serializers do not authenticate", claim.lower())
        self.assertIn("generic or successor E1", claim)
        self.assertIn("global miss", claim)

    def test_resolver_api_has_no_queue_or_issuer_entrypoint(self) -> None:
        self.assertEqual(
            tuple(REGISTRY.resolve_registry_v4.__annotations__),
            ("root", "requested_head", "return"),
        )
        for name in (
            "enqueue_v4",
            "issue_v4",
            "authorize_e1_v4",
            "register_branch_v4",
        ):
            self.assertFalse(hasattr(REGISTRY, name))


if __name__ == "__main__":
    unittest.main()
