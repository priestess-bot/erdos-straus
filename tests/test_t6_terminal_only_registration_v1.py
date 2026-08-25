from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_PATH = ROOT / "scripts" / "t6_persistent_selector_runtime_v1.py"
SPEC = importlib.util.spec_from_file_location("terminal_only_runtime", RUNTIME_PATH)
assert SPEC and SPEC.loader
RUNTIME = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = RUNTIME
SPEC.loader.exec_module(RUNTIME)

FIXTURE_PATH = ROOT / "tests" / "test_t6_persistent_selector_state_v1.py"
FIXTURE_SPEC = importlib.util.spec_from_file_location("terminal_only_fixtures", FIXTURE_PATH)
assert FIXTURE_SPEC and FIXTURE_SPEC.loader
FIXTURES = importlib.util.module_from_spec(FIXTURE_SPEC)
sys.modules[FIXTURE_SPEC.name] = FIXTURES
FIXTURE_SPEC.loader.exec_module(FIXTURES)

CONTRACT = RUNTIME.state_contract


PRODUCER_ID = "terminal_only.test"
BRANCH_ID = "terminal_branch.test"
OWNER = "type_i_full_carrier_post_g"
SOURCE_SCHEDULE = "terminal_only.source.test"
VERIFIER_ID = "terminal_only.verifier.test"


