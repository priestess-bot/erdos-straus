from fractions import Fraction
import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_general_b_compensated_square_full_linear_profile_600m.py"
RESULT = ROOT / "reproductions" / "type-i-general-b-compensated-square-full-linear-profile-600m-results.json"

SPEC = importlib.util.spec_from_file_location("type_i_general_b_compensated_square_full_linear", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIGeneralBCompensatedSquareFullLinearProfileTests(unittest.TestCase):
    def test_nonfirst_linear_r_witness(self):
        witness = profile.compensated.compensated_witness(42622969, 15466, 13, 53, 1327, 27, 1)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(
            (witness["H"], witness["K"], witness["E"], witness["q"], witness["source_denominator"], witness["source_term"]),
            (417569, 287705041, 1898884, 15440, 42552640, 6447265360),
        )
        self.assertTrue(bool(witness["upper_half"]))
        self.assertEqual(
            Fraction(4, 42552640),
            Fraction(1, 6447265360) + Fraction(1, 15466 * 13 * 53) + Fraction(1, 15466 * 53 * 417569),
        )

    def test_full_linear_menu_profile_is_reproducible(self):
        payload = profile.run_audit()
        self.assertEqual(payload, json.loads(RESULT.read_text(encoding="utf-8")))
        self.assertEqual(
            (
                payload["input_residual_count"],
                payload["full_linear_R_compensated_square_covered_count"],
                payload["full_linear_R_compensated_square_miss_count"],
                payload["linear_source_coordinate_bound_max"],
                payload["linear_R_exhaustively_checked"],
                payload["directed_linear_source_state_count"],
                payload["K_square_divisors_exhaustively_checked"],
                payload["target_divisor_hits"],
                payload["target_normal_forms_exhaustively_checked"],
                payload["H_square_divisors_exhaustively_checked"],
                payload["compensated_square_candidate_count"],
                payload["upper_half_covered_count"],
            ),
            (13, 6, 7, 13378, 502, 884, 571698, 392, 196, 4196, 9, 6),
        )
        self.assertEqual(
            payload["misses"],
            [214729, 878089, 2210569, 13782409, 64214329, 105295129, 536944489],
        )


if __name__ == "__main__":
    unittest.main()
