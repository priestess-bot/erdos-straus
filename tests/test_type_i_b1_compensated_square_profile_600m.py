from fractions import Fraction
import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_b1_compensated_square_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-b1-compensated-square-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("type_i_b1_compensated_square_profile", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIBOneCompensatedSquareProfileTests(unittest.TestCase):
    def test_odd_complement_r_three_example(self):
        witness = profile.compensated_witness(73, 4, 5, 7, 3, 1)
        self.assertEqual(
            witness,
            {
                "A": 4,
                "B": 1,
                "C": 5,
                "H": 11,
                "m": 7,
                "R": 3,
                "K": 55,
                "T": 1,
                "E": 100,
                "q": 2,
                "source_denominator": 40,
                "source_term": 22,
                "upper_half": True,
            },
        )
        assert witness is not None
        self.assertEqual(
            Fraction(4, 40),
            Fraction(1, 22) + Fraction(1, 20) + Fraction(1, 220),
        )

    def test_self_square_is_the_t_equal_four_special_case(self):
        witness = profile.compensated_witness(337, 17, 5, 3, 7, 4)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual((witness["E"], witness["q"], witness["source_denominator"]), (400, 14, 280))

    def test_finite_profile_is_reproducible(self):
        payload = profile.run_audit()
        self.assertEqual(payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(
            (
                payload["input_residual_count"],
                payload["compensated_square_covered_count"],
                payload["compensated_square_miss_count"],
                payload["B_one_normal_forms_exhaustively_checked"],
                payload["H_square_divisors_exhaustively_checked"],
                payload["compensated_square_candidate_count"],
                payload["upper_half_covered_count"],
                payload["maximum_selected_gap"],
            ),
            (57, 36, 21, 447, 19465, 151, 20, 991),
        )


if __name__ == "__main__":
    unittest.main()
