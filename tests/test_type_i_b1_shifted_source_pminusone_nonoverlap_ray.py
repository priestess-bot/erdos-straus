import importlib.util
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MERSENNE_SPEC = importlib.util.spec_from_file_location(
    "type_i_mersenne_bridge_selector",
    ROOT / "reproductions" / "type_i_mersenne_bridge_selector.py",
)
assert MERSENNE_SPEC and MERSENNE_SPEC.loader
selector = importlib.util.module_from_spec(MERSENNE_SPEC)
sys.modules[MERSENNE_SPEC.name] = selector
MERSENNE_SPEC.loader.exec_module(selector)

DICHOTOMY_SPEC = importlib.util.spec_from_file_location(
    "type_i_b1_pminusone_same_gap_dichotomy",
    ROOT / "reproductions" / "type_i_b1_pminusone_same_gap_dichotomy.py",
)
assert DICHOTOMY_SPEC and DICHOTOMY_SPEC.loader
dichotomy = importlib.util.module_from_spec(DICHOTOMY_SPEC)
sys.modules[DICHOTOMY_SPEC.name] = dichotomy
DICHOTOMY_SPEC.loader.exec_module(dichotomy)


class TypeIBOneShiftedSourcePMinusOneNonoverlapRayTests(unittest.TestCase):
    def test_ray_is_primitive_and_has_the_shifted_bridge(self):
        step, initial = 1_363_440, 905_353
        self.assertEqual(math.gcd(step, initial), 1)
        for index in range(20):
            prime = step * index + initial
            A = 1_140 * index + 757
            witness = selector.shifted_source_b1_witness(prime, 3, 63, 299)

            self.assertEqual(prime % 24, 1)
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(witness["normal_form"], [A, 1, 299])
            self.assertEqual(witness["source_denominator"], prime - 3)
            self.assertEqual(witness["E"], 190)
            self.assertEqual(witness["K"] % 190, 0)

            t = (prime - 1) // 4
            self.assertNotEqual((5 * 5 * (A + 1) * (A + 1)) % 16, 0)
            self.assertNotEqual(t * t % 16, 0)
            self.assertIsNone(dichotomy.same_gap_type_ii_tail(5, 16, A))

    def test_displayed_prime_sample(self):
        prime = 2_268_793
        self.assertTrue(dichotomy.is_prime(prime))
        witness = selector.shifted_source_b1_witness(prime, 3, 63, 299)
        self.assertIsNotNone(witness)


if __name__ == "__main__":
    unittest.main()
