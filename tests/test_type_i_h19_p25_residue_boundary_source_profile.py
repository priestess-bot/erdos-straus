import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_p25_residue_boundary_source_profile",
    ROOT / "reproductions" / "type_i_h19_p25_residue_boundary_source_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19P25ResidueBoundarySourceProfileTests(unittest.TestCase):
    def test_source_state_profile_rebuilds_and_uses_source_square_bridges(self):
        variable = json.loads(
            (ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        support = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-p25-residue-boundary-source-profile-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(variable, support)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["source_state_histogram"], {"p_minus_1": 21, "shifted": 7})
        self.assertEqual(actual["normal_B_histogram"], {"B_eq_1": 23, "B_gt_1": 5})
        self.assertTrue(actual["all_bridge_factors_divide_source_square"])
        self.assertTrue(actual["all_bridge_conditions_match_normalized_source_square"])
        self.assertTrue(
            all(
                record["bridge_factor"]
                and record["source_denominator"] ** 2 % record["bridge_factor"] == 0
                for record in actual["records"]
            )
        )
        self.assertTrue(
            all(
                (
                    int(edge["reverse_two_tail_lift"]["source_denominator"]) ** 2
                    // math.gcd(int(edge["E"]), 4)
                )
                % int(edge["E"])
                == 0
                for record in support["records"]
                for edge in [record["selected_edge"]]
            )
        )
        self.assertTrue(
            all(
                (record["source_denominator"] ** 2 // record["source_square_normalizer"])
                % record["bridge_factor"]
                == 0
                for record in actual["records"]
            )
        )


if __name__ == "__main__":
    unittest.main()
