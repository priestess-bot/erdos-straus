"""Verify complete full-spectrum structure behind the 200 selected B>1 witnesses."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_b_gt_one_full_spectrum_profile_600m",
    ROOT / "reproductions" / "type_i_linear_b_gt_one_full_spectrum_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearBGreaterThanOneFullSpectrumProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_fresh_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["prime_count"], 200)
        self.assertEqual(self.actual["complete_linear_R_count"], 10_292)
        self.assertEqual(
            self.actual["classification_totals"],
            {"hit": 1_018, "finite_exponent": 2_752, "subgroup_character": 6_522},
        )

    def test_first_B_greater_than_one_is_usually_reselectable_to_B_one(self):
        self.assertEqual(self.actual["B_eq_1_reselected_prime_count"], 182)
        self.assertEqual(self.actual["no_B_eq_1_hit_prime_count"], 18)
        for record in self.actual["profiles"]:
            self.assertGreater(int(record["selected_first_witness"]["B"]), 1)
            self.assertGreaterEqual(int(record["classification_counts"]["hit"]), 1)
            selected_R = int(record["selected_first_witness"]["R"])
            selected = next(row for row in record["records"] if int(row["R"]) == selected_R)
            self.assertEqual(selected["classification"], "hit")

    def test_unique_non_B_one_pressure_core_is_exactly_isolated(self):
        unique = {
            int(record["prime"]): record
            for record in self.actual["profiles"]
            if int(record["classification_counts"]["hit"]) == 1
        }
        self.assertEqual(sorted(unique), profile.EXPECTED_UNIQUE_GENERAL_B_HIT_PRIMES)
        self.assertEqual(
            sorted(prime for prime, record in unique.items() if not record["B_eq_1_hit_R"]),
            [878_089, 26_034_649, 57_399_241, 283_319_689],
        )


if __name__ == "__main__":
    unittest.main()
