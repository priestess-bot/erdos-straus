import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_cross_half_factor_subgroup_profile",
    ROOT / "reproductions" / "type_ii_h19_cross_half_factor_subgroup_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19CrossHalfFactorSubgroupProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with audit.DEFAULT_INPUT.open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-cross-half-factor-subgroup-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(profile), checked)

    def test_cross_states_are_predominantly_one_side_support_transfers(self):
        with (ROOT / "reproductions" / "type-ii-h19-cross-half-factor-subgroup-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["cross_essential_state_count"], 184)
        self.assertEqual(result["one_side_supports_target_count"], 179)
        self.assertEqual(result["target_supporting_side_count"], 187)
        self.assertEqual(result["target_supporting_side_subgroup_saturated_count"], 0)
        self.assertEqual(result["one_side_transporter_omega_histogram"], {"1": 76, "2": 91, "3": 11, "6": 1})
        self.assertEqual(result["maximum_minimum_transporter_omega"], 6)
        self.assertEqual(result["high_overflow_state_count"], 91)
        self.assertTrue(result["all_high_overflow_states_have_joint_target_in_subgroup"])
        self.assertEqual(
            result["high_overflow_side_subgroup_kind_histogram"],
            {
                "both_external": 1,
                "both_support_target": 5,
                "left_external_right_supports": 46,
                "left_supports_right_external": 39,
            },
        )
        self.assertEqual(
            result["side_subgroup_kind_histogram"],
            {
                "both_external": 1,
                "both_support_target": 4,
                "left_external_right_supports": 67,
                "left_supports_right_external": 112,
            },
        )


if __name__ == "__main__":
    unittest.main()
