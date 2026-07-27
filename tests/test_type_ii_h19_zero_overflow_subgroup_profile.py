import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_subgroup_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_subgroup_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19ZeroOverflowSubgroupProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_subgroup_classification(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-subgroup-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(overflow), checked)

    def test_all_high_overflow_states_are_finite_exponent_not_subgroup_obstructions(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-subgroup-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_hit_count"], 649)
        self.assertEqual(
            result["classification_counts"],
            {"ordinary_divisor_hit": 558, "finite_exponent_obstruction": 91},
        )
        self.assertTrue(result["all_positive_overflow_states_have_target_in_subgroup"])


if __name__ == "__main__":
    unittest.main()
