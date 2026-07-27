import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "marked_equivalence_short_certificate",
    ROOT / "reproductions" / "short_certificate.py",
)
assert SPEC and SPEC.loader
short_certificate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = short_certificate
SPEC.loader.exec_module(short_certificate)


class TypeIIScaledTailMarkedEquivalenceTests(unittest.TestCase):
    def test_marked_source_and_fixed_type_ii_target_have_the_same_tail(self):
        prime = 67_369
        gap = 35
        first_scale = 7
        spf = short_certificate.smallest_prime_factors(100_000)
        witness = short_certificate.type_ii_scaled_first_tail_deflation_witness(
            prime, gap, first_scale, spf
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        x, target_y, target_z = witness.target_solution
        source_x, source_y, source_z = witness.source_solution
        source_tail = (
            Fraction(4, witness.source_denominator) - Fraction(1, source_x)
        )
        target_tail = prime * (Fraction(4, prime) - Fraction(1, x))
        self.assertEqual(source_tail, Fraction(gap, x))
        self.assertEqual(target_tail, Fraction(gap, x))
        self.assertEqual(
            (source_x // first_scale, source_y * prime, source_z * prime),
            (x, target_y, target_z),
        )
