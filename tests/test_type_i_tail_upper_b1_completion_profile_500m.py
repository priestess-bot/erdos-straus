import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_upper_b1_completion_profile_500m",
    ROOT / "reproductions" / "type_i_tail_upper_b1_completion_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailUpperB1CompletionProfile500MTests(unittest.TestCase):
    def test_composed_upper_b1_closure_rebuilds_all_tail_misses(self):
        base = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        direct_extension = json.loads(
            (
                ROOT / "reproductions" / "type-i-direct-b1-gap-extension-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        pminus_extension = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-b1-gap-extension-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-tail-upper-b1-completion-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(base, direct_extension, pminus_extension)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["direct_upper_B_eq_1_count"],
                actual["lower_source_state_reselected_B_eq_1_count"],
                actual["lower_source_state_direct_gap_extension_count"],
                actual["direct_B_eq_1_gap_extension_count"],
                actual["upper_B_eq_1_closure_count"],
                actual["maximum_selected_B_eq_1_normal_gap"],
            ),
            (1717, 1709, 3, 1, 4, 1717, 5963),
        )
        self.assertEqual(
            [row["prime"] for row in actual["lower_source_state_reselected_records"]],
            [629_689, 58_757_449, 83_445_289],
        )
        self.assertEqual(
            actual["lower_source_state_direct_gap_extension_record"]["prime"], 218_482_009
        )


if __name__ == "__main__":
    unittest.main()
