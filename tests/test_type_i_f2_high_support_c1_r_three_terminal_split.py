from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_f2_high_support_c1_r_three_terminal_split.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_f2_high_support_c1_r_three_terminal_split", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2HighSupportC1RThreeTerminalSplitTests(unittest.TestCase):
    def test_stored_split_replays(self) -> None:
        receipt = MODULE.verify()
        self.assertEqual(
            receipt["conclusion"]["two_mod_three_factor_of_N"],
            "DIRECT_TYPE_I_TERMINAL",
        )

    def test_terminal_controls_are_direct_certificates(self) -> None:
        for prime, factor, expected in ((73, 5, (20, 220, 4015)), (313, 5, (80, 3760, 73555))):
            row = MODULE.terminal_certificate(prime, factor)
            with self.subTest(prime=prime):
                self.assertEqual((row["x"], row["y"], row["z"]), expected)

    def test_g_controls_are_not_global_no_solution_claims(self) -> None:
        for prime in (97, 241):
            with self.subTest(prime=prime):
                row = MODULE.r3_g_residual(prime)
                self.assertEqual(row["classification"], "R3_G_RESIDUAL")


if __name__ == "__main__":
    unittest.main()
