"""Verify the complete high-order separator census behind 200 B>1 spectra."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_b_gt_one_high_order_separator_census_600m",
    ROOT / "reproductions" / "type_i_linear_b_gt_one_high_order_separator_census_600m.py",
)
assert SPEC and SPEC.loader
census = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = census
SPEC.loader.exec_module(census)


class TypeILinearBGtOneHighOrderSeparatorCensus600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = census.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-b-gt-one-high-order-separator-census-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_census(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["subgroup_character_R_count"], 6_522)
        self.assertEqual(
            self.actual["separator_order_counts"], {"2": 6_461, "4": 49, "8": 12}
        )

    def test_high_order_pairs_are_real_but_not_automatic_contradictions(self):
        self.assertEqual(self.actual["higher_order_separator_R_count"], 61)
        self.assertEqual(self.actual["higher_order_to_higher_order_relation_count"], 2)
        relations = [
            row
            for row in self.actual["higher_order_collision_relations"]
            if int(row["other_separator_order"]) > 2
        ]
        self.assertEqual(
            relations,
            [
                {
                    "prime": 159_108_889,
                    "higher_order_R": 47_227,
                    "higher_order_separator_order": 4,
                    "other_R": 53_036_295,
                    "other_separator_order": 4,
                    "shared_odd_prime": 70_841,
                },
                {
                    "prime": 403_509_649,
                    "higher_order_R": 843,
                    "higher_order_separator_order": 4,
                    "other_R": 33_625_803,
                    "other_separator_order": 4,
                    "shared_odd_prime": 211,
                },
            ],
        )

    def test_two_residue_injection_remains_disjoint_from_minus_one_orbits(self):
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                self.assertFalse(
                    int(record["two_injecting_endpoint_count"]) > 0
                    and bool(record["minus_one_in_two_subgroup"])
                )


if __name__ == "__main__":
    unittest.main()
