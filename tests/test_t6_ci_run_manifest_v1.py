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

        self.assertIn("schema_version is not integer 1", schema_errors)
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


if __name__ == "__main__":
    unittest.main()
