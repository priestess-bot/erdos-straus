from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_runtime_terminal_scope_boundary.py"
SPEC = importlib.util.spec_from_file_location("q1_runtime_terminal_scope_boundary", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class QOneRuntimeTerminalScopeBoundaryTests(unittest.TestCase):
    def test_gap_eleven_terminal_is_exact(self) -> None:
        record = MODULE.bradford_gap_eleven_control()
        self.assertEqual((record["p"], record["m"], record["d"]), (241_441, 11, 1_083))

    def test_local_runtime_miss_is_not_complete_terminal_miss(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
