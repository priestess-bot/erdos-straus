import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_pure_new_factor_release",
    ROOT / "reproductions" / "type_ii_pure_new_factor_release.py",
)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


class TypeIIPureNewFactorReleaseTests(unittest.TestCase):
    def test_ten_million_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-pure-new-factor-release-h19-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 34)
        self.assertEqual(result["pure_new_release_count"], 32)
        self.assertEqual(result["missing_through_cap"], [345_601, 9_744_001])
        self.assertEqual(result["maximum_first_pure_new_shift"], 121)

    def test_two_hundred_million_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-pure-new-factor-release-h19-200m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 199)
        self.assertEqual(result["pure_new_release_count"], 193)
        self.assertEqual(
            result["missing_through_cap"],
            [345_601, 9_744_001, 55_722_241, 92_421_169, 178_400_041, 192_369_241],
        )
        self.assertEqual(result["maximum_first_pure_new_shift"], 192)
        record = next(row for row in result["profiles"] if row["prime"] == 29_060_641)
        self.assertEqual(record["first_pure_new_shift"], 192)
        self.assertEqual(record["selected_witness"]["collision_multiplicity"], 0)

    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-pure-new-factor-release-h19-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["new_factor_state_count"], 260)
        self.assertEqual(result["pure_new_release_count"], 253)
        self.assertEqual(
            result["missing_through_cap"],
            [
                345_601,
                9_744_001,
                55_722_241,
                92_421_169,
                178_400_041,
                192_369_241,
                283_163_161,
            ],
        )
        self.assertEqual(result["maximum_first_pure_new_shift"], 200)
        record = next(row for row in result["profiles"] if row["prime"] == 258_662_881)
        self.assertEqual(record["first_pure_new_shift"], 200)


if __name__ == "__main__":
    unittest.main()
