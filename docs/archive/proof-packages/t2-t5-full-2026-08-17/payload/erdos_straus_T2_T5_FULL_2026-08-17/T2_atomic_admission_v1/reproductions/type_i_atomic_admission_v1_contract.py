#!/usr/bin/env python3
from dataclasses import dataclass, replace
from enum import Enum

class Kind(str, Enum):
    TERMINAL = "DIRECT_TERMINAL"
    PENDING = "PENDING_DISPATCH_LOCAL_STRICT"
    BOUNDARY = "BOUNDARY"
    REJECT = "REJECT"

@dataclass(frozen=True)
class Receipt:
    arm_id: str
    source_state_id: str
    source_tree_scope: str
    parent_receipt_digest: str
    raw_path_digest: str
    candidate_menu_digest: str
    priority_prefix_digest: str
    priority_prefix_miss: bool
    owner_tuple: tuple[str, ...]
    target_recomputed: bool
    inherited_target_type: bool
    parent_rank: tuple[int, int]
    target_rank: tuple[int, int]
    terminal: bool = False
    double_low: bool = True

def classify(r: Receipt):
    if r.arm_id not in {"h4_a1_clean_q_atomic_v1", "c8_double_low_parent_atomic_v1"}:
        return Kind.REJECT, "UNSUPPORTED_ARM"
    if not r.source_state_id or not r.parent_receipt_digest:
        return Kind.REJECT, "MISSING_PERSISTENT_SOURCE"
    if not r.source_tree_scope:
        return Kind.REJECT, "SOURCE_SCOPE_MISMATCH"
    if not r.raw_path_digest:
        return Kind.REJECT, "RAW_PATH_DIGEST_MISMATCH"
    if not r.candidate_menu_digest:
        return Kind.REJECT, "CANDIDATE_MENU_DIGEST_MISMATCH"
    if not r.priority_prefix_digest or not r.priority_prefix_miss:
        return Kind.REJECT, "PRIORITY_PREFIX_NOT_MISS"
    if not r.owner_tuple:
        return Kind.REJECT, "OWNER_MISMATCH"
    if r.inherited_target_type:
        return Kind.REJECT, "TARGET_TYPE_INHERITED"
    if not r.target_recomputed:
        return Kind.REJECT, "TARGET_RECHART_MISMATCH"
    if r.terminal:
        return Kind.TERMINAL, "TERMINAL_FIRST"
    if r.arm_id == "c8_double_low_parent_atomic_v1" and not r.double_low:
        return Kind.BOUNDARY, "BOUNDARY_C8_NO_DOUBLE_LOW"
    if r.target_rank >= r.parent_rank:
        return Kind.REJECT, "STANDALONE_STUTTER"
    return Kind.PENDING, "PHASE_LOCAL_STRICT"

def base(arm, parent_rank=(0,72), target_rank=(0,67)):
    return Receipt(arm,"source:id","scope:v1","parent:d","raw:d","menu:d","priority:d",True,
                   (arm,"source:id","path"),True,False,parent_rank,target_rank)

def verify():
    strict=base("h4_a1_clean_q_atomic_v1")
    assert classify(strict)==(Kind.PENDING,"PHASE_LOCAL_STRICT")
    assert classify(replace(strict,target_rank=(0,72)))[1]=="STANDALONE_STUTTER"
    assert classify(replace(strict,parent_receipt_digest=""))[1]=="MISSING_PERSISTENT_SOURCE"
    assert classify(replace(strict,source_tree_scope=""))[1]=="SOURCE_SCOPE_MISMATCH"
    assert classify(replace(strict,priority_prefix_miss=False))[1]=="PRIORITY_PREFIX_NOT_MISS"
    assert classify(replace(strict,inherited_target_type=True))[1]=="TARGET_TYPE_INHERITED"
    c8=base("c8_double_low_parent_atomic_v1",(0,157392),(0,38261))
    assert classify(replace(c8,double_low=False))==(Kind.BOUNDARY,"BOUNDARY_C8_NO_DOUBLE_LOW")
    assert classify(replace(strict,terminal=True))==(Kind.TERMINAL,"TERMINAL_FIRST")
    physical_capacity=1
    demands=[1,1]
    assert all(d<=physical_capacity for d in demands) and sum(demands)>physical_capacity
    print("T2 atomic_admission_input_v1 controls passed")

if __name__=="__main__":
    verify()
