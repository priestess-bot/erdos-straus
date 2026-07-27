import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_overflow_tail_deflation_profile",
    ROOT / "reproductions" / "type_ii_h19_overflow_tail_deflation_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19OverflowTailDeflationProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_overflow_and_quadratic_profiles(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json").open(encoding="utf-8") as handle:
            quadratic = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-overflow-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(overflow, quadratic), checked)

    def test_composite_boundary_is_mostly_closed_by_its_own_tail(self):
        with (ROOT / "reproductions" / "type-ii-h19-overflow-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["high_overflow_state_count"], 91)
        self.assertEqual(result["same_tail_deflation_state_count"], 70)
        self.assertEqual(result["r_plus_one_divides_p_minus_one_count"], 70)
        self.assertTrue(result["same_tail_deflation_is_exactly_r_divisor_condition"])
        self.assertEqual(
            result["same_tail_deflation_miss_quadratic_k_histogram"],
            {"1": 7, "2": 4, "3": 6, "4": 1, "6": 1, "7": 1, "11": 1},
        )
        self.assertEqual(result["maximum_same_tail_deflation_miss_quadratic_k"], 11)
        self.assertEqual(result["composite_only_overflow_state_count"], 31)
        self.assertEqual(result["composite_only_same_tail_deflation_count"], 25)
        self.assertEqual(result["composite_only_same_tail_deflation_miss_count"], 6)
        self.assertEqual(result["composite_only_miss_quadratic_k_histogram"], {"1": 2, "2": 1, "3": 3})
        self.assertEqual(result["maximum_composite_only_miss_quadratic_k"], 3)
        self.assertTrue(result["all_same_tail_deflation_misses_have_quadratic_external_source"])
        self.assertTrue(result["all_same_tail_deflation_misses_use_different_external_q"])
        self.assertEqual(
            [record["prime"] for record in result["composite_only_misses"]],
            [11054401, 20958961, 90527089, 113509489, 540645121, 660142081],
        )

    def test_even_source_specialization_uses_r_as_the_normal_quotient(self):
        tail = {
            "tail_factor": 7_060_200_525,
            "gap": 12_012_251,
            "overflow": 735,
            "normal_form": [1, 735, 13_069],
        }
        result = profile.tail_deflation_row(26_410_609, 2_351, tail)
        self.assertTrue(result["tail_deflation_condition_holds"])
        self.assertTrue(result["r_plus_one_divides_p_minus_one"])
        self.assertEqual(result["source_denominator"], 26_399_380)


if __name__ == "__main__":
    unittest.main()
