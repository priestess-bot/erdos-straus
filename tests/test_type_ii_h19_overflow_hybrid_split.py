import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_overflow_hybrid_split",
    ROOT / "reproductions" / "type_ii_h19_overflow_hybrid_split.py",
)
assert SPEC and SPEC.loader
split = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = split
SPEC.loader.exec_module(split)


class H19OverflowHybridSplitTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_join_of_the_two_profiles(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json").open(encoding="utf-8") as handle:
            quadratic = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-overflow-hybrid-split-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(split.run_audit(overflow, quadratic), checked)

    def test_high_overflow_and_r_uncovered_states_are_standard_closed(self):
        with (ROOT / "reproductions" / "type-ii-h19-overflow-hybrid-split-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["high_overflow_first_hit_count"], 91)
        self.assertEqual(result["r_uncovered_count"], 15)
        self.assertEqual(result["quadratic_external_descent_miss_count"], 4)
        self.assertTrue(result["all_high_overflow_have_quadratic_descent"])
        self.assertTrue(result["all_r_uncovered_have_quadratic_descent"])
        self.assertTrue(result["all_quadratic_misses_have_zero_overflow_first_hit"])
        self.assertEqual(result["maximum_high_overflow_quadratic_k"], 20)
        self.assertEqual(
            result["high_overflow_quadratic_k_histogram"],
            {"1": 29, "2": 15, "3": 21, "4": 4, "5": 6, "6": 2, "7": 5, "8": 2, "9": 1, "11": 1, "12": 1, "15": 3, "20": 1},
        )


if __name__ == "__main__":
    unittest.main()
