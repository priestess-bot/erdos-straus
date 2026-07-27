import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_reverse_two_tail_linear_e_full_b_boundary",
    ROOT / "reproductions" / "type_i_h19_reverse_two_tail_linear_e_full_b_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIH19ReverseTwoTailLinearEFullBBoundaryTests(unittest.TestCase):
    def test_no_unbounded_b_linear_lift_releases_the_b20_residual(self):
        profile = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-overflow-b20-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = boundary.run_audit(profile, 127)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["unbounded_b_audited_count"],
                actual["unbounded_b_normal_form_count"],
                actual["strict_reverse_lift_count"],
            ),
            (42, 1_708, 507),
        )
        self.assertEqual(actual["unbounded_b_linear_e_captured_count"], 0)
        self.assertEqual(actual["full_box_linear_e_captured_count"], 622)
        self.assertEqual(actual["unbounded_b_linear_e_misses"], profile["misses_by_b_cap"]["20"])
        self.assertEqual(actual["least_square_surplus_exponent_histogram"], {"1": 39, "2": 2, "5": 1})
        self.assertEqual(actual["least_square_surplus_support_histogram"], {"1": 39, "2": 2, "4": 1})
        self.assertEqual(
            actual["multi_prime_square_surplus_primes"],
            [243_145_681, 334_152_361, 707_590_321],
        )
        self.assertTrue(all(record["linear_e_witness"] is None for record in actual["records"]))
        extreme = next(record for record in actual["records"] if record["prime"] == 334_152_361)
        self.assertEqual(
            (
                extreme["least_square_surplus"]["extra_exponent_count"],
                extreme["least_square_surplus"]["extra_prime_support_count"],
                extreme["least_square_surplus"]["square_surplus"],
            ),
            (5, 4, 1_654_220),
        )


if __name__ == "__main__":
    unittest.main()
