import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_min_nonbase_factor_boundary",
    ROOT / "reproductions" / "h19_k23_global_min_nonbase_factor_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23GlobalMinNonbaseFactorBoundaryTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_final_first_power_profile(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-first-power-tail-reroute-2097152.json"
        ).open(encoding="utf-8") as handle:
            reroutes = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-min-nonbase-factor-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(boundary.run_audit(profile, reroutes), checked)

    def test_least_nonbase_prime_rule_has_substantial_finite_failure_set(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-min-nonbase-factor-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_final_one_support_count"], 5_128)
        self.assertEqual(result["least_nonbase_prime_works_count"], 3_685)
        self.assertEqual(result["least_nonbase_prime_fails_count"], 1_443)
        self.assertEqual(len(result["failures"]), 1_443)


if __name__ == "__main__":
    unittest.main()
