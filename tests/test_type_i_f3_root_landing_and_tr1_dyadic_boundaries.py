from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f3_root_landing_and_tr1_dyadic_boundaries.py"
SPEC = importlib.util.spec_from_file_location("f3_root_landing_tr1_dyadic", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RootLandingAndDyadicBoundaryTests(unittest.TestCase):
    def test_static_atomic_countercontrol(self) -> None:
        record = MODULE.root_atomic_countercontrol()
        self.assertEqual(record["A_star"], 590_150)
        self.assertEqual((record["Q_x"], record["Q_y"]), (25, 37))

    def test_dyadic_control_and_companion_residue(self) -> None:
        self.assertEqual(MODULE.dyadic_local_control()["D_star"], 4)
        self.assertEqual(MODULE.atomic_companion_residue_control()["y_mod_p"], 2)

    def test_focused_controls_replay(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
