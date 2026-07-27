import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_source_state_small_b_profile",
    ROOT / "reproductions" / "type_i_h19_source_state_small_b_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19SourceStateSmallBProfileTests(unittest.TestCase):
    def test_minimum_b_profile_rebuilds_for_all_h19_source_states(self):
        support = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-source-state-small-b-profile-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(support)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["least_B_histogram"], {"1": 647, "2": 12, "4": 2, "7": 2, "13": 1})
        self.assertEqual(actual["p_eq_25_mod_48_least_B_histogram"], {"1": 237, "2": 4, "4": 2})
        self.assertEqual(actual["maximum_least_B_record"]["least_B_form"]["B"], 13)
        self.assertEqual(actual["p_eq_25_mod_48_maximum_least_B_record"]["least_B_form"]["B"], 4)


if __name__ == "__main__":
    unittest.main()
