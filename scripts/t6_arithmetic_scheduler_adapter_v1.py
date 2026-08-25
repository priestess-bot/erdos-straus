#!/usr/bin/env python3
"""Fail-closed bridge from arithmetic schedulers to RuntimeExecutorV1.

This adapter deliberately does not register producers or mutate the runtime
queue. It only enforces the authority boundary before a scheduler result is
handed to PersistentSelectorRuntimeV1, whose independent projector, validator,
T5 check and admission path remain mandatory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Callable

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import t6_persistent_selector_runtime_v1 as runtime


ArithmeticSchedulerV1 = Callable[
    [runtime.SourceExecutionContextV1, str],
    runtime.ProducerOutputV1,
]


@dataclass(frozen=True)
class ArithmeticSchedulerAdapterV1:
    """Wrap one branch-specific scheduler without granting persistence rights."""

    producer_id: str
    branch_id: str
    scheduler: ArithmeticSchedulerV1

    def __post_init__(self) -> None:
        if not self.producer_id or not self.branch_id:
            raise ValueError("adapter requires producer_id and branch_id")
        if not callable(self.scheduler):
            raise TypeError("scheduler must be callable")

    def __call__(
        self,
        source: runtime.SourceExecutionContextV1,
        invoked_branch_id: str,
    ) -> runtime.ProducerOutputV1:
        if invoked_branch_id != self.branch_id:
            raise runtime.RuntimeContractError(
                runtime.RuntimeRejectCode.UNKNOWN_BRANCH,
                "adapter invoked for an unregistered branch",
            )
        output = self.scheduler(source, self.branch_id)
        if isinstance(output, runtime.CandidateTransitionV1):
            if (
                output.producer_id != self.producer_id
                or output.branch_id != self.branch_id
            ):
                raise runtime.RuntimeContractError(
                    runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "candidate identity differs from adapter registration",
                )
            # Reuse the coordinator-owned authority firewall. The adapter
            # cannot convert a legacy owner/family/queue flag into authority.
            runtime._reject_candidate_authority(output.witness_payload)
            if not output.ticket_type:
                raise runtime.RuntimeContractError(
                    runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "candidate ticket_type must be nonempty",
                )
            return output
        if isinstance(output, runtime.GuardMissV1):
            if not output.reason_code or not output.detail:
                raise runtime.RuntimeContractError(
                    runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "guard miss must carry a reason and detail",
                )
            return output
        if isinstance(output, runtime.TerminalDraftV1):
            if not output.verifier_id or not output.lift_evidence_id:
                raise runtime.RuntimeContractError(
                    runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
                    "terminal draft must identify verifier and lift evidence",
                )
            return output
        raise runtime.RuntimeContractError(
            runtime.RuntimeRejectCode.PRODUCER_RESULT_INVALID,
            "arithmetic scheduler returned a legacy/non-runtime object",
        )


def adapt_scheduler_v1(
    *,
    producer_id: str,
    branch_id: str,
    scheduler: ArithmeticSchedulerV1,
) -> runtime.ProducerExecutorV1:
    """Return an executor compatible with the shared runtime registry."""

    return ArithmeticSchedulerAdapterV1(
        producer_id=producer_id,
        branch_id=branch_id,
        scheduler=scheduler,
    )


__all__ = ["ArithmeticSchedulerAdapterV1", "adapt_scheduler_v1"]
