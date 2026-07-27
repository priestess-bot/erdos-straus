import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_pressure_reverse_two_tail_closure",
    ROOT / "reproductions" / "type_ii_tail_pressure_reverse_two_tail_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailPressureReverseTwoTailClosureTests(unittest.TestCase):
    def test_all_five_hundred_million_pressure_points_have_short_reverse_edges(self):
        external_path = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-500m-results.json"
        artifact_path = ROOT / "reproductions" / "type-ii-tail-pressure-reverse-two-tail-500m-results.json"
        external = json.loads(external_path.read_text(encoding="utf-8"))
        expected = json.loads(artifact_path.read_text(encoding="utf-8"))
        actual = closure.run_audit(external)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["pressure_point_count"], 124)
        self.assertEqual(actual["captured_count"], 124)
        self.assertEqual(actual["misses"], [])
        self.assertEqual(actual["maximum_selected_gap"], 111)
        self.assertEqual((actual["even_source_count"], actual["odd_source_count"]), (106, 18))
        self.assertEqual(actual["minimum_descent_slack"], 217)
        boundary = next(record for record in actual["records"] if record["prime"] == 477_015_289)
        self.assertEqual(boundary["gap"], 27)
        self.assertEqual(
            boundary["reverse_two_tail_lift"],
            {
                "source_denominator": 32_897_608,
                "source_term": 8_833_617,
                "bridge_divisor": 61_564_910_063_707_146_394_555_256_094_736,
            },
        )


if __name__ == "__main__":
    unittest.main()
