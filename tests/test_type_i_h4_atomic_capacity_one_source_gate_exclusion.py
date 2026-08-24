from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
if str(REPRODUCTIONS) not in sys.path:
    sys.path.insert(0, str(REPRODUCTIONS))
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_h4_atomic_capacity_one_source_gate_exclusion.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_h4_atomic_capacity_one_source_gate_exclusion", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class H4AtomicCapacityOneSourceGateExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.receipt = MODULE.build_receipt()

    def test_stored_receipt_replays(self) -> None:
        MODULE.verify()

    def test_low_p_negative_residue_menu_is_empty(self) -> None:
        low = self.receipt["low_p"]
        self.assertEqual(low["phase_carrier_pairs"], 109)
        self.assertEqual(low["q_values"], 2204)
        self.assertEqual(low["phase_primes"], 524)
        self.assertEqual(low["D_candidates"], 1_054_140)
        self.assertEqual(low["divisibility_hits"], [])

    def test_high_p_parameterization_has_one_arithmetic_survivor(self) -> None:
        high = self.receipt["high_p"]
        self.assertEqual(high["k1_phase_values"], 0)
        self.assertEqual(high["k_ge_2_phase_values"], 1)
        self.assertEqual(
            high["phase_survivors"],
            [
                {
                    "u": 117,
                    "a": 2046,
                    "d": 85,
                    "q": 48_842_701,
                    "p": 8_303_259_169,
                    "D": 141_150_521_603,
                    "ell": 10,
                    "k": 17,
                    "delta": 4_884_270,
                }
            ],
        )

    def test_sole_survivor_fails_actual_carrier_equality(self) -> None:
        carrier = self.receipt["sole_survivor_actual_carrier"]
        self.assertEqual(carrier["required_d"], 85)
        self.assertEqual(carrier["actual_d"], 1)
        self.assertFalse(carrier["carrier_matches"])
        self.assertEqual(
            self.receipt["conclusion"]["actual_h4_clean_q_capacity_one"],
            "EMPTY",
        )

    def test_non_phase_arithmetic_rows_are_not_promoted(self) -> None:
        # The two previously reported loose rows fail before the exact phase menu.
        for d, q, p in ((23, 47, 2161), (35, 71, 4969)):
            with self.subTest(p=p):
                matching = [
                    row
                    for row in self.receipt["high_p"]["phase_survivors"]
                    if row["d"] == d and row["q"] == q and row["p"] == p
                ]
                self.assertEqual(matching, [])


if __name__ == "__main__":
    unittest.main()
