import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_bounded_r_residual_three_split_boundary",
    ROOT / "reproductions" / "type_ii_h19_bounded_r_residual_three_split_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19BoundedRResidualThreeSplitBoundaryTests(unittest.TestCase):
    def test_checked_one_billion_bounded_r_source_rays(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-bounded-r-residual-three-split-boundary-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["r_cap"], 9_999)
        self.assertEqual(result["residual_prime_count"], 15)
        self.assertEqual(result["source_ray_count"], 245)
        self.assertEqual(result["eligible_residual_three_split_ray_count"], 101)
        self.assertEqual(result["residual_three_split_hit_count"], 0)

    def test_out_of_range_source_is_not_eligible(self):
        self.assertIsNone(audit.residual_three_split_witness(73, 36))


if __name__ == "__main__":
    unittest.main()
