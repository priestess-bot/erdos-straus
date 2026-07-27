import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_offset_profile_100m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIITailShiftedQuadraticOffsetProfile100MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-100m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-100m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(profile.run_audit(self.input_payload()), checked)

    def test_two_point_offset_boundary_is_exact_in_the_audited_family(self):
        payload = self.input_payload()
        small = profile.run_audit(payload, 241)
        self.assertEqual(small["offset_descent_count"], 39)
        self.assertEqual(small["offset_missing_primes"], [878_089, 5_478_169])
        first_boundary = profile.run_audit(payload, 3_705)
        self.assertEqual(first_boundary["offset_missing_primes"], [5_478_169])
        full = profile.run_audit(payload, 7_161)
        self.assertEqual(full["core_prime_count"], 719_781)
        self.assertEqual(full["two_tail_descent_count"], 719_281)
        self.assertEqual(full["zero_offset_quadratic_descent_count_on_tail_misses"], 459)
        self.assertEqual(full["offset_descent_count"], 41)
        self.assertEqual(full["offset_missing_primes"], [])
        records = {record["prime"]: record["offset_descent"] for record in full["records"]}
        self.assertEqual(
            (records[878_089]["shift"], records[878_089]["k"], records[878_089]["source_distance"]),
            (3_705, 54_649, 4),
        )
        self.assertEqual(
            (records[5_478_169]["shift"], records[5_478_169]["k"], records[5_478_169]["source_distance"]),
            (7_161, 341_938, 4),
        )


if __name__ == "__main__":
    unittest.main()
