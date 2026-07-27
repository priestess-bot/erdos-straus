import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_pure_new_100m_closure",
    ROOT
    / "reproductions"
    / "type_ii_tail_deflation_p_minus_one_pure_new_100m_closure.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOnePureNew100mClosureTests(unittest.TestCase):
    def test_state_dependent_pure_new_closure_through_one_hundred_million(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-pure-new-100m-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000_000)
        self.assertEqual(result["core_prime_count"], 719_781)
        self.assertEqual(result["strict_descent_count"], 719_740)
        self.assertEqual(result["strict_descent_residual_count"], 41)
        self.assertEqual(result["base_short_certificate_count"], 27)
        self.assertEqual(result["later_pure_new_one_prime_count"], 14)
        self.assertEqual(result["least_h_first_later_multi_new_count"], 5)
        self.assertEqual(
            result["later_pure_new_shift_histogram"],
            {"3": 6, "4": 3, "5": 2, "9": 1, "24": 1, "48": 1},
        )
        self.assertEqual(result["unclosed_primes"], [])
        deep = next(record for record in result["records"] if record["prime"] == 56_040_889)
        self.assertEqual(deep["first_later_shift"], 11)
        self.assertEqual(deep["least_h_first_later_witness"]["shift"], 11)
        self.assertEqual(deep["first_pure_new_witness"]["shift"], 48)


if __name__ == "__main__":
    unittest.main()