def build_runtime(output_factory):
    branch = RUNTIME.TerminalOnlyBranchRegistrationV1(
        branch_id=BRANCH_ID,
        source_owners=frozenset({OWNER}),
        evidence_refs=("claim:terminal-only-test",),
        source_terminal_schedule_id=SOURCE_SCHEDULE,
        terminal_verifier_ids=frozenset({VERIFIER_ID}),
    )
    producer = RUNTIME.TerminalOnlyProducerRegistrationV1(
        producer_id=PRODUCER_ID,
        implementation_ref="tests/test_t6_terminal_only_registration_v1.py:executor",
        branches=(branch,),
    )

    def source_schedule(source):
        return RUNTIME.TerminalMissV1(
            schedule_id=SOURCE_SCHEDULE,
            scope="terminal-only-test-scope",
            evidence_id=f"source-miss:{source.state_id}",
        )

    def verifier(source, payload, lift):
        return (
            payload.get("kind") == "TEST_TERMINAL"
            and payload.get("p") == source.header.root_context
            and lift == "identity:test"
        )

    runtime = RUNTIME.PersistentSelectorRuntimeV1(
        initializer=RUNTIME.InitializerRegistrationV1(
            producer_id="initializer.test",
            branch_ids=frozenset({"root.test"}),
            target_owners=frozenset({OWNER}),
        ),
        producers=(),
        executors={},
        projectors={},
        transition_validators={},
        source_terminal_schedulers={SOURCE_SCHEDULE: source_schedule},
        target_terminal_schedulers={},
        terminal_verifiers={VERIFIER_ID: verifier},
        dispatch_precedence={},
        terminal_producers=(producer,),
        terminal_executors={PRODUCER_ID: output_factory},
        terminal_dispatch_precedence={
            OWNER: (RUNTIME.TerminalDispatchEntryV1(PRODUCER_ID, BRANCH_ID),)
        },
    )
    raw = FIXTURES.make_state(
        FIXTURES.facts(
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
    root = runtime.bootstrap_nonterminal_v1(
        raw,
        RUNTIME.T5StateDescriptorV1(
            induction_rank=73,
            major_phase="TYPEI",
            type_i_protocol="CHARGED",
            eta_p=0,
        ),
    )
    return runtime, root, raw


class TerminalOnlyRegistrationTests(unittest.TestCase):
    def test_terminal_draft_is_verified_without_queue_mutation(self) -> None:
        runtime, root, _ = build_runtime(
            lambda source, branch: RUNTIME.TerminalDraftV1(
                verifier_id=VERIFIER_ID,
                certificate_payload={
                    "kind": "TEST_TERMINAL",
                    "p": source.header.root_context,
                },
                lift_evidence_id="identity:test",
            )
        )
        decision = runtime.run_state_once_v1(root)
        self.assertTrue(decision.accepted)
        self.assertIsNotNone(decision.terminal)
        self.assertEqual(len(runtime.queue_snapshot_v1()), 1)
        self.assertEqual(runtime.producer_rules_v1().keys(), {"initializer.test"})

    def test_terminal_only_candidate_fails_closed(self) -> None:
        runtime, root, _ = build_runtime(
            lambda source, branch: RUNTIME.CandidateTransitionV1(
                producer_id=PRODUCER_ID,
                branch_id=BRANCH_ID,
                witness_payload={"source_occurrence": "candidate"},
                ticket_type="LOCAL_DROP",
            )
        )
        decision = runtime.run_state_once_v1(root)
        self.assertFalse(decision.accepted)
        self.assertEqual(
            decision.reason_code,
            RUNTIME.RuntimeRejectCode.TERMINAL_ONLY_CANDIDATE,
        )
        self.assertEqual(len(runtime.queue_snapshot_v1()), 1)

    def test_terminal_only_state_cannot_bootstrap_as_persistent_target(self) -> None:
        runtime, _, raw = build_runtime(
            lambda source, branch: RUNTIME.GuardMissV1("MISS", "miss")
        )
        forged = dict(raw)
        forged["producer_id"] = PRODUCER_ID
        forged["branch_id"] = BRANCH_ID
        forged["state_id"] = CONTRACT.build_state_id_v1(forged)
        with self.assertRaises(RUNTIME.RuntimeContractError):
            runtime.bootstrap_nonterminal_v1(
                forged,
                RUNTIME.T5StateDescriptorV1(
                    induction_rank=73,
                    major_phase="TYPEI",
                    type_i_protocol="CHARGED",
                ),
            )

    def test_terminal_and_successor_registration_cannot_share_id(self) -> None:
        branch = RUNTIME.BranchRegistrationV1(
            branch_id="successor.test",
            source_owners=frozenset({OWNER}),
            target_owners=frozenset({"type_i_a_gt_one_overflow_residual"}),
            evidence_refs=("claim:successor-test",),
            allowed_tickets=frozenset({"LOCAL_DROP"}),
            projector_id="projector.test",
            transition_validator_id="validator.test",
            source_terminal_schedule_id="source.test",
            target_terminal_schedule_id="target.test",
        )
        successor = RUNTIME.ProducerRegistrationV1(
            producer_id=PRODUCER_ID,
            implementation_ref="successor",
            branches=(branch,),
        )
        terminal = RUNTIME.TerminalOnlyProducerRegistrationV1(
            producer_id=PRODUCER_ID,
            implementation_ref="terminal",
            branches=(
                RUNTIME.TerminalOnlyBranchRegistrationV1(
                    branch_id=BRANCH_ID,
                    source_owners=frozenset({OWNER}),
                    evidence_refs=("claim:terminal-test",),
                    source_terminal_schedule_id=SOURCE_SCHEDULE,
                    terminal_verifier_ids=frozenset({VERIFIER_ID}),
                ),
            ),
        )
        with self.assertRaises(ValueError):
            RUNTIME.PersistentSelectorRuntimeV1(
                initializer=RUNTIME.InitializerRegistrationV1(
                    "initializer.test", frozenset({"root.test"}), frozenset({OWNER})
                ),
                producers=(successor,),
                executors={},
                projectors={},
                transition_validators={},
                source_terminal_schedulers={},
                target_terminal_schedulers={},
                terminal_verifiers={},
                dispatch_precedence={OWNER: (RUNTIME.DispatchEntryV1(PRODUCER_ID, "successor.test"),)},
                terminal_producers=(terminal,),
                terminal_executors={},
                terminal_dispatch_precedence={
                    OWNER: (RUNTIME.TerminalDispatchEntryV1(PRODUCER_ID, BRANCH_ID),)
                },
            )


if __name__ == "__main__":
    unittest.main()
