import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_canonical_ray",
    ROOT / "reproductions" / "type_ii_canonical_ray.py",
)
assert SPEC and SPEC.loader
canonical_ray = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = canonical_ray
SPEC.loader.exec_module(canonical_ray)


class TypeIICanonicalRayTests(unittest.TestCase):
    def test_canonical_squarefree_decomposition(self):
        self.assertEqual(canonical_ray.canonical_pair(1), (1, 1))
        self.assertEqual(canonical_ray.canonical_pair(8), (2, 2))
        self.assertEqual(canonical_ray.canonical_pair(36), (6, 1))
        self.assertEqual(canonical_ray.canonical_pair(125), (5, 5))

    def test_canonical_modulus_dominates_every_representation_of_a_shift(self):
        for a, c in ((1, 4), (1, 8), (2, 9), (3, 12), (5, 5), (6, 7)):
            self.assertTrue(canonical_ray.canonical_dominates_raw_pair(a, c))

    def test_same_raw_factor_transfers_to_the_canonical_ray(self):
        cases = ((313, 1, 4, 47), (409, 1, 8, 63), (1489, 2, 9, 71))
        for prime, a, c, h in cases:
            canonical_a, canonical_c = canonical_ray.canonical_pair(a * a * c)
            self.assertGreaterEqual(prime, 4 * a * a * c)
            self.assertEqual((prime + 4 * a * a * c) % h, 0)
            self.assertEqual((h + 1) % (4 * a * c), 0)
            self.assertEqual((h + 1) % (4 * canonical_a * canonical_c), 0)
            certificate = canonical_ray.ray.short_certificate.type_ii_raw_ray_certificate(
                prime,
                canonical_a,
                canonical_c,
                (h + 1) // (4 * canonical_a * canonical_c),
            )
            self.assertIsNotNone(certificate)

    def test_canonical_box_profile(self):
        result = canonical_ray.run_profile(10_000, 14, 14)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["canonical_pair_count"], 169)
        self.assertEqual(result["canonical_box_captured_count"], 143)
        self.assertEqual(result["remaining_after_greedy"], [])

    def test_checked_profile_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-rays-1m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000)
        self.assertEqual(result["canonical_pair_count"], 169)
        self.assertEqual(result["base_captured_count"], 9_708)
        self.assertEqual(len(result["base_missing"]), 24)
        self.assertEqual(len(result["joint_base_failure_profiles"]), 24)
        classes = [
            ray["class"]
            for profile in result["joint_base_failure_profiles"]
            for ray in profile["rays"]
        ]
        self.assertEqual(classes.count("outside:0"), 297)
        self.assertEqual(len(result["greedy_complement"]), 8)
        self.assertEqual(result["remaining_after_greedy"], [])

    def test_low_boundary_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-rays-low-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 11_000)
        self.assertEqual(result["core_prime_count"], 153)
        self.assertEqual(result["canonical_box_captured_count"], 153)
        self.assertEqual(result["remaining_after_greedy"], [])


if __name__ == "__main__":
    unittest.main()
