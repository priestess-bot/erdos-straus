import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_one_prime_power_exponent_compression",
    ROOT / "reproductions" / "h19_k23_global_one_prime_power_exponent_compression.py",
)
assert SPEC and SPEC.loader
compression = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compression
SPEC.loader.exec_module(compression)


class H19K23GlobalOnePrimePowerExponentCompressionTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_power_profile(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-descent-profile-2097152.json"
        ).open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-exponent-compression-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(compression.run_audit(profile), checked)

    def test_fixed_global_menu_has_explicit_finite_exponent_bounds(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-one-prime-power-exponent-compression-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["global_max_carmichael_bound"], 82_798)
        self.assertEqual(result["global_max_carmichael_bound_gap"], 82_799)
        self.assertEqual(result["used_tail_max_carmichael_bound"], 78)
        self.assertEqual(result["used_tail_max_carmichael_bound_gap"], 79)
        self.assertEqual(
            result["selected_exponent_compression_histogram"],
            {"1->1": 5_056, "2->2": 70, "3->3": 1, "4->4": 1},
        )


if __name__ == "__main__":
    unittest.main()
