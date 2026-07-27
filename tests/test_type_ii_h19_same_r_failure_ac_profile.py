import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_same_r_failure_ac_profile",
    ROOT / "reproductions" / "type_ii_h19_same_r_failure_ac_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19SameRFailureACProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_same_r_external_source_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-overflow-tail-deflation-profile-1b-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-same-r-failure-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(input_payload, 6), checked)

    def test_all_same_r_failures_have_a_direct_ac_certificate_by_radius_six(self):
        with (ROOT / "reproductions" / "type-ii-h19-same-r-failure-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["same_r_external_source_miss_count"], 21)
        self.assertEqual(result["direct_ac_captured_count"], 21)
        self.assertEqual(result["direct_ac_missing_primes"], [])
        self.assertEqual(result["minimal_ac_radius_histogram"], {"3": 7, "4": 6, "5": 4, "6": 4})
        self.assertEqual(result["maximum_minimal_ac_radius"], 6)

    def test_radius_six_is_necessary_for_the_stored_boundary(self):
        self.assertIsNone(profile.direct_ac_witness(540_645_121, 5))
        witness = profile.direct_ac_witness(540_645_121, 6)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            {key: witness[key] for key in ("radius", "a", "c", "k", "h", "gap", "divisor")},
            {"radius": 6, "a": 6, "c": 6, "k": 12, "h": 1727, "gap": 313055, "divisor": 216},
        )


if __name__ == "__main__":
    unittest.main()
