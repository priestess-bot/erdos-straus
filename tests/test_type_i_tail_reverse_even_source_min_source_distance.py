import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_min_source_distance",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_min_source_distance.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeITailReverseEvenSourceMinimumDistanceTests(unittest.TestCase):
    def test_complete_tail_miss_minimum_distance_rebuilds(self):
        tail = json.loads(
            (
                ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-min-source-distance-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit.run_audit(tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["captured_count"],
                len(actual["misses"]),
                actual["short_distance_le_29_count"],
            ),
            (1717, 1717, 0, 1645),
        )
        self.assertEqual(actual["normal_forms_exhaustively_checked"], 78215)
        self.assertEqual(actual["strict_reverse_lifts_exhaustively_checked"], 166089)
        self.assertEqual(actual["maximum_minimum_source_distance"], 48244917)
        self.assertEqual(
            actual["minimum_source_distance_bucket_histogram"],
            {
                "<=29": 1645,
                "<=1000": 45,
                "<=p/1000": 18,
                "<=p/100": 2,
                "<=p/10": 7,
            },
        )


if __name__ == "__main__":
    unittest.main()
