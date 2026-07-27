import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_quadratic_square_only_boundary",
    ROOT / "reproductions" / "type_i_h19_quadratic_square_only_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIH19QuadraticSquareOnlyBoundaryTests(unittest.TestCase):
    def test_all_post_affine_residuals_escape_small_h_quadratics(self):
        result = boundary.run_audit()
        self.assertEqual(
            result["source_state"]["post_affine_residual_branch_count"], 14
        )
        self.assertEqual(
            result["source_state"]["quadratic_pair_count_per_progression"],
            10_619_136,
        )
        self.assertTrue(
            all(
                row["quadratic_square_only_certificate"] is None
                and row["pair_count_exhausted"] == 10_619_136
                for row in result["residual_progressions"]
            )
        )
        self.assertEqual(result["total_eligible_gap_tests"], 9_364_817)

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-i-h19-quadratic-square-only-boundary.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(
            result["source_state"]["quadratic_pair_count_per_progression"],
            10_619_136,
        )
        self.assertEqual(result["total_eligible_gap_tests"], 9_364_817)


if __name__ == "__main__":
    unittest.main()
