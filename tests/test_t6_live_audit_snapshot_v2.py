from __future__ import annotations

import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_live_audit_snapshot_v2.py"
SPEC = importlib.util.spec_from_file_location("t6_live_audit_snapshot_v2", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot load audit module from {MODULE_PATH}")
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)

INTEGRATION_AUDITED = "9215f8c92c53c0eb1081849b0a03e5cb922facad"
WORKPACK_ORIGIN = "c851bd213936b3bc8b3103b469292c139d229e97"
OBSERVED_AT = "2026-08-26T00:00:00Z"
PROVENANCE_NOW = datetime(2026, 8, 26, tzinfo=timezone.utc)
MANIFEST_BYTES = b'{"fixture":"content-replay-owned-elsewhere"}\n'

PHASE1_TRACKED_PATHS = (
    "scripts/t6_live_audit_snapshot_v2.py",
    "schemas/t6-live-audit-snapshot-v2.schema.json",
    "schemas/t6-gate0-run-provenance-v1.schema.json",
    ".github/workflows/research-kb-ci.yml",
    "requirements-ci.txt",
    "README.md",
    "data/t6-selector-obligation-ledger-v1.json",
    "data/t6-proof-frontier-v2.json",
    "data/t6-wave1/t6-f2-f3-residual-frontier-v1.json",
)


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def clone_with_committed_r2(destination: Path) -> Path:
    repository = destination / "repository"
    subprocess.run(
        ["git", "clone", "--quiet", "--shared", str(ROOT), str(repository)],
        check=True,
    )
    run_git(repository, "config", "user.name", "R2 Snapshot Tests")
    run_git(repository, "config", "user.email", "r2@example.invalid")
    for relative in PHASE1_TRACKED_PATHS:
        target = repository / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    run_git(repository, "add", *PHASE1_TRACKED_PATHS)
    if run_git(repository, "status", "--porcelain"):
        run_git(repository, "commit", "-qm", "track Phase 1 test fixture")
    return repository


def clone_repository(source: Path, destination: Path) -> Path:
    repository = destination / "repository"
    subprocess.run(
        ["git", "clone", "--quiet", "--shared", str(source), str(repository)],
        check=True,
    )
    run_git(repository, "config", "user.name", "R2 Snapshot Tests")
    run_git(repository, "config", "user.email", "r2@example.invalid")
    return repository


def locator() -> AUDIT.Gate0RunLocatorV1:
    return AUDIT.Gate0RunLocatorV1(
        repository=AUDIT.TRUSTED_REPOSITORY,
        workflow_id=AUDIT.TRUSTED_WORKFLOW_ID,
        workflow_path=AUDIT.TRUSTED_WORKFLOW_PATH,
        run_id=32_900_000_001,
        run_attempt=1,
        job_id=97_900_000_001,
        artifact_id=5_000_000_001,
        artifact_name=AUDIT.TRUSTED_ARTIFACT_NAME,
    )


def content_replay_fixture(
    root: Path, head_sha: str, evidence_locator: AUDIT.Gate0RunLocatorV1
) -> tuple[dict[str, object], bytes, dict[str, object]]:
    tree = run_git(root, "rev-parse", f"{head_sha}^{{tree}}")
    digests = {
        "kb_claim_set_digest": "1" * 64,
        "runtime_source_digest": "2" * 64,
        "producer_registry_digest": "3" * 64,
        "grammar_hash": "4" * 64,
        "test_manifest_digest": "5" * 64,
    }
    manifest = {
        "head_sha": head_sha,
        "workflow_repository": evidence_locator.repository,
        "workflow_run_id": str(evidence_locator.run_id),
        "workflow_run_attempt": str(evidence_locator.run_attempt),
        "workflow_sha": head_sha,
        "workflow_event": "push",
        "workflow_ref": "refs/heads/main",
        "workflow_job": AUDIT.TRUSTED_GATE0_JOB_NAME,
    }
    basis = {
        "schema_id": "t6_gate0_manifest_content_replay_v1",
        "run_manifest_schema_id": "t6_ci_run_manifest_v1",
        "manifest_payload_sha256": "6" * 64,
        "manifest_bytes_sha256": hashlib.sha256(MANIFEST_BYTES).hexdigest(),
        "head_sha": head_sha,
        "head_tree_sha": tree,
        "status": "PASS",
        "content_replay": "PASS_EXACT_HEAD_COMMANDS_AND_DIGESTS",
        "producer_registry_status": (
            "LOCAL_RUNTIME_ONLY_NO_SHARED_ALL_PRODUCER_REGISTRY"
        ),
        "digest_domain": "fixture domains remain separate",
        "digests": digests,
    }
    return manifest, MANIFEST_BYTES, basis


