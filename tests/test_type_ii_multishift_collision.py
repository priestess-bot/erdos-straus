import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_multishift_collision",
    ROOT / "reproductions" / "type_ii_multishift_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class TypeIIMultiShiftCollisionTests(unittest.TestCase):
    def test_collision_primes_are_exactly_the_prime_divisors_of_shift_differences(self):
        self.assertEqual(collision.collision_primes((1, 2, 3, 4)), (2, 3))
        self.assertEqual(
            collision.collision_primes(tuple(range(1, 15))),
            (2, 3, 5, 7, 11, 13),
        )

    def test_small_profile_has_pairwise_coprime_private_cofactors(self):
        result = collision.run_profile(10_000, 14)
        self.assertEqual(result["common_failure_count"], 1)
        self.assertEqual(result["common_failures"], [3361])
        self.assertTrue(result["all_private_cofactors_pairwise_coprime"])

    def test_checked_profile_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-collision-1m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000)
        self.assertEqual(result["collision_primes"], [2, 3, 5, 7, 11, 13])
        self.assertEqual(result["common_failure_count"], 24)
        self.assertTrue(result["all_private_cofactors_pairwise_coprime"])

    def test_extended_profile_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-collision-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["common_failure_count"], 128)
        self.assertTrue(result["all_private_cofactors_pairwise_coprime"])


if __name__ == "__main__":
    unittest.main()
