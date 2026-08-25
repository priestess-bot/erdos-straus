from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_ii_q_one_c9_high_r_side_dual_small_chart.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_c9_r_side_dual", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DUAL = load_module()


class QOneC9RSideDualTests(unittest.TestCase):
    def test_all_three_small_chart_rows_and_phase_ticket(self) -> None:
        DUAL.verify()

    def test_r_side_is_strictly_smaller_than_d_side(self) -> None:
        for prime in (1033, 2713, 9433):
            receipt = DUAL.c9_r_side_dual(prime)
            self.assertGreater(receipt["d_side_R"], receipt["r_side"]["R"])


if __name__ == "__main__":
    unittest.main()
