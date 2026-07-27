import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_escape_affine_boundary",
    ROOT / "reproductions" / "type_i_escape_affine_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIEscapeAffineBoundaryTests(unittest.TestCase):
    def test_depth_four_escape_has_no_uniform_type_i_hits(self):
        result = boundary.run_affine_boundary_audit()
        self.assertEqual(result["coefficient"], 245_044_800)
        self.assertEqual(result["scale_divisor_count"], 720)
        self.assertEqual(result["fixed_gap_state_count"], 72)
        self.assertEqual(result["affine_candidate_count"], 434)
        self.assertEqual(result["constant_candidate_count"], 434)
        self.assertEqual(result["affine_hits"], [])
        self.assertEqual(result["constant_hits"], [])

    def test_fixed_gap_state_is_primitive_and_candidate_checks_are_consistent(self):
        state = boundary.fixed_gap_state(24, 3)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(
            state,
            {
                "gap": 3,
                "scale": 6,
                "offset": 1,
                "content": 1,
                "primitive_scale": 6,
                "primitive_offset": 1,
            },
        )
        self.assertFalse(boundary.affine_candidate_holds(24, state, 1))
        self.assertFalse(boundary.constant_candidate_holds(state, 1))


if __name__ == "__main__":
    unittest.main()
