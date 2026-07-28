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


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def ray_parameters(exponent):
    r = 1 << (2 * exponent)
    C = 19 * r - 5
    modulus = 15 * (1 << (exponent + 1))
    A0 = next(
        A
        for A in range(1, modulus + 1)
        if (A + 1) % (1 << (exponent + 1)) == 1 << exponent
        and A % 3 == 1
        and A % 5 == 2
    )
    step = 4 * C * modulus
    initial = 4 * C * A0 - 19
    return r, C, modulus, A0, step, initial


class TypeIBOneSquareEssentialSameGapNonoverlapRayTests(unittest.TestCase):
    def assert_ray_state(self, exponent, index):
        r, C, modulus, A0, step, initial = ray_parameters(exponent)
        A = A0 + modulus * index
        prime = step * index + initial
        witness = dichotomy.b1_pminusone_witness(5, r, A)
        t = (prime - 1) // 4

        self.assertEqual(prime, witness["p"])
        self.assertEqual(prime % 24, 1)
        self.assertTrue(witness["bridge_condition"])
        self.assertFalse(witness["same_gap_type_ii_condition"])
        self.assertIsNone(witness["same_gap_type_ii_tail"])
        self.assertEqual(valuation(t, 2), exponent)
        self.assertEqual(valuation(r, 2), 2 * exponent)
        self.assertEqual(t * t % r, 0)
        self.assertNotEqual(t % r, 0)
        self.assertNotEqual(witness["K"] % r, 0)
        self.assertEqual(valuation(4 * r, 2) - valuation(prime - 1, 2), exponent)

    def test_each_ray_is_primitive_and_core(self):
        for exponent in range(1, 8):
            _, _, _, _, step, initial = ray_parameters(exponent)
            self.assertEqual(math.gcd(step, initial), 1)
            for index in range(20):
                self.assertEqual((step * index + initial) % 24, 1)
                self.assert_ray_state(exponent, index)

    def test_prime_samples_have_unbounded_square_defect(self):
        for exponent, index, prime in (
            (1, 1, 27_529),
            (2, 1, 223_633),
            (3, 0, 33_889),
            (4, 5, 53_779_393),
            (5, 6, 495_378_049),
        ):
            _, _, _, _, step, initial = ray_parameters(exponent)
            self.assertEqual(step * index + initial, prime)
            self.assertTrue(dichotomy.is_prime(prime))
            self.assert_ray_state(exponent, index)


if __name__ == "__main__":
    unittest.main()
