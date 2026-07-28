"""Verify exact half-density gaps at every frozen linear F-type state."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_finite_exponent_antipodal_density_profile_600m",
    ROOT / "reproductions" / "type_i_linear_finite_exponent_antipodal_density_profile_600m.py",
)
assert SPEC and SPEC.loader
density = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = density
SPEC.loader.exec_module(density)


class TypeILinearFiniteExponentAntipodalDensityProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = density.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-finite-exponent-antipodal-density-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["finite_exponent_R_count"], 68)

    def test_every_f_state_is_below_or_at_the_half_density_boundary(self):
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                R = int(record["R"])
                K = int(record["K"])
                A = {int(divisor) % R for divisor in sympy.divisors(K)}
                self.assertFalse(A & {(-residue) % R for residue in A})
                self.assertEqual(len(A), int(record["K_divisor_residue_count"]))
                self.assertEqual(
                    2 * len(A), int(record["twice_divisor_residue_count"])
                )
                self.assertLessEqual(
                    int(record["twice_divisor_residue_count"]),
                    int(record["generated_subgroup_order"]),
                )
                self.assertEqual(
                    int(record["generated_subgroup_order"])
                    - int(record["twice_divisor_residue_count"]),
                    int(record["half_density_deficit"]),
                )

    def test_lattice_index_recovers_the_exact_support_subgroup_order(self):
        for profile in self.actual["profiles"]:
            prime = int(profile["prime"])
            for record in profile["records"]:
                R = int(record["R"])
                K = int(record["K"])
                certificate = density.sources.unit_group_subgroup_certificate(
                    density.sources.exact_factorization(K), R
                )
                order, index = density.generated_subgroup_order(certificate)
                self.assertEqual(order, int(record["generated_subgroup_order"]))
                self.assertEqual(index, int(record["generated_subgroup_index"]))
                self.assertTrue(bool(certificate["target_in_generated_subgroup"]))
                self.assertEqual((prime * R + 1) // 4, K)


if __name__ == "__main__":
    unittest.main()
