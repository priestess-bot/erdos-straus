import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_one_prime_power_descent_profile",
    ROOT / "reproductions" / "h19_k23_global_one_prime_power_descent_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class H19K23GlobalOnePrimePowerDescentProfileTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_its_two_inputs(self):
        with (
            ROOT / "reproductions" / "h19-k23-full-global-tail-closure-2097152.json"
        ).open(encoding="utf-8") as handle:
            global_payload = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-one-support-closure-2097152.json"
        ).open(encoding="utf-8") as handle:
            reroute_payload = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(profile.run_audit(global_payload, reroute_payload), checked)

    def test_prime_power_selector_is_required_beyond_first_powers(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["final_one_support_count"], 5_128)
        self.assertEqual(
            result["new_prime_exponent_histogram"],
            {"1": 5_056, "2": 70, "3": 1, "4": 1},
        )
        self.assertEqual(
            result["first_power_one_witness_histogram"],
            {"absent": 46, "available": 5_082},
        )
        self.assertEqual(
            result["route_histogram"],
            {"rerouted-from-two-support": 41, "retained-one-support": 5_087},
        )


if __name__ == "__main__":
    unittest.main()
