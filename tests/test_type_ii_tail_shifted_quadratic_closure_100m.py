import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_closure_100m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailShiftedQuadraticClosure100MTests(unittest.TestCase):
    def load_input(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-100m-results.json").open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_hundred_million_artifact_rebuilds(self):
        with (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-closure-100m-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(self.load_input()), checked)

    def test_bounded_shifted_branch_closes_each_zero_shift_miss(self):
        result = closure.run_audit(self.load_input())
        self.assertEqual(result["core_prime_count"], 719_781)
        self.assertEqual(result["two_tail_descent_count"], 719_281)
        self.assertEqual(result["quadratic_factor_descent_count_on_tail_misses"], 459)
        self.assertEqual(result["zero_shift_quadratic_miss_count"], 41)
        self.assertEqual(result["shifted_quadratic_descent_count"], 41)
        self.assertEqual(result["shifted_quadratic_missing_primes"], [])
        self.assertEqual(result["shifted_quadratic_k_bound"], 340_574)
        records = {record["prime"]: record["shifted_quadratic_descent"] for record in result["records"]}
        self.assertEqual(records[878_089]["k"], 54_649)
        self.assertEqual(records[5_478_169]["k"], 340_574)
        self.assertEqual(records[6_294_649]["k"], 65_569)


if __name__ == "__main__":
    unittest.main()
