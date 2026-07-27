import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_short_shift_low_e_profile",
    ROOT / "reproductions" / "type_i_short_shift_low_e_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIShortShiftLowEProfileTests(unittest.TestCase):
    def test_ten_million_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-short-shift-low-e-profile-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (7, 7))
        self.assertEqual(actual["shifts"], [3, 7, 9, 25])

    def test_twenty_million_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-short-shift-low-e-b7-profile-20m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile(
            ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-20m-results.json",
            profile.SHIFTS,
            1_000_000,
            7,
        )
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (18, 18))
        self.assertEqual(actual["selected_B_histogram"], {"1": 7, "2": 2, "3": 2, "5": 3, "7": 4})


if __name__ == "__main__":
    unittest.main()
