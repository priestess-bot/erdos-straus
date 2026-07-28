"""Verify quadratic-shadow compatibility at the genuine order-four G state."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_order_four_shadow_compatibility_57399241",
    ROOT / "reproductions" / "type_i_linear_order_four_shadow_compatibility_57399241.py",
)
assert SPEC and SPEC.loader
compatibility = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compatibility
SPEC.loader.exec_module(compatibility)


class TypeILinearOrderFourShadowCompatibility57399241Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = compatibility.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-order-four-shadow-compatibility-57399241-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_shared_prime_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["quadratic_shadow_conductor"], 12_713)
        self.assertEqual(self.actual["shared_odd_prime_relation_count"], 5)

    def test_every_relation_has_the_predicted_reciprocal_sign(self):
        for relation in self.actual["relations"]:
            q = relation["shared_odd_prime"]
            self.assertEqual(relation["modulus_difference_over_four"] % q, 0)
            self.assertEqual(
                relation["shadow_times_quadratic_over_prime"],
                relation["minus_one_over_prime"],
            )


if __name__ == "__main__":
    unittest.main()
