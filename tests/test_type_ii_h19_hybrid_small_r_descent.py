import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_hybrid_small_r_descent",
    ROOT / "reproductions" / "type_ii_h19_hybrid_small_r_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19HybridSmallRDescentTests(unittest.TestCase):
    def test_checked_one_billion_hybrid_closure(self):
        path = ROOT / "reproductions" / "type-ii-h19-hybrid-small-r-descent-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 103)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["quadratic_descent_count"], 660)
        self.assertEqual(result["bounded_r_even_source_count"], 4)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            [
                (row["prime"], row["r"], row["distance"], row["d"])
                for row in result["bounded_r_records"]
            ],
            [
                (35_840_809, 103, 7, 49_641),
                (132_285_169, 31, 3, 1_407_289),
                (141_326_089, 31, 3, 1_503_469),
                (640_775_689, 15, 34_091, 1253),
            ],
        )


if __name__ == "__main__":
    unittest.main()
