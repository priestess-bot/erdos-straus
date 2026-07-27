import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_hybrid_small_r_p_minus_one_descent",
    ROOT / "reproductions" / "type_ii_h19_hybrid_small_r_p_minus_one_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19HybridSmallRPMinusOneDescentTests(unittest.TestCase):
    def test_checked_one_billion_hybrid_closure(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-hybrid-small-r-p-minus-one-descent-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 103)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["bounded_r_strict_lift_count"], 564)
        self.assertEqual(result["p_minus_one_residual_count"], 100)
        self.assertEqual(result["p_minus_one_scaled_source_candidate_count"], 10_046)
        self.assertEqual(result["p_minus_one_tail_divisor_test_count"], 97_636_776)
        self.assertEqual(result["p_minus_one_hit_candidate_count"], 723)
        self.assertEqual(result["p_minus_one_strict_lift_count"], 100)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            result["bounded_r_strict_lift_count"]
            + result["p_minus_one_strict_lift_count"],
            result["h19_residual_count"],
        )


if __name__ == "__main__":
    unittest.main()
