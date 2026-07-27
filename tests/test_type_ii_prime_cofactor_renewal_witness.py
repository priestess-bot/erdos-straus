import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_prime_cofactor_renewal_witness",
    ROOT / "reproductions" / "type_ii_prime_cofactor_renewal_witness.py",
)
assert SPEC and SPEC.loader
renewal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = renewal
SPEC.loader.exec_module(renewal)


class TypeIIPrimeCofactorRenewalWitnessTests(unittest.TestCase):
    def test_h23_renews_the_h22_closed_model(self):
        result = renewal.run_witness()
        self.assertEqual(result["h22"]["modulus"], 77_597_520)
        self.assertEqual(
            result["h22"]["second_level_covering_primes"],
            {"0": [23], "1": [23], "2": [3, 23]},
        )
        self.assertEqual(result["h23"]["modulus"], 1_784_742_960)
        self.assertEqual(result["h23"]["residue_class"], 1_474_353_409)
        self.assertEqual(result["h23"]["residue_mod_h22_modulus"], 529)
        self.assertEqual(result["h23"]["residue_mod_23"], 3)
        self.assertEqual(
            result["h23"]["changed_shift_forced_factor"],
            {
                "shift": 5,
                "forced_divisor": 69,
                "extra_prime_power": 0,
                "fixed_factor": 69,
            },
        )
        self.assertEqual(result["h23"]["second_level_form_count"], 24)
        self.assertEqual(result["h23"]["second_level_covering_primes"], [])

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-prime-cofactor-renewal-h23-witness.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h22"]["residue_class"], 529)
        self.assertEqual(result["h23"]["residue_class"], 1_474_353_409)
        self.assertEqual(result["h23"]["second_level_covering_primes"], [])


if __name__ == "__main__":
    unittest.main()
