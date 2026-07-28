import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mixed_terminal_dense_upper_b1_reselection_profile",
    ROOT / "reproductions" / "type_i_mixed_terminal_dense_upper_b1_reselection_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIMixedTerminalDenseUpperB1ReselectionProfileTests(unittest.TestCase):
    def test_upper_b1_reselection_closes_the_dense_residual(self):
        source_profile = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-upper-b1-reselection-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source_profile)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["stored_upper_B_eq_1_count"],
                actual["stored_lower_B_eq_1_count"],
                actual["reselected_upper_B_eq_1_count"],
                actual["upper_B_eq_1_miss_count"],
                actual["upper_B_eq_1_closure_count"],
            ),
            (247, 207, 40, 40, 0, 247),
        )
        self.assertEqual(actual["reselection_normal_forms_exhaustively_checked"], 2_331)
        self.assertEqual(actual["reselection_strict_reverse_lifts_exhaustively_checked"], 6_643)
        self.assertEqual(
            actual["reselected_upper_B_eq_1_realization_gap_exceeding_source_box_count"], 0
        )
        self.assertEqual(actual["maximum_reselected_upper_B_eq_1_realization_gap"], 87)
        self.assertEqual(actual["maximum_direct_upper_B_eq_1_gap"], 131)
        self.assertEqual(actual["maximum_selected_upper_B_eq_1_normal_gap"], 131)


if __name__ == "__main__":
    unittest.main()
