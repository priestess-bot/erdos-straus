import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_affine_square_uniform_audit",
    ROOT / "reproductions" / "type_ii_h19_affine_square_uniform_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19AffineSquareUniformAuditTests(unittest.TestCase):
    def test_all_k23_residual_progressions_are_decided(self):
        result = audit.run_audit()
        self.assertEqual(result["source_state"]["residual_branch_count"], 18)
        self.assertEqual(len(result["residual_progressions"]), 18)
        self.assertEqual(
            result["certificate_progression_count"],
            sum(
                row["uniform_square_affine_certificate"] is not None
                for row in result["residual_progressions"]
            ),
        )
        self.assertEqual(result["certificate_progression_count"], 1)
        self.assertEqual(result["square_only_certificate_count"], 1)
        hit_rows = [
            row
            for row in result["residual_progressions"]
            if row["uniform_square_affine_certificate"] is not None
        ]
        self.assertEqual(len(hit_rows), 1)
        self.assertEqual(hit_rows[0]["v_mod_29"], 12)
        self.assertEqual(
            hit_rows[0]["uniform_square_affine_certificate"],
            {
                "gap": 191,
                "future_shift": 48,
                "fixed_factor": 9048,
                "scale_a": 7569,
                "square_only": True,
            },
        )
        for row in result["residual_progressions"]:
            self.assertGreater(
                row.get(
                    "candidate_fixed_factor_count_before_hit",
                    row.get("candidate_fixed_factor_count_exhausted", 0),
                ),
                0,
            )

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-affine-square-uniform-audit.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["source_state"]["residual_branch_count"], 18)
        self.assertEqual(result["certificate_progression_count"], 1)
        self.assertEqual(result["square_only_certificate_count"], 1)


if __name__ == "__main__":
    unittest.main()
