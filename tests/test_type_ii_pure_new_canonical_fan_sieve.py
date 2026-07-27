import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_pure_new_canonical_fan_sieve",
    ROOT / "reproductions" / "type_ii_pure_new_canonical_fan_sieve.py",
)
assert SPEC and SPEC.loader
fan_sieve = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fan_sieve
SPEC.loader.exec_module(fan_sieve)


class TypeIIPureNewCanonicalFanSieveTests(unittest.TestCase):
    def test_newness_guard_excludes_every_h19_overlap(self):
        self.assertEqual(fan_sieve.h19_newness_guard(20, 100), 400)
        for shift in range(20, 101):
            for base_shift in range(1, 20):
                self.assertLess(abs(4 * (shift - base_shift)), 400)

    def test_large_prime_roots_are_exact_and_distinct(self):
        prime = 4_079
        shifts = fan_sieve.eligible_shifts(prime, 1_008)
        self.assertGreater(len(shifts), 0)
        roots = fan_sieve.forbidden_roots(prime, 1_008)
        self.assertEqual(len(roots), 1 + len(shifts))
        self.assertEqual(roots[0], 0)
        self.assertEqual(len(set(roots)), len(roots))

    def test_reciprocal_mass_dominates_the_harmonic_lower_bound(self):
        mass = fan_sieve.reciprocal_phi_sum(100)
        lower = fan_sieve.harmonic_lower_bound(100)
        self.assertGreater(mass, lower)

    def test_checked_artifact_has_all_local_guards(self):
        with (
            ROOT / "reproductions" / "type-ii-pure-new-canonical-fan-sieve-results.json"
        ).open(encoding="utf-8") as handle:
            payload = json.load(handle)
        by_bound = {entry["shift_bound"]: entry for entry in payload["geometries"]}
        self.assertEqual(set(by_bound), {50, 100, 1_008})
        for entry in by_bound.values():
            self.assertTrue(entry["all_roots_distinct"])
            self.assertTrue(entry["all_large_primes_h19_new"])
            self.assertGreater(
                entry["reciprocal_phi_sum"]["float"],
                entry["harmonic_lower_bound"]["float"],
            )


if __name__ == "__main__":
    unittest.main()
