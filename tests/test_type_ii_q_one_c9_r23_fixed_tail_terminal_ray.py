from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_c9_r23_fixed_tail_terminal_ray.py"
SPEC = importlib.util.spec_from_file_location("q1_c9_r23_fixed_tail", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class QOneC9R23FixedTailTerminalRayTests(unittest.TestCase):
    def test_terminal_control(self) -> None:
        MODULE.verify()

    def test_off_ray_is_not_promoted(self) -> None:
        with self.assertRaises(AssertionError):
            MODULE.terminal_ray(3049)


if __name__ == "__main__":
    unittest.main()
