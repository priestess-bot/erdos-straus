"""Check the coordinate translation between Ghermoul p2 and B=1 normal forms."""

from __future__ import annotations

import unittest


def p2(x: int, y: int, z: int) -> int:
    return x * (4 * y * z - z - 1) - y * z


class GhermoulP2B1NormalFormEquivalenceTests(unittest.TestCase):
    def test_forward_coordinates_reconstruct_the_b1_normal_form(self):
        for x in range(1, 12):
            for y in range(1, 12):
                for z in range(1, 12):
                    q = p2(x, y, z)
                    prime_parameter = 4 * q + 1
                    m, R, A = 4 * x - 1, 4 * y - 1, z
                    C = 4 * x * y - x - y
                    H = A * R - 1
                    K = C * H
                    self.assertEqual(m * R, 4 * C + 1)
                    self.assertEqual(prime_parameter, 4 * A * C - m)
                    self.assertEqual(4 * K, prime_parameter * R + 1)
                    self.assertEqual((prime_parameter - 1) // 4, q)

    def test_reverse_coordinates_recover_p2(self):
        for x in range(1, 12):
            for y in range(1, 12):
                for z in range(1, 12):
                    m, R, A = 4 * x - 1, 4 * y - 1, z
                    C = (m * R - 1) // 4
                    prime_parameter = 4 * A * C - m
                    recovered_x = (m + 1) // 4
                    recovered_y = (R + 1) // 4
                    self.assertEqual((recovered_x, recovered_y, A), (x, y, z))
                    self.assertEqual((prime_parameter - 1) // 4, p2(x, y, z))


if __name__ == "__main__":
    unittest.main()
