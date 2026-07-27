import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pure_new_square_ray_profile",
    ROOT / "reproductions" / "type_ii_h19_pure_new_square_ray_profile.py",
)
assert SPEC and SPEC.loader
square_profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = square_profile
SPEC.loader.exec_module(square_profile)


class TypeIIH19PureNewSquareRayProfileTests(unittest.TestCase):
    def test_known_square_ray_witness_is_new_and_reconstructs(self):
        witness = square_profile.pure_new_square_witness(
            992_339_401, 6, set(), square_profile.single.primes_through(40_000)
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["h"], 191)
        self.assertEqual(witness["shift"], 36)
        self.assertEqual(witness["divisor"], 36)

    def test_sequence_radius_cap_is_the_exact_order_boundary(self):
        radius = square_profile.sequence_radius_cap(176_089)
        self.assertEqual(radius, 210)
        self.assertLessEqual(4 * radius * radius - 2 * radius, 176_089)
        self.assertGreater(4 * (radius + 1) * (radius + 1) - 2 * (radius + 1), 176_089)

    def test_radius_cap_is_validated(self):
        with self.assertRaises(ValueError):
            square_profile.run_profile(
                {
                    "prime_limit": 100,
                    "base_shift_bound": 19,
                    "profiles": [],
                },
                4,
            )

    def test_checked_artifact_has_exact_coverage_summary(self):
        path = ROOT / "reproductions" / "type-ii-h19-pure-new-square-ray-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 541)
        self.assertEqual(result["pure_new_square_ray_count"], 530)
        self.assertEqual(result["radius_cap"], 16_000)
        self.assertEqual(result["maximum_sequence_radius_bound"], 15_750)
        self.assertEqual(
            result["order_exhausted_missing"],
            [
                176_089,
                225_289,
                870_241,
                4_722_169,
                20_368_321,
                26_953_921,
                70_005_049,
                87_503_329,
                439_768_081,
                629_071_081,
                826_129_441,
            ],
        )
        self.assertEqual(result["missing_through_radius_cap"], result["order_exhausted_missing"])
        self.assertEqual(result["cap_truncated_missing"], [])


if __name__ == "__main__":
    unittest.main()
