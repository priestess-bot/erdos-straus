import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_first_power_tail_reroute",
    ROOT / "reproductions" / "h19_k23_global_first_power_tail_reroute.py",
)
assert SPEC and SPEC.loader
reroute = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = reroute
SPEC.loader.exec_module(reroute)


class H19K23GlobalFirstPowerTailRerouteTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_power_profile(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-first-power-tail-reroute-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(reroute.run_audit(profile), checked)

    def test_every_final_one_support_record_has_a_first_power_global_tail(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-first-power-tail-reroute-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_final_one_support_count"], 5_128)
        self.assertEqual(result["same_tail_first_power_count"], 5_082)
        self.assertEqual(result["later_tail_first_power_reroute_count"], 46)
        self.assertTrue(
            all(
                row["new_tail_gap"] > row["old_tail_gap"]
                and row["old_new_prime_exponent"] > 1
                for row in result["reroutes"]
            )
        )


if __name__ == "__main__":
    unittest.main()
