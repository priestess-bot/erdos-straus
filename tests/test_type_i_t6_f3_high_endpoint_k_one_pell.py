from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_high_endpoint_k_one_pell.py"


def load_module():
    spec = importlib.util.spec_from_file_location("high_endpoint_k_one_pell", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PELL = load_module()


class HighKOnePellTests(unittest.TestCase):
    def test_symbolic_parameterization(self) -> None:
        PELL.verify_symbolic_parameterization()

    def test_noncore_shadow_stays_outside_quantifier(self) -> None:
        PELL.check_noncore_shadow()

    def test_core_curve_shadow_is_gap_three_preempted(self) -> None:
        PELL.check_core_curve_shadow_terminal_preemption()


if __name__ == "__main__":
    unittest.main()
