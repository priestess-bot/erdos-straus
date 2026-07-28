from fractions import Fraction
import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_general_b_compensated_square_residual_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-general-b-compensated-square-residual-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("type_i_general_b_compensated_square_residual", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIGeneralBCompensatedSquareResidualProfileTests(unittest.TestCase):
    def test_general_b_nontrivial_compensator(self):
        witness = profile.compensated_witness(30997849, 33989, 3, 76, 119, 23, 128)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            (witness["H"], witness["K"], witness["E"], witness["q"], witness["source_denominator"], witness["source_term"]),
            (781744, 178237632, 26615808, 32720, 29840640, 199833310),
        )
        self.assertTrue(bool(witness["upper_half"]))
        self.assertEqual(
            Fraction(4, 29840640),
            Fraction(1, 199833310) + Fraction(1, 33989 * 3 * 76) + Fraction(1, 33989 * 76 * 781744),
        )

    def test_finite_selected_linear_profile_is_reproducible(self):
        payload = profile.run_audit()
        self.assertEqual(payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(
            (
                payload["input_residual_count"],
                payload["general_B_compensated_square_covered_count"],
                payload["general_B_compensated_square_miss_count"],
                payload["H_square_divisors_exhaustively_checked_within_selected_forms"],
                payload["general_B_compensated_square_candidate_count"],
                payload["upper_half_covered_count"],
                payload["selected_B_histogram"],
            ),
            (21, 8, 13, 429, 12, 6, {"1": 3, "2": 2, "3": 2, "11": 1}),
        )


if __name__ == "__main__":
    unittest.main()
