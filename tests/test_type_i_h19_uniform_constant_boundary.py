import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_uniform_constant_boundary",
    ROOT / "reproductions" / "type_i_h19_uniform_constant_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIH19UniformConstantBoundaryTests(unittest.TestCase):
    def test_all_post_affine_residuals_escape_uniform_constant_type_i(self):
        result = boundary.run_audit()
        self.assertEqual(
            result["source_state"]["post_affine_residual_branch_count"], 14
        )
        self.assertTrue(
            all(
                row["candidate_gap_count_exhausted"] == 564
                and row["uniform_constant_type_i_certificate"] is None
                for row in result["residual_progressions"]
            )
        )
        self.assertEqual(result["total_divisor_residue_checks"], 19_366)

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-i-h19-uniform-constant-boundary.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["source_state"]["post_affine_residual_branch_count"], 14)
        self.assertEqual(result["total_divisor_residue_checks"], 19_366)


if __name__ == "__main__":
    unittest.main()
