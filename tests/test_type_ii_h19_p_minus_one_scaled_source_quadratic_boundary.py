import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_p_minus_one_scaled_source_quadratic_boundary",
    ROOT / "reproductions" / "type_ii_h19_p_minus_one_scaled_source_quadratic_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19PMinusOneScaledSourceQuadraticBoundaryTests(unittest.TestCase):
    def test_checked_one_billion_quadratic_miss_boundary(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-p-minus-one-scaled-source-quadratic-boundary-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["quadratic_descent_miss_count"], 4)
        self.assertEqual(result["unique_scaled_source_candidate_count"], 118)
        self.assertEqual(result["hit_candidate_count"], 0)
        self.assertEqual(result["covered_prime_count"], 0)
        self.assertEqual(
            result["uncovered_primes"],
            [35_840_809, 132_285_169, 141_326_089, 640_775_689],
        )


if __name__ == "__main__":
    unittest.main()
