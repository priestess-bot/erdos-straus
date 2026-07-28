from fractions import Fraction
import unittest

import sympy

from reproductions import short_certificate
from reproductions import type_i_fixed_pminusone_ray_pressure_profile_600m as rays


class TypeIFixedUniversalPminusoneBOneRaysTests(unittest.TestCase):
    def test_every_menu_entry_has_the_universal_pminusone_square_condition(self):
        for prime in short_certificate.primes_up_to(100_000):
            if prime % 24 != 1:
                continue
            for E in rays.UNIVERSAL_E_VALUES:
                self.assertEqual(((prime - 1) * (prime - 1) // 4) % E, 0, (prime, E))

    def test_R_three_is_exactly_the_three_p_plus_one_factor_condition(self):
        witnessed = 0
        for prime in short_certificate.primes_up_to(100_000):
            if prime % 24 != 1:
                continue
            K = (3 * prime + 1) // 4
            factor_condition = any(int(q) % 3 == 2 for q in sympy.factorint(K))
            witness = rays.fixed_pminusone_witness(prime, 3)
            self.assertEqual(witness is not None, factor_condition, prime)
            if witness is None:
                continue
            witnessed += 1
            self.assertEqual(witness["source_denominator"], prime - 1)
            self.assertEqual(
                Fraction(4, prime - 1),
                Fraction(1, witness["source_term"])
                + Fraction(1, witness["A"] * witness["C"])
                + Fraction(1, witness["A"] * witness["C"] * witness["H"]),
            )
        self.assertGreater(witnessed, 0)

    def test_displayed_R_three_example_is_a_pminusone_bridge(self):
        witness = rays.fixed_pminusone_witness(73, 3)
        self.assertEqual(
            witness,
            {
                "A": 4,
                "B": 1,
                "C": 5,
                "H": 11,
                "m": 7,
                "R": 3,
                "K": 55,
                "E": 4,
                "source_denominator": 72,
                "source_term": 990,
            },
        )


if __name__ == "__main__":
    unittest.main()
