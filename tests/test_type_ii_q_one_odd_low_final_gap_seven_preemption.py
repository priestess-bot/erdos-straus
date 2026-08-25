from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_odd_low_final_gap_seven_preemption.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_odd_low_final_gap7", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PREEMPTION = load_module()


class QOneOddLowFinalGapSevenPreemptionTests(unittest.TestCase):
    def test_crt_classification_and_terminal_control(self) -> None:
        PREEMPTION.verify()

    def test_only_one_low_class_survives_the_fixed_gap_preemption(self) -> None:
        self.assertEqual(PREEMPTION.low_final_class(601), 265)
        self.assertEqual(PREEMPTION.low_final_class(1033), 25)
        self.assertIsNone(PREEMPTION.low_final_class(73))


if __name__ == "__main__":
    unittest.main()
