import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_ac_escape_affine_ray_boundary",
    ROOT / "reproductions" / "type_ii_ac_escape_affine_ray_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIIAcEscapeAffineRayBoundaryTests(unittest.TestCase):
    def test_depth_four_escape_has_no_uniform_affine_raw_ac_ray(self):
        result = boundary.run_affine_ray_audit()
        self.assertEqual(result["progression"], {"coefficient": 245_044_800, "constant": 1})
        self.assertEqual(result["coefficient_divisor_count"], 1_008)
        self.assertEqual(result["candidate_ac_pair_count"], 896_000)
        self.assertEqual(result["fixed_divisor_case_count"], 58_230)
        self.assertEqual(result["uniform_affine_raw_ray_hits"], [])


if __name__ == "__main__":
    unittest.main()
