import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_short_shift_low_e_profile_50m",
    ROOT / "reproductions" / "type_i_short_shift_low_e_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIShortShiftLowEProfile50MTests(unittest.TestCase):
    def test_fifty_million_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-short-shift-low-e-b7-profile-50m-results.json").read_text(
                encoding="utf-8"
            )
        )
        shifts = (3, 5, 7, 9, 11, 17, 25, 29)
        actual = profile.run_profile(
            ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-50m-results.json",
            shifts,
            1_000_000,
            7,
        )
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (35, 35))
        self.assertEqual(
            actual["selected_shift_histogram"],
            {"3": 3, "5": 4, "7": 2, "9": 18, "11": 1, "17": 1, "25": 5, "29": 1},
        )
        self.assertEqual(actual["selected_B_histogram"], {"1": 17, "2": 4, "3": 4, "5": 6, "7": 4})

    def test_three_fixed_four_shift_obstacles_survive_larger_box(self):
        for prime in (32_499_289, 37_467_049, 43_827_529):
            self.assertIsNone(profile.first_witness(prime, (3, 7, 9, 25), 100_000_000, 64))


if __name__ == "__main__":
    unittest.main()
