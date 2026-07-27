import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_selector_boundary",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_selector_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRSelectorBoundaryTests(unittest.TestCase):
    def test_checked_one_billion_boundary_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["r_caps"], [103, 999, 9_999])
        self.assertTrue(result["all_checked_r_are_7_mod_8"])
        self.assertEqual(
            [
                (stage["r_cap"], stage["covered_count"], stage["uncovered_count"])
                for stage in result["stages"]
            ],
            [(103, 564, 100), (999, 640, 24), (9_999, 649, 15)],
        )
        self.assertEqual(result["stages"][-1]["uncovered_primes"][0], 3_361)
        self.assertEqual(result["stages"][-1]["uncovered_primes"][-1], 749_224_921)

    def test_caps_must_be_increasing_and_admissible(self):
        with self.assertRaises(ValueError):
            audit.parse_caps("999,103")
        with self.assertRaises(ValueError):
            audit.parse_caps("103,104")


if __name__ == "__main__":
    unittest.main()
