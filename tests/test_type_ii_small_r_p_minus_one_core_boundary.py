import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_r_p_minus_one_core_boundary",
    ROOT / "reproductions" / "type_ii_small_r_p_minus_one_core_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIISmallRPMinusOneCoreBoundaryTests(unittest.TestCase):
    def test_all_core_primes_through_one_hundred_thousand(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-small-r-p-minus-one-core-boundary-100k-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000)
        self.assertEqual(result["core_prime_count"], 1_181)
        self.assertEqual(result["small_r_strict_lift_count"], 978)
        self.assertEqual(result["small_r_residual_count"], 203)
        self.assertEqual(result["p_minus_one_scaled_source_candidate_count"], 5_077)
        self.assertEqual(result["p_minus_one_tail_divisor_test_count"], 2_766_887)
        self.assertEqual(result["p_minus_one_hit_candidate_count"], 706)
        self.assertEqual(result["joint_strict_lift_count"], 1_174)
        self.assertEqual(
            result["joint_unclosed_primes"],
            [5_209, 12_601, 21_169, 27_481, 48_409, 80_809, 97_561],
        )


if __name__ == "__main__":
    unittest.main()
