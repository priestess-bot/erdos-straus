from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_q_one_c8_terminal_prefix_two_ray_reduction.py"
SPEC = importlib.util.spec_from_file_location("c8_two_ray_reduction", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class C8TerminalPrefixTwoRayReductionTests(unittest.TestCase):
    def test_two_base_rays(self) -> None:
        MODULE.verify()

    def test_excluded_residue_is_rejected(self) -> None:
        with self.assertRaises(AssertionError):
            MODULE.ray_from_u(5)


if __name__ == "__main__":
    unittest.main()
