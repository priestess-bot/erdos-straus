import importlib.util
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("external_source", ROOT / "reproductions" / "external_source.py")
assert SPEC and SPEC.loader
external_source = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = external_source
SPEC.loader.exec_module(external_source)


class ExternalSourceExperimentTests(unittest.TestCase):
    def test_small_experiment_has_exact_witnesses(self):
        result = external_source.run_experiment(100_000, 128)
        self.assertEqual(result["core_prime_count"], 1181)
        self.assertEqual(result["residual_after_direct_families"], 83)
        self.assertEqual(result["external_source_certified_count"], 83)
        self.assertEqual(result["external_source_missing"], [])
        self.assertGreater(result["largest_minimal_source_found"], 1)

    def test_factor_ray_normal_form_is_bijective_on_known_witnesses(self):
        first = external_source.external_source_factor_ray_normal_form(193, 2, 39)
        self.assertEqual(
            first,
            {"source": 2, "gap": 39, "q": 5, "r": 3, "t": 29},
        )
        self.assertEqual(
            external_source.external_source_factor_ray_witness(193, 3, 5),
            first,
        )

        second = external_source.external_source_factor_ray_normal_form(73, 4, 7)
        self.assertEqual(
            second,
            {"source": 4, "gap": 7, "q": 11, "r": 3, "t": 5},
        )
        self.assertEqual(
            external_source.external_source_factor_ray_witness(73, 3, 11),
            second,
        )

    def test_all_small_external_source_witnesses_round_trip_through_factor_rays(self):
        limit = 5_000
        trial_primes = external_source.short_certificate.primes_up_to(
            math.isqrt(4 * limit + 128) + 1
        )
        for prime in external_source.short_certificate.primes_up_to(limit):
            if prime % 24 != 1:
                continue
            for source in range(1, 33):
                for gap in external_source.divisors(prime + source, trial_primes):
                    normal = external_source.external_source_factor_ray_normal_form(
                        prime, source, gap
                    )
                    if normal is None:
                        continue
                    self.assertEqual(
                        external_source.external_source_factor_ray_witness(
                            prime, normal["r"], normal["q"]
                        ),
                        normal,
                    )


if __name__ == "__main__":
    unittest.main()
