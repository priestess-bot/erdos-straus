import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_reverse_two_tail_square_necessity",
    ROOT / "reproductions" / "type_i_h19_reverse_two_tail_square_necessity.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19ReverseTwoTailSquareNecessityTests(unittest.TestCase):
    def test_linear_e_restriction_has_exact_h19_residuals(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-square-necessity-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(h19, 127)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["h19_residual_count"], actual["b_one_normal_form_count"], actual["strict_reverse_lift_count"]),
            (664, 7_175, 37_075),
        )
        self.assertEqual((actual["linear_e_captured_count"], len(actual["linear_e_misses"])), (599, 65))
        self.assertEqual(actual["least_square_surplus_exponent_histogram"], {"1": 54, "2": 9, "3": 1, "5": 1})
        self.assertEqual(actual["least_square_surplus_support_histogram"], {"1": 55, "2": 9, "4": 1})
        self.assertEqual(
            (actual["maximum_least_square_surplus_exponent_count"], actual["maximum_least_square_surplus_support_count"]),
            (5, 4),
        )
        self.assertEqual(actual["linear_e_misses"][:4], [1_520_401, 7_378_849, 8_955_769, 13_422_481])
        self.assertTrue(all(record["strict_reverse_lift_count"] > 0 for record in actual["records"]))
        for record in actual["records"]:
            witness = record["linear_e_witness"]
            if witness is not None:
                self.assertEqual((4 * witness["K"]) % witness["E"], 0)
            else:
                surplus = record["least_square_surplus"]
                self.assertIsNotNone(surplus)
                self.assertGreater(surplus["extra_exponent_count"], 0)
        extreme = next(record for record in actual["records"] if record["prime"] == 334_152_361)
        self.assertEqual(extreme["strict_reverse_lift_count"], 1)
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
