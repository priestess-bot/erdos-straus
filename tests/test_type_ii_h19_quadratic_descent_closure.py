import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_quadratic_descent_closure",
    ROOT / "reproductions" / "type_ii_h19_quadratic_descent_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIIH19QuadraticDescentClosureTests(unittest.TestCase):
    def test_small_h19_closure(self):
        result = closure.run_audit(10_000, 19)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["canonical_residual_count"], 1)
        self.assertEqual(result["adaptive_descent_count"], 0)
        self.assertEqual(result["mixed_factor_descent_count"], 1)
        self.assertEqual(result["quadratic_factor_descent_count"], 1)
        self.assertEqual(result["adaptive_descent_misses"], [3_361])
        record = result["records"][0]
        self.assertEqual(record["mixed_factor_external_source_descent"]["k"], 2)
        self.assertEqual(
            record["mixed_factor_external_source_descent"]["factor"], 34
        )
        self.assertLess(
            record["quadratic_factor_external_source_descent"]["source_denominator"],
            record["prime"],
        )

    def test_checked_ten_million_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-quadratic-descent-closure-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["canonical_captured_count"], 82_842)
        self.assertEqual(result["canonical_residual_count"], 45)
        self.assertEqual(result["adaptive_descent_count"], 38)
        self.assertEqual(result["mixed_factor_descent_count"], 45)
        self.assertEqual(result["quadratic_factor_descent_count"], 45)
        self.assertEqual(
            result["adaptive_descent_misses"],
            [3_361, 345_601, 1_398_769, 3_660_721, 6_868_801, 6_899_281, 9_744_001],
        )
        self.assertEqual(result["mixed_factor_descent_misses"], [])
        self.assertEqual(result["quadratic_factor_descent_misses"], [])
        self.assertEqual(
            result["mixed_factor_k_histogram"],
            {"1": 16, "2": 18, "3": 3, "4": 2, "5": 2, "6": 3, "12": 1},
        )
        record = next(row for row in result["records"] if row["prime"] == 3_361)
        self.assertEqual(
            record["mixed_factor_external_source_descent"]["factor"], 34
        )
        self.assertEqual(
            record["quadratic_factor_external_source_descent"]["certificate"]["gap"],
            39,
        )

    def test_checked_twenty_million_artifact_refutes_fixed_k_list(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-quadratic-descent-closure-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 158_595)
        self.assertEqual(result["canonical_captured_count"], 158_530)
        self.assertEqual(result["canonical_residual_count"], 65)
        self.assertEqual(result["adaptive_descent_count"], 55)
        self.assertEqual(result["mixed_factor_descent_count"], 65)
        self.assertEqual(result["quadratic_factor_descent_count"], 65)
        self.assertEqual(result["mixed_factor_descent_misses"], [])
        self.assertEqual(result["quadratic_factor_descent_misses"], [])
        self.assertEqual(
            result["mixed_factor_k_histogram"],
            {"1": 25, "2": 25, "3": 4, "4": 2, "5": 3, "6": 3, "9": 1, "12": 2},
        )
        record = next(row for row in result["records"] if row["prime"] == 12_180_169)
        self.assertEqual(record["mixed_factor_external_source_descent"]["k"], 9)


if __name__ == "__main__":
    unittest.main()
