import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_cross_half_factor_complexity",
    ROOT / "reproductions" / "type_ii_h19_cross_half_factor_complexity.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19CrossHalfFactorComplexityTests(unittest.TestCase):
    def test_artifact_rebuilds_exactly(self):
        with (ROOT / "reproductions" / "type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json").open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-cross-half-factor-complexity-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(audit.run_audit(profile), checked)

    def test_cross_essential_witnesses_are_not_all_bilinear_prime_pairs(self):
        with (ROOT / "reproductions" / "type-ii-h19-cross-half-factor-complexity-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["cross_essential_state_count"], 184)
        self.assertEqual(
            result["minimum_cross_omega_histogram"],
            {"2": 21, "3": 93, "4": 53, "5": 13, "6": 2, "7": 2},
        )
        self.assertEqual(result["maximum_minimum_cross_omega"], 7)
        for record in result["records"]:
            self.assertGreater(int(record["left_divisor"]), 1)
            self.assertGreater(int(record["right_divisor"]), 1)
            self.assertEqual(
                int(record["minimum_cross_omega"]),
                audit.omega(int(record["left_divisor"])) + audit.omega(int(record["right_divisor"])),
            )


if __name__ == "__main__":
    unittest.main()
