"""Verify the Gaussian quartic source-label pullback."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_gaussian_quartic_source_pullback_57399241",
    ROOT / "reproductions" / "type_i_linear_gaussian_quartic_source_pullback_57399241.py",
)
assert SPEC and SPEC.loader
pullback = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pullback
SPEC.loader.exec_module(pullback)


class TypeILinearGaussianQuarticSourcePullback57399241Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = pullback.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-gaussian-quartic-source-pullback-57399241-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_all_k_prime_pullbacks(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["pullback_relation_count"], 3)
        self.assertEqual(self.actual["gaussian_factor_pi"], [13, 112])

    def test_quartic_phase_equals_the_source_label_pullback(self):
        for relation in self.actual["relations"]:
            self.assertEqual(
                relation["quartic_character_exponent_at_12713"],
                relation["pullback_rhs_exponent"],
            )
            expected_legendre = (
                1
                if relation["quartic_character_exponent_at_12713"] == 0
                else -1
            )
            self.assertEqual(relation["legendre_q_over_7"], expected_legendre)


if __name__ == "__main__":
    unittest.main()