class MockGitHubApi:
    def __init__(
        self,
        *,
        head_sha: str,
        manifest_bytes: bytes = MANIFEST_BYTES,
        run_status: str = "completed",
        run_conclusion: str | None = "success",
    ) -> None:
        evidence_locator = locator()
        self.workflow = {
            "id": AUDIT.TRUSTED_WORKFLOW_ID,
            "name": AUDIT.TRUSTED_WORKFLOW_NAME,
            "path": AUDIT.TRUSTED_WORKFLOW_PATH,
            "state": "active",
        }
        self.run = {
            "id": evidence_locator.run_id,
            "run_attempt": evidence_locator.run_attempt,
            "head_sha": head_sha,
            "event": "push",
            "head_branch": "main",
            "workflow_id": AUDIT.TRUSTED_WORKFLOW_ID,
            "path": AUDIT.TRUSTED_WORKFLOW_PATH + "@refs/heads/main",
            "status": run_status,
            "conclusion": run_conclusion,
            "repository": {
                "id": AUDIT.TRUSTED_REPOSITORY_ID,
                "full_name": AUDIT.TRUSTED_REPOSITORY,
            },
            "head_repository": {
                "id": AUDIT.TRUSTED_REPOSITORY_ID,
                "full_name": AUDIT.TRUSTED_REPOSITORY,
            },
        }
        self.jobs = [
            {
                "id": evidence_locator.job_id,
                "name": AUDIT.TRUSTED_GATE0_JOB_NAME,
                "run_id": evidence_locator.run_id,
                "run_attempt": evidence_locator.run_attempt,
                "head_sha": head_sha,
                "status": "completed",
                "conclusion": "success",
            }
        ]
        digest = hashlib.sha256(manifest_bytes).hexdigest()
        self.artifact = {
            "id": evidence_locator.artifact_id,
            "name": AUDIT.TRUSTED_ARTIFACT_NAME,
            "expired": False,
            "expires_at": "2026-09-25T00:00:00Z",
            "size_in_bytes": len(manifest_bytes),
            "digest": "sha256:" + digest,
            "workflow_run": {
                "id": evidence_locator.run_id,
                "repository_id": AUDIT.TRUSTED_REPOSITORY_ID,
                "head_repository_id": AUDIT.TRUSTED_REPOSITORY_ID,
                "head_sha": head_sha,
            },
        }

    def get_workflow(self, repository: str, workflow_id: int):
        return copy.deepcopy(self.workflow)

    def get_run_attempt(self, repository: str, run_id: int, run_attempt: int):
        return copy.deepcopy(self.run)

    def list_run_attempt_jobs(
        self, repository: str, run_id: int, run_attempt: int
    ):
        return copy.deepcopy(self.jobs)

    def get_artifact(self, repository: str, artifact_id: int):
        return copy.deepcopy(self.artifact)


class PassingDigestAuditClient:
    def verify_current_digest_vector(
        self, *, repository: str, head_sha: str, digest_vector
    ):
        vector = dict(sorted(digest_vector.items()))
        return {
            "schema_id": "t6_current_digest_audit_basis_v1",
            "schema_version": 1,
            "decision": "PASS",
            "audited_head_sha": head_sha,
            "digest_vector": vector,
            "digest_vector_sha256": hashlib.sha256(
                AUDIT.canonical_json_bytes(vector)
            ).hexdigest(),
            "independent_reviewer_id": "mock-independent-reviewer",
            "evidence_locator": "mock://current-digest-audit/pass",
            "review_method": "independent-current-head-replay",
        }


def schema_validator(repository: Path) -> Draft202012Validator:
    live = json.loads(
        (repository / AUDIT.LIVE_SNAPSHOT_SCHEMA_PATH).read_text(encoding="utf-8")
    )
    provenance = json.loads(
        (repository / AUDIT.GATE0_PROVENANCE_SCHEMA_PATH).read_text(encoding="utf-8")
    )
    registry = Registry().with_resource(
        provenance["$id"], Resource.from_contents(provenance)
    )
    return Draft202012Validator(
        live,
        registry=registry,
        format_checker=FormatChecker(),
    )


