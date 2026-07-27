import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_r_release_cross_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_r_release_cross_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19ZeroOverflowRReleaseCrossProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json").open(encoding="utf-8") as handle:
            release = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-cross-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(release), checked)

    def test_later_r_releases_remain_predominantly_cross_essential(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-cross-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["later_release_state_count"], 39)
        self.assertEqual(
            result["later_release_ray_kind_histogram"],
            {"cross_essential": 57, "left_only": 6, "right_only": 4},
        )
        self.assertEqual(
            result["later_release_state_kind_set_histogram"],
            {"cross_essential": 33, "left_only": 2, "left_only,right_only": 4},
        )


if __name__ == "__main__":
    unittest.main()
