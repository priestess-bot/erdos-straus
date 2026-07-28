import importlib.util
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b1_pminusone_same_gap_dichotomy",
    ROOT / "reproductions" / "type_i_b1_pminusone_same_gap_dichotomy.py",
)
assert SPEC and SPEC.loader
dichotomy = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dichotomy
SPEC.loader.exec_module(dichotomy)


class TypeIBOneSquareEssentialSameGapNonoverlapRayTests(unittest.TestCase):
    def test_ray_is_primitive_and_core(self):
        self.assertEqual(math.gcd(17_040, 3_673), 1)
        for index in range(20):
            self.assertEqual((17_040 * index + 3_673) % 24, 1)

    def test_prime_samples_have_square_essential_nonoverlap(self):
        for index, prime in ((0, 3_673), (5, 88_873), (6, 105_913), (7, 122_953)):
            A = 60 * index + 13
            witness = dichotomy.b1_pminusone_witness(5, 4, A)

            self.assertEqual(witness["p"], prime)
            self.assertTrue(witness["prime_check"])
            self.assertTrue(witness["bridge_condition"])
            self.assertFalse(witness["same_gap_type_ii_condition"])
            self.assertIsNone(witness["same_gap_type_ii_tail"])

            t = (prime - 1) // 4
            self.assertEqual(t % 2, 0)
            self.assertNotEqual(t % 4, 0)
            self.assertEqual(t * t % 4, 0)
            self.assertNotEqual(witness["K"] % 4, 0)
            self.assertNotEqual((prime - 1) % 16, 0)


if __name__ == "__main__":
    unittest.main()
