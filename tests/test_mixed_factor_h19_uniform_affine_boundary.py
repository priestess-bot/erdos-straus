import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "mixed_factor_h19_uniform_affine_boundary",
    ROOT / "reproductions" / "mixed_factor_h19_uniform_affine_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class MixedFactorH19UniformAffineBoundaryTests(unittest.TestCase):
    def test_all_post_affine_residuals_escape_every_uniform_mixed_factor(self):
        result = boundary.run_audit()
        self.assertEqual(
            result["source_state"]["post_affine_residual_branch_count"], 14
        )
        self.assertEqual(result["source_state"]["stationary_scale_count"], 37)
        self.assertEqual(len(result["residual_progressions"]), 14)
        self.assertTrue(
            all(
                source["uniform_affine_mixed_factor_hits"] == []
                for row in result["residual_progressions"]
                for source in row["source_audits"]
            )
        )

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "mixed-factor-h19-uniform-affine-boundary.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(
            result["source_state"]["post_affine_residual_branch_count"], 14
        )


if __name__ == "__main__":
    unittest.main()
