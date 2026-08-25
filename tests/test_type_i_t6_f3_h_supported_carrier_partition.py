from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_t6_f3_h_supported_carrier_partition.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_t6_f3_h_supported_carrier_partition", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
PARTITION = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = PARTITION
SPEC.loader.exec_module(PARTITION)


class HSupportedCarrierPartitionTests(unittest.TestCase):
    def test_r4_has_root_menu_eligibility_and_transverse_factor(self) -> None:
        row = PARTITION.classify(PARTITION.fixture())
        self.assertEqual(row["root_carrier"], 31)
        self.assertEqual(row["transverse_factor_candidate"], 13)
        self.assertFalse(row["integer_raw_occurrence_bound"])
        self.assertEqual(row["E1_status"], "OPEN")
        self.assertEqual(row["residual_code"], PARTITION.R4_RESIDUAL)
        self.assertFalse(row["recursive"])

    def test_r6_modulo_three_partition(self) -> None:
        m_one = PARTITION.classify(
            PARTITION.fixture(
                route_code=PARTITION.R6,
                h=3 * 7 * 13,
                m=4,
                k=7 * 13,
                d_star=17,
            )
        )
        m_zero = PARTITION.classify(
            PARTITION.fixture(
                route_code=PARTITION.R6,
                h=3 * 7 * 13,
                m=6,
                k=3 * 7,
                d_star=11,
            )
        )
        k_three = PARTITION.classify(
            PARTITION.fixture(
                route_code=PARTITION.R6,
                h=3 * 7,
                m=6,
                k=3,
                d_star=11,
            )
        )
        self.assertEqual(m_one["root_carrier"], 7)
        self.assertEqual(m_zero["root_carrier"], 7)
        self.assertIsNone(k_three["root_carrier"])
        self.assertEqual(k_three["root_menu_modulus"], 7)
        self.assertTrue(k_three["root_menu_required"])
        self.assertEqual(k_three["residual_code"], PARTITION.R6_K3_RESIDUAL)
        self.assertEqual(k_three["transverse_factor_candidate"], 11)

    def test_quotient_only_and_m3_q5_fail_closed(self) -> None:
        with self.assertRaisesRegex(
            PARTITION.PartitionError, "QUOTIENT_ONLY_NOT_OWNED"
        ):
            PARTITION.classify(
                PARTITION.fixture(h=3 * 31, k=3 * 31 * 37)
            )
        with self.assertRaisesRegex(PARTITION.PartitionError, "M3_Q5_NOT_OWNED"):
            PARTITION.classify(PARTITION.fixture(d_star=5 * 13))

    def test_terminal_precedence_and_menu_dispositions(self) -> None:
        terminal = PARTITION.classify(
            PARTITION.fixture(terminal_first_hit=True)
        )
        root_menu = PARTITION.classify(PARTITION.fixture(root_menu_hit=True))
        dstar_menu = PARTITION.classify(PARTITION.fixture(dstar_menu_hit=True))
        self.assertEqual(terminal["outcome"], "TERMINAL_FIRST")
        self.assertEqual(root_menu["outcome"], "ROOT_SUPPORTED_MENU_TERMINAL")
        self.assertEqual(dstar_menu["outcome"], "DSTAR_MENU_TERMINAL")
        self.assertFalse(terminal["recursive"])

    def test_arithmetic_factor_cannot_self_authorize_tr1(self) -> None:
        row = PARTITION.classify(PARTITION.fixture())
        self.assertEqual(row["outcome"], "OPEN_MINIMAL_RESIDUAL")
        self.assertFalse(row["recursive"])
        self.assertFalse(row["integer_raw_occurrence_bound"])
        receipt = PARTITION.json.loads(
            PARTITION.RECEIPT_PATH.read_text(encoding="utf-8")
        )
        self.assertEqual(
            receipt["physicalization_status"], "OPEN_MINIMAL_RESIDUALS"
        )
        self.assertIn("TR1 integer raw occurrence/E1", receipt["does_not_claim"])
        self.assertIn("TR1PhysicalTransitionV1", receipt["does_not_claim"])


if __name__ == "__main__":
    unittest.main()
