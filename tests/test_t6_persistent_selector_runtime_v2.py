from __future__ import annotations

import copy
from dataclasses import replace
import inspect
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_acyclic_transition_bundle_v2 as acyclic  # noqa: E402
import t6_persistent_selector_runtime_v1 as legacy_runtime  # noqa: E402
import t6_persistent_selector_runtime_v2 as runtime_v2  # noqa: E402
import t6_structured_transition_receipts_v1 as legacy_receipts  # noqa: E402


def run_git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "GIT_NO_REPLACE_OBJECTS": "1"},
    ).stdout.strip()


def digest(label: str) -> str:
    return acyclic.canonical_digest_v2({"fixture": label})


def make_acyclic_chain():
    projection = acyclic.make_canonical_target_projection_v2(
        target_schema_id="t6_persistent_selector_state_v2",
        target_schema_version=2,
        root_context="root:p=73",
        equation_rank=73,
        facts={"chart_R": 75, "chart_K": 1369},
        mark_behavior="IDENTITY_MARK",
        projector_id="projector.fixture.v2",
        projector_digest=digest("projector"),
        tie_break_rule_id="tie-break.fixture.v2",
        tie_break_rule_digest=digest("tie-break"),
    )
    preclassification = acyclic.make_preclassification_digest_v2(
        projection,
        normal_form_verifier_id="normal-form.fixture.v2",
        normal_form_verifier_digest=digest("normal-form"),
        predicate_results_digest=digest("predicate-results"),
        precedence_table_id="precedence.fixture.v2",
        precedence_table_digest=digest("precedence"),
    )
    terminal = acyclic.make_terminal_digest_set_v2(
        projection,
        source_state_id="state:source-fixture",
        source_state_digest=digest("source-state"),
        schedule_id="terminal.fixture.v2",
        schedule_digest=digest("terminal-schedule"),
        result_digest=digest("terminal-result"),
        coverage_scope_digest=digest("terminal-scope"),
    )
    t5_draft = acyclic.make_t5_coordinate_draft_v2(
        projection,
        taxonomy_id="taxonomy.fixture.v2",
        taxonomy_digest=digest("taxonomy"),
        coordinates=(73, 2, 4, 8, 7, 0, 0),
    )
    anchor = acyclic.make_edge_anchor_v2(
        projection,
        preclassification,
        terminal,
        t5_draft,
        producer_id="producer.fixture.v2",
        producer_digest=digest("producer"),
        branch_id="branch.fixture.v2",
        candidate_witness_digest=digest("candidate-witness"),
    )
    target = acyclic.make_raw_target_state_v2(projection, anchor)
    bundle = acyclic.make_final_transition_receipt_bundle_v2(
        anchor,
        target,
        e1_occurrence_receipt_digest=digest("E1"),
        e2_projection_receipt_digest=digest("E2"),
        e3_typing_receipt_digest=digest("E3"),
        e4_lift_receipt_digest=digest("E4"),
        e5_ticket_receipt_digest=digest("E5"),
    )
    sidecar = acyclic.make_state_admission_sidecar_v2(
        target,
        bundle,
        owner_id="owner.fixture",
        owner_digest=digest("owner"),
        grammar_digest=digest("grammar"),
        admission_gate_digest=digest("admission-gate"),
        target_potential_receipt_digest=digest("target-potential"),
        state_admission_receipt_digest=digest("state-admission"),
    )
    return target, bundle, sidecar


