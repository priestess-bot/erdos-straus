#!/usr/bin/env python3
"""Verify the parent-to-final c8 second-full-excess fallback macro.

The existing local theorem correctly says that the c8 checkpoint move raises
capacity from 8.  This verifier compares the actual persistent q=1 d=1 parent
with the final target instead: the parent capacity is p-1 and the congruence
75*c=64 (mod p) forces 9 <= c <= p-2.  The c8 checkpoint is macro-internal.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from math import gcd

import type_i_q_one_full_carrier_d_one_c_eight_double_low_parent_anchored_atomic_macro as parent_macro
import type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction as c8

PRODUCER_ID = "f2_c8_second_full_excess_final_target_v1"
BRANCH_ID = "c8_second_full_excess_final_target"
TARGET_OWNER = "type_i_a_gt_one_overflow_residual"


@dataclass(frozen=True)
class ParentToFinalReceipt:
    prime: int
    parent_state_id: str
    source_tree_scope: str
    parent_support: int
    parent_capacity: int
    checkpoint_support: int
    checkpoint_capacity: int
    full_excess_q: int
    target_support: int
    target_capacity: int
    target_carrier: int
    target_residual: int
    parent_n7: tuple[int, ...]
    target_n7: tuple[int, ...]


@dataclass(frozen=True)
class TerminalControl:
    prime: int
    outcome: str
    denominators: tuple[int, int, int] | None
    scope: str


@dataclass(frozen=True)
class FallbackAdmissionProposal:
    status: str
    required_producer_id: str
    required_branch_id: str
    required_source_owner: str
    required_target_owner: str
    target_n7: tuple[int, ...]
    required_evidence: tuple[str, ...]


def n7(prime: int, support: int, capacity: int, eta_p: int = 0) -> tuple[int, ...]:
    boundary = (prime - 1) ** 2 // 4
    return (prime, 2, 4, boundary // support, capacity, eta_p, 0)


def parent_to_final_receipt(s: int, *, parent_eta_p: int = 0) -> ParentToFinalReceipt:
    """Rebuild the persistent parent, c8 checkpoint and deterministic final target."""
    if parent_eta_p < 0:
        raise ValueError("parent eta must be nonnegative")
    checkpoint = c8.c_eight_target(s)
    c8.gcd_boundary(checkpoint)
    parent = parent_macro.c_eight_checkpoint(s)
    p, m, q = checkpoint.prime, checkpoint.M, checkpoint.Q
    target_support = m * q
    target_capacity = c8.capacity_increase(checkpoint)
    target_carrier = target_support * target_capacity
    numerator = 4 * target_carrier - 1
    target_residual, remainder = divmod(numerator, p)
    parent_support = int(parent["parent_support"])
    parent_capacity = p - 1
    parent_rank = n7(p, parent_support, parent_capacity, parent_eta_p)
    target_rank = n7(p, target_support, target_capacity)

    if not (
        p >= 4_129
        and checkpoint.K == 8 * m
        and checkpoint.R - 1 == 2 * q
        and q % 2 == 1
        and gcd(m, q) == 1
        and gcd(p, m * q) == 1
        and checkpoint.R % 4 == 3
        and target_support == m * q > m
        and 75 * target_capacity % p == 64
        and 9 <= target_capacity <= p - 2
        and remainder == 0
        and p * target_residual + 1 == 4 * target_carrier
        and target_residual % 4 == 3
        and target_residual > p
        and parent_capacity == p - 1
        and target_rank < parent_rank
        and str(parent["parent_state_id"])
        and str(parent["scope"])
    ):
        raise AssertionError("c8 parent-to-final fallback macro changed")

    return ParentToFinalReceipt(
        prime=p,
        parent_state_id=str(parent["parent_state_id"]),
        source_tree_scope=str(parent["scope"]),
        parent_support=parent_support,
        parent_capacity=parent_capacity,
        checkpoint_support=m,
        checkpoint_capacity=8,
        full_excess_q=q,
        target_support=target_support,
        target_capacity=target_capacity,
        target_carrier=target_carrier,
        target_residual=target_residual,
        parent_n7=parent_rank,
        target_n7=target_rank,
    )


def symbolic_capacity_bounds(prime: int, capacity: int) -> bool:
    """Check the short contradiction proving 9 <= c <= p-2."""
    if not (prime >= 4_129 and 1 <= capacity < prime):
        return False
    if (75 * capacity - 64) % prime:
        return False
    low_excluded = all(0 < 75 * c - 64 < prime for c in range(1, 9))
    parent_stutter_excluded = (75 * (prime - 1) - 64) % prime != 0
    return low_excluded and parent_stutter_excluded and 9 <= capacity <= prime - 2


def terminal_control(s: int) -> TerminalControl:
    """Return known terminal evidence; unknown controls are not silently a MISS."""
    target = c8.c_eight_target(s)
    if target.prime == 157_393:
        denominators = (39_375, 57_920_624, 2_280_624_570_000)
        if Fraction(4, target.prime) != sum(
            (Fraction(1, value) for value in denominators), Fraction(0, 1)
        ):
            raise AssertionError("stored c8 terminal control changed")
        return TerminalControl(target.prime, "HIT", denominators, "gap-seven-control")
    return TerminalControl(target.prime, "UNRESOLVED", None, "no-terminal-control")


def propose_after_actual_miss(
    receipt: ParentToFinalReceipt,
) -> FallbackAdmissionProposal:
    """State shared-admission requirements without granting a queue right."""
    return FallbackAdmissionProposal(
        status="PROPOSAL_NOT_ACTIVE_ACTUAL_MISS_AND_SHARED_ADMISSION_REQUIRED",
        required_producer_id=PRODUCER_ID,
        required_branch_id=BRANCH_ID,
        required_source_owner="c8_terminal_first_surviving_parent",
        required_target_owner=TARGET_OWNER,
        target_n7=receipt.target_n7,
        required_evidence=(
            "admitted_c8_parent_trace",
            "complete_terminal_first_miss_receipt",
            "parent_to_checkpoint_path_receipt",
            "canonical_p_source_complete_excess_receipt",
            "target_local_terminal_hit_F_G_receipt",
            "shared_producer_registry_entry",
            "shared_common_gate_acceptance",
            "downstream_overflow_totality",
        ),
    )


def verify() -> None:
    receipt = parent_to_final_receipt(3_279, parent_eta_p=7)
    if not (
        receipt.prime == 157_393
        and receipt.parent_support == 17_031_063_699
        and receipt.checkpoint_support == 580_110_575_661_140_706_117
        and receipt.full_excess_q == 58_971_931_474_577_975
        and receipt.target_support
        == 34_210_241_115_566_771_375_771_444_426_075_973_075
        and receipt.target_capacity == 4_198
        and receipt.target_residual
        == 3_649_834_292_583_515_308_444_175_375_033_627_543
        and receipt.parent_n7[4:] == (157_392, 7, 0)
        and receipt.target_n7[4:] == (4_198, 0, 0)
        and symbolic_capacity_bounds(receipt.prime, receipt.target_capacity)
    ):
        raise AssertionError("stored c8 parent-to-final fallback control changed")
    terminal = terminal_control(3_279)
    proposal = propose_after_actual_miss(receipt)
    if not (
        terminal.outcome == "HIT"
        and terminal.denominators is not None
        and proposal.status.startswith("PROPOSAL_NOT_ACTIVE")
        and proposal.required_target_owner == TARGET_OWNER
    ):
        raise AssertionError("c8 terminal/proposal boundary changed")
    print(
        "verified c8 second-full-excess parent macro: internal 8->4198 rise, "
        "persistent parent 157392->4198 strict N7 drop; stored control is terminal"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        parser.error("pass --verify")
    verify()


if __name__ == "__main__":
    main()
