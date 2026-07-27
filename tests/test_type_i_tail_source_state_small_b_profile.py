import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_source_state_small_b_profile",
    ROOT / "reproductions" / "type_i_tail_source_state_small_b_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeITailSourceStateSmallBProfileTests(unittest.TestCase):
    def test_500m_profile_refutes_the_h19_small_b_menu(self):
        support = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-source-state-small-b-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(support)
        self.assertEqual(actual, expected)
        self.assertEqual(
            actual["least_B_histogram"],
            {"1": 1645, "2": 37, "3": 16, "4": 5, "5": 5, "7": 1, "8": 3, "9": 1, "11": 1, "14": 1, "16": 1, "17": 1},
        )
        self.assertEqual(actual["outside_H19_menu_count"], 29)
        self.assertEqual(actual["maximum_least_B_record"]["least_B_form"]["B"], 17)


if __name__ == "__main__":
    unittest.main()
