#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "f1-reachable-state-exhaustion-v1.json"
FRONTIER = ROOT / "data" / "t6-proof-frontier-v3.json"

EXPECTED_FAMILIES = [
    "direct_terminal_leaf", "initial_core_root", "generic_nontrivial_marked_state",
    "type_ii_relation_f_endpoint", "type_ii_relation_g_endpoint",
    "t2_v1_atomic_pending_target", "h4_non_v1_branch_or_descendant",
    "c8_terminal_first_surviving_parent", "type_i_c2_19_macro_target",
    "proper_root_stutter_k_one", "proper_root_stutter_k_gt_one",
    "type_i_a_one_overflow", "type_i_high_support_sink",
    "type_i_low_support_persistent_overflow", "type_i_a_gt_one_overflow_residual",
    "type_i_full_carrier_post_g",
]
EXPECTED_GATES = ["root_serializer_nonterminal_output", "admitted_verified_edge_target"]


def audit():
    errors = []
    m = json.loads(MANIFEST.read_text())
    f = json.loads(FRONTIER.read_text())
    if m.get("baseline") != "d3b3b6a": errors.append("wrong baseline")
    if m.get("status") != "CLOSED_CONTRACT_LEVEL": errors.append("F1 not closed at contract level")
    if m.get("registered_family_count") != 16: errors.append("family count changed")
    if m.get("registered_edge_producer_count") != 15: errors.append("edge producer count changed")
    if m.get("enqueue_gate_count") != 2: errors.append("enqueue gate count changed")
    if m.get("family_registry") != EXPECTED_FAMILIES: errors.append("family registry drift")
    if m.get("producer_exhaustion", {}).get("gates") != EXPECTED_GATES: errors.append("producer gate drift")
    if m.get("normalizer", {}).get("mode") != "ordered_first_match": errors.append("normalizer no longer deterministic first-match")
    if m.get("normalizer", {}).get("cached_owner_is_input") is not False: errors.append("cached owner became an input")
    if m.get("legacy_o1", {}).get("reachable_state_classification") != "CLOSED_BY_F1": errors.append("O1 classification component not closed")
    if m.get("legacy_o1", {}).get("classified_family_exit_totality") != "OPEN_UNDER_F2_F3": errors.append("O1 exit component overstated")
    if f.get("F1", {}).get("status") != "CLOSED_CONTRACT_LEVEL": errors.append("frontier F1 mismatch")
    if f.get("F2", {}).get("status") != "OPEN": errors.append("F2 must remain open")
    if f.get("F3", {}).get("status") != "OPEN": errors.append("F3 must remain open")
    if f.get("T6_GLOBAL_SELECTOR_TOTALITY") != "OPEN": errors.append("T6 must remain open")
    return errors


if __name__ == "__main__":
    errors = audit()
    if errors:
        print("FAIL")
        for e in errors: print("-", e)
        raise SystemExit(1)
    print("PASS: F1 proof boundary is internally consistent")
    print("families=16 edge_producers=15 enqueue_gates=2 F2=OPEN F3=OPEN T6=OPEN")
