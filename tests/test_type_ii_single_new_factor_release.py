import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_single_new_factor_release",
    ROOT / "reproductions" / "type_ii_single_new_factor_release.py",
)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


class TypeIISingleNewFactorReleaseTests(unittest.TestCase):
    def test_small_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-single-new-factor-release-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["multi_new_first_count"], 4)
        self.assertEqual(result["one_new_release_count"], 4)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            {row["prime"]: row["first_one_new_shift"] for row in result["profiles"]},
            {1_127_281: 41, 4_722_169: 96, 7_378_849: 29, 8_955_769: 35},
        )

    def test_two_hundred_million_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-single-new-factor-release-h19-200m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["multi_new_first_count"], 26)
        self.assertEqual(result["one_new_release_count"], 26)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(max(row["first_one_new_shift"] for row in result["profiles"]), 96)
        record = next(row for row in result["profiles"] if row["prime"] == 113_509_489)
        self.assertEqual(record["first_multi_new_multiplicity"], 3)
        self.assertEqual(record["first_one_new_shift"], 38)
        self.assertEqual(record["selected_witness"]["new_multiplicity"], 1)

    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-single-new-factor-release-h19-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["multi_new_first_count"], 37)
        self.assertEqual(result["one_new_release_count"], 37)
        self.assertEqual(result["missing_through_cap"], [])
        record = max(result["profiles"], key=lambda row: row["first_one_new_shift"])
        self.assertEqual(record["prime"], 4_722_169)
        self.assertEqual(record["first_one_new_shift"], 96)


if __name__ == "__main__":
    unittest.main()
