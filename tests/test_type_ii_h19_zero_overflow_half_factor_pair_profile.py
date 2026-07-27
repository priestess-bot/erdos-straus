import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_zero_overflow_half_factor_pair_profile",
    ROOT / "reproductions" / "type_ii_h19_zero_overflow_half_factor_pair_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19ZeroOverflowHalfFactorPairProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-selector-boundary-1b-results.json").open(encoding="utf-8") as handle:
            selector = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-bounded-r-overflow-profile-1b-results.json").open(encoding="utf-8") as handle:
            overflow = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(selector, overflow), checked)

    def test_cross_half_factor_criterion_recovers_exactly_the_zero_overflow_states(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_r_state_count"], 649)
        self.assertEqual(result["cross_half_factor_zero_overflow_count"], 558)
        self.assertEqual(result["cross_half_factor_high_overflow_count"], 91)
        self.assertEqual(
            result["zero_overflow_kind_histogram"],
            {"left_only": 89, "right_only": 279, "both_sides": 6, "cross_essential": 184, "none": 91},
        )
        for record in result["records"]:
            a, b = int(record["left_half_factor"]), int(record["right_half_factor"])
            self.assertEqual(a * b, (int(record["r"]) * int(record["prime"]) + 1) // 4)
            if record["zero_overflow"]:
                divisor = int(record["ordinary_divisor"])
                self.assertEqual(divisor, int(record["left_divisor"]) * int(record["right_divisor"]))
                self.assertEqual(divisor % int(record["r"]), int(record["r"]) - 1)
                self.assertEqual(a * b % divisor, 0)
                if record["zero_overflow_kind"] == "cross_essential":
                    self.assertFalse(record["left_half_factor_hits_target"])
                    self.assertFalse(record["right_half_factor_hits_target"])


if __name__ == "__main__":
    unittest.main()
