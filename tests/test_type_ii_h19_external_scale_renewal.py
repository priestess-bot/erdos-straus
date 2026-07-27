import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_external_scale_renewal",
    ROOT / "reproductions" / "type_ii_h19_external_scale_renewal.py",
)
assert SPEC and SPEC.loader
renewal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = renewal
SPEC.loader.exec_module(renewal)


class TypeIIH19ExternalScaleRenewalTests(unittest.TestCase):
    def test_k10_cover_renews_on_every_mod_five_branch(self):
        result = renewal.run_audit()
        self.assertEqual(
            result["base_scales"], [1, 2, 3, 4, 5, 6, 8, 9, 12, 15]
        )
        self.assertEqual(
            result["extended_scales"], [1, 2, 3, 4, 5, 6, 8, 9, 12, 15, 10]
        )
        self.assertEqual(result["pre_extension"]["covering_primes"], [])
        self.assertEqual(
            result["extension_before_split"]["covering_primes"], [5]
        )
        self.assertEqual(
            sorted(result["covering_root_map_mod_5"]), ["0", "1", "2", "3", "4"]
        )
        branches = result["renewal"]["branches"]
        self.assertEqual(
            [branch["parameter_offset"] for branch in branches], list(range(5))
        )
        self.assertTrue(all(branch["covering_primes"] == [] for branch in branches))
        self.assertTrue(all(branch["combined_form_count"] == 31 for branch in branches))
        for branch in branches:
            self.assertEqual(
                [row["k"] for row in branch["sources"]],
                [1, 2, 3, 4, 5, 6, 8, 9, 12, 15, 10],
            )
            for row in branch["sources"]:
                self.assertNotIn(row["target_residue"], row["divisor_residues"])

        stationary = result["all_common_stationary_scales"]
        self.assertEqual(stationary["scale_gcd"], 360)
        self.assertEqual(len(stationary["scales"]), 24)
        self.assertEqual(stationary["scales"][-1], 360)
        self.assertEqual(len(stationary["branches"]), 5)
        self.assertTrue(
            all(
                branch["combined_form_count"] == 44
                and branch["covering_primes"] == []
                for branch in stationary["branches"]
            )
        )
        for branch in stationary["branches"]:
            self.assertEqual(
                [row["k"] for row in branch["sources"]], stationary["scales"]
            )
            for row in branch["sources"]:
                self.assertNotIn(row["target_residue"], row["divisor_residues"])

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-external-scale-renewal-k10-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(
            result["extension_before_split"]["covering_primes"], [5]
        )
        self.assertEqual(len(result["renewal"]["branches"]), 5)
        self.assertTrue(
            all(
                branch["covering_primes"] == []
                for branch in result["renewal"]["branches"]
            )
        )
        self.assertEqual(
            result["all_common_stationary_scales"]["scale_gcd"], 360
        )


if __name__ == "__main__":
    unittest.main()
