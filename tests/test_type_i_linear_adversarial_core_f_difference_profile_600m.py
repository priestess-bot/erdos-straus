"""Verify exact divisor-difference coverage at the four adversarial cores."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_adversarial_core_f_difference_profile_600m",
    ROOT / "reproductions" / "type_i_linear_adversarial_core_f_difference_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearAdversarialCoreFDifferenceProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-adversarial-core-f-difference-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_all_45_f_states(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["finite_exponent_R_count"], 45)
        self.assertEqual(self.actual["difference_target_hit_count"], 0)

    def test_near_saturation_still_misses_minus_one(self):
        witness = self.actual["maximum_difference_density_witness"]
        self.assertEqual(
            {key: witness[key] for key in ("prime", "R", "difference_residue_count", "generated_subgroup_order")},
            {
                "prime": 26_034_649,
                "R": 375,
                "difference_residue_count": 192,
                "generated_subgroup_order": 200,
            },
        )
        near = next(
            row
            for row in self.actual["near_saturation_records"]
            if row["prime"] == 26_034_649 and row["R"] == 375
        )
        self.assertEqual(near["difference_missing_residues"], [127, 133, 172, 251, 254, 313, 344, 374])
        self.assertIn(374, near["difference_missing_residues"])

    def test_every_record_keeps_the_exact_f_boundary(self):
        for row in self.actual["profiles"]:
            for record in row["records"]:
                self.assertFalse(record["difference_target_in_spectrum"])
                self.assertGreaterEqual(record["difference_density_deficit"], 8)
                self.assertLessEqual(
                    record["difference_residue_count"],
                    record["generated_subgroup_order"],
                )


if __name__ == "__main__":
    unittest.main()
