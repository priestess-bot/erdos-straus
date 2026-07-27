import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_shifted_source_b1_menu_profile_10m",
    ROOT / "reproductions" / "type_i_shifted_source_b1_menu_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIShiftedSourceB1MenuProfile10MTests(unittest.TestCase):
    def test_complete_shifted_menu_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile(
            ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-10m-results.json"
        )
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (12, 5))
        self.assertEqual(
            actual["misses"],
            [1083289, 1103449, 2469289, 3389929, 3942409, 4762489, 5770249],
        )
        self.assertEqual(actual["selected_shift_histogram"], {"9": 4, "25": 1})


if __name__ == "__main__":
    unittest.main()
