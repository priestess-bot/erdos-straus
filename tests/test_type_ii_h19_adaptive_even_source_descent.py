import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_adaptive_even_source_descent",
    ROOT / "reproductions" / "type_ii_h19_adaptive_even_source_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19AdaptiveEvenSourceDescentTests(unittest.TestCase):
    def test_distance_three_does_not_close_the_first_boundary(self):
        path = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-100m-c3-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["odd_distance_cap"], 3)
        self.assertEqual(result["odd_distance_fallback_count"], 0)
        self.assertEqual(result["missing_through_cap"], [35_840_809])

    def test_one_and_two_hundred_million_boundary_artifacts(self):
        expected = {
            "100m": (164, 163, [(35_840_809, 7)]),
            "200m": (
                255,
                252,
                [(35_840_809, 7), (132_285_169, 3), (141_326_089, 3)],
            ),
        }
        for label, (residuals, quadratic, fallbacks) in expected.items():
            path = ROOT / "reproductions" / f"type-ii-h19-adaptive-even-source-descent-{label}-results.json"
            with path.open(encoding="utf-8") as handle:
                result = json.load(handle)
            self.assertEqual(result["h19_residual_count"], residuals)
            self.assertEqual(result["quadratic_factor_descent_count"], quadratic)
            self.assertEqual(result["odd_distance_fallback_count"], len(fallbacks))
            self.assertEqual(result["missing_through_cap"], [])
            self.assertEqual(
                [(row["prime"], row["distance"]) for row in result["fallbacks"]],
                fallbacks,
            )

    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 300_000_000)
        self.assertEqual(result["h19_residual_count"], 328)
        self.assertEqual(result["quadratic_factor_descent_count"], 325)
        self.assertEqual(result["odd_distance_cap"], 7)
        self.assertEqual(result["odd_distance_fallback_count"], 3)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            [(row["prime"], row["distance"]) for row in result["fallbacks"]],
            [(35_840_809, 7), (132_285_169, 3), (141_326_089, 3)],
        )

    def test_five_hundred_million_closure_keeps_the_same_fallbacks(self):
        path = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-500m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 500_000_000)
        self.assertEqual(result["h19_residual_count"], 425)
        self.assertEqual(result["quadratic_factor_descent_count"], 422)
        self.assertEqual(result["odd_distance_fallback_count"], 3)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            [(row["prime"], row["distance"]) for row in result["fallbacks"]],
            [(35_840_809, 7), (132_285_169, 3), (141_326_089, 3)],
        )

    def test_one_billion_second_layer_miss_persists_through_distance_9999(self):
        path = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-1b-c9999-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_factor_descent_count"], 660)
        self.assertEqual(result["odd_distance_cap"], 9999)
        self.assertEqual(result["odd_distance_fallback_count"], 3)
        self.assertEqual(result["missing_through_cap"], [640_775_689])

    def test_one_billion_state_dependent_distance_closes_the_profile(self):
        path = ROOT / "reproductions" / "type-ii-h19-adaptive-even-source-descent-1b-c99999-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_factor_descent_count"], 660)
        self.assertEqual(result["odd_distance_cap"], 99_999)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            [(row["prime"], row["distance"]) for row in result["fallbacks"]],
            [
                (35_840_809, 7),
                (132_285_169, 3),
                (141_326_089, 3),
                (640_775_689, 34_091),
            ],
        )


if __name__ == "__main__":
    unittest.main()
