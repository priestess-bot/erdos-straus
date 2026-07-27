import unittest

from reproductions.type_i_normal_gap_source_even_bridge import gap_source_even_bridge


class TypeINormalGapSourceEvenBridgeTests(unittest.TestCase):
    def test_positive_b1_gap_source_bridge(self):
        self.assertEqual(
            gap_source_even_bridge(73, 7, 4, 1, 5),
            {
                "R": 3,
                "K": 55,
                "bridge_factor": 22,
                "source_denominator": 66,
                "source_term": 165,
            },
        )

    def test_positive_overflow_gap_source_bridge(self):
        witness = gap_source_even_bridge(1033, 7, 13, 2, 10)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            witness,
            {
                "R": 23,
                "K": 5940,
                "bridge_factor": 162,
                "source_denominator": 1026,
                "source_term": 37620,
            },
        )

    def test_negative_forms_do_not_fake_the_canonical_bridge(self):
        self.assertIsNone(gap_source_even_bridge(73, 15, 2, 1, 11))
        self.assertIsNone(gap_source_even_bridge(73, 7, 1, 2, 10))

    def test_invalid_normal_form_is_rejected(self):
        with self.assertRaises(ValueError):
            gap_source_even_bridge(73, 7, 1, 1, 5)


if __name__ == "__main__":
    unittest.main()
