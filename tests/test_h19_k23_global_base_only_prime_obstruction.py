import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_base_only_prime_obstruction",
    ROOT / "reproductions" / "h19_k23_global_base_only_prime_obstruction.py",
)
assert SPEC and SPEC.loader
obstruction = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = obstruction
SPEC.loader.exec_module(obstruction)


class H19K23GlobalBaseOnlyPrimeObstructionTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(obstruction.run_audit(pressure), checked)

    def test_every_pressure_seed_yields_a_primitive_core_prime_progression(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 2_097_152)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["prime_progression_family_count"], 22)
        self.assertTrue(
            all(
                family["prime_progression_gcd"] == 1
                and family["core_prime_residue_mod_24"] == 1
                and family["canonical_base_only_miss_gaps"]
                == family["unit_shift_base_only_miss_gaps"]
                for family in result["families"]
            )
        )


if __name__ == "__main__":
    unittest.main()
