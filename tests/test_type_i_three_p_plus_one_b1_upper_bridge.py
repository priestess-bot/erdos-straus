from fractions import Fraction
import unittest

from reproductions import short_certificate


def distinct_prime_factors(value: int, spf: list[int]) -> list[int]:
    factors: list[int] = []
    while value > 1:
        prime = spf[value]
        factors.append(prime)
        while value % prime == 0:
            value //= prime
    return factors


def three_p_plus_one_b1_bridge(p: int, q: int) -> dict[str, int] | None:
    if p % 24 != 1:
        return None
    N = (3 * p + 1) // 4
    if q % 3 != 2 or N % q:
        return None
    quotient = N // q
    if (quotient + 1) % 3:
        return None
    r = (quotient + 1) // 3
    gap = (4 * q + 1) // 3
    R = 3
    K = N
    E = 2 * q
    source = (4 * N - E) // R
    if gap * R != 4 * q + 1 or K != q * (R * r - 1):
        return None
    if p != 4 * r * q - gap or (4 * K - E) % R:
        return None
    if (4 * K - E) // R != source:
        return None
    if (4 * K * K) % E or E % R != 1 or E % 2 or E >= 2 * K:
        return None
    if not (2 <= source < p and source > (p + 1) // 2):
        return None
    source_term = source * K // E
    if source_term * E != source * K:
        return None
    return {
        "A": r,
        "C": q,
        "gap": gap,
        "R": R,
        "K": K,
        "E": E,
        "source": source,
        "source_term": source_term,
    }


class TypeIThreePPlusOneBOneUpperBridgeTests(unittest.TestCase):
    def test_displayed_example(self):
        self.assertEqual(
            three_p_plus_one_b1_bridge(73, 5),
            {
                "A": 4,
                "C": 5,
                "gap": 7,
                "R": 3,
                "K": 55,
                "E": 10,
                "source": 70,
                "source_term": 385,
            },
        )

    def test_each_qualifying_factor_gives_an_upper_bridge(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((3 * limit + 1) // 4 + 1)
        witnessed = 0
        for p in short_certificate.primes_up_to(limit):
            if p % 24 != 1:
                continue
            N = (3 * p + 1) // 4
            for q in distinct_prime_factors(N, spf):
                if q % 3 != 2:
                    continue
                witness = three_p_plus_one_b1_bridge(p, q)
                self.assertIsNotNone(witness, (p, q))
                assert witness is not None
                self.assertEqual(
                    Fraction(4, witness["source"]),
                    Fraction(1, witness["source_term"])
                    + Fraction(1, witness["A"] * witness["C"])
                    + Fraction(1, witness["A"] * witness["K"]),
                )
                witnessed += 1
        self.assertGreater(witnessed, 0)

    def test_same_normal_form_has_odd_canonical_external_source(self):
        witness = three_p_plus_one_b1_bridge(73, 5)
        assert witness is not None
        self.assertEqual((witness["R"] + 1) // 4, 1)
        self.assertEqual(witness["K"] % 2, 1)
        self.assertEqual(witness["source"] % 2, 0)


if __name__ == "__main__":
    unittest.main()
