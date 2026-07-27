import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_dynamic_scale_polynomial_boundary",
    ROOT / "reproductions" / "h19_k23_pressure_dynamic_scale_polynomial_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23PressureDynamicScalePolynomialBoundaryTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_ray(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-polynomial-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(boundary.run_audit(bridge), checked)

    def test_natural_growing_scale_has_no_eventual_polynomial_square_tail(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-dynamic-scale-polynomial-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(result["global_factor"], 41400)
        self.assertEqual(result["eventual_polynomial_candidate_count"], 5)
        self.assertEqual(result["polynomial_descent_hits"], [])


if __name__ == "__main__":
    unittest.main()
