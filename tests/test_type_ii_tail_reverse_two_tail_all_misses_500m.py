import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TypeIITailReverseTwoTailAllMisses500MTests(unittest.TestCase):
    def test_stored_full_tail_miss_closure_has_only_verified_strict_edges(self):
        path = ROOT / "reproductions" / "type-ii-tail-reverse-two-tail-500m-all-misses-results.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["pressure_point_count"], 1_717)
        self.assertEqual(payload["captured_count"], 1_717)
        self.assertEqual(payload["misses"], [])
        self.assertEqual(payload["maximum_selected_gap"], 127)
        self.assertEqual((payload["even_source_count"], payload["odd_source_count"]), (1_423, 294))
        self.assertEqual(payload["minimum_descent_slack"], 1)
        self.assertEqual(len(payload["records"]), 1_717)
        for record in payload["records"]:
            prime = record["prime"]
            lift = record["reverse_two_tail_lift"]
            source = record["source_solution"]
            target = record["target_solution"]
            self.assertEqual(record["replaced_target_position"], 2)
            self.assertEqual(source[0], lift["source_term"])
            self.assertLess(1, lift["source_denominator"])
            self.assertLess(lift["source_denominator"], prime)
            self.assertEqual(Fraction(4, prime), sum((Fraction(1, term) for term in target), Fraction()))
            self.assertEqual(
                Fraction(4, lift["source_denominator"]),
                sum((Fraction(1, term) for term in source), Fraction()),
            )
