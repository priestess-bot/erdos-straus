import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_first_power_forbidden_pair_boundary",
    ROOT / "reproductions" / "h19_k23_global_first_power_forbidden_pair_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23GlobalFirstPowerForbiddenPairBoundaryTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_progressions(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-first-power-forbidden-pair-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(boundary.run_audit(pressure), checked)

    def test_every_pressure_tail_has_a_forbidden_two_factor_model(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-first-power-forbidden-pair-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_family_count"], 22)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["pressure_tail_state_count"], 1_584)
        self.assertEqual(result["forbidden_pair_miss_count"], 0)
        self.assertGreater(result["minimum_forbidden_pair_count"], 0)


if __name__ == "__main__":
    unittest.main()
