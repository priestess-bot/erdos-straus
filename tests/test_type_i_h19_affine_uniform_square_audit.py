import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_affine_uniform_square_audit",
    ROOT / "reproductions" / "type_i_h19_affine_uniform_square_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19AffineUniformSquareAuditTests(unittest.TestCase):
    def test_all_k23_residual_progressions_are_decided(self):
        result = audit.run_audit()
        self.assertEqual(result["source_state"]["residual_branch_count"], 18)
        self.assertEqual(len(result["residual_progressions"]), 18)
        self.assertEqual(result["certificate_progression_count"], 4)
        self.assertEqual(result["strictly_type_i_sized_certificate_count"], 1)
        hit_rows = [
            row
            for row in result["residual_progressions"]
            if row["uniform_affine_type_i_certificate"] is not None
        ]
        self.assertEqual([row["v_mod_29"] for row in hit_rows], [2, 9, 12, 25])
        self.assertEqual(
            [row["uniform_affine_type_i_certificate"]["scale_a"] for row in hit_rows],
            [338, 119, 833, 10_829],
        )
        self.assertTrue(
            hit_rows[-1]["uniform_affine_type_i_certificate"]["type_ii_sized"]
            is False
        )
        for row in result["residual_progressions"]:
            if row["uniform_affine_type_i_certificate"] is None:
                self.assertEqual(row["candidate_gap_count_exhausted"], 564)

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-i-h19-affine-uniform-square-audit.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["source_state"]["residual_branch_count"], 18)
        self.assertEqual(result["certificate_progression_count"], 4)
        self.assertEqual(result["strictly_type_i_sized_certificate_count"], 1)


if __name__ == "__main__":
    unittest.main()
