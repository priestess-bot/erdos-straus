#!/usr/bin/env python3
"""Focused field-level controls for the finite T2 v1 receipt grammar.

Arithmetic E1--E4 obligations remain the responsibility of the source-specific verifiers.
"""
from dataclasses import dataclass, replace
from enum import Enum


ADAPTER_VERSION = "atomic_admission_input_v1"
ARMS = {"h4_a1_clean_q_atomic_v1", "c8_double_low_parent_atomic_v1"}


class Kind(str, Enum):
    TERMINAL = "DIRECT_TERMINAL"
    PENDING = "PENDING_DISPATCH_LOCAL_STRICT"
    BOUNDARY = "BOUNDARY"
    REJECT = "REJECT"

@dataclass(frozen=True)
class Receipt:
    adapter_version: str
    arm_id: str
    source_state_id: str
    source_origin_tag: str
    source_tree_scope: str
    source_chart: tuple[int, int, int, int]
    parent_receipt_digest: str
    raw_path_digest: str
    candidate_menu_digest: str
    priority_prefix_digest: str
    priority_prefix_miss: bool
    owner_tuple: tuple[str, ...]
    maximal_payload: tuple[int, int, int, int]
    target_chart: tuple[int, int, int, int]
    target_rechart_digest: str
    local_e5_classification: str
    target_recomputed: bool
    inherited_target_type: bool
    parent_rank: tuple[int, int]
    target_rank: tuple[int, int]
    terminal: bool = False
    double_low: bool = True


def valid_chart(chart: tuple[int, int, int, int]) -> bool:
    if not isinstance(chart, tuple) or len(chart) != 4 or not all(isinstance(value, int) for value in chart):
        return False
    p, R, K, A = chart
    return p > 1 and R > 0 and K > 0 and A > 0 and K % A == 0


def valid_payload(payload: tuple[int, int, int, int], p: int) -> bool:
    if not isinstance(payload, tuple) or len(payload) != 4 or not all(isinstance(value, int) for value in payload):
        return False
    Qx, beta_x, Qy, beta_y = payload
    return bool(Qx > 1 and Qy > 1 and beta_x > 0 and beta_y > 0 and Qx % p and Qy % p)


def valid_rank(rank: tuple[int, int]) -> bool:
    return isinstance(rank, tuple) and len(rank) == 2 and all(isinstance(value, int) and value >= 0 for value in rank)


def classify(r: Receipt):
    if r.adapter_version != ADAPTER_VERSION:
        return Kind.REJECT, "ADAPTER_VERSION_MISMATCH"
    if r.arm_id not in ARMS:
        return Kind.REJECT, "UNSUPPORTED_ARM"
    if not r.source_state_id or not r.parent_receipt_digest:
        return Kind.REJECT, "MISSING_PERSISTENT_SOURCE"
    if not r.source_origin_tag or not r.source_tree_scope:
        return Kind.REJECT, "SOURCE_SCOPE_MISMATCH"
    if not valid_chart(r.source_chart):
        return Kind.REJECT, "SOURCE_CHART_MISMATCH"
    if not r.raw_path_digest:
        return Kind.REJECT, "RAW_PATH_DIGEST_MISMATCH"
    if not r.candidate_menu_digest:
        return Kind.REJECT, "CANDIDATE_MENU_DIGEST_MISMATCH"
    if not r.priority_prefix_digest or not r.priority_prefix_miss:
        return Kind.REJECT, "PRIORITY_PREFIX_NOT_MISS"
    if not r.owner_tuple:
        return Kind.REJECT, "OWNER_MISMATCH"
    if not valid_payload(r.maximal_payload, r.source_chart[0]):
        return Kind.REJECT, "MAXIMAL_PAYLOAD_MISMATCH"
    if not valid_chart(r.target_chart) or not r.target_rechart_digest:
        return Kind.REJECT, "TARGET_RECHART_MISMATCH"
    if r.inherited_target_type:
        return Kind.REJECT, "TARGET_TYPE_INHERITED"
    if not r.target_recomputed:
        return Kind.REJECT, "TARGET_RECHART_MISMATCH"
    if r.terminal:
        if r.local_e5_classification != "TERMINAL_FIRST":
            return Kind.REJECT, "TERMINAL_CLASSIFICATION_MISMATCH"
        return Kind.TERMINAL, "TERMINAL_FIRST"
    if r.local_e5_classification != "LOCAL_DROP":
        return Kind.REJECT, "LOCAL_E5_CLASSIFICATION_MISMATCH"
    if not valid_rank(r.parent_rank) or not valid_rank(r.target_rank):
        return Kind.REJECT, "LOCAL_RANK_FORMAT_MISMATCH"
    if r.arm_id == "c8_double_low_parent_atomic_v1" and not r.double_low:
        return Kind.BOUNDARY, "BOUNDARY_C8_NO_DOUBLE_LOW"
    if r.target_rank >= r.parent_rank:
        return Kind.REJECT, "STANDALONE_STUTTER"
    return Kind.PENDING, "PHASE_LOCAL_STRICT"

def base(arm, parent_rank=(0,72), target_rank=(0,67)):
    return Receipt(
        ADAPTER_VERSION, arm, "source:id", "source:root", "scope:v1", (73, 3, 55, 1),
        "parent:d", "raw:d", "menu:d", "priority:d", True, (arm, "source:id", "path"),
        (2, 1, 5, 1), (73, 7, 128, 2), "target:d", "LOCAL_DROP", True, False,
        parent_rank, target_rank,
    )

def verify():
    strict=base("h4_a1_clean_q_atomic_v1")
    assert classify(strict)==(Kind.PENDING,"PHASE_LOCAL_STRICT")
    assert classify(replace(strict, adapter_version=""))[1]=="ADAPTER_VERSION_MISMATCH"
    assert classify(replace(strict,target_rank=(0,72)))[1]=="STANDALONE_STUTTER"
    assert classify(replace(strict,parent_receipt_digest=""))[1]=="MISSING_PERSISTENT_SOURCE"
    assert classify(replace(strict,source_tree_scope=""))[1]=="SOURCE_SCOPE_MISMATCH"
    assert classify(replace(strict,source_chart=(73, 3, 55, 2)))[1]=="SOURCE_CHART_MISMATCH"
    assert classify(replace(strict,priority_prefix_miss=False))[1]=="PRIORITY_PREFIX_NOT_MISS"
    assert classify(replace(strict,inherited_target_type=True))[1]=="TARGET_TYPE_INHERITED"
    assert classify(replace(strict,maximal_payload=(1, 1, 5, 1)))[1]=="MAXIMAL_PAYLOAD_MISMATCH"
    assert classify(replace(strict,target_rechart_digest=""))[1]=="TARGET_RECHART_MISMATCH"
    assert classify(replace(strict,local_e5_classification=""))[1]=="LOCAL_E5_CLASSIFICATION_MISMATCH"
    assert classify(replace(strict,target_rank=(-1, 67)))[1]=="LOCAL_RANK_FORMAT_MISMATCH"
    c8=base("c8_double_low_parent_atomic_v1",(0,157392),(0,38261))
    assert classify(replace(c8,double_low=False))==(Kind.BOUNDARY,"BOUNDARY_C8_NO_DOUBLE_LOW")
    assert classify(replace(strict,terminal=True,local_e5_classification="TERMINAL_FIRST"))==(Kind.TERMINAL,"TERMINAL_FIRST")
    physical_capacity=1
    demands=[1,1]
    assert all(d<=physical_capacity for d in demands) and sum(demands)>physical_capacity
    print("T2 atomic_admission_input_v1 controls passed")

if __name__=="__main__":
    verify()
