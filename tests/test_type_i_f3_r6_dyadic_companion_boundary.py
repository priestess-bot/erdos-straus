from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f3_r6_dyadic_companion_boundary.py"
SPEC = importlib.util.spec_from_file_location("f3_r6_dyadic_companion", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class R6DyadicCompanionBoundaryTests(unittest.TestCase):
    def test_scope_controls(self) -> None:
        MODULE.verify_controls()


if __name__ == "__main__":
    unittest.main()
