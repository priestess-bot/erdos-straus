import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "two_source_full_tail_size_obstruction",
    ROOT / "reproductions" / "two_source_full_tail_size_obstruction.py",
)
assert SPEC and SPEC.loader
obstruction = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = obstruction
SPEC.loader.exec_module(obstruction)


class TwoSourceFullTailSizeObstructionTests(unittest.TestCase):
    def test_sharp_bound_for_a_known_core_prime(self):
        self.assertEqual(obstruction.source_denominator(73, 1), 55)
        self.assertEqual(obstruction.residual_after_preserved_term(73, 1), Fraction(3, 55))
        self.assertEqual(obstruction.full_source_tail_bound(73), Fraction(2, 55))
        self.assertTrue(obstruction.verify_pointwise_obstruction(73, 1))

    def test_finite_audit(self):
        result = obstruction.run_audit(10_000)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["stationary_scale_state_count"], 2425)
        self.assertTrue(result["sample_profiles"])


if __name__ == "__main__":
    unittest.main()
