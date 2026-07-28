"""Verify shared-prime quadratic compatibility across the four adversarial spectra."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_cross_state_quadratic_separator_compatibility_profile_600m",
    ROOT / "reproductions" / "type_i_linear_cross_state_quadratic_separator_compatibility_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearCrossStateQuadraticSeparatorCompatibilityProfile600MTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-cross-state-quadratic-separator-compatibility-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["primes"], list(profile.ADVERSARIAL_PRIMES))
        self.assertGreater(self.actual["shared_odd_prime_relation_count"], 0)

    def test_each_shared_prime_obeys_modulus_difference_and_quadratic_compatibility(self):
        for prime_profile in self.actual["profiles"]:
            for relation in prime_profile["relations"]:
                R = int(relation["left_R"])
                U = int(relation["right_R"])
                q = int(relation["shared_odd_prime"])
                m = int(relation["left_conductor"])
                n = int(relation["right_conductor"])
                self.assertEqual(abs(R - U) % 4, 0)
                self.assertEqual((abs(R - U) // 4) % q, 0)
                self.assertEqual(math.gcd(q, m * n), 1)
                self.assertEqual(int(sympy.jacobi_symbol(m * n, q)), 1)


if __name__ == "__main__":
    unittest.main()
