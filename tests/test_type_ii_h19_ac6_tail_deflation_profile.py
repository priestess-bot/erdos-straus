import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_ac6_tail_deflation_profile",
    ROOT / "reproductions" / "type_ii_h19_ac6_tail_deflation_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19AC6TailDeflationProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_h19_ac_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-ac6-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(input_payload, 6), checked)

    def test_every_radius_six_miss_has_a_two_tail_strict_descent(self):
        with (ROOT / "reproductions" / "type-ii-h19-ac6-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["direct_ac_short_count"], 647)
        self.assertEqual(result["direct_ac_short_miss_count"], 17)
        self.assertEqual(result["tail_deflation_captured_count"], 17)
        self.assertEqual(result["tail_deflation_missing_primes"], [])
        self.assertEqual(
            result["minimal_tail_deflation_gap_histogram"],
            {"3": 3, "7": 5, "11": 4, "15": 2, "19": 2, "27": 1},
        )
        self.assertEqual(result["maximum_minimal_tail_deflation_gap"], 27)

    def test_three_support_mixed_boundary_has_a_gap_fifteen_tail_descent(self):
        with (ROOT / "reproductions" / "type-ii-h19-ac6-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        record = next(record for record in result["records"] if record["prime"] == 942_584_161)
        self.assertEqual(
            record["tail_deflation_witness"]["gap"],
            15,
        )
        self.assertEqual(
            record["tail_deflation_witness"]["source_denominator"],
            58_911_511,
        )


if __name__ == "__main__":
    unittest.main()
