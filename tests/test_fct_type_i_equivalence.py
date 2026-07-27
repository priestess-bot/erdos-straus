import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "fct_type_i_equivalence", ROOT / "reproductions" / "fct_type_i_equivalence.py"
)
assert SPEC and SPEC.loader
fct = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fct
SPEC.loader.exec_module(fct)


class FCTTypeIEquivalenceTests(unittest.TestCase):
    def test_known_external_source_witnesses_recover_fct_data(self):
        first = fct.fct_from_external_source(73, 4, 7)
        self.assertIsNotNone(first)
        assert first is not None
        self.assertEqual((first.c0, first.c1, first.c2), (4, 3, 7))
        self.assertEqual(first.denominators, (20, 220, 4015))
        self.assertTrue(fct.verify_fct_identity(first))
        certificate = fct.certificate_from_fct(first)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(certificate.divisor, 80)

        second = fct.fct_from_external_source(193, 2, 39)
        self.assertIsNotNone(second)
        assert second is not None
        self.assertEqual((second.c0, second.c1, second.c2), (2, 3, 39))
        self.assertEqual(second.denominators, (58, 290, 27985))
        self.assertEqual(
            Fraction(4, 193),
            sum((Fraction(1, value) for value in second.denominators), Fraction()),
        )

    def test_fct_data_recovers_type_i_certificate(self):
        data = fct.fct_data(4, 3, 7)
        self.assertIsNotNone(data)
        assert data is not None
        self.assertEqual(data.prime, 73)
        self.assertEqual(data.k, 5)
        certificate = fct.certificate_from_fct(data)
        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual((certificate.gap, certificate.x, certificate.divisor), (7, 20, 80))

    def test_finite_external_source_audit(self):
        result = fct.run_audit(5_000, 32)
        self.assertEqual(result["core_prime_count"], 76)
        self.assertGreater(result["external_source_witness_count"], 0)
        self.assertTrue(result["sample_witnesses"])


if __name__ == "__main__":
    unittest.main()
