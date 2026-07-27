import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_r_p_minus_one_tail_deflation_closure",
    ROOT / "reproductions" / "type_ii_small_r_p_minus_one_tail_deflation_closure.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIISmallRPMinusOneTailDeflationClosureTests(unittest.TestCase):
    def test_four_branch_core_closure_through_one_hundred_thousand(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-small-r-p-minus-one-tail-deflation-closure-100k-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000)
        self.assertEqual(result["core_prime_count"], 1_181)
        self.assertEqual(result["prior_small_r_or_p_minus_one_count"], 1_174)
        self.assertEqual(result["prior_small_r_or_p_minus_one_residual_count"], 7)
        self.assertEqual(result["even_source_strict_lift_count"], 2)
        self.assertEqual(result["tail_deflation_residual_count"], 5)
        self.assertEqual(result["tail_deflation_strict_lift_count"], 5)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            result["prior_small_r_or_p_minus_one_count"]
            + result["even_source_strict_lift_count"]
            + result["tail_deflation_strict_lift_count"],
            result["core_prime_count"],
        )
        self.assertEqual(
            [record["witness"]["gap"] for record in result["records"]],
            [11, 35, 7, 7, 3],
        )


if __name__ == "__main__":
    unittest.main()
