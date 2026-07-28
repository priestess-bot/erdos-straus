"""Verify the complete adversarial-core block-alignment profile."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_adversarial_core_f_block_alignment_profile_600m",
    ROOT
    / "reproductions"
    / "type_i_linear_adversarial_core_f_block_alignment_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearAdversarialCoreFBlockAlignmentProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-adversarial-core-f-block-alignment-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_all_f_states_and_orientations(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["finite_exponent_R_count"], 45)
        self.assertEqual(self.actual["directed_orientation_count"], 69)
        self.assertEqual(self.actual["target_alignment_hit_count"], 0)
        self.assertEqual(self.actual["minimum_alignment_pigeonhole_margin"], 0)
        self.assertEqual(self.actual["positive_margin_minimum"], 11)
        self.assertEqual(self.actual["zero_alignment_pigeonhole_margin_count"], 2)
        self.assertEqual(self.actual["nonvacuous_zero_margin_count"], 1)

    def test_per_prime_margin_profile_is_frozen(self):
        by_prime = {
            int(row["prime"]): row for row in self.actual["profiles"]
        }
        self.assertEqual(
            {
                prime: (
                    row["finite_exponent_R_count"],
                    row["directed_orientation_count"],
                    row["minimum_alignment_pigeonhole_margin"],
                    row["zero_alignment_pigeonhole_margin_count"],
                )
                for prime, row in by_prime.items()
            },
            {
                878_089: (2, 4, 21, 0),
                26_034_649: (6, 8, 49, 0),
                57_399_241: (24, 36, 0, 2),
                283_319_689: (13, 21, 100, 0),
            },
        )

    def test_nonvacuous_equality_is_the_single_391_hole(self):
        equality_rows = []
        for prime_profile in self.actual["profiles"]:
            for record in prime_profile["records"]:
                for orientation in record["orientations"]:
                    if orientation["alignment_pigeonhole_margin"] != 0:
                        continue
                    equality_rows.append((record["prime"], record["R"], orientation))
        self.assertEqual(len(equality_rows), 2)
        substantive = [
            (prime, modulus, orientation)
            for prime, modulus, orientation in equality_rows
            if orientation["target_pullback_in_affine_subgroup_count"] > 0
        ]
        self.assertEqual(len(substantive), 1)
        prime, modulus, orientation = substantive[0]
        self.assertEqual((prime, modulus, orientation["a"], orientation["s"]),
                         (57_399_241, 455, 150, 841))
        self.assertEqual(orientation["H_affine_order"], 6)
        self.assertEqual(orientation["D_affine_residue_count"], 5)
        self.assertEqual(orientation["target_pullback_in_affine_subgroup_residues"], [391])
        self.assertEqual(orientation["alignment_residues"], [])


if __name__ == "__main__":
    unittest.main()
