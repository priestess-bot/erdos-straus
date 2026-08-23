from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "t6_persistent_selector_runtime_v1",
    ROOT / "scripts" / "t6_persistent_selector_runtime_v1.py",
)
assert SPEC and SPEC.loader
runtime = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runtime
SPEC.loader.exec_module(runtime)

CONTRACT = runtime.state_contract


def load_state_fixtures():
    path = ROOT / "tests" / "test_t6_persistent_selector_state_v1.py"
    spec = importlib.util.spec_from_file_location("runtime_state_fixtures", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


FIX = load_state_fixtures()


def runtime_setup(
    *,
    terminal: bool = False,
    source_terminal: bool = False,
    authority_field: bool = False,
    guard_prefix: bool = False,
    validation_evidence: tuple[str, ...] = ("claim:test", "proof.test"),
):
    branch = runtime.BranchRegistrationV1(
        branch_id="branch.test",
        source_owners=frozenset({"type_i_full_carrier_post_g"}),
        target_owners=frozenset({"type_i_low_support_persistent_overflow"}),
        evidence_refs=("claim:test",),
        allowed_tickets=frozenset({"LOCAL_DROP"}),
        projector_id="project.test",
        transition_validator_id="validate.test",
        source_terminal_schedule_id="source-terminal.test",
        target_terminal_schedule_id="terminal.test",
        terminal_verifier_ids=frozenset({"terminal.verifier"}),
    )
    miss_branch = runtime.BranchRegistrationV1(
        branch_id="branch.miss",
        source_owners=branch.source_owners,
        target_owners=branch.target_owners,
        evidence_refs=branch.evidence_refs,
        allowed_tickets=branch.allowed_tickets,
        projector_id=branch.projector_id,
        transition_validator_id=branch.transition_validator_id,
        source_terminal_schedule_id=branch.source_terminal_schedule_id,
        target_terminal_schedule_id=branch.target_terminal_schedule_id,
        terminal_verifier_ids=branch.terminal_verifier_ids,
    )
    producer = runtime.ProducerRegistrationV1(
        producer_id="producer.test",
        implementation_ref="tests/test_t6_persistent_selector_runtime_v1.py:test_producer",
        branches=((miss_branch, branch) if guard_prefix else (branch,)),
    )

    def executor(source, branch_id):
        if branch_id == "branch.miss":
            return runtime.GuardMissV1("EXPECTED_MISS", "test precedence")
        return runtime.CandidateTransitionV1(
            producer_id="producer.test",
            branch_id=branch_id,
            witness_payload=(
                {"owner": "type_i_low_support_persistent_overflow"}
                if authority_field
                else {"chart_R": 75, "chart_K": 1369}
            ),
            ticket_type="LOCAL_DROP",
        )

    def projector(source, candidate):
        facts = dict(source.header.facts)
        facts.update(
            {
                "major_phase": "TYPEI",
                "endpoint_fiber": "NONE",
                "relation_q": None,
                "provenance_kind": "OVERFLOW",
                "full_carrier_scope": False,
                "atomic_arm": "NONE",
                "dispatch_status": "NONE",
                "proper_root_k": None,
                "is_overflow": True,
                "support_A": 37,
                "carrier_M": 74,
                "overflow_d": 71,
                "chart_R": 75,
                "chart_K": 1369,
                "sink_scc_receipt": False,
                "same_chart_promotion_receipt": True,
            }
        )
        return runtime.TargetProjectionV1(
            root_context=source.header.root_context,
            equation_rank=source.header.equation_rank,
            facts=facts,
            t5=runtime.T5StateDescriptorV1(
                induction_rank=source.header.equation_rank,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
            mark_behavior=runtime.IDENTITY_MARK,
        )

    def scheduler(projection, witness):
        if terminal:
            return runtime.TerminalDraftV1(
                verifier_id="terminal.verifier",
                certificate_payload={"ok": True},
                lift_evidence_id="lift.test",
            )
        return runtime.TerminalMissV1(
            schedule_id="terminal.test",
            scope="test-scope",
            evidence_id="terminal-miss-test",
        )

    def source_scheduler(source):
        if source_terminal:
            return runtime.TerminalDraftV1(
                verifier_id="terminal.verifier",
                certificate_payload={"ok": True},
                lift_evidence_id="source-lift.test",
            )
        return runtime.TerminalMissV1(
            schedule_id="source-terminal.test",
            scope="source-test-scope",
            evidence_id="source-terminal-miss-test",
        )

    def validator(source, candidate, projection):
        return runtime.TransitionValidationV1(
            source_state_id=source.state_id,
            producer_id=candidate.producer_id,
            branch_id=candidate.branch_id,
            projection_digest=runtime.PersistentSelectorRuntimeV1._projection_digest_v1(
                projection
            ),
            E1=True,
            E2=True,
            E3_pre_admission=True,
            E4=True,
            evidence_ids=validation_evidence,
        )

    return runtime.PersistentSelectorRuntimeV1(
        initializer=runtime.InitializerRegistrationV1(
            producer_id="initializer.test",
            branch_ids=frozenset({"root.test"}),
            target_owners=frozenset({"type_i_full_carrier_post_g"}),
        ),
        producers=(producer,),
        executors={"producer.test": executor},
        projectors={"project.test": projector},
        transition_validators={"validate.test": validator},
        source_terminal_schedulers={"source-terminal.test": source_scheduler},
        target_terminal_schedulers={"terminal.test": scheduler},
        terminal_verifiers={
            "terminal.verifier": lambda source, payload, lift: (
                payload.get("ok") is True
                and source.state_id.startswith("state:")
                and bool(lift)
            )
        },
        dispatch_precedence={
            "type_i_full_carrier_post_g": (
                (
                    runtime.DispatchEntryV1("producer.test", "branch.miss"),
                    runtime.DispatchEntryV1("producer.test", "branch.test"),
                )
                if guard_prefix
                else (runtime.DispatchEntryV1("producer.test", "branch.test"),)
            )
        },
    )


class RuntimeBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.runtime = runtime_setup()
        self.raw = FIX.make_state(
            FIX.facts(
                provenance_kind="FULL_CARRIER_POST_G",
                full_carrier_scope=True,
                chart_R=51,
                chart_K=931,
                support_A=1,
            ),
            producer="initializer.test",
            branch="root.test",
            gate=CONTRACT.ROOT_INITIALIZER_OUTPUT,
        )
        self.root = self.runtime.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )

    def test_bootstrap_uses_common_admission_and_queue(self):
        self.assertEqual(self.root.owner, "type_i_full_carrier_post_g")
        self.assertEqual(len(self.runtime.queue_snapshot_v1()), 1)

    def test_candidate_authority_fields_cannot_grant_persistence(self):
        guarded_runtime = runtime_setup(authority_field=True)
        root = guarded_runtime.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )
        decision = guarded_runtime.run_state_once_v1(root)
        self.assertFalse(decision.accepted)
        self.assertEqual(
            decision.reason_code, runtime.RuntimeRejectCode.CANDIDATE_AUTHORITY_FIELD
        )

    def test_terminal_scheduler_preempts_target_queue(self):
        decision = self.runtime.run_state_once_v1(self.root)
        # The fixture scheduler returns a miss, so this branch reaches target
        # admission; mutate the scheduler to a verified terminal for preemption.
        self.assertTrue(decision.accepted)
        self.assertIsNotNone(decision.successor)

        terminal_runtime = runtime_setup(terminal=True)
        terminal_root = terminal_runtime.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )
        terminal_decision = terminal_runtime.run_state_once_v1(terminal_root)
        self.assertTrue(terminal_decision.accepted)
        self.assertIsNotNone(terminal_decision.terminal)
        self.assertEqual(len(terminal_runtime.queue_snapshot_v1()), 1)

    def test_ticket_must_drop_parent_to_final_target(self):
        with self.assertRaises(runtime.RuntimeContractError):
            runtime.verify_t5_ticket_v1(
                "LOCAL_DROP", [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]
            )

    def test_source_terminal_preempts_producer(self):
        terminal_runtime = runtime_setup(source_terminal=True)
        root = terminal_runtime.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )
        decision = terminal_runtime.run_state_once_v1(root)
        self.assertTrue(decision.accepted)
        self.assertIsNotNone(decision.terminal)
        self.assertEqual(len(terminal_runtime.queue_snapshot_v1()), 1)

    def test_validator_must_cover_registered_proof_refs(self):
        incomplete = runtime_setup(validation_evidence=("proof.test",))
        root = incomplete.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )
        decision = incomplete.run_state_once_v1(root)
        self.assertFalse(decision.accepted)
        self.assertEqual(
            decision.reason_code, runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID
        )

    def test_fixed_precedence_records_prior_guard_miss(self):
        ordered = runtime_setup(guard_prefix=True)
        root = ordered.bootstrap_nonterminal_v1(
            self.raw,
            runtime.T5StateDescriptorV1(
                induction_rank=73,
                major_phase="TYPEI",
                type_i_protocol="CHARGED",
                eta_p=0,
            ),
        )
        decision = ordered.run_state_once_v1(root)
        self.assertTrue(decision.accepted)
        assert decision.successor is not None
        receipt = decision.successor.transition_receipt
        self.assertTrue(receipt["dispatch_precedence_digest"])

    def test_unissued_candidate_cannot_enter_admission(self):
        candidate = runtime.CandidateTransitionV1(
            producer_id="producer.test",
            branch_id="branch.test",
            witness_payload={"chart_R": 75, "chart_K": 1369},
            ticket_type="LOCAL_DROP",
        )
        produced = runtime.ProducedCandidateV1(
            candidate=candidate,
            execution_id="execution:not-issued",
            dispatch_receipt={},
        )
        decision = self.runtime.admit_candidate_transition_v1(self.root, produced)
        self.assertFalse(decision.accepted)
        self.assertEqual(
            decision.reason_code, runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID
        )


if __name__ == "__main__":
    unittest.main()
