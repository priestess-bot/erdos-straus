import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_miss_upper_b3_reselection_profile",
    ROOT / "reproductions" / "type_i_pminusone_miss_upper_b3_reselection_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIPMinusOneMissUpperB3ReselectionProfileTests(unittest.TestCase):
    def test_source_reselection_releases_all_but_one_upper_b1_state(self):
        source_profile = json.loads(
            (ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-b3-reselection-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source_profile)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_minus_one_residual_count"],
                actual["stored_upper_B_eq_1_count"],
                actual["reselected_upper_B_eq_1_count"],
                actual["upper_B_eq_1_miss_count"],
                actual["upper_B_le_3_closure_count"],
            ),
            (185, 119, 65, 1, 185),
        )
        self.assertEqual(actual["upper_B_eq_1_realization_gap_exceeding_source_box_count"], 26)
        self.assertEqual(actual["maximum_upper_B_eq_1_realization_gap"], 597_803)
        miss = actual["upper_B_eq_1_misses"]
        self.assertEqual(len(miss), 1)
        self.assertEqual(miss[0]["prime"], 218_482_009)
        self.assertEqual(miss[0]["least_upper_realization"]["realization"]["B"], 3)


if __name__ == "__main__":
    unittest.main()
