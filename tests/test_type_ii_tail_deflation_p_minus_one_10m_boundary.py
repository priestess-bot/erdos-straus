import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_10m_boundary",
    ROOT / "reproductions" / "type_ii_tail_deflation_p_minus_one_10m_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOne10mBoundaryTests(unittest.TestCase):
    def test_three_layer_boundary_through_ten_million(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-10m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["tail_deflation_strict_lift_count"], 82_803)
        self.assertEqual(result["tail_deflation_residual_count"], 84)
        self.assertEqual(result["p_minus_one_strict_lift_count"], 77)
        self.assertEqual(result["combined_strict_lift_count"], 82_880)
        self.assertEqual(result["combined_unclosed_count"], 7)
        self.assertEqual(
            result["uncovered_primes"],
            [
                214_729,
                297_049,
                878_089,
                1_511_449,
                3_942_409,
                5_478_169,
                6_294_649,
            ],
        )


if __name__ == "__main__":
    unittest.main()
