import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_saturation_profile_200m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_saturation_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIITailShiftedQuadraticSaturationProfile200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-saturation-profile-200m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(profile.run_audit(self.input_payload()), checked)

    def test_saturated_prime_subgroups_cover_only_two_minimal_offset_rays(self):
        result = profile.run_audit(self.input_payload())
        self.assertEqual(result["minimal_offset_ray_count"], 65)
        self.assertEqual(result["saturated_subgroup_hit_count"], 2)
        self.assertEqual(result["saturated_subgroup_hit_primes"], [1_511_449, 168_478_249])
        self.assertEqual(result["square_essential_saturated_subgroup_hit_count"], 0)
        self.assertEqual(len(result["saturated_subgroup_miss_primes"]), 63)


if __name__ == "__main__":
    unittest.main()
