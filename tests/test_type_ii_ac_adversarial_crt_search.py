"""Independently verify the finite AC CRT adversarial-search artifact."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest
from fractions import Fraction

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_ac_adversarial_crt_search",
    ROOT / "reproductions" / "type_ii_ac_adversarial_crt_search.py",
)
assert SPEC and SPEC.loader
search = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = search
SPEC.loader.exec_module(search)


def independent_divisors(factors):
    values = [1]
    for prime, exponent in factors:
        values = [
            value * prime**power
            for value in values
            for power in range(exponent + 1)
        ]
    return values


class TypeIIACAdversarialCRTSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = search.run_search()
        cls.expected = json.loads(
            (
                ROOT / "reproductions" / "type-ii-ac-adversarial-crt-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(
            self.actual["progression"]["modulus"],
            739_393_512,
        )
        self.assertEqual(self.actual["progression"]["residue"], 1)

    def test_transversals_partition_every_involution_orbit(self):
        for modulus_text, values in self.actual["progression"]["transversals"].items():
            modulus = int(modulus_text)
            transversal = set(map(int, values))
            units = {
                residue
                for residue in range(1, modulus)
                if math.gcd(residue, modulus) == 1
            }
            self.assertEqual(len(transversal) * 2, len(units))
            for residue in units:
                partner = (-pow(residue, -1, modulus)) % modulus
                self.assertNotEqual(residue, partner)
                self.assertEqual((residue in transversal) + (partner in transversal), 1)

    def test_crt_class_avoids_every_screened_bad_factor_root(self):
        progression = self.actual["progression"]
        pairs = {
            int(shift): int(row["modulus"])
            for shift, row in progression["canonical_pairs"].items()
        }
        transversals = {
            int(modulus): set(map(int, values))
            for modulus, values in progression["transversals"].items()
        }
        for row in progression["screening_prime_rows"]:
            screened_prime = int(row["prime"])
            chosen = int(row["chosen_core_residue"])
            self.assertNotIn(chosen, set(map(int, row["forbidden_roots"])))
            for candidate in self.actual["candidates"]:
                prime = int(candidate["prime"])
                self.assertEqual(prime % screened_prime, chosen)
                for shift, modulus in pairs.items():
                    if (prime + 4 * shift) % screened_prime:
                        continue
                    self.assertIn(screened_prime % modulus, transversals[modulus])

    def test_first_complete_fan_failure_is_an_exact_ten_ray_failure(self):
        candidate = next(
            candidate
            for candidate in self.actual["candidates"]
            if candidate["failed_ray_count"] == self.actual["fan_bound"]
        )
        self.assertEqual(
            (candidate["multiplier"], candidate["prime"], candidate["failed_ray_count"]),
            (175, 129_393_864_601, 10),
        )
        self.assertTrue(sympy.isprime(candidate["prime"]))
        self.assertEqual(candidate["prime"] % 24, 1)
        self.assertEqual(len(candidate["rays"]), 10)
        for ray in candidate["rays"]:
            factors = [
                (int(row["prime"]), int(row["exponent"]))
                for row in ray["factorization"]
            ]
            self.assertEqual(
                math.prod(prime**exponent for prime, exponent in factors),
                ray["shifted"],
            )
            residues = {
                divisor % int(ray["modulus"])
                for divisor in independent_divisors(factors)
                if divisor > 1
            }
            self.assertNotIn(int(ray["modulus"]) - 1, residues)
            self.assertEqual(ray["ray_witness_count"], 0)
            self.assertIsNone(ray["least_ray_witness"])
            diagnosis = ray["support_diagnosis"]
            modulus = int(ray["modulus"])
            prime_residues = {
                int(row["prime"]) % modulus for row in ray["factorization"]
            }
            self.assertEqual(
                diagnosis["generated_subgroup"],
                search.generated_subgroup(prime_residues, modulus),
            )
            self.assertEqual(diagnosis["divisor_residues"], sorted(residues | {1}))
            self.assertEqual(diagnosis["target_residue"], modulus - 1)
            self.assertNotIn(modulus - 1, diagnosis["generated_subgroup"])
            self.assertEqual(diagnosis["failure_class"], "support_outside")

    def test_every_frozen_progression_candidate_has_an_ordinary_tail_exit(self):
        for candidate in self.actual["candidates"]:
            witness = candidate["ordinary_type_ii_tail_witness"]
            self.assertIsNotNone(witness)
            prime = int(candidate["prime"])
            gap = int(witness["gap"])
            self.assertEqual((prime - 1) % (gap + 1), 0)
            self.assertEqual(int(witness["x"]), (prime + gap) // 4)
            self.assertEqual(
                Fraction(4, prime),
                sum((Fraction(1, int(value)) for value in witness["target_solution"]), Fraction()),
            )
            self.assertEqual(
                Fraction(4, int(witness["source_denominator"])),
                sum((Fraction(1, int(value)) for value in witness["source_solution"]), Fraction()),
            )

        complete = next(
            candidate
            for candidate in self.actual["candidates"]
            if candidate["failed_ray_count"] == self.actual["fan_bound"]
        )
        self.assertEqual(complete["ordinary_type_ii_tail_witness"]["gap"], 23)


if __name__ == "__main__":
    unittest.main()
