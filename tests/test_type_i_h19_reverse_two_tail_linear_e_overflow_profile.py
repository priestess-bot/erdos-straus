import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_reverse_two_tail_linear_e_overflow_profile",
    ROOT / "reproductions" / "type_i_h19_reverse_two_tail_linear_e_overflow_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIH19ReverseTwoTailLinearEOverflowProfileTests(unittest.TestCase):
    def test_low_overflow_does_not_close_the_linear_e_residual(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile(h19, 127, 20)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["normal_form_count"], actual["strict_reverse_lift_count"]), (14_453, 44_624))
        self.assertEqual(
            {key: actual["cumulative_linear_e_captured_by_b_cap"][key] for key in map(str, range(1, 6))},
            {"1": 599, "2": 610, "3": 618, "4": 621, "5": 622},
        )
        self.assertTrue(
            all(actual["cumulative_linear_e_captured_by_b_cap"][str(b)] == 622 for b in range(6, 21))
        )
        self.assertEqual(actual["first_linear_e_b_counts"], {"1": 599, "2": 11, "3": 8, "4": 3, "5": 1})
        self.assertEqual(len(actual["misses_by_b_cap"]["20"]), 42)
        self.assertIn(334_152_361, actual["misses_by_b_cap"]["20"])
        for record in actual["records"]:
            witness = record["linear_e_witness"]
            if witness is not None:
                self.assertEqual((4 * witness["K"]) % witness["E"], 0)


if __name__ == "__main__":
    unittest.main()
