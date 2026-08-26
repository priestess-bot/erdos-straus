from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_ci_run_manifest_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "t6_ci_run_manifest_v1_under_test", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MANIFEST = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MANIFEST
SPEC.loader.exec_module(MANIFEST)


class CIRunManifestTests(unittest.TestCase):
    @staticmethod
    def git(root: Path, *args: str) -> str:
        completed = subprocess.run(
            ("git", *args),
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    @staticmethod
    def write(root: Path, relative: str, value: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def initialize_repository(self, root: Path) -> None:
        self.git(root, "init", "--quiet")
        self.git(root, "config", "user.email", "manifest-tests@example.invalid")
        self.git(root, "config", "user.name", "Manifest Tests")

    def commit_all(self, root: Path, message: str) -> None:
        self.git(root, "add", "--all")
        self.git(root, "commit", "--quiet", "-m", message)

    @staticmethod
    def pass_results() -> list[dict[str, object]]:
        return [
            {
                "id": spec.command_id,
                "status": "PASS",
                "exit_code": 0,
                "duration_ms": index,
                "detail": None,
            }
            for index, spec in enumerate(MANIFEST.gate0_command_specs())
        ]

    def write_valid_grammar(self, root: Path) -> None:
        grammar = {"owners": ["owner.test"], "schema_version": 1}
        jq_output = (
            json.dumps(
                grammar, ensure_ascii=True, separators=(",", ":"), sort_keys=True
            )
            + "\n"
        ).encode("ascii")
        document = {
            "schema_id": "test_grammar",
            "grammar": grammar,
            "grammar_hash": MANIFEST.sha256_bytes(jq_output),
        }
        self.write(
            root,
            MANIFEST.GRAMMAR_PATH,
            json.dumps(document, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )

    @staticmethod
    def coordinator_registry_fixture(root: Path) -> dict[str, object]:
        head = MANIFEST.current_revision(root)["head_sha"]
        role_subdigests = {
            key: MANIFEST.sha256_bytes(f"role:{key}".encode())
            for key in sorted(MANIFEST.ROLE_SUBDIGEST_KEYS)
        }
        return {
            "schema_id": "t6_gate0_coordinator_evidence_registry_diagnostic_v1",
            "head_sha": head,
            "registry_path": MANIFEST.COORDINATOR_ROLE_REGISTRY_PATH,
            "status": MANIFEST.EVIDENCE_REGISTRY_STATUS,
            "role_authority": False,
            "registry_digest": "a" * 64,
            "evidence_inventory_digest": "b" * 64,
            "role_subdigests": role_subdigests,
            "role_grant_counts": {key: 0 for key in sorted(role_subdigests)},
            "active_role_grant_count": 0,
            "active_producer_count": 0,
            "complete_terminal_schedule_count": 0,
        }

    @staticmethod
    def terminal_registry_fixture(root: Path) -> dict[str, object]:
        return {
            "schema_id": "t6_gate0_complete_terminal_registry_diagnostic_v1",
            "head_sha": MANIFEST.current_revision(root)["head_sha"],
            "registry_path": MANIFEST.COMPLETE_TERMINAL_REGISTRY_PATH,
            "status": MANIFEST.COMPLETE_TERMINAL_REGISTRY_STATUS,
            "registry_digest": "c" * 64,
            "registry_source_sha256": "d" * 64,
            "local_schedule_count": 6,
            "complete_schedule_count": 0,
            "complete_miss_issuance_enabled": False,
            "local_miss_implies_complete_miss": False,
            "terminal_receipt_grants_queue_authority": False,
        }

    @staticmethod
    def discovery_output(
        skips: list[dict[str, str]] | None = None,
        *,
        tests_run: int = 100,
        outcome: str = "OK",
    ) -> bytes:
        observed = (
            MANIFEST.expected_unittest_skips_payload() if skips is None else skips
        )
        lines = [
            f"{item['test_id'].rsplit('.', 1)[-1]} ({item['test_id']}) "
            f"... skipped {item['reason']!r}"
            for item in observed
        ]
        lines.extend(
            [
                "----------------------------------------------------------------------",
                f"Ran {tests_run} tests in 1.000s",
                "",
                outcome + (f" (skipped={len(observed)})" if observed else ""),
            ]
        )
        return ("\n".join(lines) + "\n").encode("utf-8")

    def initialize_manifest_repository(self, root: Path) -> None:
        self.initialize_repository(root)
        self.write(root, "claims/example.md", "# Claim\n")
        self.write(root, "scripts/t6_runtime.py", "VALUE = 1\n")
        self.write(root, "tests/test_example.py", "VALUE = 1\n")
        self.write_valid_grammar(root)
        self.commit_all(root, "initial manifest fixture")

    def build_valid_manifest(
        self, root: Path, registry: dict[str, object]
    ) -> dict[str, object]:
        revision = MANIFEST.current_revision(root)
        results = self.pass_results()
        full_result = next(
            result for result in results if result["id"] == "full_unittest_discovery"
        )
        unittest_discovery = MANIFEST.build_unittest_discovery_receipt(
            self.discovery_output(), full_result
        )
        self.assertEqual(unittest_discovery["status"], "PASS")
        with (
            mock.patch.object(
                MANIFEST, "producer_registry_payload", return_value=registry
            ),
            mock.patch.object(
                MANIFEST,
                "coordinator_evidence_registry_diagnostic",
                return_value=self.coordinator_registry_fixture(root),
            ),
            mock.patch.object(
                MANIFEST,
                "complete_terminal_registry_diagnostic",
                return_value=self.terminal_registry_fixture(root),
            ),
            mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}, clear=True),
        ):
            return MANIFEST.build_manifest(
                root,
                revision=revision,
                head_sha_after=revision["head_sha"],
                dirty_before=(),
                dirty_after=(),
                allow_dirty=False,
                require_github=False,
                results=results,
                unittest_discovery=unittest_discovery,
                infrastructure_errors=(),
            )

    def verify_with_registry(
        self,
        root: Path,
        payload: dict[str, object],
        registry: dict[str, object],
        *,
        require_pass: bool = False,
    ) -> tuple[str, ...]:
        with (
            mock.patch.object(
                MANIFEST, "producer_registry_payload", return_value=registry
            ),
            mock.patch.object(
                MANIFEST,
                "coordinator_evidence_registry_diagnostic",
                return_value=self.coordinator_registry_fixture(root),
            ),
            mock.patch.object(
                MANIFEST,
                "complete_terminal_registry_diagnostic",
                return_value=self.terminal_registry_fixture(root),
            ),
            mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}, clear=True),
        ):
            return MANIFEST.verify_manifest(
                root,
                payload,
                require_pass=require_pass,
            )

    def test_gate0_command_matrix_is_exact_and_ordered(self) -> None:
        expected = [
            ("kb_validate", ("python", "scripts/kb.py", "validate"), 1_800),
            ("kb_build", ("python", "scripts/kb.py", "build"), 1_800),
            (
                "generated_indexes_clean",
                ("git", "diff", "--exit-code", "--", "index/"),
                1_800,
            ),
            (
                "pre_t6_contract_audit",
                (
                    "python",
                    "reproductions/pre_t6_contract_kernel_audit.py",
                    "--root",
                    ".",
                    "--require-full-tree",
                ),
                1_800,
            ),
            (
                "constructor_inventory_audit",
                ("python", "scripts/audit_t6_constructor_inventory_v1.py"),
                1_800,
            ),
            (
                "ruff",
                ("ruff", "check", "scripts", "reproductions", "tests"),
                1_800,
            ),
            (
                "compileall",
                (
                    "python",
                    "-m",
                    "compileall",
                    "-q",
                    "scripts",
                    "reproductions",
                    "tests",
                ),
                1_800,
            ),
            ("git_diff_check", ("git", "diff", "--check"), 1_800),
            (
                "full_unittest_discovery",
                (
                    "python",
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "tests",
                    "-p",
                    "test_*.py",
                    "-v",
                ),
                18_000,
            ),
        ]
        observed = [
            (spec.command_id, spec.argv, spec.timeout_seconds)
            for spec in MANIFEST.gate0_command_specs()
        ]
        self.assertEqual(observed, expected)
        self.assertEqual(len(observed), 9)

    def test_duplicate_json_keys_are_rejected_at_any_depth(self) -> None:
        with self.assertRaisesRegex(MANIFEST.ManifestError, "duplicate JSON key 'x'"):
            MANIFEST.load_json_bytes_reject_duplicates(b'{"outer":{"x":1,"x":2}}')

    def test_status_is_derived_and_cannot_be_forged(self) -> None:
        passing = self.pass_results()
        self.assertEqual(
            MANIFEST.derive_status(
                checkout_state="CLEAN",
                results=passing,
                infrastructure_errors=(),
            ),
            "PASS",
        )
        self.assertEqual(
            MANIFEST.derive_status(
                checkout_state="DIRTY_ALLOWED",
                results=passing,
                infrastructure_errors=(),
            ),
            "DIAGNOSTIC_ONLY",
        )
        failed = copy.deepcopy(passing)
        failed[0]["status"] = "FAIL"
        failed[0]["exit_code"] = 1
        self.assertEqual(
            MANIFEST.derive_status(
                checkout_state="CLEAN",
                results=failed,
                infrastructure_errors=(),
            ),
            "FAIL",
        )
        self.assertEqual(
            MANIFEST.derive_status(
                checkout_state="CLEAN",
                results=passing,
                infrastructure_errors=("infrastructure failed",),
            ),
            "FAIL",
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            forged = self.build_valid_manifest(root, registry)
            forged["results"][0]["status"] = "FAIL"
            forged["results"][0]["exit_code"] = 1
            forged["status"] = "PASS"
            forged = MANIFEST.seal_manifest(forged)
            errors = self.verify_with_registry(
                root, forged, registry, require_pass=True
            )
        self.assertIn(
            "status does not follow command results and checkout state", errors
        )

    def test_file_set_digest_binds_content_paths_and_membership(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_repository(root)
            self.write(root, "claims/alpha.md", "alpha\n")
            self.commit_all(root, "add alpha")

            def receipt() -> dict[str, object]:
                revision = MANIFEST.current_revision(root)
                entries = tuple(
                    entry
                    for entry in MANIFEST.git_tree_entries(root, revision["head_sha"])
                    if entry.path.startswith("claims/")
                )
                return MANIFEST.file_set_receipt(
                    root,
                    entries,
                    scope_id="claims",
                    patterns=("claims/*.md",),
                )

            baseline = receipt()
            self.write(root, "claims/alpha.md", "changed\n")
            self.commit_all(root, "change alpha")
            content_changed = receipt()
            self.git(root, "mv", "claims/alpha.md", "claims/beta.md")
            self.commit_all(root, "rename alpha")
            path_changed = receipt()
            self.write(root, "claims/gamma.md", "gamma\n")
            self.commit_all(root, "add gamma")
            member_added = receipt()

        digests = {
            baseline["digest"],
            content_changed["digest"],
            path_changed["digest"],
            member_added["digest"],
        }
        self.assertEqual(len(digests), 4)
        self.assertEqual(member_added["file_count"], 2)
        self.assertEqual(
            [item["path"] for item in member_added["files"]],
            ["claims/beta.md", "claims/gamma.md"],
        )

    def test_runtime_source_digest_uses_transitive_local_import_closure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_repository(root)
            self.write(root, "claims/example.md", "# Claim\n")
            self.write(root, "tests/test_example.py", "VALUE = 1\n")
            self.write(root, "scripts/t6_entry.py", "import runtime_helper\n")
            self.write(
                root,
                "scripts/runtime_helper.py",
                "from projection_math import VALUE\n",
            )
            self.write(root, "reproductions/projection_math.py", "VALUE = 1\n")
            self.write(root, "reproductions/unrelated.py", "VALUE = 2\n")
            self.commit_all(root, "add transitive runtime fixture")
            revision = MANIFEST.current_revision(root)
            entries = MANIFEST.git_tree_entries(root, revision["head_sha"])

            closure = MANIFEST.local_python_import_closure(
                root,
                entries,
                root_paths=("scripts/t6_entry.py",),
            )
            runtime_entries = MANIFEST.runtime_source_entries(root, entries)
            scopes = MANIFEST.build_digest_scopes(root, entries)

        expected_paths = [
            "reproductions/projection_math.py",
            "scripts/runtime_helper.py",
            "scripts/t6_entry.py",
        ]
        self.assertEqual([entry.path for entry in closure], expected_paths)
        self.assertEqual([entry.path for entry in runtime_entries], expected_paths)
        self.assertEqual(scopes["runtime_source"]["root_file_count"], 1)
        self.assertEqual(scopes["runtime_source"]["transitive_file_count"], 2)
        self.assertNotIn(
            "reproductions/unrelated.py",
            [item["path"] for item in scopes["runtime_source"]["files"]],
        )

    def test_runtime_import_closure_rejects_ambiguous_local_modules(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_repository(root)
            self.write(root, "scripts/t6_entry.py", "import shared\n")
            self.write(root, "scripts/shared.py", "VALUE = 1\n")
            self.write(root, "reproductions/shared.py", "VALUE = 2\n")
            self.commit_all(root, "add ambiguous runtime fixture")
            revision = MANIFEST.current_revision(root)
            entries = MANIFEST.git_tree_entries(root, revision["head_sha"])

            with self.assertRaises(MANIFEST.ManifestError) as error:
                MANIFEST.local_python_import_closure(
                    root,
                    entries,
                    root_paths=("scripts/t6_entry.py",),
                )

        self.assertIn("ambiguous local module 'shared'", str(error.exception))
        self.assertIn("scripts/shared.py", str(error.exception))
        self.assertIn("reproductions/shared.py", str(error.exception))

    def test_grammar_hash_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_repository(root)
            self.write_valid_grammar(root)
            self.commit_all(root, "valid grammar")
            revision = MANIFEST.current_revision(root)
            entries = MANIFEST.git_tree_entries(root, revision["head_sha"])
            valid = MANIFEST.grammar_receipt(root, entries)
            self.assertEqual(len(valid["grammar_hash"]), 64)

            document = json.loads(
                (root / MANIFEST.GRAMMAR_PATH).read_text(encoding="utf-8")
            )
            document["grammar_hash"] = "0" * 64
            self.write(
                root,
                MANIFEST.GRAMMAR_PATH,
                json.dumps(document, indent=2, sort_keys=True) + "\n",
            )
            self.commit_all(root, "tamper grammar hash")
            revision = MANIFEST.current_revision(root)
            entries = MANIFEST.git_tree_entries(root, revision["head_sha"])
            with self.assertRaisesRegex(
                MANIFEST.ManifestError, "stored grammar hash does not replay"
            ):
                MANIFEST.grammar_receipt(root, entries)

    def test_unittest_discovery_receipt_requires_exact_skip_allowlist(self) -> None:
        result = next(
            item
            for item in self.pass_results()
            if item["id"] == "full_unittest_discovery"
        )
        expected = MANIFEST.expected_unittest_skips_payload()
        receipt = MANIFEST.build_unittest_discovery_receipt(
            self.discovery_output(expected, tests_run=1_234), result
        )
        self.assertEqual(receipt["status"], "PASS")
        self.assertEqual(receipt["tests_run"], 1_234)
        self.assertEqual(receipt["skip_count"], 13)
        self.assertEqual(receipt["summary_skip_count"], 13)
        self.assertEqual(receipt["skips"], sorted(expected, key=lambda item: item["test_id"]))

        missing = MANIFEST.build_unittest_discovery_receipt(
            self.discovery_output(expected[:-1]), result
        )
        self.assertEqual(missing["status"], "FAIL")
        self.assertTrue(
            any(
                error.startswith("missing expected unittest skips:")
                for error in missing["policy_errors"]
            )
        )

        unexpected_skips = [
            *expected,
            {
                "test_id": "test_unexpected.ExampleTests.test_unexpected_skip",
                "reason": "unexpected",
            },
        ]
        unexpected = MANIFEST.build_unittest_discovery_receipt(
            self.discovery_output(unexpected_skips), result
        )
        self.assertEqual(unexpected["status"], "FAIL")
        self.assertTrue(
            any(
                error.startswith("unexpected unittest skips:")
                for error in unexpected["policy_errors"]
            )
        )

        changed_skips = copy.deepcopy(expected)
        changed_skips[0]["reason"] = "changed reason"
        changed = MANIFEST.build_unittest_discovery_receipt(
            self.discovery_output(changed_skips), result
        )
        self.assertEqual(changed["status"], "FAIL")
        self.assertTrue(
            any(
                error.startswith("changed unittest skip reasons:")
                for error in changed["policy_errors"]
            )
        )

        bad_summary = self.discovery_output(expected).replace(
            b"OK (skipped=13)", b"OK (skipped=12)"
        )
        mismatched = MANIFEST.build_unittest_discovery_receipt(bad_summary, result)
        self.assertEqual(mismatched["status"], "FAIL")
        self.assertIn(
            "unittest summary skip count does not match parsed skip records",
            mismatched["policy_errors"],
        )

    def test_unittest_discovery_receipt_is_bound_to_the_command_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            payload = self.build_valid_manifest(root, registry)
            full_result = next(
                result
                for result in payload["results"]
                if result["id"] == "full_unittest_discovery"
            )
            full_result["duration_ms"] += 1
            payload = MANIFEST.seal_manifest(payload)
            errors = self.verify_with_registry(root, payload, registry)
        self.assertIn(
            "unittest discovery command result digest does not replay", errors
        )

    def test_unittest_discovery_policy_failure_is_not_self_repairable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            payload = self.build_valid_manifest(root, registry)
            receipt = payload["unittest_discovery"]
            receipt["skips"] = receipt["skips"][:-1]
            receipt["skip_count"] -= 1
            receipt["summary_skip_count"] -= 1
            receipt["summary_line"] = "OK (skipped=12)"
            receipt["policy_errors"] = []
            receipt["status"] = "PASS"
            payload = MANIFEST.seal_manifest(payload)
            errors = self.verify_with_registry(
                root, payload, registry, require_pass=True
            )
        self.assertIn("unittest_discovery.policy_errors do not replay", errors)
        self.assertIn("unittest_discovery.status does not replay", errors)
        self.assertIn("unittest discovery receipt policy did not pass", errors)

    def test_manifest_status_fails_when_an_expected_skip_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            revision = MANIFEST.current_revision(root)
            results = self.pass_results()
            full_result = next(
                result
                for result in results
                if result["id"] == "full_unittest_discovery"
            )
            skips = MANIFEST.expected_unittest_skips_payload()[:-1]
            receipt = MANIFEST.build_unittest_discovery_receipt(
                self.discovery_output(skips), full_result
            )
            with (
                mock.patch.object(
                    MANIFEST, "producer_registry_payload", return_value=registry
                ),
                mock.patch.object(
                    MANIFEST,
                    "coordinator_evidence_registry_diagnostic",
                    return_value=self.coordinator_registry_fixture(root),
                ),
                mock.patch.object(
                    MANIFEST,
                    "complete_terminal_registry_diagnostic",
                    return_value=self.terminal_registry_fixture(root),
                ),
                mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "false"}, clear=True),
            ):
                payload = MANIFEST.build_manifest(
                    root,
                    revision=revision,
                    head_sha_after=revision["head_sha"],
                    dirty_before=(),
                    dirty_after=(),
                    allow_dirty=False,
                    require_github=False,
                    results=results,
                    unittest_discovery=receipt,
                    infrastructure_errors=(),
                )
        self.assertEqual(payload["status"], "FAIL")
        self.assertTrue(
            any(
                "missing expected unittest skips:" in error
                for error in payload["infrastructure_errors"]
            )
        )

    def test_schema_and_python_identity_use_strict_replay(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            baseline = self.build_valid_manifest(root, registry)

            wrong_schema = copy.deepcopy(baseline)
            wrong_schema["schema_version"] = True
            wrong_schema = MANIFEST.seal_manifest(wrong_schema)
            schema_errors = self.verify_with_registry(root, wrong_schema, registry)

            wrong_discovery_schema = copy.deepcopy(baseline)
            wrong_discovery_schema["unittest_discovery"]["schema_version"] = True
            wrong_discovery_schema = MANIFEST.seal_manifest(wrong_discovery_schema)
            discovery_schema_errors = self.verify_with_registry(
                root, wrong_discovery_schema, registry
            )

            wrong_version = copy.deepcopy(baseline)
            wrong_version["python_version"] = "forged-python"
            wrong_version = MANIFEST.seal_manifest(wrong_version)
            version_errors = self.verify_with_registry(root, wrong_version, registry)

            wrong_implementation = copy.deepcopy(baseline)
            wrong_implementation["python_implementation"] = "forged-runtime"
            wrong_implementation = MANIFEST.seal_manifest(wrong_implementation)
            implementation_errors = self.verify_with_registry(
                root, wrong_implementation, registry
            )

        self.assertIn(
            "manifest contract identity is neither legacy v1 nor current v2",
            schema_errors,
        )
        self.assertIn(
            "unittest_discovery.schema_version is not integer 1",
            discovery_schema_errors,
        )
        self.assertIn(
            "python_version does not match the verifying interpreter", version_errors
        )
        self.assertIn(
            "python_implementation does not match the verifying interpreter",
            implementation_errors,
        )

    def test_captured_command_output_is_streamed_and_returned(self) -> None:
        spec = MANIFEST.CommandSpec(
            "capture_control",
            (
                "python",
                "-c",
                "import sys; print('stdout-control'); print('stderr-control', file=sys.stderr)",
            ),
            timeout_seconds=10,
        )
        streamed: list[bytes] = []
        with mock.patch.object(MANIFEST, "_stream_bytes_to_ci", streamed.append):
            result, captured = MANIFEST.run_command(
                ROOT, spec, capture_output=True
            )
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["exit_code"], 0)
        self.assertIsNotNone(captured)
        self.assertIn(b"stdout-control", captured)
        self.assertIn(b"stderr-control", captured)
        self.assertEqual(b"".join(streamed), captured)

    def test_manifest_payload_tamper_and_head_advance_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            payload = self.build_valid_manifest(root, registry)
            self.assertEqual(
                self.verify_with_registry(root, payload, registry, require_pass=True),
                (),
            )

            tampered = copy.deepcopy(payload)
            tampered["python_version"] = "forged"
            errors = self.verify_with_registry(root, tampered, registry)
            self.assertIn("manifest_payload_sha256 does not replay", errors)

            self.write(root, "claims/after.md", "# Later claim\n")
            self.commit_all(root, "advance head")
            errors = self.verify_with_registry(root, payload, registry)
        self.assertIn("manifest head_sha does not match checkout HEAD", errors)
        self.assertIn("manifest head_tree_sha does not match checkout tree", errors)

    def test_zero_authority_registries_resolve_from_exact_head(self) -> None:
        revision = MANIFEST.current_revision(ROOT)
        entries = MANIFEST.git_tree_entries(ROOT, revision["head_sha"])
        evidence = MANIFEST.coordinator_evidence_registry_diagnostic(
            ROOT, revision["head_sha"]
        )
        terminal = MANIFEST.complete_terminal_registry_diagnostic(
            ROOT, entries, revision["head_sha"]
        )

        self.assertEqual(evidence["status"], MANIFEST.EVIDENCE_REGISTRY_STATUS)
        self.assertFalse(evidence["role_authority"])
        self.assertEqual(set(evidence["role_subdigests"]), MANIFEST.ROLE_SUBDIGEST_KEYS)
        self.assertEqual(set(evidence["role_grant_counts"].values()), {0})
        self.assertEqual(evidence["active_role_grant_count"], 0)
        self.assertEqual(evidence["active_producer_count"], 0)
        self.assertEqual(evidence["complete_terminal_schedule_count"], 0)
        self.assertEqual(terminal["status"], MANIFEST.COMPLETE_TERMINAL_REGISTRY_STATUS)
        self.assertEqual(terminal["complete_schedule_count"], 0)
        self.assertFalse(terminal["complete_miss_issuance_enabled"])

    def test_zero_authority_diagnostic_mutations_do_not_self_attest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            baseline = self.build_valid_manifest(root, registry)
            mutations = []
            for path, value in (
                (("coordinator_evidence_registry", "registry_digest"), "0" * 64),
                (("coordinator_evidence_registry", "evidence_inventory_digest"), "0" * 64),
                (
                    (
                        "coordinator_evidence_registry",
                        "role_subdigests",
                        "producer_registry",
                    ),
                    "0" * 64,
                ),
                (("coordinator_evidence_registry", "active_producer_count"), 1),
                (("complete_terminal_registry", "registry_digest"), "0" * 64),
                (("complete_terminal_registry", "complete_schedule_count"), 1),
                (
                    ("complete_terminal_registry", "complete_miss_issuance_enabled"),
                    True,
                ),
            ):
                mutation = copy.deepcopy(baseline)
                target = mutation
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                mutations.append(MANIFEST.seal_manifest(mutation))
            for mutation in mutations:
                errors = self.verify_with_registry(root, mutation, registry)
                self.assertTrue(
                    any("does not replay from HEAD" in error for error in errors),
                    errors,
                )

    def test_resolver_reported_digests_are_independently_recomputed(self) -> None:
        head = MANIFEST.current_revision(ROOT)["head_sha"]
        completed = subprocess.run(
            [
                sys.executable,
                MANIFEST.COORDINATOR_ROLE_RESOLVER_PATH,
                "--root",
                str(ROOT),
                "--head",
                head,
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        baseline = json.loads(completed.stdout)
        mutations = []

        outer = copy.deepcopy(baseline)
        outer["registry_digest"] = "0" * 64
        mutations.append(outer)

        inventory = copy.deepcopy(baseline)
        inventory["artifact_evidence_inventory"]["digest"] = "0" * 64
        unsigned = dict(inventory)
        unsigned.pop("registry_digest")
        inventory["registry_digest"] = MANIFEST.canonical_sha256(unsigned)
        mutations.append(inventory)

        role = copy.deepcopy(baseline)
        role["role_subdigests"]["producer_registry"] = "0" * 64
        unsigned = dict(role)
        unsigned.pop("registry_digest")
        role["registry_digest"] = MANIFEST.canonical_sha256(unsigned)
        mutations.append(role)

        for mutation in mutations:
            encoded = MANIFEST.canonical_json_bytes(mutation) + b"\n"
            forged_result = subprocess.CompletedProcess(
                args=("resolver",), returncode=0, stdout=encoded, stderr=b""
            )
            with (
                self.subTest(marker=mutation),
                mock.patch.object(MANIFEST, "_run_bytes", return_value=forged_result),
                self.assertRaises(MANIFEST.ManifestError),
            ):
                MANIFEST.coordinator_evidence_registry_diagnostic(ROOT, head)

    def test_manifest_verifier_dispatches_legacy_v1_and_current_v2(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_manifest_repository(root)
            registry = {"schema_id": "test_registry", "producers": []}
            current = self.build_valid_manifest(root, registry)
            self.assertEqual(current["schema_id"], "t6_ci_run_manifest_v2")
            self.assertEqual(current["schema_version"], 2)
            self.assertEqual(self.verify_with_registry(root, current, registry), ())

            legacy = copy.deepcopy(current)
            legacy["schema_id"] = MANIFEST.LEGACY_SCHEMA_ID
            legacy["schema_version"] = MANIFEST.LEGACY_SCHEMA_VERSION
            legacy["artifact_id"] = MANIFEST.LEGACY_ARTIFACT_ID
            legacy.pop("coordinator_evidence_registry")
            legacy.pop("complete_terminal_registry")
            legacy = MANIFEST.seal_manifest(legacy)
            self.assertEqual(self.verify_with_registry(root, legacy, registry), ())

            legacy_with_v2_authority = copy.deepcopy(legacy)
            legacy_with_v2_authority["coordinator_evidence_registry"] = (
                self.coordinator_registry_fixture(root)
            )
            legacy_with_v2_authority = MANIFEST.seal_manifest(legacy_with_v2_authority)
            errors = self.verify_with_registry(
                root, legacy_with_v2_authority, registry
            )
            self.assertTrue(any("top-level field mismatch" in item for item in errors))

            for source, version in (
                (legacy, True),
                (legacy, 1.0),
                (current, 2.0),
            ):
                confused = copy.deepcopy(source)
                confused["schema_version"] = version
                confused = MANIFEST.seal_manifest(confused)
                errors = self.verify_with_registry(root, confused, registry)
                self.assertIn(
                    "manifest contract identity is neither legacy v1 nor current v2",
                    errors,
                )

    def test_manifest_git_reads_ignore_replace_refs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.initialize_repository(root)
            self.write(root, "claims/alpha.md", "original\n")
            self.commit_all(root, "replace-ref control")
            revision = MANIFEST.current_revision(root)
            entries = MANIFEST.git_tree_entries(root, revision["head_sha"])
            entry = next(item for item in entries if item.path == "claims/alpha.md")
            baseline = MANIFEST.git_blob_bytes(root, entry)
            replacement = subprocess.run(
                ["git", "hash-object", "-w", "--stdin"],
                cwd=root,
                input=b"replacement\n",
                check=True,
                capture_output=True,
            ).stdout.decode().strip()
            self.git(root, "replace", entry.object_id, replacement)
            raw = subprocess.run(
                ["git", "cat-file", "blob", entry.object_id],
                cwd=root,
                check=True,
                capture_output=True,
                env={key: value for key, value in os.environ.items() if key != "GIT_NO_REPLACE_OBJECTS"},
            ).stdout
            self.assertEqual(raw, b"replacement\n")
            self.assertEqual(MANIFEST.git_blob_bytes(root, entry), baseline)
            self.git(root, "replace", "-d", entry.object_id)

            original_head = revision["head_sha"]
            original_tree = revision["head_tree_sha"]
            self.write(root, "claims/alpha.md", "replacement commit\n")
            self.commit_all(root, "replacement commit")
            replacement_commit = self.git(root, "rev-parse", "HEAD")
            self.git(root, "checkout", "--quiet", "--detach", original_head)
            self.git(root, "replace", original_head, replacement_commit)
            environment = {
                key: value
                for key, value in os.environ.items()
                if key != "GIT_NO_REPLACE_OBJECTS"
            }
            raw_tree = subprocess.run(
                ["git", "rev-parse", "HEAD^{tree}"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
                env=environment,
            ).stdout.strip()
            self.assertNotEqual(raw_tree, original_tree)
            self.assertEqual(
                MANIFEST.current_revision(root),
                {
                    "head_sha": original_head,
                    "head_tree_sha": original_tree,
                    "git_object_format": revision["git_object_format"],
                },
            )


if __name__ == "__main__":
    unittest.main()
