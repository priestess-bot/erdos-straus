import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_offset_profile_200m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIITailShiftedQuadraticOffsetProfile200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds_at_the_two_hundred_million_boundary(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-200m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(profile.run_audit(self.input_payload(), 202_521), checked)

    def test_new_offset_records_are_exact_in_the_audited_family(self):
        payload = self.input_payload()
        old_box = profile.run_audit(payload, 7_161)
        self.assertEqual(old_box["offset_missing_primes"], [152_498_329, 171_292_489])
        middle_box = profile.run_audit(payload, 48_265)
        self.assertEqual(middle_box["offset_missing_primes"], [152_498_329])
        full = profile.run_audit(payload, 202_521)
        self.assertEqual(full["core_prime_count"], 1_383_890)
        self.assertEqual(full["two_tail_descent_count"], 1_383_059)
        self.assertEqual(full["zero_offset_quadratic_descent_count_on_tail_misses"], 766)
        self.assertEqual(full["zero_offset_quadratic_miss_count"], 65)
        self.assertEqual(full["offset_descent_count"], 65)
        self.assertEqual(full["offset_missing_primes"], [])
        records = {record["prime"]: record["offset_descent"] for record in full["records"]}
        self.assertEqual(
            (records[171_292_489]["shift"], records[171_292_489]["source_distance"]),
            (48_265, 4),
        )
        self.assertEqual(
            (records[152_498_329]["shift"], records[152_498_329]["source_distance"]),
            (202_521, 16),
        )


if __name__ == "__main__":
    unittest.main()
