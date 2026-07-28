"""Verify the quadratic pullback formula independently on the frozen pressure set."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_quadratic_obstruction_reciprocity_pullback",
    ROOT / "reproductions" / "type_i_linear_quadratic_obstruction_reciprocity_pullback.py",
)
assert SPEC and SPEC.loader
pullback = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pullback
SPEC.loader.exec_module(pullback)


class TypeILinearQuadraticObstructionReciprocityPullbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = pullback.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-quadratic-obstruction-reciprocity-pullback-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["profile_count"], 7)
        self.assertGreater(self.actual["verified_relation_count"], 0)

    def test_reciprocity_identity_holds_directly_for_all_eligible_triples(self):
        for prime in pullback.PRESSURE_PRIMES:
            _, states_by_R = pullback.sources.enumerate_linear_source_states(prime)
            for R, states in states_by_R.items():
                for a, s in states:
                    K = (prime * R + 1) // 4
                    for q, _ in pullback.sources.exact_factorization(K):
                        if q % 2 == 0:
                            continue
                        for t in (a, s):
                            if (t * R + 1) % q:
                                continue
                            self.assertEqual(prime % q, t % q)
                            self.assertEqual(math.gcd(q, R), 1)
                            for m in pullback.odd_squarefree_negative_conductors(R):
                                self.assertEqual(m % 4, 3)
                                c = R // m
                                self.assertEqual(
                                    int(sympy.jacobi_symbol(q, m)),
                                    int(sympy.jacobi_symbol(prime * c, q)),
                                )


if __name__ == "__main__":
    unittest.main()
