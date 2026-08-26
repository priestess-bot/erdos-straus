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


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_coordinator_role_registry_v5.py"
DATA_PATH = ROOT / "data" / "t6-wave1" / "t6-coordinator-role-registry-v5.json"
SCHEMA_PATH = ROOT / "schemas" / "t6-coordinator-role-registry-v5.schema.json"
CLAIM_PATH = (
    ROOT / "claims" / "t6-coordinator-q1-root-v1-base-admission-authority-v5.md"
)
SPEC = importlib.util.spec_from_file_location("t6_registry_v5_test_module", MODULE_PATH)
assert SPEC and SPEC.loader
REGISTRY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = REGISTRY
SPEC.loader.exec_module(REGISTRY)


def run_git(root: Path, *args: str) -> str:
    env = os.environ.copy()
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True, env=env
    )
    return result.stdout.strip()


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2, allow_nan=False) + "\n",
        encoding="ascii",
    )


class ActiveFixture:
    """A compact exact-HEAD tree containing all V2/V3/V4/V5 authority inputs."""

    def __init__(self, base: Path) -> None:
        self.base = base
        self.count = 0
        self.source = json.loads(DATA_PATH.read_text(encoding="ascii"))

    @staticmethod
    def paths(source: dict[str, object]) -> set[str]:
        result = {
            REGISTRY.REGISTRY_PATH,
            REGISTRY.SCHEMA_PATH,
            REGISTRY.RESOLVER_PATH,
        }
        for version in ("v2", "v3", "v4"):
            data_path = f"data/t6-wave1/t6-coordinator-role-registry-{version}.json"
            result.update(
                {
                    data_path,
                    f"schemas/t6-coordinator-role-registry-{version}.schema.json",
                    f"scripts/t6_coordinator_role_registry_{version}.py",
                }
            )
            nested = json.loads((ROOT / data_path).read_text(encoding="ascii"))
            result.update(item["path"] for item in nested["artifacts"])
            result.update(item["path"] for item in nested.get("pinned_documents", []))
        for item in source["artifacts"]:
            result.add(item["path"])
        for item in source["pinned_documents"]:
            result.add(item["path"])
        return result

    def commit(
        self,
        source: dict[str, object] | None = None,
        *,
        overrides: dict[str, bytes] | None = None,
    ) -> tuple[Path, str]:
        self.count += 1
        self.base.mkdir(parents=True, exist_ok=True)
        root = self.base / f"repo-{self.count}"
        root.mkdir()
        document = copy.deepcopy(source if source is not None else self.source)
        overrides = overrides or {}
        for path in sorted(self.paths(document) | set(overrides)):
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            if path in overrides:
                target.write_bytes(overrides[path])
            else:
                shutil.copyfile(ROOT / path, target)
        write_json(root / REGISTRY.REGISTRY_PATH, document)
        run_git(root, "init", "-q")
        run_git(root, "add", ".")
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=V5 test",
                "-c",
                "user.email=v5@example.invalid",
                "commit",
                "-q",
                "-m",
                "fixture",
            ],
            cwd=root,
            check=True,
        )
        return root, run_git(root, "rev-parse", "HEAD")


