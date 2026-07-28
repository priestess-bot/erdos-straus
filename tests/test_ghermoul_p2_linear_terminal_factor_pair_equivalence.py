"""Independently check p2 factor pairs against linear B=1 terminal sources."""

from __future__ import annotations

from fractions import Fraction
import unittest

import sympy


def p2_data(x: int, y: int, z: int) -> tuple[int, int, int, int, int]:
    R = 4 * y - 1
    C = 4 * x * y - x - y
    H = z * R - 1
    K = C * H
    p = 4 * (x * (4 * y * z - z - 1) - y * z) + 1
    return p, R, C, H, K


def factor_pair_sources(x: int, y: int, z: int) -> set[tuple[int, int, int, int]]:
    """Recover (a, s, E, Q) solely from the stated factor-pair criterion."""
    _, R, _, _, K = p2_data(x, y, z)
    sources = set()
    for E in map(int, sympy.divisors(4 * K)):
        Q = 4 * K // E
        if (
            E % 2 == 0
            and E >= R + 1
            and Q >= R + 1
            and E % R == 1
            and Q % R == 1
        ):
            sources.add(((Q - 1) // R, (E - 1) // R, E, Q))
    return sources


def direct_linear_sources(x: int, y: int, z: int) -> set[tuple[int, int, int, int]]:
    """Enumerate all positive linear sources directly, without factor pairs."""
    p, R, _, _, _ = p2_data(x, y, z)
    sources = set()
    for s in range(1, p):
        if s % 2 == 0:
            continue
        a, remainder = divmod(p - s, 1 + s * R)
        if remainder == 0 and a >= 1:
            E = s * R + 1
            sources.add((a, s, E, a * R + 1))
    return sources


class GhermoulP2LinearTerminalFactorPairEquivalenceTests(unittest.TestCase):
    def test_factor_pairs_equal_direct_linear_sources_on_small_p2_forms(self):
        for x in range(1, 6):
            for y in range(1, 5):
                for z in range(1, 8):
                    p, R, C, H, K = p2_data(x, y, z)
                    self.assertGreater(p, 0)
                    self.assertEqual(4 * K, p * R + 1)
                    self.assertEqual(
                        factor_pair_sources(x, y, z), direct_linear_sources(x, y, z)
                    )
                    for a, s, E, Q in factor_pair_sources(x, y, z):
                        self.assertEqual(p, a + s + a * s * R)
                        self.assertEqual(E * Q, 4 * C * H)
                        self.assertEqual(E, s * R + 1)
                        self.assertEqual(Q, a * R + 1)
                        self.assertEqual((p - s) % E, 0)

    def test_p73_and_p297049_replay_known_linear_bridges(self):
        self.assertIn((18, 1, 4, 55), factor_pair_sources(4, 1, 2))
        self.assertIn((624, 25, 476, 11_857), factor_pair_sources(4, 5, 1046))

    def test_pminusone_subfamily_is_exactly_y_divides_x_times_z_plus_one(self):
        for x in range(1, 6):
            for y in range(1, 5):
                for z in range(1, 8):
                    p, R, _, _, _ = p2_data(x, y, z)
                    expected = (x * (z + 1)) % y == 0
                    pminusone_sources = {
                        source
                        for source in factor_pair_sources(x, y, z)
                        if source[1] == 1
                    }
                    self.assertEqual(bool(pminusone_sources), expected)
                    if expected:
                        a = (p - 1) // (R + 1)
                        self.assertEqual((p - 1) % (R + 1), 0)
                        self.assertEqual(
                            pminusone_sources,
                            {(a, 1, R + 1, a * R + 1)},
                        )

        self.assertEqual(
            {
                source
                for source in factor_pair_sources(4, 5, 1_046)
                if source[1] == 1
            },
            set(),
        )

    def test_known_non_linear_878089_form_has_no_linear_factor_pair(self):
        p, R, C, H, K = p2_data(36, 21, 74)
        self.assertEqual((p, R, C, H, K), (878_089, 83, 2_967, 6_141, 18_220_347))
        self.assertEqual(factor_pair_sources(36, 21, 74), set())

    def test_recovered_sources_replay_both_unit_fraction_identities(self):
        p, R, C, H, K = p2_data(4, 5, 1046)
        a, s, E, Q = 624, 25, 476, 11_857
        A = 1_046
        n = p - s
        self.assertEqual(n, a * E)
        self.assertEqual(4 * K, E * Q)
        self.assertEqual((4 * K - E) // R, n)
        self.assertEqual(E % R, 1)
        self.assertEqual(
            Fraction(4, p),
            Fraction(1, A * C) + Fraction(1, A * C * H) + Fraction(1, p * K),
        )
        self.assertEqual(
            Fraction(4, n),
            Fraction(1, a * K) + Fraction(1, A * C) + Fraction(1, A * C * H),
        )


if __name__ == "__main__":
    unittest.main()
