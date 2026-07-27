import importlib.util
import json
import sys
import unittest
from pathlib import Path



ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_r_release_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_r_release_profile.py",
)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


class H19ZeroOverflowRReleaseProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_later_r_release_scan(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(release.run_audit(overflow), checked)

    def test_later_r_releases_some_but_not_all_high_overflow_states(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-r-release-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["r_cap"], 9999)
        self.assertEqual(result["high_overflow_first_hit_count"], 91)
        self.assertEqual(result["later_zero_overflow_release_count"], 39)
        self.assertEqual(result["unreleased_through_r_cap_count"], 52)

    def test_interval_start_preserves_the_first_r_residue_class(self):
        self.assertEqual(release.first_later_zero_overflow(564_358_369, 31, 47, 40), 47)
        self.assertIsNone(release.first_later_zero_overflow(564_358_369, 31, 39, 40))


if __name__ == "__main__":
    unittest.main()
