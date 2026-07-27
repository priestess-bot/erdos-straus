import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "chamberland_ac_ray_translation",
    ROOT / "reproductions" / "chamberland_ac_ray_translation.py",
)
assert SPEC and SPEC.loader
translation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = translation
SPEC.loader.exec_module(translation)


class ChamberlandAcRayTranslationTests(unittest.TestCase):
    def test_non_nested_chamberland_pair_becomes_an_ac_ray(self):
        # Chamberland's p=1009 example: 1009=23*47-4*3*6.
        record = translation.from_chamberland(23, 47, 3, 6)
        self.assertEqual(
            {key: record[key] for key in ("p", "a", "c", "k", "b")},
            {"p": 1009, "a": 3, "c": 2, "k": 1, "b": 44},
        )
        canonical = translation.canonical_ac_from_chamberland(23, 47, 3, 6)
        self.assertEqual((canonical["q"], canonical["reordered"]), (23, 0))

    def test_nonordered_chamberland_coordinates_do_not_fake_an_ac_certificate(self):
        # The factor translation is exact, but the same coordinates need not
        # satisfy the Type II divisor ordering A <= B.
        record = translation.from_chamberland(39, 7, 5, 10)
        self.assertEqual(
            {key: record[key] for key in ("p", "a", "c", "k", "b")},
            {"p": 73, "a": 5, "c": 2, "k": 1, "b": 2},
        )
        self.assertIsNone(
            translation.ray.short_certificate.type_ii_raw_ray_certificate(73, 5, 2, 1)
        )
        canonical = translation.canonical_ac_from_chamberland(39, 7, 5, 10)
        self.assertEqual(
            {
                key: canonical[key]
                for key in ("p", "q", "r", "a", "b", "c", "k", "reordered")
            },
            {
                "p": 73,
                "q": 15,
                "r": 7,
                "a": 2,
                "b": 5,
                "c": 2,
                "k": 1,
                "reordered": 1,
            },
        )

    def test_canonicalization_rebuilds_a_small_chamberland_box(self):
        primes = set(translation.ray.short_certificate.primes_up_to(50_000))
        checked = 0
        reordered = 0
        for q in range(3, 200, 4):
            quotient = (q + 1) // 4
            divisors = [value for value in range(1, quotient + 1) if quotient % value == 0]
            for s1 in divisors:
                for s2 in divisors:
                    for r in range(1, 201):
                        prime = q * r - 4 * s1 * s2
                        if prime not in primes or prime % 24 != 1:
                            continue
                        canonical = translation.canonical_ac_from_chamberland(q, r, s1, s2)
                        self.assertEqual(canonical["p"], prime)
                        self.assertEqual(
                            canonical["q"],
                            4 * canonical["a"] * canonical["c"] * canonical["k"] - 1,
                        )
                        self.assertEqual(
                            prime + 4 * canonical["a"] ** 2 * canonical["c"],
                            r * canonical["q"],
                        )
                        checked += 1
                        reordered += canonical["reordered"]
        self.assertEqual((checked, reordered), (3_509, 62))

    def test_ac_ray_round_trips_to_a_nested_chamberland_pair(self):
        record = translation.to_chamberland(84_525_841, 1, 14, 30, 1679)
        self.assertEqual(
            {key: record[key] for key in ("r", "s1", "s2", "a", "c", "k")},
            {"r": 50_343, "s1": 1, "s2": 14, "a": 1, "c": 14, "k": 30},
        )

    def test_bounded_witnesses_translate_in_the_small_audit(self):
        result = translation.run_audit(10_000, 14)
        self.assertEqual(result["translated_witness_count"], result["core_prime_count"])
        self.assertGreater(result["translated_witness_count"], 0)


if __name__ == "__main__":
    unittest.main()
