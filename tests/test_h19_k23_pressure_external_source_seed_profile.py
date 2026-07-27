import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_external_source_seed_profile",
    ROOT / "reproductions" / "h19_k23_pressure_external_source_seed_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23PressureExternalSourceSeedProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_bridge_misses(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-external-source-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(bridge), checked)

    def test_both_fixed_factor_miss_seeds_have_direct_source_descents(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-external-source-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["fixed_factor_miss_seed_count"], 2)
        self.assertEqual(result["resolved_seed_count"], 2)
        witnesses = {row["prime_seed"]: row["first_source_witness"] for row in result["rows"]}
        self.assertEqual(witnesses[2220549727681245601]["scale"], 1)
        self.assertEqual(witnesses[2220549727681245601]["selected_factor"], 48989)
        self.assertEqual(witnesses[748375048866405601]["scale"], 120)
        self.assertEqual(witnesses[748375048866405601]["selected_factor"], 41672)


if __name__ == "__main__":
    unittest.main()
