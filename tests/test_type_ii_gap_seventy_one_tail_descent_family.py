from fractions import Fraction
import unittest

import sympy


class TypeIIGapSeventyOneTailDescentFamilyTests(unittest.TestCase):
    def test_explicit_congruence_family_reconstructs_a_strict_descent(self):
        primes = [10_009, 5_771_131_031_426_401]
        for r in (1, 2, 4):
            gap = 24 * r - 1
            residue = (-145) % gap
            prime = next(
                (gap + 1) * (residue + gap * u) + 1
                for u in range(100)
                if sympy.isprime((gap + 1) * (residue + gap * u) + 1)
            )
            primes.append(prime)
        for prime in primes:
            self.assertTrue(sympy.isprime(prime))
            if prime % 5_112 == 4_897:
                gap = 71
            else:
                gap = next(
                    24 * r - 1
                    for r in (1, 2, 4)
                    if (prime - 1) // (24 * r) % (24 * r - 1) == (-145) % (24 * r - 1)
                )
            divisor = 36
            x = (prime + gap) // 4
            self.assertEqual(4 * x, prime + gap)
            self.assertEqual(x * x % divisor, 0)
            self.assertEqual(divisor % gap, (-x) % gap)
            y = prime * (x + divisor) // gap
            z = prime * (x + x * x // divisor) // gap
            self.assertEqual(Fraction(4, prime), Fraction(1, x) + Fraction(1, y) + Fraction(1, z))
            source = (prime + gap) // (gap + 1)
            self.assertTrue(2 <= source < prime)
            self.assertEqual(
                Fraction(4, source),
                Fraction(1, x) + Fraction(1, y // prime) + Fraction(1, z // prime),
            )


if __name__ == "__main__":
    unittest.main()
