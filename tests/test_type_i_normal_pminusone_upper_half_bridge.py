import unittest


def p_minus_one_bridge_state(prime: int, R: int) -> tuple[int, int, int, int, int]:
    """Return (K, r, t, E, n) for the formal p-minus-one normal bridge state."""
    if prime % 24 != 1 or R < 3 or R % 4 != 3:
        raise ValueError("require a core-prime congruence and a legal normal R")
    K = (prime * R + 1) // 4
    r = (R + 1) // 4
    t = (prime - 1) // 4
    return K, r, t, R + 1, prime - 1


class TypeINormalPMinusOneUpperHalfBridgeTests(unittest.TestCase):
    def test_square_condition_is_exact_and_the_bridge_is_small_side(self):
        primes = (73, 97, 193, 337, 1009, 67369)
        for prime in primes:
            for R in range(3, 200, 4):
                K, r, t, E, source = p_minus_one_bridge_state(prime, R)
                self.assertEqual(4 * K, prime * R + 1)
                self.assertEqual(E, R + 1)
                self.assertEqual(E % R, 1)
                self.assertEqual(E % 4, 0)
                self.assertEqual(source, prime - 1)
                self.assertEqual(source % 2, 0)
                self.assertEqual(E < 2 * K, 2 * source >= prime + 1)
                self.assertEqual(E <= 4 * K - 2 * R, True)
                self.assertEqual((4 * K * K) % E == 0, (t * t) % r == 0)

    def test_illegal_congruence_states_are_rejected(self):
        with self.assertRaises(ValueError):
            p_minus_one_bridge_state(71, 3)
        with self.assertRaises(ValueError):
            p_minus_one_bridge_state(73, 5)


if __name__ == "__main__":
    unittest.main()
