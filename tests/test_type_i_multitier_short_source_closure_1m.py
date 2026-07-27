import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_multitier_short_source_closure_1m",
    ROOT / "reproductions" / "type_i_multitier_short_source_closure_1m.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIMultitierShortSourceClosure1MTests(unittest.TestCase):
    def test_composed_closure_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-multitier-short-source-closure-1m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["core_prime_count"], actual["captured_count"]), (9732, 9732))
        self.assertEqual(
            actual["stage_histogram"],
            {
                "dyadic-p-minus-one": 9149,
                "fixed-menu-p-minus-one": 555,
                "square-allowed-low-E-p-minus-one": 25,
                "short-general-source": 3,
            },
        )
        self.assertEqual(actual["maximum_selected_E"], {"prime": 187009, "stage": "square-allowed-low-E-p-minus-one", "E": 576, "B": 39, "source_distance": 1})
        self.assertEqual(actual["maximum_selected_B"], {"prime": 645481, "stage": "square-allowed-low-E-p-minus-one", "E": 60, "B": 435, "source_distance": 1})
        self.assertEqual(actual["maximum_source_distance"], {"prime": 297049, "stage": "short-general-source", "E": 476, "B": 1, "source_distance": 25})


if __name__ == "__main__":
    unittest.main()
