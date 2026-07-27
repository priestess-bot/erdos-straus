import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_tail_profile",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_tail_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19FourthEvenSourceTailProfileTests(unittest.TestCase):
    def test_checked_artifact_separates_source_and_tail_conditions(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-tail-profile-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["scanned_odd_distances_through"], 34_091)
        self.assertEqual(result["compatible_source_ray_count"], 33)
        self.assertEqual(result["compatible_distance_count"], 24)
        self.assertEqual(result["tail_residue_success_count"], 1)
        self.assertEqual(
            result["first_tail_residue_success"],
            {
                "distance": 34_091,
                "source_denominator": 640_741_598,
                "d": 1253,
                "r": 15,
                "s": 511_366,
                "k": 4699,
                "m1": 2_402_908_834,
                "square_tail_divisor_count": 122,
                "target_residue_factor_count": 12,
                "least_target_residue_factor": 1406,
            },
        )

    def test_even_caps_are_rejected(self):
        with self.assertRaises(ValueError):
            profile.run_profile(34_090)


if __name__ == "__main__":
    unittest.main()
