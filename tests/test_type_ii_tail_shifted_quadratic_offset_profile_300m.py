import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_offset_profile_300m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_offset_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIITailShiftedQuadraticOffsetProfile300MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-300m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds_at_three_hundred_million(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-300m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(profile.run_audit(self.input_payload(), 202_521), checked)

    def test_existing_offset_record_closes_three_hundred_million(self):
        result = profile.run_audit(self.input_payload(), 202_521)
        self.assertEqual(result["core_prime_count"], 2_030_611)
        self.assertEqual(result["two_tail_descent_count"], 2_029_455)
        self.assertEqual(result["zero_offset_quadratic_descent_count_on_tail_misses"], 1_067)
        self.assertEqual(result["zero_offset_quadratic_miss_count"], 89)
        self.assertEqual(result["offset_descent_count"], 89)
        self.assertEqual(result["offset_missing_primes"], [])
        max_record = max(
            result["records"], key=lambda record: record["offset_descent"]["shift"]
        )
        self.assertEqual(
            (max_record["prime"], max_record["offset_descent"]["shift"]),
            (152_498_329, 202_521),
        )


if __name__ == "__main__":
    unittest.main()
