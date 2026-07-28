from fractions import Fraction
import json
from pathlib import Path
import unittest

import sympy

from reproductions import short_certificate


ROOT = Path(__file__).resolve().parents[1]
EARLY = ROOT / "reproductions" / "type-i-tail-reverse-b1-even-source-500m-results.json"
LATE = ROOT / "reproductions" / "type-i-mixed-terminal-dense-b1-600m-results.json"
RAYS = (3, 7, 11, 15, 23, 35, 47, 71, 143)


def target_residue(R: int) -> int:
    return -pow(4, -1, R) % R


def direct_prime_factor_witness(p: int, R: int, q: int) -> dict[str, int] | None:
    """Use one q in the target residue class as C on a universal p-1 ray."""
    if p % 24 != 1 or R not in RAYS or q % R != target_residue(R):
        return None
    E = R + 1
    K = (p * R + 1) // 4
    if K % q:
        return None
    C = q
    H = K // C
    if (H + 1) % R or (4 * C + 1) % R:
        return None
    A = (H + 1) // R
    m = (4 * C + 1) // R
    source = p - 1
    if (
        p != 4 * A * C - m
        or (4 * K - E) % R
        or (4 * K - E) // R != source
        or (4 * K * K) % E
        or E % R != 1
        or E >= 2 * K
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


def p_plus_one_condition(p: int) -> bool:
    return any(int(q) % 4 == 3 for q in sympy.factorint((p + 1) // 2))


def direct_ray_condition(p: int, R: int) -> bool:
    K = (p * R + 1) // 4
    return any(int(q) % R == target_residue(R) for q in sympy.factorint(K))


class TypeIUniversalPminusonePrimeFactorMenuTests(unittest.TestCase):
    def test_every_qualifying_menu_factor_reconstructs_both_identities(self):
        witnessed = 0
        for p in short_certificate.primes_up_to(100_000):
            if p % 24 != 1:
                continue
            for R in RAYS:
                K = (p * R + 1) // 4
                for q in sympy.factorint(K):
                    q = int(q)
                    if q % R != target_residue(R):
                        continue
                    witness = direct_prime_factor_witness(p, R, q)
                    self.assertIsNotNone(witness, (p, R, q))
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

    def test_large_sieve_primes_have_the_expected_distinct_root_count(self):
        for ell in short_certificate.primes_up_to(10_000):
            if ell <= 149:
                continue
            roots = {(-pow(24, -1, ell)) % ell}
            expected = 1
            if ell % 4 == 3:
                roots.add((-pow(12, -1, ell)) % ell)
                expected += 1
            for R in RAYS:
                if ell % R == target_residue(R):
                    roots.add((-(R + 1) * pow(24 * R, -1, ell)) % ell)
                    expected += 1
            self.assertEqual(len(roots), expected, ell)

    def test_frozen_pressure_set_has_the_stated_direct_factor_menu_profile(self):
        early = json.loads(EARLY.read_text(encoding="utf-8"))
        late = json.loads(LATE.read_text(encoding="utf-8"))
        primes = {int(row["prime"]) for row in early["records"]} | {int(p) for p in early["misses"]}
        primes |= {int(row["prime"]) for row in late["records"]}
        self.assertEqual(len(primes), 1964)
        covered = {p for p in primes if p_plus_one_condition(p)}
        self.assertEqual(len(covered), 760)
        first_hit_counts = []
        for R in RAYS:
            new = {p for p in primes if direct_ray_condition(p, R)} - covered
            first_hit_counts.append(len(new))
            covered |= new
        self.assertEqual(first_hit_counts, [431, 158, 82, 99, 17, 21, 12, 4, 4])
        self.assertEqual(len(covered), 1588)


if __name__ == "__main__":
    unittest.main()
