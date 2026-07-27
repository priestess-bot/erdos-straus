import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b4_prefix_profile_10m",
    ROOT / "reproductions" / "type_i_b4_prefix_profile_10m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIBFourPrefixProfile10MTests(unittest.TestCase):
    def test_checked_ten_million_summary(self):
        result = json.loads(
            (ROOT / "reproductions" / "type-i-b4-prefix-profile-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            (result["prime_limit"], result["b_cap"], result["core_prime_count"], result["captured_count"]),
            (10_000_009, 4, 82_887, 82_886),
        )
        self.assertEqual((result["misses"], result["first_miss"]), ([21169], 21169))

    def test_smaller_prefix_recomputes(self):
        result = profile.run_profile(100_009)
        self.assertEqual(
            (result["core_prime_count"], result["captured_count"], result["misses"]),
            (1181, 1180, [21169]),
        )


if __name__ == "__main__":
    unittest.main()
