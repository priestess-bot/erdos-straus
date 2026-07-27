import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_tail_fixed_base_boundary",
    ROOT / "reproductions" / "h19_k23_global_tail_fixed_base_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23GlobalTailFixedBaseBoundaryTests(unittest.TestCase):
    def test_all_global_tail_denominators_are_checked(self):
        result = boundary.run_audit()
        self.assertEqual(result["global_p_minus_one_factor"], 165_600)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["fixed_base_full_cover_count"], 0)
        by_gap = {row["tail_gap"]: row for row in result["global_tail_rows"]}
        self.assertEqual(by_gap[31]["first_uncovered_state"]["target_residue"], 11)
        self.assertEqual(by_gap[39]["first_uncovered_state"]["target_residue"], 38)
        self.assertEqual(by_gap[95]["first_uncovered_state"]["target_residue"], 41)

    def test_checked_artifact_matches_symbolic_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-fixed-base-boundary.json"
        ).open(encoding="utf-8") as handle:
            artifact = json.load(handle)
        self.assertEqual(artifact, boundary.run_audit())


if __name__ == "__main__":
    unittest.main()
