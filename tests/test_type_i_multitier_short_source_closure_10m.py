import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_multitier_short_source_closure_10m",
    ROOT / "reproductions" / "type_i_multitier_short_source_closure_10m.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIMultitierShortSourceClosure10MTests(unittest.TestCase):
    def test_composed_closure_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-multitier-short-source-closure-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["core_prime_count"], actual["captured_count"]), (82887, 82887))
        self.assertEqual(
            actual["stage_histogram"],
            {
                "dyadic-p-minus-one": 79062,
                "fixed-menu-p-minus-one": 3673,
                "fixed-shifted-source-b1": 5,
                "short-general-source": 7,
                "square-allowed-low-E-p-minus-one": 140,
            },
        )
        self.assertEqual(actual["maximum_selected_E"]["E"], 24986)
        self.assertEqual(actual["maximum_selected_B"]["B"], 2701)
        self.assertEqual(actual["maximum_source_distance"]["source_distance"], 263)


if __name__ == "__main__":
    unittest.main()
