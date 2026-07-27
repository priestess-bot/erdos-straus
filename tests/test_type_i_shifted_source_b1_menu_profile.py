import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_shifted_source_b1_menu_profile",
    ROOT / "reproductions" / "type_i_shifted_source_b1_menu_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIShiftedSourceB1MenuProfileTests(unittest.TestCase):
    def test_one_million_residual_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-shifted-source-b1-menu-profile-1m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (3, 3))
        self.assertEqual(actual["selected_shift_histogram"], {"9": 2, "25": 1})


if __name__ == "__main__":
    unittest.main()
