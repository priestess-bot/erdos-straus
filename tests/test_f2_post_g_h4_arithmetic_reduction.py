from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "f2_post_g_h4_arithmetic_reduction.py"
SPEC = importlib.util.spec_from_file_location("f2_h4_reduction", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load focused H4 reduction verifier")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2PostGH4ArithmeticReductionTest(unittest.TestCase):
    def test_focused_controls_and_boundary(self) -> None:
        result = MODULE.verify()
        self.assertEqual(
            result["status"], "ARITHMETIC_CONTROLS_PASS_SEMANTIC_RESIDUAL_OPEN"
        )
        self.assertEqual(
            [row["outcome"] for row in result["r4_mod_0"]],
            ["direct_strict_capacity", "top_capacity_then_strict_61"],
        )
        self.assertTrue(
            all(row["parent_macro_endpoint_decreases"] for row in result["r4_mod_other"])
        )
        self.assertTrue(
            all(row["capacity"] <= row["p"] - 2 for row in result["r4_mod_1_clean_q"])
        )
        self.assertFalse(result["scope_boundary"]["common_admission"] == "replayed")


if __name__ == "__main__":
    unittest.main()