class PersistentSelectorRuntimeV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="t6-runtime-v2-test-")
        cls.repository = Path(cls.temp.name) / "repository"
        subprocess.run(
            ["git", "clone", "-q", "--no-hardlinks", str(ROOT), str(cls.repository)],
            check=True,
            capture_output=True,
            env={**os.environ, "GIT_NO_REPLACE_OBJECTS": "1"},
        )
        runtime_path = cls.repository / runtime_v2.RUNTIME_PATH
        if runtime_path.exists():
            run_git(cls.repository, "rm", "-q", runtime_v2.RUNTIME_PATH)
            run_git(
                cls.repository,
                "-c",
                "user.name=Runtime V2 Test",
                "-c",
                "user.email=runtime-v2@example.invalid",
                "commit",
                "-q",
                "-m",
                "fixture without runtime v2",
            )
        cls.head_without_runtime = run_git(cls.repository, "rev-parse", "HEAD")
        runtime_path.parent.mkdir(parents=True, exist_ok=True)
        runtime_path.write_bytes((SCRIPTS / runtime_path.name).read_bytes())
        run_git(cls.repository, "add", runtime_v2.RUNTIME_PATH)
        run_git(
            cls.repository,
            "-c",
            "user.name=Runtime V2 Test",
            "-c",
            "user.email=runtime-v2@example.invalid",
            "commit",
            "-q",
            "-m",
            "fixture with runtime v2",
        )
        cls.head = run_git(cls.repository, "rev-parse", "HEAD")
        cls.runtime = runtime_v2.open_runtime_v2(
            root=cls.repository,
            requested_head=cls.head,
        )
        target, bundle, sidecar = make_acyclic_chain()
        cls.request = runtime_v2.make_successor_admission_request_v2(
            target,
            bundle,
            sidecar,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def assert_rejects(self, code, callback) -> runtime_v2.RuntimeContractErrorV2:
        before = self.runtime.queue_snapshot_v2()
        with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
            callback()
        self.assertEqual(raised.exception.code, code)
        self.assertEqual(self.runtime.queue_snapshot_v2(), before)
        return raised.exception

    def test_exact_head_snapshot_is_sealed_and_has_zero_authority(self) -> None:
        snapshot = self.runtime.authority_snapshot_v2()
        mapping = self.runtime.authority_mapping_v2()
        unsigned = dict(mapping)
        observed_digest = unsigned.pop("digest")
        self.assertEqual(observed_digest, acyclic.canonical_digest_v2(unsigned))
        self.assertEqual(snapshot.head_sha, self.head)
        self.assertEqual(snapshot.active_role_grant_count, 0)
        self.assertEqual(snapshot.authorized_route_count, 0)
        self.assertEqual(snapshot.initializer_count, 0)
        self.assertEqual(snapshot.complete_terminal_schedule_count, 0)
        self.assertEqual(snapshot.status, runtime_v2.RUNTIME_STATUS)
        self.assertEqual(snapshot.proof_boundary, "NOT_GATE2_NOT_T6_CLOSURE")

    def test_runtime_exposes_no_route_initializer_or_mutable_queue(self) -> None:
        self.assertEqual(self.runtime.route_ids_v2(), ())
        self.assertEqual(self.runtime.initializer_ids_v2(), ())
        self.assertEqual(self.runtime.queue_snapshot_v2(), ())
        self.assertIsInstance(self.runtime.queue_snapshot_v2(), tuple)
        with self.assertRaises(TypeError):
            runtime_v2.PersistentSelectorRuntimeV2()

    def test_open_signature_has_no_caller_authority_surface(self) -> None:
        parameters = inspect.signature(runtime_v2.open_runtime_v2).parameters
        self.assertEqual(tuple(parameters), ("root", "requested_head"))
        forbidden = {
            "producers",
            "projectors",
            "transition_validators",
            "schedulers",
            "evidence_ids",
            "artifact_digest_manifest",
        }
        self.assertTrue(forbidden.isdisjoint(parameters))
        with self.assertRaises(TypeError):
            runtime_v2.open_runtime_v2(
                root=self.repository,
                requested_head=self.head,
                producers={},
            )

    def test_no_argument_bootstrap_is_stably_rejected(self) -> None:
        self.assert_rejects(
            runtime_v2.RuntimeRejectCodeV2.BOOTSTRAP_AUTHORITY_UNAVAILABLE,
            self.runtime.bootstrap_v2,
        )

    def test_caller_and_legacy_bootstrap_payloads_are_rejected(self) -> None:
        for payload in (
            {"schema_id": "t6_persistent_selector_state_v1"},
            legacy_runtime.InitializerRegistrationV1(
                producer_id="legacy.initializer",
                branch_ids=frozenset({"legacy.branch"}),
                target_owners=frozenset({"legacy.owner"}),
            ),
            legacy_receipts.ArtifactDigestManifestV1({}),
        ):
            with self.subTest(payload_type=type(payload).__name__):
                self.assert_rejects(
                    runtime_v2.RuntimeRejectCodeV2.
                    CALLER_BOOTSTRAP_PAYLOAD_FORBIDDEN,
                    lambda payload=payload: self.runtime.bootstrap_v2(payload),
                )

    def test_well_formed_acyclic_v2_successor_has_no_authority(self) -> None:
        self.assert_rejects(
            runtime_v2.RuntimeRejectCodeV2.SUCCESSOR_AUTHORITY_UNAVAILABLE,
            lambda: self.runtime.admit_successor_v2(self.request),
        )

    def test_v1_transition_validation_is_rejected_before_queue(self) -> None:
        legacy = legacy_runtime.TransitionValidationV1(
            source_state_id="state:source",
            producer_id="producer.legacy",
            branch_id="branch.legacy",
            projection_digest=digest("legacy-projection"),
            E1=True,
            E2=True,
            E3_pre_admission=True,
            E4=True,
            evidence_ids=("legacy:evidence",),
        )
        self.assert_rejects(
            runtime_v2.RuntimeRejectCodeV2.
            CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN,
            lambda: self.runtime.admit_successor_v2(legacy),
        )

    def test_v1_terminal_miss_and_raw_state_are_rejected(self) -> None:
        inputs = (
            legacy_runtime.TerminalMissV1(
                schedule_id="legacy.schedule",
                scope="LOCAL",
                evidence_id="legacy:evidence",
            ),
            {"state_id": "legacy:raw", "queue_gate": "ADMITTED_SUCCESSOR"},
            legacy_receipts.ArtifactDigestManifestV1({}),
            ["evidence:caller-owned"],
        )
        for value in inputs:
            with self.subTest(value_type=type(value).__name__):
                self.assert_rejects(
                    runtime_v2.RuntimeRejectCodeV2.
                    CALLER_OR_LEGACY_SUCCESSOR_FORBIDDEN,
                    lambda value=value: self.runtime.admit_successor_v2(value),
                )

    def test_exact_request_type_with_wrong_fields_fails_v2_replay(self) -> None:
        forged = object.__new__(runtime_v2.SuccessorAdmissionRequestV2)
        object.__setattr__(forged, "target", {"legacy": "raw-state"})
        object.__setattr__(forged, "transition_bundle", self.request.transition_bundle)
        object.__setattr__(forged, "admission_sidecar", self.request.admission_sidecar)
        self.assert_rejects(
            runtime_v2.RuntimeRejectCodeV2.V2_BUNDLE_INVALID,
            lambda: self.runtime.admit_successor_v2(forged),
        )

    def test_invalid_head_is_wrapped_in_stable_resolution_code(self) -> None:
        with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
            runtime_v2.open_runtime_v2(root=self.repository, requested_head="HEAD")
        self.assertEqual(
            raised.exception.code,
            runtime_v2.RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
        )

    def test_runtime_absent_from_requested_head_is_rejected(self) -> None:
        with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
            runtime_v2.open_runtime_v2(
                root=self.repository,
                requested_head=self.head_without_runtime,
            )
        self.assertEqual(
            raised.exception.code,
            runtime_v2.RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
        )

    def test_runtime_worktree_drift_is_rejected_and_restored(self) -> None:
        runtime_path = self.repository / runtime_v2.RUNTIME_PATH
        original = runtime_path.read_bytes()
        runtime_path.write_bytes(original + b"# uncommitted drift\n")
        try:
            with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
                runtime_v2.open_runtime_v2(
                    root=self.repository,
                    requested_head=self.head,
                )
            self.assertEqual(
                raised.exception.code,
                runtime_v2.RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
            )
        finally:
            runtime_path.write_bytes(original)

    def test_role_grant_or_bool_zero_cannot_open_this_revision(self) -> None:
        resolved = runtime_v2.role_registry.resolve_registry_v1(
            root=self.repository,
            requested_head=self.head,
        )
        mutations = (
            {"active_role_grant_count": 1},
            {"active_role_grant_count": False},
            {"authorized_branches": ["caller.branch"]},
        )
        for mutation in mutations:
            forged = copy.deepcopy(resolved)
            forged.update(mutation)
            forged.pop("registry_digest")
            forged["registry_digest"] = runtime_v2.role_registry.canonical_digest_v1(
                forged
            )
            with self.subTest(mutation=mutation):
                with mock.patch.object(
                    runtime_v2.role_registry,
                    "resolve_registry_v1",
                    return_value=forged,
                ):
                    with self.assertRaises(
                        runtime_v2.RuntimeContractErrorV2
                    ) as raised:
                        runtime_v2.open_runtime_v2(
                            root=self.repository,
                            requested_head=self.head,
                        )
                self.assertEqual(
                    raised.exception.code,
                    runtime_v2.RuntimeRejectCodeV2.AUTHORITY_STATE_INVALID,
                )

    def test_terminal_registry_is_parsed_from_exact_head_not_loader(self) -> None:
        with mock.patch.object(
            runtime_v2.terminal_contract,
            "load_production_registry_v1",
            side_effect=AssertionError("worktree loader must not run"),
        ):
            reopened = runtime_v2.open_runtime_v2(
                root=self.repository,
                requested_head=self.head,
            )
        self.assertEqual(reopened.queue_snapshot_v2(), ())

    def test_dependency_content_drift_is_rejected(self) -> None:
        original = runtime_v2._read_exact_head_blob_v2

        def drift(root: Path, head_sha: str, path: str):
            blob = original(root, head_sha, path)
            if path == runtime_v2.HEAD_BOUND_DEPENDENCIES[1]:
                return replace(blob, content=blob.content + b"# drift\n")
            return blob

        with mock.patch.object(
            runtime_v2,
            "_read_exact_head_blob_v2",
            side_effect=drift,
        ):
            with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
                runtime_v2.open_runtime_v2(
                    root=self.repository,
                    requested_head=self.head,
                )
        self.assertEqual(
            raised.exception.code,
            runtime_v2.RuntimeRejectCodeV2.EXACT_HEAD_DEPENDENCY_MISMATCH,
        )

    def test_malformed_exact_head_terminal_registry_is_rejected(self) -> None:
        original = runtime_v2._read_exact_head_blob_v2

        def malformed(root: Path, head_sha: str, path: str):
            blob = original(root, head_sha, path)
            if path == runtime_v2.TERMINAL_REGISTRY_PATH:
                return replace(blob, content=b'{"schema_id":1,"schema_id":2}')
            return blob

        with mock.patch.object(
            runtime_v2,
            "_read_exact_head_blob_v2",
            side_effect=malformed,
        ):
            with self.assertRaises(runtime_v2.RuntimeContractErrorV2) as raised:
                runtime_v2.open_runtime_v2(
                    root=self.repository,
                    requested_head=self.head,
                )
        self.assertEqual(
            raised.exception.code,
            runtime_v2.RuntimeRejectCodeV2.AUTHORITY_RESOLUTION_FAILED,
        )


if __name__ == "__main__":
    unittest.main()
