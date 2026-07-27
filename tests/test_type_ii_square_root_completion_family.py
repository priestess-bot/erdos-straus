import unittest

import sympy

from reproductions import type_ii_square_root_completion_family as family


class TypeIISquareRootCompletionFamilyTests(unittest.TestCase):
    def test_completion_factor_is_minimal(self):
        self.assertEqual(family.completion_factor(8, 1), 1)
        self.assertEqual(family.completion_factor(8, 7), 7)
        self.assertEqual(family.completion_factor(8, 14), 7)
        self.assertEqual(family.completion_factor(8, 49), 7)
        self.assertEqual(family.completion_factor(8, 133), 133)
        self.assertEqual(family.completion_factor(18, 36), 1)

    def test_m31_d7_h19_record_reconstructs_a_completed_descent(self):
        witness = family.two_tail_witness(8, 7, 2_803_593_722_609_700)
        self.assertEqual(witness["gap"], 31)
        self.assertEqual(witness["completion_factor"], 7)
        self.assertEqual(witness["prime"], 89_714_999_123_510_401)
        self.assertTrue(sympy.isprime(witness["prime"]))
        self.assertLess(witness["source_denominator"], witness["prime"])

    def test_tail_certificate_recovers_the_completed_divisor_normal_form(self):
        normalized = family.verify_normal_form(89_714_999_123_510_401, 31, 7)
        self.assertEqual(normalized["q"], 8)
        self.assertEqual(normalized["parameter"], 2_803_593_722_609_700)
        self.assertEqual(normalized["source_denominator"], 2_803_593_722_609_701)
