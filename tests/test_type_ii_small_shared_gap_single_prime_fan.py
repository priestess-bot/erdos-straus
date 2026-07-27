import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_shared_gap_single_prime_fan",
    ROOT / "reproductions" / "type_ii_small_shared_gap_single_prime_fan.py",
)
assert SPEC and SPEC.loader
fan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fan
SPEC.loader.exec_module(fan)


class TypeIISmallSharedGapSinglePrimeFanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spf = fan.short_certificate.smallest_prime_factors(100_011)

    def test_m7_and_m11_single_prime_branches_are_constructive(self):
        m7 = fan.single_prime_fan_witness(673, self.spf)
        m11 = fan.single_prime_fan_witness(3049, self.spf)
        self.assertEqual(
            (m7.branch, m7.gap, m7.type_ii_divisor, m7.shared_divisor),
            ("m7_single_prime", 7, 5, 8),
        )
        self.assertEqual(
            (m11.branch, m11.gap, m11.type_ii_divisor, m11.shared_divisor),
            ("m11_single_prime", 11, 5, 12),
        )

    def test_one_million_audit_is_stable(self):
        audit = fan.run_audit(1_000_000)
        self.assertEqual(audit["core_prime_count"], 9_732)
        self.assertEqual(
            audit["counts"],
            {
                "m3_factor_2_mod_3": 5_192,
                "m7_explicit_residue": 2_271,
                "m7_single_prime": 530,
                "m11_explicit_residue": 509,
                "m11_single_prime": 352,
                "single_prime_residual": 878,
            },
        )
        self.assertEqual(audit["covered_count"], 8_854)


if __name__ == "__main__":
    unittest.main()
