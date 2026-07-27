import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_even_source_distance_boundary",
    ROOT / "reproductions" / "type_ii_h19_even_source_distance_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19EvenSourceDistanceBoundaryTests(unittest.TestCase):
    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-h19-even-source-distance-boundary-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["quadratic_descent_miss_count"], 3)
        self.assertEqual(result["distances"], [1, 3, 5, 7])
        self.assertEqual(result["distance_hit_counts"], {"1": 0, "3": 2, "5": 0, "7": 1})
        self.assertEqual(
            [(row["prime"], [hit["distance"] for hit in row["hits"]]) for row in result["records"]],
            [(35_840_809, [7]), (132_285_169, [3]), (141_326_089, [3])],
        )


if __name__ == "__main__":
    unittest.main()
