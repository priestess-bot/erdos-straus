import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_even_source_polynomial_boundary",
    ROOT / "reproductions" / "h19_k23_pressure_even_source_polynomial_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23PressureEvenSourcePolynomialBoundaryTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_ray(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-even-source-polynomial-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(boundary.run_audit(bridge), checked)

    def test_complete_distance_one_polynomial_fan_has_no_uniform_tail(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-even-source-polynomial-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(result["p_minus_one_base_factor"], 165600)
        self.assertEqual(result["compatible_polynomial_ray_count"], 18)
        self.assertEqual(result["polynomial_descent_hits"], [])


if __name__ == "__main__":
    unittest.main()
