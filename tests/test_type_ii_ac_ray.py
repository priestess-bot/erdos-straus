import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_ac_ray", ROOT / "reproductions" / "type_ii_ac_ray.py"
)
assert SPEC and SPEC.loader
type_ii_ac_ray = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = type_ii_ac_ray
SPEC.loader.exec_module(type_ii_ac_ray)


class TypeIIACRayTests(unittest.TestCase):
    def test_bounded_k_templates_have_an_avoidance_modulus(self):
        pairs = ((1, 1), (1, 14), (5, 5))
        k_bound = 9
        modulus = type_ii_ac_ray.bounded_k_avoidance_modulus(pairs, k_bound)
        representative = modulus + 1
        self.assertEqual(modulus % 24, 0)

        # Every p == 1 (mod modulus) has the same nonzero residue K+A
        # modulo the corresponding generator h.
        for a, c in pairs:
            for k in range(1, k_bound + 1):
                h = 4 * a * c * k - 1
                self.assertEqual(modulus % h, 0)
                self.assertGreater(h, k + a)
                self.assertEqual((k * representative + a) % h, (k + a) % h)
                self.assertNotEqual((k * representative + a) % h, 0)

    def test_small_a_c_ray_audit_has_exact_witnesses(self):
        result = type_ii_ac_ray.run_experiment(10_000, 5)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["captured_count"], 143)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_minimal_ac_radius"], 5)
        self.assertEqual(
            result["ac_radius_record_holders"][-1],
            {
                "prime": 3361,
                "radius": 5,
                "a": 5,
                "c": 5,
                "k": 1,
                "h": 99,
                "gap": 39,
                "divisor": 125,
            },
        )

    def test_ray_factor_condition_recovers_known_large_k_witness(self):
        prime = 8_803_369
        bound = 3
        spf = type_ii_ac_ray.short_certificate.smallest_prime_factors(
            prime + 4 * bound**3
        )
        witness = type_ii_ac_ray.ray_witness(prime, bound, spf)
        self.assertEqual(witness[:4], (1, 3, 16, 191))
        assert witness is not None
        certificate = witness[4]
        self.assertEqual((certificate.gap, certificate.divisor), (46_091, 3))
        self.assertTrue(type_ii_ac_ray.short_certificate.verify_certificate(certificate))

        # The same A,C ray also has a much larger K, which produces the
        # smaller gap-191 certificate found by the moving-window audit.
        large_k_certificate = (
            type_ii_ac_ray.short_certificate.type_ii_factor_certificate(
                prime, 1, 3, 3_841
            )
        )
        self.assertIsNotNone(large_k_certificate)
        assert large_k_certificate is not None
        self.assertEqual((large_k_certificate.gap, large_k_certificate.divisor), (191, 3))
        self.assertTrue(
            type_ii_ac_ray.short_certificate.verify_certificate(large_k_certificate)
        )

    def test_radius_fourteen_record_witness(self):
        certificate = type_ii_ac_ray.short_certificate.type_ii_raw_ray_certificate(
            84_525_841, 1, 14, 30
        )
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.divisor), (50_343, 14))
        self.assertTrue(type_ii_ac_ray.short_certificate.verify_certificate(certificate))

    def test_extended_radius_fourteen_audit_artifact(self):
        payload = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-ii-ac-ray-2e8-bound14-results.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["prime_limit"], 200_000_000)
        self.assertEqual(payload["ac_box"], {"a_max": 14, "c_max": 14})
        self.assertEqual(payload["core_prime_count"], 1_383_890)
        self.assertEqual(payload["captured_count"], 1_383_890)
        self.assertEqual(payload["missing"], [])
        self.assertEqual(payload["largest_minimal_ac_radius"], 14)
        self.assertEqual(
            payload["ac_radius_record_holders"][-1],
            {
                "prime": 84_525_841,
                "radius": 14,
                "a": 1,
                "c": 14,
                "k": 30,
                "h": 1_679,
                "gap": 50_343,
                "divisor": 14,
            },
        )

    def test_half_billion_radius_fourteen_audit_artifact(self):
        payload = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-ii-ac-ray-500m-bound14-results.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["prime_limit"], 500_000_000)
        self.assertEqual(payload["ac_box"], {"a_max": 14, "c_max": 14})
        self.assertEqual(payload["core_prime_count"], 3_292_848)
        self.assertEqual(payload["captured_count"], 3_292_848)
        self.assertEqual(payload["missing"], [])
        self.assertEqual(payload["largest_minimal_ac_radius"], 14)
        self.assertEqual(
            payload["ac_radius_record_holders"][-1],
            {
                "prime": 84_525_841,
                "radius": 14,
                "a": 1,
                "c": 14,
                "k": 30,
                "h": 1_679,
                "gap": 50_343,
                "divisor": 14,
            },
        )

    def test_ray_factor_pair_identity(self):
        # Every accepted AC-ray witness factors p+4*A^2*C as h times its
        # recovered gap. This is the exact arithmetic used by the residual
        # sieve; it is stronger than merely checking h divides the shift.
        result = type_ii_ac_ray.run_experiment(10_000, 5)
        for entry in result["ac_radius_record_holders"]:
            prime = entry["prime"]
            a = entry["a"]
            c = entry["c"]
            h = entry["h"]
            certificate = type_ii_ac_ray.short_certificate.type_ii_raw_ray_certificate(
                prime, a, c, entry["k"]
            )
            self.assertIsNotNone(certificate)
            assert certificate is not None
            self.assertEqual(prime + 4 * a * a * c, h * certificate.gap)
            self.assertEqual(h % (4 * a * c), 4 * a * c - 1)
            self.assertTrue(
                type_ii_ac_ray.short_certificate.verify_certificate(certificate)
            )
