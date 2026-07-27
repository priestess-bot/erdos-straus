import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_p_minus_one_scaled_source_descent",
    ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19PMinusOneScaledSourceDescentTests(unittest.TestCase):
    def test_b_two_p_minus_one_lift_is_not_globally_obstructed(self):
        candidate = next(
            candidate
            for candidate in audit.candidates.scaled_candidates(73, 72)
            if candidate["a"] == 35
            and candidate["b"] == 2
            and candidate["shift"] == 3
        )
        witness, _ = audit.descent.scaled_tail_witness(
            73, 72, candidate["a"], candidate["b"], candidate["shift"]
        )
        self.assertIsNotNone(witness)
        self.assertEqual(witness["certificate"]["gap"], 7)
        self.assertEqual(witness["source_solution"], [1_260, 20, 210])
        self.assertEqual(witness["target_solution"], [30_660, 20, 210])

    def test_checked_one_billion_p_minus_one_audit(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-p-minus-one-scaled-source-descent-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["input_r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertEqual(result["unique_scaled_source_candidate_count"], 1_231)
        self.assertEqual(result["hit_candidate_count"], 89)
        self.assertEqual(result["covered_prime_count"], 15)
        self.assertEqual(result["uncovered_primes"], [])
        target = next(record for record in result["records"] if record["prime"] == 99_532_801)
        self.assertIsNotNone(target["first_witness"])
        self.assertEqual(target["hit_candidate_count"], 11)
        witness, _ = audit.descent.scaled_tail_witness(
            99_532_801, 99_532_800, 99_493_921, 4, 38_880
        )
        self.assertIsNotNone(witness)
        self.assertEqual(witness["certificate"]["gap"], 439)


if __name__ == "__main__":
    unittest.main()
