from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_high_support_r_three_raw_menu_boundary.py"
SPEC = importlib.util.spec_from_file_location("f2_r_three_raw_menu", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RThreeRawMenuTests(unittest.TestCase):
    def test_prime_d_control_has_only_the_anchor(self) -> None:
        menu = MODULE.raw_menu(2_521)
        self.assertEqual(menu["D_factors"], (5_039,))
        self.assertEqual(menu["children"], ((1, 2, 1),))

    def test_composite_d_control_has_non_anchor_children(self) -> None:
        menu = MODULE.raw_menu(118_801)
        self.assertEqual(menu["D_factors"], (53, 4_483))
        self.assertTrue(all(child[0] > 1 for child in menu["children"]))

    def test_fixed_controls_replay(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
