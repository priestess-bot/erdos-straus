import math
import unittest

import sympy


def generated_subgroup(modulus, generators):
    """Direct finite closure used only for the small documented examples."""
    subgroup = {1}
    frontier = [1]
    while frontier:
        residue = frontier.pop()
        for generator in generators:
            candidate = residue * generator % modulus
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return subgroup


class LinearCharacterProductInformationBoundaryTests(unittest.TestCase):
    def test_linear_source_products_force_four_into_prime_support_subgroup(self):
        examples = (
            (73, 18, 1, 3),
            (3_942_409, 11_200, 9, 39),
        )
        for prime, a, s, modulus in examples:
            with self.subTest(prime=prime, modulus=modulus):
                K = (prime * modulus + 1) // 4
                factors = sympy.factorint(K)
                self.assertEqual(prime, a + s + a * s * modulus)
                self.assertEqual(4 * K, (a * modulus + 1) * (s * modulus + 1))
                self.assertEqual(K % modulus, pow(4, -1, modulus))
                self.assertEqual(
                    K,
                    math.prod(
                        int(q) ** int(exponent) for q, exponent in factors.items()
                    ),
                )
                support = generated_subgroup(modulus, [int(q) for q in factors])
                self.assertIn(4 % modulus, support)

    def test_equal_total_character_value_does_not_decide_subgroup_obstruction(self):
        non_obstructed_factors = sympy.factorint(55)
        self.assertEqual(
            [sympy.legendre_symbol(int(q), 3) for q in non_obstructed_factors],
            [-1, -1],
        )
        self.assertIn(-1 % 3, generated_subgroup(3, non_obstructed_factors))

        obstructed_factors = sympy.factorint(38_438_488)
        for prime in obstructed_factors:
            self.assertEqual(
                sympy.legendre_symbol(int(prime), 3)
                * sympy.legendre_symbol(int(prime), 13),
                1,
            )
        self.assertEqual(
            sympy.legendre_symbol(-1, 3) * sympy.legendre_symbol(-1, 13),
            -1,
        )
        self.assertNotIn(-1 % 39, generated_subgroup(39, obstructed_factors))


if __name__ == "__main__":
    unittest.main()
