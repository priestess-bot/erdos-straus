"""Verify the known-transfer boundary audit for single-hit F states."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions/type_i_linear_single_hit_f_budget_transfer_boundary_7.py"
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-single-hit-f-budget-transfer-boundary-7-results.json"
)

spec = importlib.util.spec_from_file_location("single_hit_budget_boundary", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load budget-transfer boundary audit")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class SingleHitBudgetTransferBoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.stored = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_global_boundary_counts(self):
        self.assertEqual(self.actual, self.stored)
        self.assertEqual(self.actual["prime_count"], 7)
        self.assertEqual(self.actual["source_state_count"], 473)
        self.assertEqual(self.actual["known_directed_edge_count"], 1199)
        self.assertEqual(self.actual["boundary_row_count"], 16)
        self.assertEqual(self.actual["boundary_state_count"], 5)
        self.assertEqual(self.actual["boundary_rows_reaching_hit_count"], 0)
        self.assertEqual(self.actual["boundary_states_reaching_hit_count"], 0)
        self.assertEqual(self.actual["boundary_direct_hit_edge_count"], 0)
        self.assertEqual(
            self.actual["boundary_states_in_hit_undirected_component_count"], 1
        )

    def test_boundary_rows_have_positive_overflow_and_no_directed_exit(self):
        for profile in self.actual["profiles"]:
            for row in profile["boundary_rows"]:
                self.assertGreater(int(row["overflow"]), 0)
                self.assertFalse(row["directed_reaches_hit"])
                self.assertEqual(int(row["direct_hit_edge_count"]), 0)


if __name__ == "__main__":
    unittest.main()
