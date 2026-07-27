import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_small_gap_profile",
    ROOT / "reproductions" / "type_i_small_gap_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeISmallGapProfileTests(unittest.TestCase):
    def test_small_profile(self):
        result = profile.run_profile(1_000, 23)
        self.assertEqual(result["core_prime_count"], 14)
        self.assertEqual(result["captured_count"], 14)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["maximum_first_gap"], 7)
        self.assertEqual(result["first_gap_counts"], {"3": 5, "7": 9})

    def test_checked_ten_million_artifact_summary(self):
        with (ROOT / "reproductions" / "type-i-small-gap-10m-profile.json").open(
            encoding="utf-8"
        ) as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["captured_count"], 82_887)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["maximum_first_gap"], 151)
        self.assertEqual(result["first_gap_counts"]["151"], 1)
        self.assertEqual(
            result["first_gap_examples"]["151"],
            {
                "prime": 8_803_369,
                "divisor": 180_472_160,
                "first_denominator": 2_200_880,
            },
        )


if __name__ == "__main__":
    unittest.main()
