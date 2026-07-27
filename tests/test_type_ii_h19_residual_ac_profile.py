import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_residual_ac_profile",
    ROOT / "reproductions" / "type_ii_h19_residual_ac_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19ResidualACProfileTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_stored_h19_residual_profile(self):
        with (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(input_payload, 9), checked)

    def test_radius_nine_captures_every_stored_h19_residual(self):
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["direct_ac_captured_count"], 664)
        self.assertEqual(result["direct_ac_missing_primes"], [])
        self.assertEqual(
            result["minimal_ac_radius_histogram"],
            {"3": 148, "4": 282, "5": 189, "6": 28, "7": 11, "8": 4, "9": 2},
        )
        self.assertEqual(result["maximum_minimal_ac_radius"], 9)

    def test_radius_eight_has_exactly_two_stored_counterexamples(self):
        self.assertIsNone(profile.direct_ac_witness(165_479_161, 8))
        self.assertIsNone(profile.direct_ac_witness(633_393_601, 8))
        self.assertEqual(
            profile.run_audit(
                json.loads(
                    (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(encoding="utf-8")
                ),
                9,
            )["previous_radius_missing_primes"],
            [165_479_161, 633_393_601],
        )


if __name__ == "__main__":
    unittest.main()
