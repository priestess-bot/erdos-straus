import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_small_b_tail_deflation_profile",
    ROOT / "reproductions" / "type_i_small_b_tail_deflation_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeISmallBTailDeflationProfileTests(unittest.TestCase):
    def test_small_profile(self):
        result = profile.run_profile(1_000, 23, 4)
        self.assertEqual(result["core_prime_count"], 14)
        self.assertEqual(result["captured_count"], 14)
        self.assertEqual(result["misses"], [])
        self.assertEqual(result["first_joint_b_counts"], {"1": 12, "2": 1, "3": 1})

    def test_checked_twenty_million_artifact_summary(self):
        with (
            ROOT / "reproductions" / "type-i-small-b-tail-deflation-20m-profile.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 20_000_000)
        self.assertEqual(result["gap_cap"], 239)
        self.assertEqual(result["b_cap"], 4)
        self.assertEqual(result["core_prime_count"], 158_595)
        self.assertEqual(result["captured_count"], 156_239)
        self.assertEqual(len(result["misses"]), 2_356)
        self.assertEqual(
            result["first_joint_b_counts"],
            {"1": 153_784, "2": 969, "3": 1_332, "4": 154},
        )


if __name__ == "__main__":
    unittest.main()
