import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_source_state_b1_overflow_profile",
    ROOT / "reproductions" / "type_i_source_state_b1_overflow_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeISourceStateB1OverflowProfileTests(unittest.TestCase):
    def test_b1_misses_reach_the_target_with_one_or_two_extra_exponents(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        tail = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-source-state-b1-overflow-profile-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(h19, tail)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["total_B_eq_1_miss_count"], 89)
        self.assertEqual(actual["total_least_extra_exponent_histogram"], {"1": 81, "2": 8})
        self.assertEqual(actual["maximum_extra_exponent_count"], 2)
        self.assertEqual(
            [profile["least_extra_exponent_histogram"] for profile in actual["profiles"]],
            [{"1": 15, "2": 2}, {"1": 66, "2": 6}],
        )


if __name__ == "__main__":
    unittest.main()
