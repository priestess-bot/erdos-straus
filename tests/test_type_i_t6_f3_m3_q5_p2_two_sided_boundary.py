from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_m3_q5_p2_two_sided_boundary.py"
SPEC = importlib.util.spec_from_file_location("f3_m3_q5_p2_two_sided_boundary", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TypeIT6F3M3Q5P2TwoSidedBoundaryTests(unittest.TestCase):
    def test_two_sided_p2_control_is_unpaid_rechart(self) -> None:
        result = MODULE.two_sided_control()
        self.assertEqual(result["p"], 73)
        self.assertGreater(result["E_left"], 1)
        self.assertGreater(result["E_right"], 1)
        self.assertEqual(result["multiplier"] % (73 * 73), 1)
        self.assertEqual(result["cofactor"], 72)
        self.assertGreater(result["rho_prime"], result["rho"])
        self.assertFalse(result["direct_rechart_is_strict"])

    def test_first_child_multiplier_is_not_endpoint_invariant(self) -> None:
        result = MODULE.object_separation_control()
        self.assertNotEqual(result["same_chart_multiplier_mod_p"], 1)
        self.assertLess(result["same_chart_cofactor"], result["p"] - 1)

    def test_malformed_endpoint_is_rejected(self) -> None:
        self.assertTrue(MODULE.malformed_endpoint_control())

    def test_status_is_explicitly_arithmetic_only(self) -> None:
        result = MODULE.verify()
        self.assertEqual(result["status"], "ARITHMETIC_CONTROL_ONLY_P2_RECHART_UNPAID")
        self.assertFalse(result["two_sided"]["fixture_is_actual_persistent_m3_q5"])


if __name__ == "__main__":
    unittest.main()
