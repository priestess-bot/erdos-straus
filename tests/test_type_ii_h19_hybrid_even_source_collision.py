import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_hybrid_even_source_collision",
    ROOT / "reproductions" / "type_ii_h19_hybrid_even_source_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class TypeIIH19HybridEvenSourceCollisionTests(unittest.TestCase):
    def test_general_cross_family_bounds(self):
        self.assertEqual(collision.standard_even_collision_bound(12, 7), 330)
        self.assertEqual(collision.even_ray_collision_bound(7, 45), 187)
        self.assertEqual(collision.even_even_collision_bound(3, 7), 4)
        for prime in collision.prime_factors(330):
            self.assertEqual(330 % prime, 0)

    def test_bounds_hold_for_small_core_instances(self):
        for prime in (73, 97, 193, 241, 337):
            base = (prime - 1) // 4
            for scale in range(1, base + 1):
                if base % scale:
                    continue
                standard = prime - base // scale
                for distance in (1, 3, 5, 7):
                    source = prime - distance
                    self.assertEqual(
                        collision.standard_even_collision_bound(scale, distance)
                        % math.gcd(standard, source),
                        0,
                    )

    def test_three_hundred_million_pressure_artifact(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-hybrid-even-source-collision-300m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 300_000_000)
        self.assertEqual(result["h19_shift_bound"], 19)
        self.assertEqual(result["pressure_point_count"], 3)
        self.assertTrue(result["all_private_parts_pairwise_coprime"])
        self.assertTrue(result["all_even_source_direct_ray_gcds_are_one"])
        self.assertEqual(
            [
                (
                    row["prime"],
                    row["distance"],
                    row["pure_new_type_ii_shift"],
                    row["even_source_direct_ray_gcd"],
                )
                for row in result["records"]
            ],
            [
                (35_840_809, 7, 45, 1),
                (132_285_169, 3, 27, 1),
                (141_326_089, 3, 63, 1),
            ],
        )

    def test_five_hundred_million_pressure_artifact(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-hybrid-even-source-collision-500m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 500_000_000)
        self.assertEqual(result["pressure_point_count"], 3)
        self.assertTrue(result["all_private_parts_pairwise_coprime"])
        self.assertTrue(result["all_even_source_direct_ray_gcds_are_one"])

    def test_one_billion_pressure_artifact_adds_the_long_distance_point(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-hybrid-even-source-collision-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["pressure_point_count"], 4)
        self.assertTrue(result["all_private_parts_pairwise_coprime"])
        self.assertTrue(result["all_even_source_direct_ray_gcds_are_one"])
        self.assertEqual(
            [
                (
                    row["prime"],
                    row["distance"],
                    row["pure_new_type_ii_shift"],
                    row["pure_new_type_ii_factor"],
                    row["even_source_direct_ray_gcd"],
                )
                for row in result["records"]
            ][-1],
            (640_775_689, 34_091, 45, 359, 1),
        )


if __name__ == "__main__":
    unittest.main()
