import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_pressure_external_source_bridge",
    ROOT / "reproductions" / "h19_k23_global_tail_pressure_external_source_bridge.py",
)
assert SPEC and SPEC.loader
bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bridge
SPEC.loader.exec_module(bridge)


class H19K23GlobalTailPressureExternalSourceBridgeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(bridge.run_audit(pressure), checked)

    def test_fixed_factor_sources_bridge_twenty_of_the_twenty_two_pressure_rays(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_family_count"], 22)
        self.assertEqual(result["fixed_factor_bridge_count"], 20)
        self.assertEqual(result["fixed_factor_bridge_miss_count"], 2)
        self.assertEqual(
            result["unbridged_prime_seeds"],
            [2220549727681245601, 748375048866405601],
        )
        target = next(row for row in result["rows"] if row["prime_seed"] == 955643834512728001)
        self.assertEqual(target["fixed_factor_bridge"]["stationary_scale"], 18)
        self.assertEqual(target["fixed_factor_bridge"]["fixed_square_tail_divisor"], 67077)


if __name__ == "__main__":
    unittest.main()
