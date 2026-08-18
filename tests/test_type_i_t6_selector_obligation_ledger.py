import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_t6_selector_obligation_ledger",
    ROOT / "reproductions" / "type_i_t6_selector_obligation_ledger.py",
)
assert SPEC and SPEC.loader
ledger = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ledger
SPEC.loader.exec_module(ledger)


class TypeIT6SelectorObligationLedgerTests(unittest.TestCase):
    def test_current_surface_is_a_verified_open_inventory(self):
        result = ledger.run_ledger()
        self.assertEqual(result["t6_global_selector_totality"], "OPEN")
        self.assertEqual(result["concrete_edge_family_count"], 15)
        self.assertEqual(result["state_family_count"], 16)
        self.assertEqual(result["acceptance_gate_count"], 14)
        self.assertEqual(len(result["minimal_selector_gap_ids"]), 9)
        self.assertIn("O1-INITIAL-ROOT", result["closed_obligation_ids"])
        self.assertNotIn("initial_core_root", result["open_state_family_ids"])
        self.assertIn("proper_root_stutter_k_gt_one", result["open_state_family_ids"])
        self.assertIn("c8_terminal_first_surviving_parent", result["open_state_family_ids"])


if __name__ == "__main__":
    unittest.main()
