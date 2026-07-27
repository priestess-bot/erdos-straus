import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_m27_m31_selector_profile",
    ROOT / "reproductions" / "h19_k23_m27_m31_selector_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23M27M31SelectorProfileTests(unittest.TestCase):
    def test_two_hundred_sixty_two_thousand_layer_profile(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
        ).open(encoding="utf-8") as handle:
            result = profile.run_profile(json.load(handle))
        self.assertEqual(result["residual_branch_count"], 14)
        self.assertTrue(result["all_branches_have_32_dividing_p_minus_one"])
        self.assertEqual(result["m27_alternative_record_count"], 1_490)
        self.assertEqual(result["m31_selector_hit_count"], 1_088)
        self.assertTrue(result["all_branches_have_133_dividing_u"])
        self.assertEqual(result["fixed_m31_factor"], 1_132_096)
        self.assertEqual(result["fixed_m31_selector_hit_count"], 667)
        self.assertEqual(result["variable_m31_selector_hit_count"], 421)
        self.assertEqual(result["one_new_prime_m31_selector_hit_count"], 421)
        self.assertEqual(result["one_new_prime_selector_miss_count"], 402)
        self.assertEqual(result["m31_selector_miss_count"], 402)
        self.assertEqual(
            result["later_tail_gap_histogram"],
            {"35": 221, "39": 84, "47": 66, "59": 24, "63": 2, "71": 3, "79": 2},
        )


if __name__ == "__main__":
    unittest.main()
