from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_odd_low_final_third_anchor_contraction.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_odd_low_final_c9", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONTRACTION = load_module()


class QOneOddLowFinalThirdAnchorContractionTests(unittest.TestCase):
    def test_symbolic_c9_controls_and_root_ticket(self) -> None:
        CONTRACTION.verify()

    def test_preempted_class_is_not_accepted_as_the_remaining_low_class(self) -> None:
        with self.assertRaises(AssertionError):
            CONTRACTION.low_checkpoint_to_c9(601)


if __name__ == "__main__":
    unittest.main()
