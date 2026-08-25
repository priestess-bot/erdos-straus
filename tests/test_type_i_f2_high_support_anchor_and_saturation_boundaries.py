from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_high_support_anchor_and_saturation_boundaries.py"
SPEC = importlib.util.spec_from_file_location("f2_high_support_anchor_boundaries", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class HighSupportAnchorAndSaturationBoundaryTests(unittest.TestCase):
    def test_r3_anchor_is_not_a_t5_reentry(self) -> None:
        row = MODULE.r3_anchor_no_reentry(73)
        self.assertGreaterEqual(row["charged_outer"], 1)
        self.assertEqual(row["R"], 223)

    def test_spf_saturation_is_not_fixed_n_or_same_chart_full_excess(self) -> None:
        row = MODULE.saturation_barrier(73, 1305, 2, 2)
        self.assertNotEqual((row["support"] * row["d"]) % row["promoted"], 0)
        self.assertNotEqual(row["K"] % row["lcm_support"], 0)

    def test_controls(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
