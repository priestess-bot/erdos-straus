import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "dynamic_distance_polynomial_descent_boundary",
    ROOT / "reproductions" / "dynamic_distance_polynomial_descent_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class DynamicDistancePolynomialDescentBoundaryTests(unittest.TestCase):
    def test_explicit_escape_has_no_fixed_shift_polynomial_tail(self):
        result = boundary.run_audit()
        self.assertEqual(
            result["progression"],
            {"coefficient": 245_044_800, "constant": 1},
        )
        self.assertEqual(result["dynamic_distance_state_count"], 215)
        self.assertEqual(result["eventual_square_tail_factor_count"], 7_001_744)
        self.assertEqual(result["polynomial_descent_hits"], [])


if __name__ == "__main__":
    unittest.main()
