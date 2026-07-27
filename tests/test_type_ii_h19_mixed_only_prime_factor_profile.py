import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_mixed_only_prime_factor_profile",
    ROOT / "reproductions" / "type_ii_h19_mixed_only_prime_factor_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19MixedOnlyPrimeFactorProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_mixed_only_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-mixed-short-or-descent-1b-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-mixed-only-prime-factor-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(input_payload), checked)

    def test_four_mixed_only_states_escape_every_one_prime_selector(self):
        with (ROOT / "reproductions" / "type-ii-h19-mixed-only-prime-factor-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["mixed_factor_only_count"], 17)
        self.assertEqual(result["one_prime_mixed_captured_count"], 13)
        self.assertEqual(
            result["minimum_distinct_prime_support_histogram"],
            {"1": 13, "2": 3, "3": 1},
        )
        self.assertEqual(result["two_prime_mixed_missing_primes"], [942_584_161])
        self.assertEqual(
            result["one_prime_mixed_missing_primes"],
            [6_868_801, 107_158_921, 165_479_161, 942_584_161],
        )
        self.assertEqual(
            {
                record["prime"]: record["stored_factor_factorization"]
                for record in result["composite_factor_required_records"]
            },
            {
                6_868_801: {"3": 1, "1019": 1},
                107_158_921: {"2": 2, "1433": 1},
                165_479_161: {"7": 1, "19": 1, "43": 1},
                942_584_161: {"5": 1, "73": 1, "337": 1},
            },
        )


if __name__ == "__main__":
    unittest.main()
