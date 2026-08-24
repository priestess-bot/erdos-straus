from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_high_support_c1_direct_cofactor_return.py"
SPEC = importlib.util.spec_from_file_location(
    "type_i_f2_high_support_c1_direct_cofactor_return", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2HighSupportC1DirectReturnTests(unittest.TestCase):
    def test_stored_receipt_replays(self) -> None:
        receipt = MODULE.verify()
        self.assertEqual(receipt["conclusion"]["paid_E5_direct_cofactor"], "EMPTY")

    def test_all_controls_are_exact_returns(self) -> None:
        receipt = MODULE.build_receipt()
        self.assertEqual(len(receipt["controls"]), 5)
        for row in receipt["controls"]:
            with self.subTest(prime=row["p"]):
                self.assertEqual(row["h"], 0)
                self.assertEqual(row["c"], 1)
                self.assertEqual(row["t"], 1)
                self.assertEqual(row["A_C"], row["A"])
                self.assertEqual(row["R_T"], row["R"])
                self.assertEqual(row["K_T"], row["A"])

    def test_positive_phase_barrier_is_strict(self) -> None:
        for prime in (73, 97, 193, 241, 313):
            with self.subTest(prime=prime):
                MODULE.verify_positive_phase_barrier(prime)


if __name__ == "__main__":
    unittest.main()
