from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_r_three_d_fixed_prime_scheduler.py"
SPEC = importlib.util.spec_from_file_location("f2_r_three_d_scheduler", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RThreeFixedPrimeSchedulerTests(unittest.TestCase):
    def test_positive_terminal_row(self) -> None:
        rows = MODULE.table(769)
        row = next(
            row for row in rows
            if (row["A"], row["C"], row["h"]) == (1, 14, 55)
        )
        self.assertEqual(row["outcome"], "TERMINAL")
        self.assertEqual(MODULE.reconstruct(769, row).numerator, 4)

    def test_prime_d_has_no_mixed_row(self) -> None:
        self.assertFalse(
            any(row["outcome"] == "TERMINAL" for row in MODULE.table(2_521))
        )

    def test_focused_replay(self) -> None:
        MODULE.verify()


if __name__ == "__main__":
    unittest.main()
