import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_miss_source_overflow_profile",
    ROOT / "reproductions" / "type_i_pminusone_miss_source_overflow_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIPMinusOneMissSourceOverflowProfileTests(unittest.TestCase):
    def test_shortest_source_states_exhibit_a_three_repeat_boundary(self):
        source_profile = json.loads(
            (ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-source-overflow-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source_profile)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["p_minus_one_residual_count"], 185)
        self.assertEqual(
            (
                actual["B_eq_1_realization_count"],
                actual["B_eq_1_miss_count"],
                actual["B_eq_1_subgroup_obstruction_count"],
                actual["B_eq_1_finite_product_obstruction_count"],
            ),
            (119, 66, 0, 66),
        )
        self.assertEqual(actual["least_extra_exponent_histogram"], {"1": 63, "2": 2, "3": 1})
        self.assertEqual(actual["maximum_extra_exponent_count"], 3)
        self.assertEqual(actual["maximum_extra_exponent_record"]["prime"], 229_474_249)
        self.assertEqual(actual["maximum_extra_exponent_record"]["least_realization_B"], 12)


if __name__ == "__main__":
    unittest.main()
