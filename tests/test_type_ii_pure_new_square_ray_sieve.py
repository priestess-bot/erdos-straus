import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_pure_new_square_ray_sieve",
    ROOT / "reproductions" / "type_ii_pure_new_square_ray_sieve.py",
)
assert SPEC and SPEC.loader
square_sieve = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = square_sieve
SPEC.loader.exec_module(square_sieve)


class TypeIIPureNewSquareRaySieveTests(unittest.TestCase):
    def test_newness_guard_excludes_every_h19_overlap(self):
        self.assertEqual(square_sieve.h19_newness_guard(5, 20), 1_600)
        for radius in range(5, 21):
            for source_shift in range(1, 20):
                self.assertNotEqual(radius * radius, source_shift)
                self.assertLess(abs(4 * (radius * radius - source_shift)), 1_600)

    def test_large_prime_roots_are_exact_and_distinct(self):
        prime = 3_599  # 3,599 == -1 (mod 20) and exceeds the R=20 guard.
        radii = square_sieve.eligible_square_radii(prime, 20)
        self.assertIn(5, radii)
        roots = square_sieve.forbidden_roots(prime, 20)
        self.assertEqual(len(roots), 1 + len(radii))
        self.assertEqual(roots[0], 0)
        self.assertEqual(roots[1], 3_499)
        self.assertEqual(len(set(roots)), len(roots))

    def test_local_geometry_matches_its_exact_count_formula(self):
        geometry = square_sieve.local_geometry(20, 10_000)
        self.assertTrue(geometry["all_roots_distinct"])
        self.assertTrue(geometry["all_large_primes_h19_new"])
        self.assertEqual(geometry["strict_prime_guard"], 1_600)
        self.assertEqual(
            geometry["reciprocal_phi_sum"],
            {
                "numerator": 1_387,
                "denominator": 1_440,
                "float": float(Fraction(1_387, 1_440)),
            },
        )
        self.assertGreater(geometry["checked_prime_count"], 0)
        self.assertGreater(geometry["root_count_histogram"].get("2", 0), 0)

    def test_checked_artifact_has_all_local_guards(self):
        with (
            ROOT / "reproductions" / "type-ii-pure-new-square-ray-sieve-results.json"
        ).open(encoding="utf-8") as handle:
            payload = json.load(handle)
        by_bound = {entry["radius_bound"]: entry for entry in payload["geometries"]}
        self.assertEqual(set(by_bound), {10, 20, 50})
        for entry in by_bound.values():
            self.assertTrue(entry["all_roots_distinct"])
            self.assertTrue(entry["all_large_primes_h19_new"])


if __name__ == "__main__":
    unittest.main()
