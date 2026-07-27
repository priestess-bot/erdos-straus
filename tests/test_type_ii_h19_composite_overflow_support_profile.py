import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_composite_overflow_support_profile",
    ROOT / "reproductions" / "type_ii_h19_composite_overflow_support_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19CompositeOverflowSupportProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_first_r_overflow_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-composite-overflow-support-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(overflow), checked)

    def test_composite_boundary_has_only_two_three_support_states(self):
        with (ROOT / "reproductions" / "type-ii-h19-composite-overflow-support-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["composite_only_overflow_state_count"], 31)
        self.assertEqual(result["minimum_distinct_prime_support_histogram"], {"1": 16, "2": 13, "3": 2})
        self.assertEqual(result["minimum_omega_histogram"], {"2": 23, "3": 4, "4": 2, "5": 1, "6": 1})
        self.assertEqual(result["at_least_three_prime_support_state_count"], 2)
        self.assertEqual(
            [record["prime"] for record in result["at_least_three_prime_support_records"]],
            [26410609, 540645121],
        )

    def test_fixed_composite_overflow_criterion_has_a_direct_small_example(self):
        # M=44, r=15, B=4, a=11 gives g=4 and e=16.
        self.assertEqual(
            profile.fixed_overflow_witnesses(44, 15, 4),
            [{"overflow": 4, "saturated_support_part": 4, "a": 11, "g": 4, "tail_factor": 16}],
        )


if __name__ == "__main__":
    unittest.main()
