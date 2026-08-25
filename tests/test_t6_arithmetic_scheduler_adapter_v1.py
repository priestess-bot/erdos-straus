from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_arithmetic_scheduler_adapter_v1.py"
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "t6_arithmetic_scheduler_adapter_v1_under_test", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

RUNTIME = MODULE.runtime


class ArithmeticSchedulerAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = object()
        self.adapter_ids = {
            "producer_id": "test_arithmetic_producer",
            "branch_id": "test_branch",
        }

    def adapter(self, scheduler):
        return MODULE.ArithmeticSchedulerAdapterV1(
            **self.adapter_ids,
            scheduler=scheduler,
        )

    def test_authority_free_candidate_passes_adapter_boundary(self) -> None:
        candidate = RUNTIME.CandidateTransitionV1(
            producer_id=self.adapter_ids["producer_id"],
            branch_id=self.adapter_ids["branch_id"],
            witness_payload={"source_occurrence": "receipt:1"},
            ticket_type="LOCAL_DROP",
        )
        output = self.adapter(lambda source, branch: candidate)(self.source, "test_branch")
        self.assertIs(output, candidate)

    def test_legacy_mapping_is_rejected(self) -> None:
        adapter = self.adapter(lambda source, branch: {"e1": True, "target": {}})
        with self.assertRaises(RUNTIME.RuntimeContractError) as error:
            adapter(self.source, "test_branch")
        self.assertEqual(
            error.exception.code,
            RUNTIME.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
        )

    def test_caller_authority_field_is_rejected(self) -> None:
        candidate = RUNTIME.CandidateTransitionV1(
            producer_id=self.adapter_ids["producer_id"],
            branch_id=self.adapter_ids["branch_id"],
            witness_payload={"persistent_queue": True},
            ticket_type="LOCAL_DROP",
        )
        with self.assertRaises(RUNTIME.RuntimeContractError) as error:
            self.adapter(lambda source, branch: candidate)(self.source, "test_branch")
        self.assertEqual(
            error.exception.code,
            RUNTIME.RuntimeRejectCode.CANDIDATE_AUTHORITY_FIELD,
        )

    def test_guard_and_terminal_outputs_are_only_pass_through_values(self) -> None:
        miss = self.adapter(
            lambda source, branch: RUNTIME.GuardMissV1("NO_SOURCE", "not admitted")
        )(self.source, "test_branch")
        self.assertIsInstance(miss, RUNTIME.GuardMissV1)
        draft = self.adapter(
            lambda source, branch: RUNTIME.TerminalDraftV1(
                verifier_id="terminal.test",
                certificate_payload={"p": 73},
                lift_evidence_id="identity",
            )
        )(self.source, "test_branch")
        self.assertIsInstance(draft, RUNTIME.TerminalDraftV1)

    def test_branch_mismatch_fails_closed(self) -> None:
        with self.assertRaises(RUNTIME.RuntimeContractError) as error:
            self.adapter(
                lambda source, branch: RUNTIME.GuardMissV1("X", "x")
            )(self.source, "other_branch")
        self.assertEqual(error.exception.code, RUNTIME.RuntimeRejectCode.UNKNOWN_BRANCH)


if __name__ == "__main__":
    unittest.main()
