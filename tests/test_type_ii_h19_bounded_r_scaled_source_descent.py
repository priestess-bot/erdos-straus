import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_scaled_source_descent",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_scaled_source_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRScaledSourceDescentTests(unittest.TestCase):
    def test_checked_one_billion_scaled_source_audit(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-bounded-r-scaled-source-descent-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertEqual(result["unique_scaled_source_candidate_count"], 1_025)
        self.assertEqual(result["hit_candidate_count"], 82)
        self.assertEqual(result["covered_prime_count"], 14)
        self.assertEqual(result["uncovered_primes"], [99_532_801])
        self.assertIsNotNone(result["records"][0]["first_witness"])
        self.assertIsNone(result["records"][8]["first_witness"])

    def test_tail_rejects_a_nonintegral_first_term(self):
        witness, _ = audit.scaled_tail_witness(73, 60, 1, 2, 1)
        self.assertIsNone(witness)


if __name__ == "__main__":
    unittest.main()
