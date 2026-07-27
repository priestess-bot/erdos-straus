import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_divisor_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_divisor_profile.py",
)
assert SPEC and SPEC.loader
criterion = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = criterion
SPEC.loader.exec_module(criterion)


class H19ZeroOverflowDivisorProfileTests(unittest.TestCase):
    def test_artifact_matches_the_full_square_tail_overflow_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json").open(encoding="utf-8") as handle:
            bounded = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-divisor-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(criterion.run_audit(bounded, overflow), checked)

    def test_ordinary_divisor_criterion_recovers_every_and_only_zero_overflow_tail(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-divisor-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_hit_count"], 649)
        self.assertEqual(result["zero_overflow_state_count"], 558)
        self.assertEqual(result["zero_overflow_tail_count"], 1990)


if __name__ == "__main__":
    unittest.main()
