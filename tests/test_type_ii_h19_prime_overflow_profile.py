import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_prime_overflow_profile",
    ROOT / "reproductions" / "type_ii_h19_prime_overflow_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19PrimeOverflowProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_first_r_overflow_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-prime-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(overflow), checked)

    def test_prime_overflow_criterion_leaves_a_strictly_smaller_composite_boundary(self):
        with (ROOT / "reproductions" / "type-ii-h19-prime-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["high_overflow_state_count"], 91)
        self.assertEqual(result["prime_overflow_state_count"], 60)
        self.assertEqual(result["composite_only_overflow_state_count"], 31)
        self.assertEqual(result["minimum_overflow_is_prime_count"], 49)

    def test_prime_overflow_criterion_has_a_direct_small_example(self):
        # M=10, r=7, q=2, a=5 gives e=q*(M/a)=4 and overflow q.
        self.assertEqual(
            profile.prime_overflow_witnesses(10, 7),
            [{"overflow_prime": 2, "a": 5, "g": 2, "tail_factor": 4}],
        )


if __name__ == "__main__":
    unittest.main()
