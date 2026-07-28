"""Verify the genuine fourth-order separator at the surviving adversarial G state."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_order_four_separator_boundary_57399241",
    ROOT / "reproductions" / "type_i_linear_order_four_separator_boundary_57399241.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeILinearOrderFourSeparatorBoundary57399241Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = boundary.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-order-four-separator-boundary-57399241-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_low_order_character_enumeration(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["quadratic_separator_count"], 0)
        self.assertEqual(self.actual["order_four_separator_count"], 2)

    def test_two_order_four_separators_are_conjugate_and_odd(self):
        separators = self.actual["order_four_separators"]
        self.assertEqual(
            [row["coefficients"] for row in separators], [[0, 1, 1], [0, 1, 3]]
        )
        for row in separators:
            self.assertEqual(row["character_order"], 4)
            self.assertEqual(row["conductor"], 88_991)
            self.assertEqual(row["generator_quarter_exponents"], [0, 0, 0])
            self.assertEqual(row["minus_one_quarter_exponent"], 2)


if __name__ == "__main__":
    unittest.main()
