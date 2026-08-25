from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_f2_high_support_determinant_dual_absorb_handoff.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_f2_high_support_determinant_dual_absorb_handoff", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2HighSupportDeterminantDualAbsorbHandoffTests(unittest.TestCase):
    def test_stored_receipt_replays(self) -> None:
        receipt = MODULE.verify()
        self.assertEqual(receipt["conclusion"]["E1_E3_reentry"], "OPEN")

    def test_controls_select_a_low_canonical_chart(self) -> None:
        for prime, support, cofactor in ((73, 1369, 1), (73, 1305, 2), (193, 9323, 9)):
            row = MODULE.dual_row(prime, support, cofactor)
            with self.subTest(prime=prime, cofactor=cofactor):
                self.assertGreaterEqual(row["R_selected"], 3)
                self.assertLess(row["R_selected"], prime)
                self.assertEqual(
                    prime * row["R_selected"] + 1,
                    4 * row["K_selected"],
                )

    def test_low_chart_is_not_promoted_to_admission(self) -> None:
        receipt = MODULE.build_receipt()
        self.assertEqual(
            receipt["conclusion"]["E5"],
            "CHARGED_TO_ABSORB_PHASE_DROP_RELATIVE_TO_ADMISSION",
        )
        self.assertEqual(receipt["conclusion"]["E1_E3_reentry"], "OPEN")


if __name__ == "__main__":
    unittest.main()
