import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_square_necessity_200m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_square_necessity.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailShiftedQuadraticSquareNecessity200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-200m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit.run_audit(self.input_payload()), checked)

    def test_twenty_five_minimal_offset_rays_need_a_proper_square_factor(self):
        result = audit.run_audit(self.input_payload())
        self.assertEqual(result["pressure_point_count"], 65)
        self.assertEqual(result["minimal_offset_rays_with_ordinary_tail_count"], 40)
        self.assertEqual(result["square_tail_essential_at_minimal_offset_count"], 25)
        self.assertEqual(
            result["square_essential_minimum_exponent_excess_histogram"],
            {"1": 17, "2": 3, "3": 4, "5": 1},
        )
        self.assertEqual(len(result["square_essential_multi_upgrade_primes"]), 8)
        self.assertIn(68_822_329, result["square_essential_multi_upgrade_primes"])
        self.assertEqual(
            result["square_essential_minimum_prime_support_histogram"],
            {"2": 5, "3": 13, "4": 7},
        )
        self.assertEqual(len(result["square_essential_four_support_primes"]), 7)
        self.assertIn(68_822_329, result["square_essential_four_support_primes"])
        self.assertIn(878_089, result["square_tail_essential_at_minimal_offset_primes"])
        self.assertIn(171_292_489, result["square_tail_essential_at_minimal_offset_primes"])
        records = {record["prime"]: record for record in result["records"]}
        self.assertEqual(records[171_292_489]["ordinary_tail_witness_count"], 0)
        self.assertEqual(records[171_292_489]["complete_square_tail_witness_count"], 3)
        self.assertEqual(records[171_292_489]["minimum_exponent_excess_over_L"], 1)
        self.assertEqual(records[171_292_489]["minimum_prime_support_count"], 4)


if __name__ == "__main__":
    unittest.main()
