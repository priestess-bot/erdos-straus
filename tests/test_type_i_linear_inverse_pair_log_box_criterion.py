"""Regression tests for the inverse-pair log-box formula."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_inverse_pair_log_box_criterion.py"
ARTIFACT = ROOT / "reproductions" / "type-i-linear-inverse-pair-log-box-criterion-results.json"
SPEC = importlib.util.spec_from_file_location("inverse_pair_log_box", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load inverse-pair criterion script")
criterion = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = criterion
SPEC.loader.exec_module(criterion)


class InversePairLogBoxCriterionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = criterion.run_audit()
        cls.expected = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_artifact_rebuilds_exactly(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["case_count"], 2)
        self.assertEqual(self.actual["inverse_pair_candidate_count"], 2)

    def test_both_rows_have_empty_finite_box_intersection(self):
        for profile in self.actual["profiles"]:
            self.assertEqual(profile["finite_target_intersection_count"], 0)
            self.assertEqual(profile["q_inverse_relation"], 1)

    def test_second_row_exceeds_the_first_overflow_boundary(self):
        first, second = self.actual["profiles"]
        self.assertEqual(first["maximum_overflow"], "77")
        self.assertEqual(second["minimum_overflow"], "99")
        self.assertEqual(second["maximum_overflow"], "99")


if __name__ == "__main__":
    unittest.main()
