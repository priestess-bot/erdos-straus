import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_b1_source_state_boundary",
    ROOT / "reproductions" / "type_i_h19_b1_source_state_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19B1SourceStateBoundaryTests(unittest.TestCase):
    def test_b1_profile_rebuilds_from_all_h19_even_bridges(self):
        support = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-b1-source-state-boundary-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(support)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["h19_even_bridge_count"], actual["B_eq_1_realization_count"], actual["B_eq_1_miss_count"]),
            (664, 647, 17),
        )
        self.assertEqual(
            (
                actual["p_eq_25_mod_48_count"],
                actual["p_eq_25_mod_48_B_eq_1_realization_count"],
                len(actual["p_eq_25_mod_48_B_eq_1_misses"]),
            ),
            (243, 237, 6),
        )


if __name__ == "__main__":
    unittest.main()
