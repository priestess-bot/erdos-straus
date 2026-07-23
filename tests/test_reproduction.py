import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("esc_reproduce", ROOT / "reproductions" / "esc_reproduce.py")
assert SPEC and SPEC.loader
reproduction = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = reproduction
SPEC.loader.exec_module(reproduction)


class ReproductionTests(unittest.TestCase):
    def test_classic_identities(self):
        self.assertEqual(reproduction.verify_reduction_identities(25), {"3t-1": 25, "4t-1": 25, "8t-3": 25})

    def test_mordell_survivors(self):
        self.assertEqual(reproduction.mordell_survivors_mod_840(), [1, 121, 169, 289, 361, 529])

    def test_factor_pair_certificates(self):
        limit = 100
        spf = reproduction.smallest_prime_factors(limit * ((3 * limit) // 4))
        for n in range(2, limit + 1):
            solution = reproduction.factor_pair_solution(n, spf)
            self.assertIsNotNone(solution)
            x, y, z = solution
            self.assertEqual(Fraction(4, n), Fraction(1, x) + Fraction(1, y) + Fraction(1, z))

    def test_bradford_certificates(self):
        limit = 500
        spf = reproduction.smallest_prime_factors(reproduction.ceil_div(limit, 2) + 1)
        for prime in reproduction.primes_up_to(limit):
            self.assertIsNotNone(reproduction.bradford_certificate(prime, spf), prime)


if __name__ == "__main__":
    unittest.main()
