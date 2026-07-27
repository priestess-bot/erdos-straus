import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_multitier_short_shift_closure_50m",
    ROOT / "reproductions" / "type_i_multitier_short_shift_closure_50m.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIMultitierShortShiftClosure50MTests(unittest.TestCase):
    def test_composed_closure_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-multitier-short-shift-closure-50m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["core_prime_count"], actual["captured_count"]), (374903, 374903))
        self.assertEqual(
            actual["stage_histogram"],
            {
                "dyadic-p-minus-one": 359988,
                "dynamic-short-shift": 35,
                "fixed-menu-p-minus-one": 14444,
                "fixed-shifted-source-b1": 12,
                "square-allowed-low-E-p-minus-one": 424,
            },
        )
        self.assertEqual(actual["maximum_selected_E"]["E"], 20808)
        self.assertEqual(actual["maximum_selected_B"]["B"], 5564)
        self.assertEqual(actual["maximum_source_distance"]["source_distance"], 29)


if __name__ == "__main__":
    unittest.main()
