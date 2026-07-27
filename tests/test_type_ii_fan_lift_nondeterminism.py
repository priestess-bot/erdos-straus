import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_fan_lift_nondeterminism",
    ROOT / "reproductions" / "type_ii_fan_lift_nondeterminism.py",
)
assert SPEC and SPEC.loader
nondeterminism = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = nondeterminism
SPEC.loader.exec_module(nondeterminism)


class TypeIIFanLiftNondeterminismTests(unittest.TestCase):
    def test_generic_crt_branches_preserve_the_old_state_but_split_the_new_factor(self):
        modulus, residue, prime, shift = 120, 1, 7, 1
        hit, miss = nondeterminism.branch_lifts(modulus, residue, prime, shift)
        self.assertEqual((hit % modulus, miss % modulus), (residue, residue))
        self.assertEqual((hit + 4 * shift) % prime, 0)
        self.assertNotEqual((miss + 4 * shift) % prime, 0)
        self.assertEqual(math.gcd(hit, modulus * prime), 1)
        self.assertEqual(math.gcd(miss, modulus * prime), 1)

    def test_h22_to_h23_has_actual_core_primes_on_both_branches(self):
        result = nondeterminism.run_witness()["h22_to_h23"]
        self.assertEqual(
            (
                result["old_forced_factor"],
                result["hit_forced_factor"],
                result["miss_forced_factor"],
            ),
            (3, 69, 3),
        )
        self.assertEqual(
            (result["hit_first_core_prime"], result["miss_first_core_prime"]),
            (15_752_297_089, 4_655_851_729),
        )

    def test_checked_artifact_rebuilds(self):
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-ii-fan-lift-nondeterminism-h23.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(nondeterminism.run_witness(), expected)


if __name__ == "__main__":
    unittest.main()
