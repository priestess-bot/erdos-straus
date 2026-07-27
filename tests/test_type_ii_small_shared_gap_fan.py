import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_shared_gap_fan",
    ROOT / "reproductions" / "type_ii_small_shared_gap_fan.py",
)
assert SPEC and SPEC.loader
fan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fan
SPEC.loader.exec_module(fan)


class TypeIISmallSharedGapFanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spf = fan.short_certificate.smallest_prime_factors(100_011)

    def test_each_explicit_branch_constructs_a_shared_type_ii_witness(self):
        witnesses = {}
        for prime in fan.short_certificate.primes_up_to(100_000):
            if prime % 24 != 1:
                continue
            witness = fan.small_shared_gap_witness(prime, self.spf)
            if witness is not None:
                witnesses.setdefault(witness.branch, witness)
        self.assertEqual(
            set(witnesses),
            {"m3_factor_2_mod_3", "m7_explicit_residue", "m11_explicit_residue"},
        )
        self.assertEqual(
            {
                witness.branch: (witness.gap, witness.shared_divisor)
                for witness in witnesses.values()
            },
            {
                "m3_factor_2_mod_3": (3, 4),
                "m7_explicit_residue": (7, 8),
                "m11_explicit_residue": (11, 12),
            },
        )

    def test_residual_has_the_exact_three_failure_conditions(self):
        self.assertTrue(fan.explicit_residual_conditions(193, self.spf))
        self.assertIsNone(fan.small_shared_gap_witness(193, self.spf))
        self.assertFalse(fan.explicit_residual_conditions(73, self.spf))

    def test_one_million_audit_is_stable(self):
        audit = fan.run_audit(1_000_000)
        self.assertEqual(audit["core_prime_count"], 9_732)
        self.assertEqual(
            audit["counts"],
            {
                "m3_factor_2_mod_3": 5_192,
                "m7_explicit_residue": 2_271,
                "m11_explicit_residue": 509,
                "explicit_residual": 1_760,
            },
        )
        self.assertEqual(audit["covered_count"], 7_972)


if __name__ == "__main__":
    unittest.main()
