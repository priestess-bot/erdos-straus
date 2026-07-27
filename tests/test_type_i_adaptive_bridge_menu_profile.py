import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_adaptive_bridge_menu_profile",
    ROOT / "reproductions" / "type_i_adaptive_bridge_menu_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIAdaptiveBridgeMenuProfileTests(unittest.TestCase):
    def test_fifty_million_final_residual_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-adaptive-bridge-menu-profile-50m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_residual_count"], actual["captured_count"]), (35, 35))
        self.assertEqual(actual["misses"], [])
        self.assertEqual(
            actual["selected_shift_histogram"],
            {"3": 2, "5": 2, "7": 2, "9": 16, "11": 1, "17": 2, "25": 7, "29": 1, "105": 2},
        )

    def test_shift_states_include_every_odd_divisor_of_E_minus_one(self):
        self.assertEqual(profile.odd_shift_states(58), ((1, 57, 58), (3, 19, 58), (19, 3, 58)))
        states = profile.odd_shift_states(676)
        self.assertEqual(len(states), 11)
        self.assertEqual(states[0], (1, 675, 52))
        self.assertEqual(states[-1], (225, 3, 52))


if __name__ == "__main__":
    unittest.main()
