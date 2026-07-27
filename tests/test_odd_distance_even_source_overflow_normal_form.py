import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "odd_distance_even_source_overflow_normal_form",
    ROOT / "reproductions" / "odd_distance_even_source_overflow_normal_form.py",
)
assert SPEC and SPEC.loader
normal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = normal
SPEC.loader.exec_module(normal)


class OddDistanceEvenSourceOverflowNormalFormTests(unittest.TestCase):
    def test_artifact_is_a_fresh_round_trip_of_every_pressure_tail(self):
        with (ROOT / "reproductions" / "type-ii-h19-pressure-small-r-1b-results.json").open(encoding="utf-8") as handle:
            profile = json.load(handle)
        with (ROOT / "reproductions" / "odd-distance-even-source-overflow-normal-form-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(normal.run_audit(profile), checked)

    def test_zero_overflow_reconstructs_the_ordinary_divisor_special_case(self):
        m1, factor, r = 922900832, 25312, 103
        a, overflow, g = normal.normalize(m1, r, factor)
        self.assertEqual((a, overflow, g), (36461, 1, 25312))
        self.assertEqual(normal.reconstruct(a, overflow, g, r), (m1, factor))

    def test_pressure_profile_exhausts_its_forty_seven_square_tails(self):
        with (ROOT / "reproductions" / "odd-distance-even-source-overflow-normal-form-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_point_count"], 4)
        self.assertEqual(result["tail_count"], 47)


if __name__ == "__main__":
    unittest.main()