class T6LiveAuditSnapshotV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary = tempfile.TemporaryDirectory()
        cls.repository = clone_with_committed_r2(Path(cls._temporary.name))
        cls.snapshot = AUDIT.build_snapshot(
            cls.repository,
            observed_at=OBSERVED_AT,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def setUp(self) -> None:
        clean_environment = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith("GITHUB_")
        }
        environment_patch = mock.patch.dict(
            os.environ, clean_environment, clear=True
        )
        environment_patch.start()
        self.addCleanup(environment_patch.stop)

    def test_default_snapshot_is_honest_and_all_upgrade_gates_are_closed(self) -> None:
        result = AUDIT.audit_snapshot(
            self.repository,
            self.snapshot,
            require_verified_head=False,
        )
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(self.snapshot["workpack_origin_sha"], WORKPACK_ORIGIN)
        self.assertEqual(
            self.snapshot["integration_audited_sha"], INTEGRATION_AUDITED
        )
        self.assertEqual(self.snapshot["head_relation"], "NO_VERIFIED_HEAD")
        self.assertEqual(self.snapshot["current_digest_audit"]["status"], "MISSING")
        self.assertEqual(self.snapshot["consumer_policy"]["status"], "PASS")
        self.assertFalse(self.snapshot["status_upgrade_allowed"])

    def test_ci_workflow_uses_direct_artifacts_and_a_dependent_snapshot_job(self) -> None:
        workflow = yaml.safe_load(
            (self.repository / AUDIT.TRUSTED_WORKFLOW_PATH).read_text(encoding="utf-8")
        )
        self.assertEqual(workflow["permissions"]["actions"], "read")
        gate = workflow["jobs"]["gate-zero"]
        gate_steps = {step.get("id") or step["name"]: step for step in gate["steps"]}
        upload = gate_steps["upload_gate0_manifest"]
        self.assertEqual(
            upload["with"]["path"], "data/t6-wave1/ci-run-manifest-v1.json"
        )
        self.assertIs(upload["with"]["archive"], False)
        self.assertEqual(upload["with"]["retention-days"], 90)
        self.assertEqual(
            gate["outputs"]["manifest_artifact_id"],
            "${{ steps.upload_gate0_manifest.outputs.artifact-id }}",
        )
        self.assertEqual(
            gate_steps["Set up Python"]["with"]["python-version"], "3.12.14"
        )

        live = workflow["jobs"]["live-audit-snapshot"]
        self.assertEqual(live["needs"], "gate-zero")
        self.assertEqual(
            live["if"], "github.event_name == 'push' && github.ref == 'refs/heads/main'"
        )
        live_steps = {step["name"]: step for step in live["steps"]}
        download = live_steps["Download the immutable Gate 0 manifest"]
        self.assertEqual(
            download["uses"],
            "actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c",
        )
        self.assertEqual(
            download["with"]["artifact-ids"],
            "${{ needs.gate-zero.outputs.manifest_artifact_id }}",
        )
        generate = live_steps["Generate the live audit snapshot"]["run"]
        verify = live_steps["Verify the live audit snapshot"]["run"]
        self.assertIn("--provenance-locator", generate)
        self.assertIn("--provenance-locator", verify)
        for name in ("Upload the live audit snapshot", "Upload the provenance locator"):
            self.assertIs(live_steps[name]["with"]["archive"], False)

    def test_exact_gate0_can_verify_while_theorem_upgrade_remains_blocked(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        api = MockGitHubApi(head_sha=head)
        replay = content_replay_fixture(self.repository, head, locator())
        with mock.patch.object(
            AUDIT, "_replay_gate0_manifest_content", return_value=replay
        ):
            snapshot = AUDIT.build_snapshot(
                self.repository,
                run_manifest_path=Path("unused-by-stub.json"),
                provenance_locator=locator(),
                github_api_client=api,
                provenance_now=PROVENANCE_NOW,
                observed_at=OBSERVED_AT,
            )
            result = AUDIT.audit_snapshot(
                self.repository,
                snapshot,
                run_manifest_path=Path("unused-by-stub.json"),
                provenance_locator=locator(),
                github_api_client=api,
                provenance_now=PROVENANCE_NOW,
            )
            promotion = AUDIT.audit_snapshot(
                self.repository,
                snapshot,
                run_manifest_path=Path("unused-by-stub.json"),
                provenance_locator=locator(),
                github_api_client=api,
                provenance_now=PROVENANCE_NOW,
                require_status_upgrade_authorized=True,
            )
        self.assertEqual(snapshot["head_relation"], "EQUAL")
        self.assertFalse(snapshot["status_upgrade_allowed"])
        self.assertTrue(result.ok, result.errors)
        self.assertFalse(promotion.ok)
        self.assertTrue(any("STATUS_UPGRADE_BLOCKED" in item for item in promotion.errors))

    def test_historical_api_attested_head_is_advanced_unverified(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = clone_repository(self.repository, Path(directory))
            verified_head = AUDIT.resolve_head(repository)
            run_git(repository, "commit", "--allow-empty", "-qm", "advance current head")
            current_head = AUDIT.resolve_head(repository)
            api = MockGitHubApi(head_sha=verified_head)
            replay = content_replay_fixture(repository, verified_head, locator())
            with mock.patch.object(
                AUDIT, "_replay_gate0_manifest_content", return_value=replay
            ):
                snapshot = AUDIT.build_snapshot(
                    repository,
                    run_manifest_path=Path("historical.json"),
                    provenance_locator=locator(),
                    github_api_client=api,
                    provenance_now=PROVENANCE_NOW,
                    observed_at=OBSERVED_AT,
                )
                result = AUDIT.audit_snapshot(
                    repository,
                    snapshot,
                    run_manifest_path=Path("historical.json"),
                    provenance_locator=locator(),
                    github_api_client=api,
                    provenance_now=PROVENANCE_NOW,
                    require_verified_head=False,
                )
        self.assertEqual(snapshot["last_verified_head_sha"], verified_head)
        self.assertEqual(snapshot["current_observed_head_sha"], current_head)
        self.assertEqual(snapshot["head_relation"], "ADVANCED_UNVERIFIED")
        self.assertFalse(snapshot["status_upgrade_allowed"])
        self.assertTrue(result.ok, result.errors)

    def test_all_gates_can_authorize_only_after_consumers_and_digest_audit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = clone_repository(self.repository, Path(directory))
            head = AUDIT.resolve_head(repository)
            api = MockGitHubApi(head_sha=head)
            replay = content_replay_fixture(repository, head, locator())
            digest_client = PassingDigestAuditClient()
            with mock.patch.object(
                AUDIT, "_replay_gate0_manifest_content", return_value=replay
            ):
                snapshot = AUDIT.build_snapshot(
                    repository,
                    run_manifest_path=Path("current.json"),
                    provenance_locator=locator(),
                    github_api_client=api,
                    digest_audit_client=digest_client,
                    provenance_now=PROVENANCE_NOW,
                    observed_at=OBSERVED_AT,
                )
                result = AUDIT.audit_snapshot(
                    repository,
                    snapshot,
                    run_manifest_path=Path("current.json"),
                    provenance_locator=locator(),
                    github_api_client=api,
                    digest_audit_client=digest_client,
                    provenance_now=PROVENANCE_NOW,
                    require_status_upgrade_authorized=True,
                )
        self.assertEqual(snapshot["head_relation"], "EQUAL")
        self.assertEqual(snapshot["current_digest_audit"]["status"], "PASS")
        self.assertEqual(snapshot["consumer_policy"]["status"], "PASS")
        self.assertTrue(snapshot["status_upgrade_allowed"])
        self.assertTrue(result.ok, result.errors)
        schema_validator(self.repository).validate(snapshot)

    def test_missing_consumer_locator_keeps_upgrade_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = clone_repository(self.repository, Path(directory))
            path = repository / AUDIT.PROOF_FRONTIER_PATH
            document = json.loads(path.read_text(encoding="utf-8"))
            document.pop("live_audit_snapshot_locator")
            path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
            run_git(repository, "add", AUDIT.PROOF_FRONTIER_PATH)
            run_git(repository, "commit", "-qm", "remove one consumer binding")
            snapshot = AUDIT.build_snapshot(repository, observed_at=OBSERVED_AT)
        self.assertEqual(snapshot["consumer_policy"]["status"], "MISSING_OR_STALE")
        self.assertFalse(snapshot["status_upgrade_allowed"])

    def test_api_provenance_uses_official_metadata_not_environment(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        manifest = {"head_sha": head}
        api = MockGitHubApi(head_sha=head)
        with mock.patch.dict(os.environ, {}, clear=True):
            local_provenance = AUDIT._verify_github_run_provenance(
                locator=locator(),
                manifest=manifest,
                manifest_bytes=MANIFEST_BYTES,
                api_client=api,
                now=PROVENANCE_NOW,
            )
        same_run_environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_REPOSITORY": locator().repository,
            "GITHUB_RUN_ID": str(locator().run_id),
            "GITHUB_RUN_ATTEMPT": str(locator().run_attempt),
            "GITHUB_SHA": head,
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_REF": "refs/heads/main",
        }
        with mock.patch.dict(os.environ, same_run_environment, clear=True):
            same_run_provenance = AUDIT._verify_github_run_provenance(
                locator=locator(),
                manifest=manifest,
                manifest_bytes=MANIFEST_BYTES,
                api_client=api,
                now=PROVENANCE_NOW,
            )
        historical_environment = dict(same_run_environment)
        historical_environment["GITHUB_RUN_ID"] = "32999999999"
        historical_environment["GITHUB_SHA"] = "f" * 40
        with mock.patch.dict(os.environ, historical_environment, clear=True):
            historical_provenance = AUDIT._verify_github_run_provenance(
                locator=locator(),
                manifest=manifest,
                manifest_bytes=MANIFEST_BYTES,
                api_client=api,
                now=PROVENANCE_NOW,
            )
        self.assertEqual(local_provenance, same_run_provenance)
        self.assertEqual(local_provenance, historical_provenance)
        self.assertEqual(
            local_provenance["gate_zero_success_basis"],
            "GATE_ZERO_JOB_COMPLETED_SUCCESS",
        )
        self.assertEqual(
            local_provenance["artifact_digest"],
            "sha256:" + hashlib.sha256(MANIFEST_BYTES).hexdigest(),
        )
        Draft202012Validator(
            json.loads(
                (self.repository / AUDIT.GATE0_PROVENANCE_SCHEMA_PATH).read_text(
                    encoding="utf-8"
                )
            ),
            format_checker=FormatChecker(),
        ).validate(local_provenance)

    def test_api_provenance_mutation_matrix_fails_closed(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        mutations = {
            "workflow path": lambda api: api.workflow.__setitem__("path", "wrong.yml"),
            "workflow name": lambda api: api.workflow.__setitem__("name", "wrong"),
            "run attempt": lambda api: api.run.__setitem__("run_attempt", 2),
            "boolean run attempt": lambda api: api.run.__setitem__(
                "run_attempt", True
            ),
            "run head": lambda api: api.run.__setitem__("head_sha", "0" * 40),
            "pull request": lambda api: api.run.__setitem__("event", "pull_request"),
            "non-main": lambda api: api.run.__setitem__("head_branch", "feature"),
            "fork": lambda api: api.run["head_repository"].__setitem__("id", 1),
            "skipped job": lambda api: api.jobs[0].__setitem__("conclusion", "skipped"),
            "duplicate job": lambda api: api.jobs.append(copy.deepcopy(api.jobs[0])),
            "boolean job attempt": lambda api: api.jobs[0].__setitem__(
                "run_attempt", True
            ),
            "failed run": lambda api: api.run.__setitem__("conclusion", "failure"),
            "expired": lambda api: api.artifact.__setitem__("expired", True),
            "expiry time": lambda api: api.artifact.__setitem__(
                "expires_at", "2026-08-25T00:00:00Z"
            ),
            "artifact size": lambda api: api.artifact.__setitem__("size_in_bytes", 1),
            "server digest": lambda api: api.artifact.__setitem__(
                "digest", "sha256:" + "0" * 64
            ),
            "workflow run": lambda api: api.artifact["workflow_run"].__setitem__(
                "id", 1
            ),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                api = MockGitHubApi(head_sha=head)
                mutate(api)
                with self.assertRaises(AUDIT.SnapshotError):
                    AUDIT._verify_github_run_provenance(
                        locator=locator(),
                        manifest={"head_sha": head},
                        manifest_bytes=MANIFEST_BYTES,
                        api_client=api,
                        now=PROVENANCE_NOW,
                    )

    def test_in_progress_run_requires_successful_gate_zero_job(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        api = MockGitHubApi(
            head_sha=head, run_status="in_progress", run_conclusion=None
        )
        in_progress_provenance = AUDIT._verify_github_run_provenance(
            locator=locator(),
            manifest={"head_sha": head},
            manifest_bytes=MANIFEST_BYTES,
            api_client=api,
            now=PROVENANCE_NOW,
        )
        completed_provenance = AUDIT._verify_github_run_provenance(
            locator=locator(),
            manifest={"head_sha": head},
            manifest_bytes=MANIFEST_BYTES,
            api_client=MockGitHubApi(head_sha=head),
            now=PROVENANCE_NOW,
        )
        self.assertEqual(in_progress_provenance, completed_provenance)
        self.assertEqual(
            in_progress_provenance["gate_zero_success_basis"],
            "GATE_ZERO_JOB_COMPLETED_SUCCESS",
        )
        api.jobs[0]["conclusion"] = "skipped"
        with self.assertRaisesRegex(AUDIT.SnapshotError, "Gate-0 job"):
            AUDIT._verify_github_run_provenance(
                locator=locator(),
                manifest={"head_sha": head},
                manifest_bytes=MANIFEST_BYTES,
                api_client=api,
                now=PROVENANCE_NOW,
            )

    def test_environment_is_only_a_cross_check(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        api = MockGitHubApi(head_sha=head)
        environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_REPOSITORY": locator().repository,
            "GITHUB_RUN_ID": str(locator().run_id),
            "GITHUB_RUN_ATTEMPT": str(locator().run_attempt),
            "GITHUB_SHA": "0" * 40,
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_REF": "refs/heads/main",
        }
        with mock.patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(AUDIT.SnapshotError, "cross-check"):
                AUDIT._verify_github_run_provenance(
                    locator=locator(),
                    manifest={"head_sha": head},
                    manifest_bytes=MANIFEST_BYTES,
                    api_client=api,
                    now=PROVENANCE_NOW,
                )

    def test_dirty_or_untracked_live_toolchain_fails_before_execution(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        for relative in AUDIT.TOOLCHAIN_PATHS:
            with self.subTest(path=relative):
                path = self.repository / relative
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                try:
                    with self.assertRaisesRegex(AUDIT.SnapshotError, "DIRTY"):
                        AUDIT._capture_execution_binding(self.repository, head)
                finally:
                    path.write_bytes(original)
        run_git(self.repository, "rm", "--cached", "-q", AUDIT.LIVE_SNAPSHOT_SCRIPT_PATH)
        try:
            with self.assertRaisesRegex(AUDIT.SnapshotError, "DIRTY|UNTRACKED"):
                AUDIT._capture_execution_binding(self.repository, head)
        finally:
            run_git(self.repository, "add", AUDIT.LIVE_SNAPSHOT_SCRIPT_PATH)
        self.assertEqual(run_git(self.repository, "status", "--porcelain"), "")

    def test_toolchain_change_between_start_and_end_is_rejected(self) -> None:
        head = AUDIT.resolve_head(self.repository)
        binding = AUDIT._capture_execution_binding(self.repository, head)
        schema = self.repository / AUDIT.LIVE_SNAPSHOT_SCHEMA_PATH
        original = schema.read_bytes()
        schema.write_bytes(original + b"\n")
        try:
            with self.assertRaises(AUDIT.SnapshotError):
                AUDIT._assert_execution_binding_unchanged(
                    self.repository, head, binding
                )
        finally:
            schema.write_bytes(original)

    def test_manifest_replay_copy_is_immune_to_source_path_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "downloaded-manifest.json"
            source.write_bytes(MANIFEST_BYTES)
            captured = source.read_bytes()
            immutable = AUDIT._materialize_immutable_manifest_copy(root, captured)
            source.write_bytes(b'{"forged":true}\n')
            self.assertEqual(immutable.read_bytes(), MANIFEST_BYTES)
            self.assertEqual(
                hashlib.sha256(immutable.read_bytes()).hexdigest(),
                hashlib.sha256(captured).hexdigest(),
            )

    def test_schema_state_machine_rejects_contradictory_combinations(self) -> None:
        validator = schema_validator(self.repository)
        validator.validate(self.snapshot)
        mutations = []

        no_basis_equal = copy.deepcopy(self.snapshot)
        no_basis_equal["head_relation"] = "EQUAL"
        no_basis_equal["verification_state"] = "VERIFIED_HEAD"
        mutations.append(no_basis_equal)

        advance_verified = copy.deepcopy(self.snapshot)
        advance_verified["head_relation"] = "ADVANCED_UNVERIFIED"
        advance_verified["verification_state"] = "VERIFIED_HEAD"
        mutations.append(advance_verified)

        forged_upgrade = copy.deepcopy(self.snapshot)
        forged_upgrade["status_upgrade_allowed"] = True
        mutations.append(forged_upgrade)

        audit_basis_while_missing = copy.deepcopy(self.snapshot)
        audit_basis_while_missing["current_digest_audit"]["basis"] = {}
        mutations.append(audit_basis_while_missing)

        integration_diverged = copy.deepcopy(self.snapshot)
        integration_diverged["integration_head_relation"] = "DIVERGED"
        integration_diverged["status_upgrade_allowed"] = True
        mutations.append(integration_diverged)

        nonnull_with_no_verified_relation = copy.deepcopy(self.snapshot)
        nonnull_with_no_verified_relation["last_verified_head_sha"] = "0" * 40
        nonnull_with_no_verified_relation["last_verified_basis"] = {}
        mutations.append(nonnull_with_no_verified_relation)

        forged_consumer_pass = copy.deepcopy(self.snapshot)
        policy = forged_consumer_pass["consumer_policy"]
        policy["status"] = "PASS"
        policy["all_consumers_bound"] = True
        for consumer_id, record in policy["consumers"].items():
            record["status"] = "BOUND"
            record["observed"] = (
                1 if consumer_id == "readme" else AUDIT.LIVE_SNAPSHOT_LOCATOR
            )
        policy["consumers"]["proof_frontier"]["status"] = "MISSING_OR_STALE"
        mutations.append(forged_consumer_pass)

        for index, mutation in enumerate(mutations):
            with self.subTest(index=index):
                self.assertTrue(list(validator.iter_errors(mutation)))

    def test_tampering_and_unknown_authority_fields_fail_closed(self) -> None:
        changed = copy.deepcopy(self.snapshot)
        changed["runtime_source_digest"] = "0" * 64
        result = AUDIT.audit_snapshot(
            self.repository, changed, require_verified_head=False
        )
        self.assertFalse(result.ok)
        self.assertIn(
            "snapshot field is stale or forged: runtime_source_digest", result.errors
        )

        unknown = copy.deepcopy(self.snapshot)
        unknown["status_override"] = {"T6": "CLOSED"}
        result = AUDIT.audit_snapshot(
            self.repository, unknown, require_verified_head=False
        )
        self.assertFalse(result.ok)
        self.assertTrue(any("top-level keys differ" in item for item in result.errors))

    def test_duplicate_keys_nonfinite_json_and_locator_policy_are_rejected(self) -> None:
        for payload, marker in (
            (b'{"schema_id":"first","schema_id":"second"}', "duplicate"),
            (b'{"value":NaN}', "non-finite"),
        ):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "value.json"
                path.write_bytes(payload)
                with self.assertRaisesRegex(AUDIT.SnapshotError, marker):
                    AUDIT.load_snapshot(path)

        payload = locator().payload()
        payload["workflow_id"] = 1
        with self.assertRaisesRegex(AUDIT.SnapshotError, "trusted"):
            AUDIT.Gate0RunLocatorV1.from_mapping(payload)

        bool_version = locator().payload()
        bool_version["schema_version"] = True
        with self.assertRaisesRegex(AUDIT.SnapshotError, "schema_version"):
            AUDIT.Gate0RunLocatorV1.from_mapping(bool_version)

        class BoolVersionDigestClient(PassingDigestAuditClient):
            def verify_current_digest_vector(self, **kwargs):
                basis = super().verify_current_digest_vector(**kwargs)
                basis["schema_version"] = True
                return basis

        with self.assertRaisesRegex(AUDIT.SnapshotError, "did not record PASS"):
            AUDIT._evaluate_current_digest_audit(
                repository=AUDIT.TRUSTED_REPOSITORY,
                head_sha="0" * 40,
                digest_vector={"one": "1" * 64},
                audit_client=BoolVersionDigestClient(),
            )


if __name__ == "__main__":
    unittest.main()
