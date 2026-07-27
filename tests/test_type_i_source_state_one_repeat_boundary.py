import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_source_state_one_repeat_boundary",
    ROOT / "reproductions" / "type_i_source_state_one_repeat_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeISourceStateOneRepeatBoundaryTests(unittest.TestCase):
    def test_one_repeat_closes_all_but_eight_cross_sample_b1_misses(self):
        overflow = json.loads(
            (ROOT / "reproductions" / "type-i-source-state-b1-overflow-profile-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-source-state-one-repeat-boundary-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(overflow)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["total_two_repeat_boundary_count"], 8)
        self.assertEqual(
            [
                (
                    profile["B_eq_1_or_one_repeat_count"],
                    profile["two_repeat_boundary_count"],
                )
                for profile in actual["profiles"]
            ],
            [(662, 2), (1711, 6)],
        )


if __name__ == "__main__":
    unittest.main()
