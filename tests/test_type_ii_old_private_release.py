import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_old_private_release",
    ROOT / "reproductions" / "type_ii_old_private_release.py",
)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


class TypeIIOldPrivateReleaseTests(unittest.TestCase):
    def test_small_profile(self):
        result = release.run_release_profile(10_000, 19, 50, 125)
        self.assertEqual(result["first_old_private_required_primes"], [3_361])
        self.assertEqual(result["missing_through_first_shift_cap"], [])
        self.assertEqual(result["missing_through_release_cap"], [])
        self.assertEqual(
            result["profiles"][0]["first_old_private_free_transition"],
            {
                "shift": 125,
                "witness": {
                    "h": 99,
                    "collision_multiplicity": 3,
                    "old_private_multiplicity": 0,
                    "new_multiplicity": 0,
                },
            },
        )

    def test_checked_h19_twenty_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-old-private-release-h19-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(
            result["first_old_private_required_primes"],
            [3_361, 813_121, 8_283_361, 14_847_529],
        )
        self.assertEqual(result["released_count"], 4)
        self.assertEqual(result["missing_through_first_shift_cap"], [])
        self.assertEqual(result["missing_through_release_cap"], [])
        self.assertEqual(
            {
                row["prime"]: row["first_old_private_free_transition"]["shift"]
                for row in result["profiles"]
            },
            {3_361: 125, 813_121: 56, 8_283_361: 52, 14_847_529: 72},
        )

    def test_checked_h19_hundred_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-old-private-release-h19-100m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 164)
        self.assertEqual(result["first_transition_count"], 163)
        self.assertEqual(result["missing_through_first_shift_cap"], [81_846_241])
        self.assertEqual(result["first_window_old_private_free_count"], 151)
        self.assertEqual(
            result["late_first_transition_profiles"],
            [
                {
                    "prime": 81_846_241,
                    "first_later_shift": 52,
                    "selected_witness": {
                        "h": 60_943,
                        "collision_multiplicity": 0,
                        "old_private_multiplicity": 0,
                        "new_multiplicity": 1,
                    },
                }
            ],
        )
        self.assertEqual(result["released_count"], 12)
        self.assertEqual(result["missing_through_release_cap"], [])
        self.assertEqual(result["old_private_release_missing_through_cap"], [])
        self.assertEqual(result["old_private_free_count_through_release_cap"], 164)
        self.assertEqual(max(
            row["first_old_private_free_transition"]["shift"]
            for row in result["profiles"]
        ), 125)


if __name__ == "__main__":
    unittest.main()
