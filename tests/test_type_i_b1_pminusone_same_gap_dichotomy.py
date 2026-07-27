import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b1_pminusone_same_gap_dichotomy",
    ROOT / "reproductions" / "type_i_b1_pminusone_same_gap_dichotomy.py",
)
assert SPEC and SPEC.loader
dichotomy = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dichotomy
SPEC.loader.exec_module(dichotomy)


class TypeIBOnePMinusOneSameGapDichotomyTests(unittest.TestCase):
    def test_checked_profile_rebuilds(self):
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-b1-pminusone-same-gap-dichotomy-results.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(dichotomy.run_audit(), expected)
        residual = expected["stored_500m_b1_residual"]
        self.assertEqual(residual["all_b1_count"], 1_713)
        self.assertEqual(residual["pminusone_count"], 1_400)
        self.assertEqual(
            [item["p"] for item in expected["nonoverlap_ray"]["prime_samples"]],
            [32497, 64081, 79873],
        )

    def test_same_gap_conditions_are_exact(self):
        overlap = dichotomy.b1_pminusone_witness(1, 6, 5)
        self.assertTrue(overlap["bridge_condition"])
        self.assertTrue(overlap["same_gap_type_ii_condition"])
        self.assertIsNotNone(overlap["same_gap_type_ii_tail"])

        nonoverlap = dichotomy.b1_pminusone_witness(7, 2, 173)
        self.assertTrue(nonoverlap["bridge_condition"])
        self.assertFalse(nonoverlap["same_gap_type_ii_condition"])
        self.assertIsNone(nonoverlap["same_gap_type_ii_tail"])

    def test_positive_parameters_are_required(self):
        for values in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                dichotomy.parameters(*values)

    def test_small_chart_matches_an_unrestricted_type_ii_divisor_search(self):
        for q in range(1, 8):
            for r in range(1, 12):
                for A in range(1, 40):
                    state = dichotomy.parameters(q, r, A)
                    p, m, C = state["p"], state["m"], state["C"]
                    if p % 24 != 1 or not dichotomy.has_pminusone_terminal_bridge(q, r, A):
                        continue
                    x = A * C
                    exists_by_all_divisors = False
                    if (p - 1) % (m + 1) == 0:
                        for divisor in range(1, x + 1):
                            if (
                                x * x % divisor == 0
                                and (divisor + x) % m == 0
                            ):
                                exists_by_all_divisors = True
                                break
                    self.assertEqual(
                        dichotomy.same_gap_type_ii_tail(q, r, A) is not None,
                        exists_by_all_divisors,
                        (q, r, A),
                    )


if __name__ == "__main__":
    unittest.main()
