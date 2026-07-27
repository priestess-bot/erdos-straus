import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_dynamic_scale_seed_profile",
    ROOT / "reproductions" / "h19_k23_pressure_dynamic_scale_seed_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23PressureDynamicScaleSeedProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_seed(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(bridge), checked)

    def test_the_actual_natural_dynamic_source_has_no_square_tail(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(result["dynamic_scale"], 4519173000401)
        self.assertEqual(result["square_divisor_count"], 27)
        self.assertEqual(result["distinct_square_divisor_residue_count"], 15)
        self.assertIsNone(result["square_tail_witness"])


if __name__ == "__main__":
    unittest.main()
