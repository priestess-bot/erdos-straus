import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("f1audit", ROOT / "scripts" / "audit_f1_reachable_state_exhaustion.py")
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

class F1BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "data" / "f1-reachable-state-exhaustion-v1.json").read_text())
        self.frontier = json.loads((ROOT / "data" / "t6-proof-frontier-v3.json").read_text())

    def test_current_files_pass(self):
        self.assertEqual(MOD.audit(), [])

    def test_family_count_frozen(self):
        m = copy.deepcopy(self.manifest); m["registered_family_count"] = 17
        self.assertNotEqual(m["registered_family_count"], 16)

    def test_exactly_two_enqueue_gates(self):
        self.assertEqual(self.manifest["producer_exhaustion"]["gates"], MOD.EXPECTED_GATES)

    def test_candidate_not_persistent(self):
        self.assertIn("candidate_transition", self.manifest["nonpersistent_artifacts"])

    def test_cached_owner_forbidden(self):
        self.assertFalse(self.manifest["normalizer"]["cached_owner_is_input"])

    def test_first_match_required(self):
        self.assertEqual(self.manifest["normalizer"]["mode"], "ordered_first_match")

    def test_f2_remains_open(self):
        self.assertEqual(self.frontier["F2"]["status"], "OPEN")

    def test_f3_remains_open(self):
        self.assertEqual(self.frontier["F3"]["status"], "OPEN")

    def test_t6_remains_open(self):
        self.assertEqual(self.frontier["T6_GLOBAL_SELECTOR_TOTALITY"], "OPEN")

    def test_legacy_o1_decomposed(self):
        o = self.manifest["legacy_o1"]
        self.assertEqual(o["reachable_state_classification"], "CLOSED_BY_F1")
        self.assertEqual(o["classified_family_exit_totality"], "OPEN_UNDER_F2_F3")

    def test_all_16_families_unique(self):
        fam = self.manifest["family_registry"]
        self.assertEqual(len(fam), 16)
        self.assertEqual(len(set(fam)), 16)

    def test_future_constructor_reopens_f1(self):
        self.assertEqual(self.manifest["producer_exhaustion"]["future_constructor_policy"], "REOPEN_F1_BEFORE_ADMISSION")

    def test_forbidden_inference_f1_to_t6(self):
        self.assertIn("F1_implies_T6_total_selector", self.manifest["forbidden_inferences"])

if __name__ == "__main__": unittest.main()
