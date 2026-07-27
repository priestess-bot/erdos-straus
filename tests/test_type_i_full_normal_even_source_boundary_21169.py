import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_full_normal_even_source_boundary_21169",
    ROOT / "reproductions" / "type_i_full_normal_even_source_boundary_21169.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIFullNormalEvenSourceBoundary21169Tests(unittest.TestCase):
    def test_complete_boundary_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-full-normal-even-source-boundary-21169-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = boundary.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["normal_form_count"], actual["strict_reverse_lift_count"]), (19, 20))
        self.assertEqual(actual["strict_even_lift_count"], 19)
        self.assertEqual(actual["minimum_even_lift_b"], 5)
        self.assertNotIn("1", actual["strict_even_lift_b_histogram"])
        self.assertEqual(
            actual["minimum_even_b_lifts"],
            [
                {
                    "gap": 4071,
                    "normal_form": [1, 5, 1262],
                    "lift": {
                        "source_denominator": 21060,
                        "source_term": 1022220,
                        "bridge_divisor": 1514667776180,
                    },
                },
                {
                    "gap": 4071,
                    "normal_form": [1, 5, 1262],
                    "lift": {
                        "source_denominator": 21168,
                        "source_term": 108525690,
                        "bridge_divisor": 14340049952,
                    },
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
