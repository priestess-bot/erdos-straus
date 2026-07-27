import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_outer_saturation_profile_200m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_outer_saturation_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailShiftedQuadraticOuterSaturationProfile200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    @classmethod
    def setUpClass(cls):
        cls.payload = cls.input_payload()
        cls.core = audit.run_audit(cls.payload, 202_521)
        cls.extended = audit.run_audit(cls.payload, 1_000_001)

    def test_artifacts_rebuild_at_both_offset_bounds(self):
        cases = [
            (self.core, "type-ii-tail-shifted-quadratic-outer-saturation-profile-200m-results.json"),
            (self.extended, "type-ii-tail-shifted-quadratic-outer-saturation-profile-200m-1m-results.json"),
        ]
        for actual, filename in cases:
            checked = json.loads((ROOT / "reproductions" / filename).read_text(encoding="utf-8"))
            self.assertEqual(actual, checked)

    def test_later_offsets_escape_most_minimal_ray_saturation_misses(self):
        core = self.core
        extended = self.extended
        self.assertEqual(core["input_symmetric_saturation_miss_count"], 17)
        self.assertEqual(core["later_saturation_count"], 11)
        self.assertEqual(len(core["later_saturation_miss_primes"]), 6)
        self.assertEqual(extended["later_saturation_count"], 14)
        self.assertEqual(
            extended["later_saturation_miss_primes"],
            [26_034_649, 168_434_809, 171_292_489],
        )
        records = {record["prime"]: record["later_saturation"] for record in extended["records"]}
        self.assertEqual(
            (records[6_294_649]["shift"], records[6_294_649]["source_distance"]),
            (33_305, 4),
        )
        self.assertEqual(
            (records[185_772_409]["shift"], records[185_772_409]["source_distance"]),
            (651_833, 4),
        )


if __name__ == "__main__":
    unittest.main()
