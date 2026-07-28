"""Verify the near-saturated F-state block-alignment audit."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_f_near_saturation_block_alignment_600m",
    ROOT
    / "reproductions"
    / "type_i_linear_f_near_saturation_block_alignment_600m.py",
)
assert SPEC and SPEC.loader
alignment = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = alignment
SPEC.loader.exec_module(alignment)


class TypeILinearFNearSaturationBlockAlignment600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = alignment.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-f-near-saturation-block-alignment-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_six_near_saturated_states(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["near_saturation_state_count"], 6)
        self.assertEqual(self.actual["directed_orientation_count"], 10)
        self.assertEqual(self.actual["target_alignment_hit_count"], 0)
        self.assertEqual(self.actual["block_identity_verified_count"], 6)

    def test_max_density_state_has_two_empty_block_alignments(self):
        record = next(
            row
            for row in self.actual["records"]
            if row["prime"] == 26_034_649 and row["R"] == 375
        )
        self.assertEqual(record["D_full_residue_count"], 192)
        self.assertEqual(record["generated_subgroup_order"], 200)
        self.assertEqual(record["D_full_missing_residues"], [
            127,
            133,
            172,
            251,
            254,
            313,
            344,
            374,
        ])
        self.assertEqual(
            [
                (
                    orientation["a"],
                    orientation["s"],
                    orientation["D_gamma_residue_count"],
                    orientation["D_affine_residue_count"],
                    orientation["target_alignment_count"],
                )
                for orientation in record["orientations"]
            ],
            [
                (73, 951, 15, 51, 0),
                (951, 73, 41, 33, 0),
            ],
        )

    def test_every_orientation_preserves_the_block_product_identity(self):
        for record in self.actual["records"]:
            for orientation in record["orientations"]:
                self.assertEqual(
                    orientation["D_product_residue_count"],
                    orientation["D_full_residue_count"],
                )
                self.assertEqual(orientation["target_alignment_residues"], [])
                self.assertEqual(orientation["target_alignment_count"], 0)
                self.assertEqual(
                    orientation["gamma_target_in_difference"], False
                )
                self.assertEqual(
                    orientation["affine_target_in_difference"], False
                )


if __name__ == "__main__":
    unittest.main()
