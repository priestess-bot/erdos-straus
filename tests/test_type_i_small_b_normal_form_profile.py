import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_small_b_normal_form_profile",
    ROOT / "reproductions" / "type_i_small_b_normal_form_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeISmallBNormalFormProfileTests(unittest.TestCase):
    def test_small_profile(self):
        result = profile.run_profile(1_000, 23, 3)
        self.assertEqual(result["core_prime_count"], 14)
        self.assertEqual(result["captured_count"], 14)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["minimum_b_counts"], {"1": 14})

    def test_checked_twenty_million_artifact_summary(self):
        with (
            ROOT / "reproductions" / "type-i-small-b-normal-form-20m-profile.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 20_000_000)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["b_cap"], 4)
        self.assertEqual(result["core_prime_count"], 158_595)
        self.assertEqual(result["captured_count"], 158_595)
        self.assertEqual(result["misses"], [])
        self.assertEqual(
            result["minimum_b_counts"], {"1": 158_590, "2": 2, "3": 2, "4": 1}
        )
        self.assertEqual(len(result["non_b_one_witnesses"]), 5)
        b_four = [
            witness
            for witness in result["non_b_one_witnesses"]
            if witness["b"] == 4
        ]
        self.assertEqual(len(b_four), 1)
        self.assertEqual(b_four[0]["prime"], 16_337_281)

    def test_checked_one_hundred_million_artifact_summary(self):
        with (
            ROOT / "reproductions" / "type-i-small-b-normal-form-100m-profile.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000_000)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["b_cap"], 8)
        self.assertEqual(result["core_prime_count"], 719_781)
        self.assertEqual(result["captured_count"], 719_781)
        self.assertEqual(result["misses"], [])
        self.assertEqual(
            result["minimum_b_counts"], {"1": 719_770, "2": 7, "3": 3, "4": 1}
        )
        self.assertEqual(len(result["non_b_one_witnesses"]), 11)
        self.assertTrue(
            all(
                witness["normal_tail_deflation_source"] is None
                for witness in result["non_b_one_witnesses"]
            )
        )


if __name__ == "__main__":
    unittest.main()
