#!/usr/bin/env python3
"""Deterministic terminal/double-low/OTHER dispatch for actual c8 parents.

The dispatcher never treats the logical complement of double-low as a target.
Its OTHER branch names the independently proved second-full-excess parent
macro.  A capacity-one optional double-low receipt is deliberately routed to
OTHER so this producer does not create the high-support C1 local minimum.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence


class C8Disposition(str, Enum):
    TERMINAL = "TERMINAL"
    DOUBLE_LOW = "DOUBLE_LOW_VERIFIED_SUCCESSOR"
    OTHER = "OTHER_VERIFIED_SUCCESSOR"


@dataclass(frozen=True)
class TerminalFirstReceipt:
    parent_state_id: str
    policy_digest: str
    outcome: str
    certificate_digest: str | None


@dataclass(frozen=True)
class DoubleLowReceipt:
    parent_state_id: str
    raw_prime: int
    source_path_digest: str
    direct_capacity: int
    split_capacity: int
    e1_e5_verified: bool
    common_reentry_verified: bool


@dataclass(frozen=True)
class C8Dispatch:
    disposition: C8Disposition
    parent_state_id: str
    selected_raw_prime: int | None
    target_constructor: str | None
    reason: str


def _valid_terminal(receipt: TerminalFirstReceipt) -> None:
    if not receipt.parent_state_id or not receipt.policy_digest:
        raise ValueError("MALFORMED_TERMINAL_FIRST_RECEIPT")
    if receipt.outcome not in {"HIT", "MISS"}:
        raise ValueError("UNKNOWN_TERMINAL_FIRST_OUTCOME")
    if receipt.outcome == "HIT" and not receipt.certificate_digest:
        raise ValueError("TERMINAL_CERTIFICATE_MISSING")
    if receipt.outcome == "MISS" and receipt.certificate_digest is not None:
        raise ValueError("TERMINAL_MISS_HAS_CERTIFICATE")


def _qualified_double_low(
    parent_state_id: str, candidate: DoubleLowReceipt
) -> bool:
    return bool(
        candidate.parent_state_id == parent_state_id
        and isinstance(candidate.raw_prime, int)
        and candidate.raw_prime > 1
        and candidate.source_path_digest
        and 1 <= candidate.direct_capacity <= 7
        and 2 <= candidate.split_capacity <= 7
        and candidate.e1_e5_verified
        and candidate.common_reentry_verified
    )


def dispatch_c8_outgoing(
    terminal: TerminalFirstReceipt,
    double_low_candidates: Sequence[DoubleLowReceipt],
) -> C8Dispatch:
    """Return one disjoint disposition under a fixed lexicographic policy."""
    _valid_terminal(terminal)
    if terminal.outcome == "HIT":
        return C8Dispatch(
            C8Disposition.TERMINAL,
            terminal.parent_state_id,
            None,
            None,
            "COMPLETE_TERMINAL_FIRST_HIT",
        )
    qualified = sorted(
        (
            candidate
            for candidate in double_low_candidates
            if _qualified_double_low(terminal.parent_state_id, candidate)
        ),
        key=lambda row: (row.raw_prime, row.source_path_digest),
    )
    if qualified:
        selected = qualified[0]
        return C8Dispatch(
            C8Disposition.DOUBLE_LOW,
            terminal.parent_state_id,
            selected.raw_prime,
            "AtomicPendingTargetV1(C8_DOUBLE_LOW)",
            "LEAST_FULLY_VERIFIED_DOUBLE_LOW_RECEIPT",
        )
    return C8Dispatch(
        C8Disposition.OTHER,
        terminal.parent_state_id,
        None,
        "C8SecondFullExcessParentMacroV1",
        "UNIVERSAL_PARENT_ANCHORED_FALLBACK",
    )


__all__ = [
    "C8Dispatch",
    "C8Disposition",
    "DoubleLowReceipt",
    "TerminalFirstReceipt",
    "dispatch_c8_outgoing",
]
