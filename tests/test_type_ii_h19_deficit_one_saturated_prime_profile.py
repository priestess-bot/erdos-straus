import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_deficit_one_saturated_prime_profile",
    ROOT / "reproductions" / "type_ii_h19_deficit_one_saturated_prime_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19DeficitOneSaturatedPrimeProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json").open(encoding="utf-8") as handle:
            release = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(overflow, release), checked)

    def test_all_deficit_one_witnesses_exhaust_one_prime_and_only_some_release(self):
        with (ROOT / "reproductions" / "type-ii-h19-deficit-one-saturated-prime-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["deficit_one_high_overflow_count"], 75)
        self.assertEqual(result["later_zero_overflow_release_count"], 38)
        self.assertEqual(result["unreleased_through_r_cap_count"], 37)
        for record in result["records"]:
            m1 = (int(record["r"]) * int(record["prime"]) + 1) // 4
            q = int(record["saturated_prime"])
            a = int(record["ordinary_divisor"])
            self.assertEqual((q * a) % int(record["r"]), int(record["r"]) - 1)
            self.assertEqual(m1 % a, 0)
            self.assertNotEqual(m1 // a % q, 0)


if __name__ == "__main__":
    unittest.main()
