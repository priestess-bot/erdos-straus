import importlib.util
from fractions import Fraction
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cyclic_reciprocal_lift", ROOT / "reproductions" / "cyclic_reciprocal_lift.py"
)
assert SPEC and SPEC.loader
cyclic = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cyclic
SPEC.loader.exec_module(cyclic)


class CyclicReciprocalLiftTests(unittest.TestCase):
    def test_real_transport_identity(self):
        source = (10, 17, 850)
        self.assertEqual(
            sum((Fraction(1, value) for value in source), Fraction()),
            Fraction(4, 25),
        )
        values = cyclic.cyclic_reciprocals(97, 25, source)
        self.assertEqual(sum(values, Fraction()), Fraction(4, 97))
        self.assertIsNone(cyclic.cyclic_target(97, 25, source))

    def test_weighted_even_standard_source_has_no_integral_target(self):
        prime = 73
        source_denominator = 72
        source = (36, 72, 72)
        self.assertEqual(
            sum((Fraction(1, value) for value in source), Fraction()),
            Fraction(4, source_denominator),
        )
        for numerator, denominator in ((1, 2), (1, 3), (2, 3), (3, 5), (5, 7)):
            values = cyclic.weighted_cyclic_reciprocals(
                prime, source_denominator, source, numerator, denominator
            )
            self.assertEqual(sum(values, Fraction()), Fraction(4, prime))
            self.assertIsNone(
                cyclic.weighted_cyclic_target(
                    prime, source_denominator, source, numerator, denominator
                )
            )

    def test_weighted_three_divisible_standard_source_has_no_integral_target(self):
        prime = 73
        source_denominator = 72
        source = (24, 144, 144)
        self.assertEqual(
            sum((Fraction(1, value) for value in source), Fraction()),
            Fraction(4, source_denominator),
        )
        for numerator, denominator in ((1, 2), (1, 3), (2, 3), (3, 5), (5, 7)):
            self.assertIsNone(
                cyclic.weighted_cyclic_target(
                    prime, source_denominator, source, numerator, denominator
                )
            )

    def test_weighted_nonstandard_source_has_a_genuine_positive_example(self):
        source = (4, 120, 120)
        self.assertEqual(
            sum((Fraction(1, value) for value in source), Fraction()), Fraction(4, 15)
        )
        target = cyclic.weighted_cyclic_target(31, 15, source, 1, 2)
        self.assertEqual(target, (16, 248, 16))
        assert target is not None
        self.assertEqual(
            sum((Fraction(1, value) for value in target), Fraction()), Fraction(4, 31)
        )

    def test_core_audit_small_range_has_no_lifts(self):
        result = cyclic.run_audit(200)
        self.assertEqual(result["core_primes"], 3)
        self.assertEqual(result["integer_cyclic_lifts"], 0)
        self.assertEqual(
            [record["prime"] for record in result["records"]], [73, 97, 193]
        )
        self.assertGreater(result["source_solutions_checked"], 30_000)


if __name__ == "__main__":
    unittest.main()
