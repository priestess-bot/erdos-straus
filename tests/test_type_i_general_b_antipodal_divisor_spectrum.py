"""Independently verify the antipodal divisor-spectrum equivalence."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_general_b_antipodal_divisor_spectrum",
    ROOT / "reproductions" / "type_i_general_b_antipodal_divisor_spectrum.py",
)
assert SPEC and SPEC.loader
antipodal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = antipodal
SPEC.loader.exec_module(antipodal)


class TypeIGeneralBAntipodalDivisorSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = antipodal.run_audit()
        cls.expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-general-b-antipodal-divisor-spectrum-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["complete_linear_R_count"], 278)
        self.assertEqual(self.actual["target_hit_R_count"], 20)

    def test_direct_divisor_sets_have_exactly_the_reported_antipodal_relation(self):
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                R = int(record["R"])
                K = int(record["K"])
                A = {int(divisor) % R for divisor in sympy.divisors(K)}
                centered = {
                    int(divisor) * pow(K, -1, R) % R
                    for divisor in sympy.divisors(K * K)
                }
                quotient = {
                    left * pow(right, -1, R) % R for left in A for right in A
                }
                intersection = A & {(-value) % R for value in A}
                self.assertEqual(quotient, centered)
                self.assertEqual(len(A), int(record["K_divisor_residue_count"]))
                self.assertEqual(len(centered), int(record["centered_square_residue_count"]))
                self.assertEqual(len(intersection), int(record["antipodal_intersection_count"]))
                self.assertEqual(R - 1 in centered, bool(record["target_hit"]))
                self.assertEqual(bool(intersection), bool(record["target_hit"]))


if __name__ == "__main__":
    unittest.main()
