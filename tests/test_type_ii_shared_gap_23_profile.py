import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_shared_gap_23_profile",
    ROOT / "reproductions" / "type_ii_shared_gap_23_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIISharedGap23ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spf = profile.short_certificate.smallest_prime_factors(100_023)

    def test_m23_base_branch_is_an_exact_shared_type_ii_certificate(self):
        witness = profile.m23_base_witness(73)
        self.assertIsNone(witness)
        witness = profile.m23_base_witness(337)
        self.assertEqual(
            (witness.gap, witness.type_ii_divisor, witness.shared_divisor),
            (23, 2, 24),
        )

    def test_one_million_profile_is_stable(self):
        audit = profile.run_audit(1_000_000)
        self.assertEqual(audit["core_prime_count"], 9_732)
        self.assertEqual(
            audit["counts"],
            {
                "earlier_type_ii": 9_327,
                "m23_base": 165,
                "m23_general": 90,
                "no_type_ii_3_7_11_23": 150,
            },
        )
        self.assertEqual(audit["captured_count"], 9_582)


if __name__ == "__main__":
    unittest.main()
