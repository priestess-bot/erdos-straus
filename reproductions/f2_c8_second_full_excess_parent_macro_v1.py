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
import importlib.util
from math import gcd
from pathlib import Path
import sys
from typing import Any, Mapping

import type_i_q_one_full_carrier_d_one_c_eight_double_low_parent_anchored_atomic_macro as parent_macro
import type_i_q_one_full_carrier_d_one_c_eight_full_excess_carry_obstruction as c8

ROOT = Path(__file__).resolve().parents[1]


def _load_common():
    path = ROOT / "scripts" / "t6_persistent_selector_state_v1.py"
    name = "t6_persistent_selector_state_v1_c8_fallback"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


common = _load_common()


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


def producer_rule() -> common.ProducerRuleV1:
    """Return this track's proposed, not-yet-shared producer rule."""
    return common.ProducerRuleV1(
        producer_id=PRODUCER_ID,
        queue_gate=common.ADMITTED_SUCCESSOR,
        branch_ids=frozenset({BRANCH_ID}),
        source_owners=frozenset({"c8_terminal_first_surviving_parent"}),
        target_owners=frozenset({TARGET_OWNER}),
    )


def common_admission(
    receipt: ParentToFinalReceipt, evidence: Mapping[str, str]
) -> common.QueueAdmissionDecisionV1:
    """Project the final chart, not the internal c8 checkpoint, through F1."""
    if set(evidence) != {"E1", "E2", "E3", "E4"} or any(
        not isinstance(value, str) or not value for value in evidence.values()
    ):
        raise ValueError("complete E1-E4 evidence digests are required")
    facts: dict[str, Any] = {
        "major_phase": "TYPEI",
        "endpoint_fiber": "NONE",
        "relation_q": None,
        "provenance_kind": "OVERFLOW",
        "full_carrier_scope": False,
        "atomic_arm": "NONE",
        "dispatch_status": "NONE",
        "proper_root_k": None,
        "is_overflow": True,
        "support_A": receipt.target_support,
        "carrier_M": None,
        "overflow_d": None,
        "chart_R": receipt.target_residual,
        "chart_K": receipt.target_carrier,
        "sink_scc_receipt": False,
        "same_chart_promotion_receipt": False,
    }
    terminal = common.seal_receipt_v1(
        {
            "schema_id": common.TERMINAL_FIRST_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"terminal:c8-second-full:{receipt.parent_state_id}",
            "scope": "complete_parent_and_final_target_terminal_screen",
            "outcome": "MISS",
        }
    )
    source = common.seal_receipt_v1(
        {
            "schema_id": common.SUCCESSOR_RECEIPT_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": f"edge:c8-second-full:{receipt.parent_state_id}",
            "producer_id": PRODUCER_ID,
            "branch_id": BRANCH_ID,
            "root_context": receipt.prime,
            "equation_rank": receipt.prime,
            "target_facts_digest": common.canonical_digest_v1(facts),
            "terminal_first_digest": terminal["digest"],
            "status": "VERIFIED_EDGE",
            "parent_state_id": receipt.parent_state_id,
            "E1": True,
            "E2": True,
            "E3": True,
            "E4": True,
            "E5": True,
            "T5_ticket": "LOCAL_DROP",
        }
    )
    mark = common.seal_receipt_v1(
        {
            "schema_id": common.MARK_SCHEMA_ID,
            "schema_version": 1,
            "receipt_id": "mark:c8-second-full-root-sol",
            "kind": common.ROOT_SOL,
            "root_context": receipt.prime,
            "equation_rank": receipt.prime,
        }
    )
    raw = {
        "schema_id": common.STATE_SCHEMA_ID,
        "schema_version": common.STATE_SCHEMA_VERSION,
        "state_id": "pending-content-address",
        "artifact_class": "persistent_state",
        "consumer": "t6_selector",
        "queue_gate": common.ADMITTED_SUCCESSOR,
        "producer_id": PRODUCER_ID,
        "branch_id": BRANCH_ID,
        "parent_state_id": receipt.parent_state_id,
        "root_context": receipt.prime,
        "equation_rank": receipt.prime,
        "mark": mark,
        "terminal_first": terminal,
        "source_receipt": source,
        "facts": facts,
    }
    raw["state_id"] = common.build_state_id_v1(raw)
    rule = producer_rule()
    return common.reject_before_persistent_queue_v1(raw, {PRODUCER_ID: rule})


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
    decision = common_admission(
        receipt,
        {
            "E1": "persistent-parent-and-c8-p-source-path",
            "E2": "unique-Q-and-canonical-final-chart",
            "E3": "target-local-terminal-hit-F-G-recomputation",
            "E4": "identity-Sol-p-lift",
        },
    )
    if not (decision.accepted and decision.owner == TARGET_OWNER):
        raise AssertionError("c8 fallback failed common admission")
    print(
        "verified c8 second-full-excess parent macro: internal 8->4198 rise, "
        "persistent parent 157392->4198 strict N7 drop"
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
