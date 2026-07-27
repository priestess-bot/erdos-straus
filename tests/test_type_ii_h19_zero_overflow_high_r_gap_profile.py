import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_high_r_gap_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_high_r_gap_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19ZeroOverflowHighRGapProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with audit.DEFAULT_BASE.open(encoding="utf-8") as handle:
            base = json.load(handle)
        intervals = []
        for path in audit.DEFAULT_INTERVALS:
            with path.open(encoding="utf-8") as handle:
                intervals.append(json.load(handle))
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-high-r-gap-profile-1b-r99999-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(base, intervals), checked)

    def test_no_new_release_occurs_between_10007_and_99999(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-high-r-gap-profile-1b-r99999-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["high_overflow_first_hit_count"], 91)
        self.assertEqual(result["initial_r_cap"], 9999)
        self.assertEqual(result["initial_later_release_count"], 39)
        self.assertEqual(result["additional_release_count_in_high_r_gap"], 0)
        self.assertEqual(result["cumulative_r_cap"], 99999)
        self.assertEqual(result["cumulative_later_zero_overflow_release_count"], 39)
        self.assertEqual(result["cumulative_unreleased_count"], 52)
        self.assertEqual(len(result["intervals"]), 9)


if __name__ == "__main__":
    unittest.main()
