import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_shared_small_a_boundary",
    ROOT / "reproductions" / "type_ii_shared_small_a_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIISharedSmallABoundaryTests(unittest.TestCase):
    def test_boundary_prime_has_no_shared_selector_normal_form_below_a_69(self):
        profile = boundary.boundary_profile()
        self.assertEqual(profile["prime"], 878_089)
        self.assertEqual(profile["gap_count"], 2)
        self.assertEqual(profile["normal_form_count"], 2)
        self.assertEqual(profile["minimum_a"], 69)
        self.assertEqual(
            profile["direct_a_one_certificate"],
            {
                "gap": 6_703,
                "divisor": 1,
                "a": 1,
                "b": 221_198,
                "c": 1,
                "k": 33,
                "ray_factor": 131,
            },
        )
        self.assertEqual(
            profile["forms"],
            (
                {
                    "gap": 51,
                    "shared_divisor": 460,
                    "certificate_divisor": 34_445,
                    "a": 83,
                    "b": 529,
                    "c": 5,
                    "k": 12,
                },
                {
                    "gap": 143,
                    "shared_divisor": 12_728,
                    "certificate_divisor": 204_723,
                    "a": 69,
                    "b": 74,
                    "c": 43,
                    "k": 1,
                },
            ),
        )


if __name__ == "__main__":
    unittest.main()
