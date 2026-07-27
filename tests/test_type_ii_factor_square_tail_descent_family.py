from fractions import Fraction
import unittest

import sympy


class TypeIIFactorSquareTailDescentFamilyTests(unittest.TestCase):
    def test_factor_square_congruence_examples_reconstruct_certificates(self):
        for q, divisor, t, prime in (
            (6, 1, 18, 433),
            (12, 4, 77, 3_697),
            (18, 36, 139, 10_009),
            (24, 9, 58, 5_569),
            (8, 8, 1_802_230_778_703_375, 57_671_384_918_508_001),
        ):
            gap = 4 * q - 1
            self.assertEqual(q * q % divisor, 0)
            self.assertEqual(t % gap, (-4 * divisor - 1) % gap)
            self.assertEqual(q * t % 6, 0)
            self.assertEqual(prime, 4 * q * t + 1)
            self.assertTrue(sympy.isprime(prime))
            self.assertEqual(prime % 24, 1)

            x = (prime + gap) // 4
            self.assertEqual(x, q * (t + 1))
            self.assertLessEqual(divisor, x)
            self.assertEqual(x * x % divisor, 0)
            self.assertEqual(divisor % gap, (-x) % gap)

            y = prime * (x + divisor) // gap
            z = prime * (x + x * x // divisor) // gap
            self.assertEqual(
                Fraction(4, prime),
                Fraction(1, x) + Fraction(1, y) + Fraction(1, z),
            )
            source = t + 1
            self.assertTrue(2 <= source < prime)
            self.assertEqual(
                Fraction(4, source),
                Fraction(1, x) + Fraction(1, y // prime) + Fraction(1, z // prime),
            )


if __name__ == "__main__":
    unittest.main()
