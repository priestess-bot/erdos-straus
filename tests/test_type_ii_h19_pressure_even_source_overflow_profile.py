import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pressure_even_source_overflow_profile",
    ROOT / "reproductions" / "type_ii_h19_pressure_even_source_overflow_profile.py",
)
assert SPEC and SPEC.loader
overflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = overflow
SPEC.loader.exec_module(overflow)


class H19PressureEvenSourceOverflowProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json").open(encoding="utf-8") as handle:
            small_r = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-pressure-even-source-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(overflow.run_audit(small_r), checked)

    def test_each_pressure_witness_has_a_nonoverflowing_tail(self):
        with (ROOT / "reproductions" / "type-ii-h19-pressure-even-source-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_point_count"], 4)
        self.assertTrue(result["all_minimum_overflows_are_one"])
        self.assertEqual([record["minimum_overflow"] for record in result["records"]], [1, 1, 1, 1])
        self.assertEqual([len(record["minimum_overflow_rows"]) for record in result["records"]], [1, 2, 2, 4])


if __name__ == "__main__":
    unittest.main()
