import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_even_source_seed_profile",
    ROOT / "reproductions" / "h19_k23_pressure_even_source_seed_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23PressureEvenSourceSeedProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_seed(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-even-source-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(bridge), checked)

    def test_distance_one_even_source_gives_a_strict_lift(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-even-source-seed-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        witness = result["first_witness"]
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(witness["distance"], 1)
        self.assertEqual(witness["shift"], 22595865002005)
        self.assertEqual(witness["r"], 33119)
        self.assertEqual(witness["square_tail_factor"], 574459478468352)
        self.assertLess(witness["source_denominator"], result["seed_prime"])


if __name__ == "__main__":
    unittest.main()
