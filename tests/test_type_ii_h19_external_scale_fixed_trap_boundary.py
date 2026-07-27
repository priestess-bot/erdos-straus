import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_external_scale_fixed_trap_boundary",
    ROOT / "reproductions" / "type_ii_h19_external_scale_fixed_trap_boundary.py",
)
assert SPEC and SPEC.loader
trap_boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = trap_boundary
SPEC.loader.exec_module(trap_boundary)


class TypeIIH19ExternalScaleFixedTrapBoundaryTests(unittest.TestCase):
    def test_all_k23_residual_progressions_have_no_fixed_factor_trap(self):
        result = trap_boundary.run_audit()
        self.assertEqual(result["source_state"]["residual_branch_count"], 18)
        self.assertEqual(result["total_candidate_gap_count"], 10_152)
        rows = result["residual_progressions"]
        self.assertEqual(len(rows), 18)
        self.assertEqual(
            [row["candidate_gap_count"] for row in rows], [564] * 18
        )
        self.assertTrue(all(row["traps"] == [] for row in rows))

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-external-scale-fixed-trap-boundary.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["total_candidate_gap_count"], 10_152)
        self.assertTrue(
            all(
                row["traps"] == []
                for row in result["residual_progressions"]
            )
        )


if __name__ == "__main__":
    unittest.main()
