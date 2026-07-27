import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_m39_m47_selector_profile",
    ROOT / "reproductions" / "h19_k23_m39_m47_selector_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23M39M47SelectorProfileTests(unittest.TestCase):
    def test_two_hundred_sixty_two_thousand_layer_profile(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
        ).open(encoding="utf-8") as handle:
            result = profile.run_profile(json.load(handle))
        self.assertEqual(result["m39_miss_record_count"], 97)
        self.assertTrue(result["all_branches_have_48_dividing_p_minus_one"])
        self.assertEqual(result["smooth_base_m47_selector_hit_count"], 21)
        self.assertEqual(result["one_new_prime_m47_selector_hit_count"], 39)
        self.assertEqual(result["two_new_prime_m47_selector_hit_count"], 6)
        self.assertEqual(result["m47_selector_miss_count"], 31)


if __name__ == "__main__":
    unittest.main()
