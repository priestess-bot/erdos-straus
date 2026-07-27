import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_collision_alternative_tail_descent",
    ROOT / "reproductions" / "type_ii_collision_alternative_tail_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIICollisionAlternativeTailDescentTests(unittest.TestCase):
    def test_all_fixed_certificate_misses_have_alternative_tail_descents(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-collision-alternative-tail-descent-h19-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["fixed_certificate_miss_count"], 9)
        self.assertEqual(result["alternative_tail_descent_count"], 9)
        self.assertEqual(result["alternative_tail_descent_misses"], [])
        records = {record["prime"]: record for record in result["records"]}
        self.assertEqual(records[372_271_201]["alternative_tail_witness"]["gap"], 7)
        self.assertEqual(
            records[372_271_201]["alternative_tail_witness"]["source_denominator"],
            46_533_901,
        )
        self.assertEqual(records[9_744_001]["alternative_tail_witness"]["gap"], 3)
        self.assertTrue(
            all(record["alternative_tail_witness"]["gap_plus_one"] % 4 == 0 for record in records.values())
        )


if __name__ == "__main__":
    unittest.main()
