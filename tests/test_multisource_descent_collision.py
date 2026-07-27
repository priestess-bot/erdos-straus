import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "multisource_descent_collision",
    ROOT / "reproductions" / "multisource_descent_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class MultisourceDescentCollisionTests(unittest.TestCase):
    def test_gcd_bound_for_all_small_core_sources(self):
        primes = collision.short_certificate.primes_up_to(10_000)
        for prime in primes:
            if prime % 24 != 1:
                continue
            base = (prime - 1) // 4
            scales = collision.short_certificate.positive_divisors_from_spf(
                base, collision.short_certificate.smallest_prime_factors(10_000)
            )
            for index, left in enumerate(scales):
                left_source = collision.source_denominator(prime, left)
                for right in scales[index + 1 :]:
                    right_source = collision.source_denominator(prime, right)
                    self.assertEqual(
                        collision.pair_collision_bound(left, right)
                        % math.gcd(left_source, right_source),
                        0,
                    )

    def test_p8328961_deep_path_has_only_finite_collision_primes(self):
        row = collision.profile(
            8_328_961, (1, 2, 3, 4, 5, 6, 8, 9, 10, 12)
        )
        self.assertEqual(row["collision_primes"], [2, 3, 5, 7, 11])
        self.assertTrue(
            all(
                math.gcd(left, right) == 1
                for index, left in enumerate(row["private_source_parts"].values())
                for right in list(row["private_source_parts"].values())[index + 1 :]
            )
        )
        self.assertEqual(
            collision.source_ray_collision_bound(12, 19),
            3_571,
        )
        joint = collision.joint_profile(
            8_328_961, (1, 2, 3, 4, 5, 6, 8, 9, 10, 12), tuple(range(1, 20))
        )
        self.assertTrue(joint["joint_private_parts_pairwise_coprime"])

    def test_checked_h19_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "multisource-descent-collision-h19-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["residual_count"], 65)
        self.assertTrue(result["all_private_source_parts_pairwise_coprime"])
        self.assertTrue(result["all_joint_private_parts_pairwise_coprime"])
        self.assertEqual(result["joint_shift_bound"], 19)
        self.assertGreaterEqual(result["profiles_with_actual_source_collision"], 0)


if __name__ == "__main__":
    unittest.main()
