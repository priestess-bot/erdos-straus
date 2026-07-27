import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_adaptive_factor_transition",
    ROOT / "reproductions" / "type_ii_adaptive_factor_transition.py",
)
assert SPEC and SPEC.loader
transition = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = transition
SPEC.loader.exec_module(transition)


class TypeIIAdaptiveFactorTransitionTests(unittest.TestCase):
    def test_small_profile(self):
        result = transition.run_profile(10_000, 19, 50)
        self.assertEqual(result["base_residual_count"], 1)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["old_private_free_count"], 0)
        self.assertEqual(result["new_factor_count"], 1)
        self.assertEqual(result["old_private_required_primes"], [3_361])
        self.assertEqual(
            result["profiles"][0]["selected_witness"]["h_factorization"],
            [{"prime": 19, "exponent": 1}, {"prime": 61, "exponent": 1}],
        )

    def test_checked_h19_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-adaptive-factor-transition-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 45)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["old_private_free_count"], 42)
        self.assertEqual(result["new_factor_count"], 35)
        self.assertEqual(
            result["old_private_required_primes"], [3_361, 813_121, 8_283_361]
        )
        profile = next(row for row in result["profiles"] if row["prime"] == 225_289)
        self.assertEqual(profile["first_later_shift"], 32)
        self.assertEqual(profile["selected_witness"]["h"], 2_591)
        self.assertEqual(profile["selected_witness"]["new_multiplicity"], 1)

    def test_checked_h19_twenty_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-adaptive-factor-transition-h19-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 65)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["old_private_free_count"], 61)
        self.assertEqual(result["new_factor_count"], 51)
        self.assertEqual(
            result["old_private_required_primes"],
            [3_361, 813_121, 8_283_361, 14_847_529],
        )
        pressure = {
            row["prime"]: row
            for row in result["profiles"]
            if row["prime"] in {7_378_849, 8_955_769, 11_910_361, 12_180_169}
        }
        self.assertEqual(
            {prime: row["first_later_shift"] for prime, row in pressure.items()},
            {7_378_849: 26, 8_955_769: 25, 11_910_361: 36, 12_180_169: 24},
        )
        self.assertTrue(
            all(row["selected_witness"]["old_private_multiplicity"] == 0 for row in pressure.values())
        )


if __name__ == "__main__":
    unittest.main()
