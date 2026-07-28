"""Regression tests for the exact cyclic-log finite-box boundary."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_cyclic_log_box_separation_64214329.py"
ARTIFACT = ROOT / "reproductions" / "type-i-linear-cyclic-log-box-separation-64214329-359.json"
SPEC = importlib.util.spec_from_file_location("cyclic_log_box_boundary", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load cyclic-log boundary script")
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class CyclicLogBoxBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = boundary.run_audit()
        cls.expected = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_artifact_rebuilds_exactly(self):
        self.assertEqual(self.actual, self.expected)

    def test_subgroup_visibility_is_strictly_weaker_than_finite_alignment(self):
        self.assertEqual(self.actual["raw_shared_pullback_count"], 60)
        self.assertEqual(self.actual["subgroup_shared_pullback_count"], 60)
        self.assertEqual(self.actual["finite_shared_alignment_count"], 0)
        self.assertEqual(
            self.actual["affine_finite_difference_residues"], [1, 2, 19, 180, 189]
        )

    def test_affine_log_box_has_large_exact_overflow(self):
        self.assertEqual(self.actual["primitive_root"], 7)
        self.assertEqual(self.actual["unit_group_order"], 358)
        self.assertEqual(
            self.actual["affine_discrete_logs"], {"19": 157, "135173": 201}
        )
        self.assertEqual(self.actual["minimum_overflow"], "12")
        self.assertEqual(self.actual["maximum_overflow"], "77")
        self.assertEqual(sum(self.actual["overflow_distribution"].values()), 60)


if __name__ == "__main__":
    unittest.main()
