import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_overflow_profile",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_overflow_profile.py",
)
assert SPEC and SPEC.loader
overflow = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = overflow
SPEC.loader.exec_module(overflow)


class H19BoundedROverflowProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_first_hit_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json").open(encoding="utf-8") as handle:
            bounded_r = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(overflow.run_audit(bounded_r), checked)

    def test_zero_overflow_is_common_but_not_universal_through_the_stored_cap(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_hit_count"], 649)
        self.assertEqual(result["uncovered_count"], 15)
        self.assertEqual(result["zero_overflow_count"], 558)
        self.assertEqual(result["positive_overflow_count"], 91)
        self.assertEqual(result["maximum_minimum_overflow"], 4563)


if __name__ == "__main__":
    unittest.main()
