import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_exponent_deficit",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_exponent_deficit.py",
)
assert SPEC and SPEC.loader
deficit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = deficit
SPEC.loader.exec_module(deficit)


class H19ZeroOverflowExponentDeficitTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_deficit_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-exponent-deficit-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(deficit.run_audit(overflow), checked)

    def test_every_stored_high_overflow_state_is_within_four_support_prime_repetitions(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-exponent-deficit-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_hit_count"], 649)
        self.assertEqual(result["exponent_deficit_histogram"], {"0": 558, "1": 75, "2": 13, "3": 2, "4": 1})
        self.assertEqual(result["maximum_exponent_deficit"], 4)


if __name__ == "__main__":
    unittest.main()
