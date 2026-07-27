import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pressure_small_r_profile",
    ROOT / "reproductions" / "type_ii_h19_pressure_small_r_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19PressureSmallRProfileTests(unittest.TestCase):
    def test_checked_one_billion_pressure_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 103)
        self.assertEqual(result["quadratic_descent_miss_count"], 4)
        self.assertEqual(result["unclosed_through_r_cap"], [])
        self.assertEqual(
            [
                (
                    row["prime"],
                    row["first_small_r_tail_hit"]["r"],
                    row["first_small_r_tail_hit"]["compatible_rays"][0]["distance"],
                )
                for row in result["records"]
            ],
            [
                (35_840_809, 103, 7),
                (132_285_169, 31, 3),
                (141_326_089, 31, 3),
                (640_775_689, 15, 34_091),
            ],
        )

    def test_invalid_r_cap_is_rejected(self):
        with self.assertRaises(ValueError):
            profile.run_audit({}, 102)


if __name__ == "__main__":
    unittest.main()
