import unittest

from reproductions import type_ii_tail_support_defect as defect


class TypeIITailSupportDefectTests(unittest.TestCase):
    def test_m31_completed_divisor_has_support_one_without_a_base(self):
        witness = defect.support_witness(8, 2_803_593_722_609_701, set(), 1)
        self.assertIsNotNone(witness)
        self.assertEqual(witness["gap"], 31)
        self.assertEqual(witness["support"], 1)

    def test_m31_fixed_factor_example_has_support_zero(self):
        witness = defect.support_witness(8, 1_802_230_778_703_376, {2, 7, 19}, 0)
        self.assertIsNotNone(witness)
        self.assertEqual(witness["gap"], 31)
        self.assertEqual(witness["support"], 0)


if __name__ == "__main__":
    unittest.main()
