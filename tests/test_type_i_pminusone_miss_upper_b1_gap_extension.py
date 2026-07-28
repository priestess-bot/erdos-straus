import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_miss_upper_b1_gap_extension",
    ROOT / "reproductions" / "type_i_pminusone_miss_upper_b1_gap_extension.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIPMinusOneMissUpperB1GapExtensionTests(unittest.TestCase):
    def test_four_gap_extension_releases_the_last_short_box_b1_miss(self):
        source_profile = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-b3-reselection-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-b1-gap-extension-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source_profile)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_minus_one_residual_count"],
                actual["initial_upper_B_eq_1_source_state_closure_count"],
                actual["extension_released_count"],
                actual["upper_B_eq_1_source_state_closure_count"],
                actual["upper_B_eq_1_unresolved_count"],
            ),
            (185, 184, 1, 185, 0),
        )
        self.assertEqual(actual["maximum_prior_upper_B_eq_1_realization_gap"], 597_803)
        record = actual["extension_records"]
        self.assertEqual(len(record), 1)
        self.assertEqual(record[0]["prime"], 218_482_009)
        self.assertEqual(record[0]["first_upper_B_eq_1_gap_in_extension"], 231)
        self.assertEqual(len(record[0]["first_gap_upper_B_eq_1_candidates"]), 3)
        self.assertEqual(
            record[0]["selected_first_gap_upper_B_eq_1_candidate"]["source_distance"], 43
        )


if __name__ == "__main__":
    unittest.main()
