from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "pre_t6_contract_kernel_audit.py"
SPEC = importlib.util.spec_from_file_location("pre_t6_contract_kernel_audit", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError(f"cannot load audit module from {MODULE_PATH}")
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


def load_json(relative: str) -> dict[str, Any]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class PreT6ContractKernelAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.kernel = load_json("data/pre-t6-contract-kernel-v1.json")
        self.frontier = load_json("data/t6-proof-frontier-v2.json")

    def run_audit(self, kernel: dict[str, Any] | None = None, frontier: dict[str, Any] | None = None):
        return AUDIT.audit(kernel or self.kernel, frontier or self.frontier)

    def test_frozen_manifests_pass(self) -> None:
        result = self.run_audit()
        self.assertTrue(result.ok, "\n".join(result.errors))

    def test_t6_cannot_be_silently_marked_closed(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["current_status"] = "CLOSED"
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("current_status" in error for error in result.errors))

    def test_registered_edge_cannot_create_nontrivial_mark(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["registered_edges"][0]["target_family_ids"].append("generic_nontrivial_marked_state")
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("creates a nontrivial marked state" in error for error in result.errors))

    def test_arithmetic_reduction_cannot_be_promoted_to_edge(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        item = next(
            item
            for item in frontier["closed_immediate_items"]
            if item["id"] == "T6-M7-P2-RESIDUAL-ISOLATION"
        )
        item["edge_complete"] = True
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("T6-M7-P2-RESIDUAL-ISOLATION.edge_complete" in error for error in result.errors))

    def test_active_gap_cannot_disappear_without_frontier_owner(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["legacy_gap_registry"] = [
            item
            for item in frontier["legacy_gap_registry"]
            if item["id"] != "GAP-O3-C8-OUTGOING"
        ]
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("active legacy gap id set" in error for error in result.errors))

    def test_duplicate_edge_id_is_rejected(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["registered_edges"].append(copy.deepcopy(frontier["registered_edges"][0]))
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("duplicate ids" in error for error in result.errors))

    def test_known_family_cannot_be_substituted_in_edge_surface(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        edge = next(
            item
            for item in frontier["registered_edges"]
            if item["id"] == "q_one_g_full_carrier_phase_root"
        )
        edge["target_family_ids"] = ["type_i_high_support_sink"]
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(
            any(
                "q_one_g_full_carrier_phase_root.target_family_ids" in error
                for error in result.errors
            )
        )

    def test_family_status_cannot_be_silently_upgraded(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        family = next(
            item
            for item in frontier["state_families"]
            if item["id"] == "proper_root_stutter_k_gt_one"
        )
        family["status"] = "CLOSED_BY_UNIVERSAL_SUCCESSOR"
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("state family statuses" in error for error in result.errors))

    def test_initializer_surface_is_frozen(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["initializer"]["targets"] = ["direct_terminal_leaf"]
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("initializer.targets" in error for error in result.errors))

    def test_kernel_cannot_claim_semantic_reachability_exhaustion(self) -> None:
        kernel = copy.deepcopy(self.kernel)
        kernel["scope"]["semantic_reachable_state_exhaustion"] = True
        result = self.run_audit(kernel=kernel)
        self.assertFalse(result.ok)
        self.assertTrue(
            any("semantic_reachable_state_exhaustion" in error for error in result.errors)
        )

    def test_future_family_requires_an_explicit_frontier_revision(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["state_families"].append(
            {"id": "future_atomic_family", "status": "OPEN"}
        )
        frontier["family_frontier_ownership"]["future_atomic_family"] = (
            "T6-F2-NONPROPER-DISPATCH-TOTALITY"
        )
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("state family id set" in error for error in result.errors))

    def test_o4_firewall_cannot_be_silently_globalized(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        frontier["superseded_process_gap"]["status"] = "CLOSED"
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("superseded process gap status" in error for error in result.errors))

    def test_open_acceptance_gate_cannot_be_silently_closed(self) -> None:
        frontier = copy.deepcopy(self.frontier)
        gate = next(
            item
            for item in frontier["acceptance_gates"]
            if item["id"] == "proper_root_physicalization"
        )
        gate["status"] = "ESTABLISHED"
        result = self.run_audit(frontier=frontier)
        self.assertFalse(result.ok)
        self.assertTrue(any("acceptance gate statuses" in error for error in result.errors))

    def test_unknown_family_is_blocked_by_admission_firewall(self) -> None:
        classification = AUDIT.classify_family(self.frontier, "future_unregistered_atomic_family")
        self.assertEqual(classification["classification"], "UNREGISTERED_REJECTED")
        self.assertEqual(classification["owner"], "constructor_admission_firewall")

    def test_open_proper_root_family_has_exact_owner(self) -> None:
        classification = AUDIT.classify_family(self.frontier, "proper_root_stutter_k_gt_one")
        self.assertEqual(classification["classification"], "T6_FRONTIER")
        self.assertEqual(classification["owner"], "T6-F3-PROPER-ROOT-PHYSICALIZATION")

    def test_closed_k_one_family_is_not_promoted_to_global_t6(self) -> None:
        classification = AUDIT.classify_family(self.frontier, "proper_root_stutter_k_one")
        self.assertEqual(classification["classification"], "CLOSED_LOCAL")
        self.assertEqual(classification["owner"], "T6-F3-PROPER-ROOT-PHYSICALIZATION")


if __name__ == "__main__":
    unittest.main()
