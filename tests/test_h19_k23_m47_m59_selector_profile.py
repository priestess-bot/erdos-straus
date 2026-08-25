import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPTIONAL_ARTIFACT = (
    ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
)
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_m47_m59_selector_profile",
    ROOT / "reproductions" / "h19_k23_m47_m59_selector_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23M47M59SelectorProfileTests(unittest.TestCase):
    @unittest.skipUnless(
        OPTIONAL_ARTIFACT.is_file(), "optional 262144-layer raw artifact is not tracked"
    )
    def test_two_hundred_sixty_two_thousand_layer_profile(self):
        with OPTIONAL_ARTIFACT.open(encoding="utf-8") as handle:
            result = profile.run_profile(json.load(handle))
        self.assertEqual(result["m47_miss_record_count"], 31)
        self.assertTrue(result["all_branches_have_60_dividing_p_minus_one"])
        self.assertTrue(result["all_branches_have_7_dividing_m59_u"])
        self.assertEqual(result["smooth_base_m59_selector_hit_count"], 10)
        self.assertEqual(result["one_new_prime_m59_selector_hit_count"], 14)
        self.assertEqual(result["m59_selector_miss_count"], 7)
        self.assertEqual(result["terminal_gap_histogram"], {"63": 2, "71": 3, "79": 2})


if __name__ == "__main__":
    unittest.main()
