from fractions import Fraction
import unittest

import sympy

from reproductions import short_certificate


def seven_p_plus_one_r7_bridge(p: int, q: int) -> dict[str, int] | None:
    """Construct the R=7, E=8 p-1 B=1 bridge from q=5 mod 7."""
    if p % 24 != 1:
        return None
    K = (7 * p + 1) // 4
    if q % 7 != 5 or K % q:
        return None
    C = q
    H = K // C
    if (H + 1) % 7 or (4 * C + 1) % 7:
        return None
    A = (H + 1) // 7
    m = (4 * C + 1) // 7
    R = 7
    E = 8
    source = p - 1
    if (
        p != 4 * A * C - m
        or 4 * K != p * R + 1
        or (4 * K - E) % R
        or (4 * K - E) // R != source
        or (4 * K * K) % E
        or E % R != 1
        or E >= 2 * K
        or not ((p + 1) // 2 <= source < p)
    ):
        return None
    source_term, remainder = divmod(source * K, E)
    if remainder:
        return None
    return {
        "A": A,
        "B": 1,
        "C": C,
        "H": H,
        "m": m,
        "R": R,
        "K": K,
        "E": E,
        "source": source,
        "source_term": source_term,
    }


class TypeISevenPPlusOneR7BOneUpperBridgeTests(unittest.TestCase):
    def test_displayed_example(self):
        self.assertEqual(
            seven_p_plus_one_r7_bridge(337, 5),
            {
                "A": 17,
                "B": 1,
                "C": 5,
                "H": 118,
                "m": 3,
                "R": 7,
                "K": 590,
                "E": 8,
                "source": 336,
                "source_term": 24780,
            },
        )

    def test_each_qualifying_factor_gives_a_pminusone_upper_bridge(self):
        witnessed = 0
        for p in short_certificate.primes_up_to(100_000):
            if p % 24 != 1:
                continue
            K = (7 * p + 1) // 4
            for q in sympy.factorint(K):
                q = int(q)
                if q % 7 != 5:
                    continue
                witness = seven_p_plus_one_r7_bridge(p, q)
                self.assertIsNotNone(witness, (p, q))
                assert witness is not None
                self.assertEqual(
                    Fraction(4, p),
                    Fraction(1, witness["A"] * witness["C"])
                    + Fraction(1, witness["A"] * witness["C"] * witness["H"])
                    + Fraction(1, p * witness["K"]),
                )
                self.assertEqual(
                    Fraction(4, witness["source"]),
                    Fraction(1, witness["source_term"])
                    + Fraction(1, witness["A"] * witness["C"])
                    + Fraction(1, witness["A"] * witness["C"] * witness["H"]),
                )
                witnessed += 1
        self.assertGreater(witnessed, 0)

    def test_three_factor_sieve_root_count_has_dimension_thirteen_over_six(self):
        for ell in short_certificate.primes_up_to(10_000):
            if ell <= 7:
                continue
            roots = {(-pow(24, -1, ell)) % ell}
            expected = 1
            if ell % 4 == 3:
                roots.add((-pow(12, -1, ell)) % ell)
                expected += 1
            if ell % 3 == 2:
                roots.add((-pow(18, -1, ell)) % ell)
                expected += 1
            if ell % 7 == 5:
                roots.add((-pow(21, -1, ell)) % ell)
                expected += 1
            self.assertEqual(len(roots), expected, ell)


if __name__ == "__main__":
    unittest.main()