class CoordinatorRoleRegistryV5Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="t6-registry-v5-")
        self.fixture = ActiveFixture(Path(self.temp.name))
        self.source = copy.deepcopy(self.fixture.source)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def reject(self, source: dict[str, object], code: str) -> None:
        root, head = self.fixture.commit(source)
        with self.assertRaises(REGISTRY.RegistryV5Error) as raised:
            REGISTRY.resolve_registry_v5(root=root, requested_head=head)
        self.assertEqual(raised.exception.code, code)

    def test_schema_and_active_source_are_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="ascii"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(self.source)
        self.assertEqual(self.source["activation_status"], REGISTRY.ACTIVE)
        self.assertEqual(len(self.source["artifacts"]), 12)
        self.assertTrue(all(item["pin_status"] == "PINNED" for item in self.source["artifacts"]))

    def test_exact_head_resolves_only_the_fixed_active_authority(self) -> None:
        root, head = self.fixture.commit()
        resolved = REGISTRY.resolve_registry_v5(root=root, requested_head=head)
        self.assertEqual(resolved["head_sha"], head)
        self.assertEqual(resolved["status"], REGISTRY.STATUS)
        self.assertEqual(resolved["new_role_grant_count"], 2)
        self.assertEqual(resolved["effective_role_capability_count"], 5)
        self.assertEqual(resolved["queue_mutator_count"], 0)
        self.assertEqual(resolved["successor_producer_count"], 0)
        self.assertEqual(
            {item["artifact_id"] for item in resolved["resolved_artifacts"]},
            {item[0] for item in REGISTRY.IDENTITIES},
        )
        contracts = {
            item["artifact_id"]: item["controlled_loader_contract"]
            for item in resolved["resolved_artifacts"]
            if "controlled_loader_contract" in item
        }
        self.assertEqual(set(contracts), set(REGISTRY.CONTROLLED_LOADER_CONTRACTS))

    def test_roles_and_nonroles_are_exact(self) -> None:
        self.assertEqual(
            {grant["role"] for grant in self.source["role_grants"]},
            {REGISTRY.ROLE_MATERIALIZER, REGISTRY.ROLE_ADMISSION},
        )
        artifacts = {item["artifact_id"]: item for item in self.source["artifacts"]}
        self.assertEqual(artifacts[REGISTRY.ADAPTER_ID]["artifact_class"], "CANONICAL_PROJECTION_ONLY")
        self.assertEqual(
            artifacts[REGISTRY.ORCHESTRATOR_ID]["artifact_class"],
            "CONTROLLED_LOADER_ORCHESTRATOR_ONLY",
        )
        self.assertEqual(
            artifacts[REGISTRY.REPLAYER_ID]["artifact_class"],
            "POST_ISSUANCE_REPLAY_DEPENDENCY_ONLY",
        )

    def test_base_semantic_excludes_v4_e1_candidate(self) -> None:
        policy = self.source["base_admission_policy"]
        self.assertTrue(policy["requires_v4_owner_receipt"])
        self.assertTrue(policy["requires_v4_scope_validation_receipt"])
        self.assertIn("v4_e1_receipt", policy["v1_state_semantic_forbidden_fields"])
        materializer = next(
            item
            for item in self.source["artifacts"]
            if item["artifact_id"] == REGISTRY.MATERIALIZER_ID
        )
        self.assertNotIn(REGISTRY.V4_OWNER_ID, materializer["dependency_manifest"]["execution_artifact_ids"])
        self.assertNotIn(REGISTRY.V4_SCOPE_ID, materializer["dependency_manifest"]["execution_artifact_ids"])

    def test_denials_keep_base_admission_nonrecursive(self) -> None:
        self.assertTrue(all(value is False for value in self.source["authority_denials"].values()))
        self.assertEqual(self.source["authorized_branches"], [])
        self.assertFalse(self.source["base_admission_policy"]["global_exhaustion"])

    def test_active_placeholder_mismatch_fails_closed(self) -> None:
        source = copy.deepcopy(self.source)
        source["artifacts"][0]["pin_status"] = "PLACEHOLDER_UNRESOLVED"
        self.reject(source, "ACTIVATION_STATUS_MISMATCH")

    def test_pending_source_has_no_authority(self) -> None:
        source = copy.deepcopy(self.source)
        source["activation_status"] = REGISTRY.PENDING
        source["artifacts"][0]["pin_status"] = "PLACEHOLDER_UNRESOLVED"
        self.reject(source, "REGISTRY_NOT_ACTIVE")

    def test_policy_and_authority_flip_reject_before_grant_resolution(self) -> None:
        source = copy.deepcopy(self.source)
        source["authority_denials"]["queue_authority"] = True
        self.reject(source, "FIXED_POLICY_MISMATCH")

    def test_grant_and_artifact_pin_mutations_reject(self) -> None:
        source = copy.deepcopy(self.source)
        source["role_grants"][0]["capabilities"] = ["UNRELATED_CAPABILITY"]
        self.reject(source, "GRANT_PIN_MISMATCH")
        source = copy.deepcopy(self.source)
        source["artifacts"][0]["expected_blob_sha256"] = "0" * 64
        self.reject(source, "ZERO_AUTHORITY_PIN")
        source = copy.deepcopy(self.source)
        source["artifacts"][0]["expected_blob_sha256"] = "f" * 64
        self.reject(source, "ARTIFACT_PIN_MISMATCH")

    def test_v4_semantic_cross_pin_mutation_rejects(self) -> None:
        source = copy.deepcopy(self.source)
        source["v4_cross_registry_binding"]["expected_v4_artifact_semantic_sha256"][
            "q1_root_owner_classifier_v2"
        ] = "f" * 64
        self.reject(source, "V4_CROSS_SEMANTIC_PIN_MISMATCH")

    def test_cross_registry_policy_binding_cannot_be_relaxed(self) -> None:
        source = copy.deepcopy(self.source)
        source["v3_cross_registry_binding"]["same_head_required"] = False
        self.reject(source, "FIXED_POLICY_MISMATCH")

    def test_v4_and_v2_are_pinned_before_any_fresh_execution(self) -> None:
        for path in (REGISTRY.V4_RESOLVER_PATH, REGISTRY.V2_RESOLVER_PATH):
            with self.subTest(path=path):
                marker_name = "v5-preexec-marker"
                payload = (
                    (ROOT / path).read_bytes()
                    + b"\nfrom pathlib import Path as _V5Marker\n"
                    + f"_V5Marker(__file__).with_name({marker_name!r}).write_text('executed')\n".encode(
                        "ascii"
                    )
                )
                root, head = self.fixture.commit(overrides={path: payload})
                marker = root / "scripts" / marker_name
                with self.assertRaises(REGISTRY.RegistryV5Error) as raised:
                    REGISTRY.resolve_registry_v5(root=root, requested_head=head)
                self.assertEqual(raised.exception.code, "ARTIFACT_PIN_MISMATCH")
                self.assertFalse(marker.exists(), path)

    def test_claim_keeps_gates_open(self) -> None:
        claim = CLAIM_PATH.read_text(encoding="utf-8")
        self.assertIn("claim_status: conditional", claim)
        self.assertIn("does not close Gate 2 or Gate 4", claim)
        self.assertIn("V4 consumer/E1 receipt", claim)

    def test_exact_canonical_types_reject_subclasses(self) -> None:
        class StringSubclass(str):
            pass

        with self.assertRaises(REGISTRY.RegistryV5Error):
            REGISTRY.digest({"a": StringSubclass("b")})


if __name__ == "__main__":
    unittest.main()
