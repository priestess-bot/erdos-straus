import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mixed_terminal_dense_b1_profile",
    ROOT / "reproductions" / "type_i_mixed_terminal_dense_b1_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIMixedTerminalDenseB1ProfileTests(unittest.TestCase):
    def test_b1_profile_rebuilds_and_partitions_all_dense_tail_misses(self):
        dense = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_audit(dense)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["tail_miss_count"], actual["b_cap"], actual["captured_count"], actual["misses"]),
            (247, 1, 247, []),
        )
        self.assertEqual(actual["maximum_selected_gap"], 131)
        self.assertEqual(actual["first_hit_b_counts"], {"1": 247})
        self.assertTrue(all(record["normal_form"][1] == 1 for record in actual["records"]))


if __name__ == "__main__":
    unittest.main()
