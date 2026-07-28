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


def p_plus_one_b1_bridge(p: int, q: int) -> dict[str, int] | None:
    if p % 24 != 1 or q % 4 != 3 or (p + 1) % q:
        return None
    h = (p + 1) // q
    if h % 4 != 2:
        return None
    c = (p + q) // 4
    r = h + 1
    k = c * h
    e = h * h
    n = (q - 1) * h
    if q * r != 4 * c + 1 or 4 * k != p * r + 1:
        return None
    if (4 * k - e) // r != n or (4 * k - e) % r:
        return None
    if (4 * k * k) % e or e % r != 1 or e % 2 or e >= 2 * k:
        return None
    if not (2 <= n < p and n > (p + 1) // 2):
        return None
    source_term = n * k // e
    if source_term * e != n * k:
        return None
    return {
        "C": c,
        "R": r,
        "K": k,
        "E": e,
        "source": n,
        "source_term": source_term,
    }


class TypeIPPlusOneBOneUpperBridgeTests(unittest.TestCase):
    def test_displayed_examples(self):
        self.assertEqual(
            p_plus_one_b1_bridge(97, 7),
            {"C": 26, "R": 15, "K": 364, "E": 196, "source": 84, "source_term": 156},
        )
        witness = p_plus_one_b1_bridge(433, 7)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["source"], 372)
        self.assertEqual(witness["R"], 63)

    def test_each_qualifying_factor_gives_an_upper_bridge(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((limit + 1) // 2 + 1)
        witnessed = 0
        for p in short_certificate.primes_up_to(limit):
            if p % 24 != 1:
                continue
            for q in distinct_prime_factors((p + 1) // 2, spf):
                if q % 4 != 3:
                    continue
                witness = p_plus_one_b1_bridge(p, q)
                self.assertIsNotNone(witness, (p, q))
                assert witness is not None
                self.assertEqual(
                    Fraction(4, witness["source"]),
                    Fraction(1, witness["source_term"])
                    + Fraction(1, witness["C"])
                    + Fraction(1, witness["C"] * ((p + 1) // q)),
                )
                witnessed += 1
        self.assertGreater(witnessed, 0)

    def test_external_retraction_has_the_exact_small_divisibility_test(self):
        limit = 100_000
        spf = short_certificate.smallest_prime_factors((limit + 1) // 2 + 1)
        for p in short_certificate.primes_up_to(limit):
            if p % 24 != 1:
                continue
            for q in distinct_prime_factors((p + 1) // 2, spf):
                if q % 4 != 3:
                    continue
                witness = p_plus_one_b1_bridge(p, q)
                assert witness is not None
                scale = (witness["R"] + 1) // 4
                self.assertEqual(
                    witness["K"] % scale == 0,
                    ((q + 1) // 2) % scale == 0,
                    (p, q),
                )


if __name__ == "__main__":
    unittest.main()
