import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_small_b_profile",
    ROOT / "reproductions" / "type_i_tail_reverse_small_b_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailReverseSmallBProfileTests(unittest.TestCase):
    @staticmethod
    def tail_payload():
        return json.loads((ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json").read_text(encoding="utf-8"))

    def test_bounded_b_five_profile_rebuilds_and_closes_all_tail_misses(self):
        expected = json.loads((ROOT / "reproductions" / "type-i-tail-reverse-small-b5-500m-results.json").read_text(encoding="utf-8"))
        actual = profile.run_profile(self.tail_payload(), 127, 5)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["tail_miss_count"], actual["captured_count"], actual["misses"]), (1_717, 1_717, []))
        self.assertEqual(actual["maximum_selected_gap"], 127)
        self.assertTrue(all(record["normal_form"][1] <= 5 for record in actual["records"]))

    def test_bounded_b_four_has_one_exact_residual(self):
        expected = json.loads((ROOT / "reproductions" / "type-i-tail-reverse-small-b4-500m-results.json").read_text(encoding="utf-8"))
        actual = profile.run_profile(self.tail_payload(), 127, 4)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["misses"], [36_851_929])
        self.assertEqual(actual["captured_count"], 1_716)

    def test_lower_b_residual_hierarchy_has_two_discrete_jumps(self):
        tail = self.tail_payload()
        b1 = profile.run_profile(tail, 127, 1)
        b2 = profile.run_profile(tail, 127, 2)
        b3 = profile.run_profile(tail, 127, 3)
        self.assertEqual(b1["misses"], [
            17_137_129,
            22_283_881,
            36_851_929,
            39_407_449,
            51_531_769,
            147_199_369,
            151_911_769,
            193_288_489,
            222_416_329,
            338_356_489,
        ])
        self.assertEqual(b2["misses"], [36_851_929, 193_288_489])
        self.assertEqual(b3["misses"], b2["misses"])
        self.assertEqual(
            [b1["captured_count"], b2["captured_count"], b3["captured_count"]],
            [1_707, 1_715, 1_715],
        )


if __name__ == "__main__":
    unittest.main()
