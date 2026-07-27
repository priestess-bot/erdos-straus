import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_targeted_quadratic_descent",
    ROOT / "reproductions" / "type_ii_h19_targeted_quadratic_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19TargetedQuadraticDescentTests(unittest.TestCase):
    def test_trial_spf_matches_the_required_interface(self):
        spf = audit.TrialSmallestFactors(1_000)
        self.assertEqual(spf[1], 1)
        self.assertEqual(spf[97], 97)
        self.assertEqual(spf[924], 2)

    def test_ten_million_cross_check_with_the_full_spf_audit(self):
        path = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-10m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 45)
        self.assertEqual(result["adaptive_descent_count"], 38)
        self.assertEqual(result["mixed_factor_descent_count"], 45)
        self.assertEqual(result["quadratic_factor_descent_count"], 45)
        self.assertEqual(result["quadratic_factor_descent_misses"], [])
        self.assertEqual(result["maximum_quadratic_k"], 12)

    def test_one_and_two_hundred_million_boundary_artifacts(self):
        expected = {
            "100m": (164, 163, [35_840_809], 98),
            "200m": (255, 252, [35_840_809, 132_285_169, 141_326_089], 98),
        }
        for label, (residuals, hits, misses, maximum_k) in expected.items():
            path = ROOT / "reproductions" / f"type-ii-h19-targeted-quadratic-descent-{label}-results.json"
            with path.open(encoding="utf-8") as handle:
                result = json.load(handle)
            self.assertEqual(result["h19_residual_count"], residuals)
            self.assertEqual(result["quadratic_factor_descent_count"], hits)
            self.assertEqual(result["quadratic_factor_descent_misses"], misses)
            self.assertEqual(result["maximum_quadratic_k"], maximum_k)

    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 300_000_000)
        self.assertEqual(result["h19_residual_count"], 328)
        self.assertEqual(result["adaptive_descent_count"], 276)
        self.assertEqual(result["mixed_factor_descent_count"], 323)
        self.assertEqual(result["quadratic_factor_descent_count"], 325)
        self.assertEqual(
            result["quadratic_factor_descent_misses"],
            [35_840_809, 132_285_169, 141_326_089],
        )
        self.assertEqual(result["maximum_quadratic_k"], 98)
        record = next(row for row in result["records"] if row["prime"] == 3_361)
        self.assertLess(
            record["quadratic_factor_external_source_descent"]["source_denominator"],
            record["prime"],
        )

    def test_five_hundred_million_boundary_keeps_the_same_three_misses(self):
        path = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-500m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 500_000_000)
        self.assertEqual(result["h19_residual_count"], 425)
        self.assertEqual(result["adaptive_descent_count"], 359)
        self.assertEqual(result["mixed_factor_descent_count"], 419)
        self.assertEqual(result["quadratic_factor_descent_count"], 422)
        self.assertEqual(
            result["quadratic_factor_descent_misses"],
            [35_840_809, 132_285_169, 141_326_089],
        )
        self.assertEqual(result["maximum_quadratic_k"], 98)

    def test_one_billion_boundary_has_a_fourth_miss_and_larger_scale(self):
        path = ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_factor_descent_count"], 660)
        self.assertEqual(
            result["quadratic_factor_descent_misses"],
            [35_840_809, 132_285_169, 141_326_089, 640_775_689],
        )
        self.assertEqual(result["maximum_quadratic_k"], 178)


if __name__ == "__main__":
    unittest.main()
