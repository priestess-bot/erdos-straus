import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_shifted_quadratic_opposite_pair_profile_200m",
    ROOT / "reproductions" / "type_ii_tail_shifted_quadratic_opposite_pair_profile.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailShiftedQuadraticOppositePairProfile200MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-square-necessity-200m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_artifact_rebuilds(self):
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-200m-results.json"
        checked = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(audit.run_audit(self.input_payload()), checked)

    def test_low_support_opposite_pairs_do_not_cover_the_minimal_offset_pressure_set(self):
        result = audit.run_audit(self.input_payload())
        self.assertEqual(result["minimal_offset_ray_count"], 65)
        self.assertEqual(
            result["minimum_signed_support_histogram"],
            {"1": 7, "2": 24, "3": 26, "4": 4, "5": 3, "6": 1},
        )
        self.assertEqual(
            result["square_essential_minimum_signed_support_histogram"],
            {"2": 2, "3": 15, "4": 4, "5": 3, "6": 1},
        )
        self.assertEqual(result["one_prime_opposite_pair_hit_count"], 7)
        self.assertEqual(result["two_prime_opposite_pair_hit_count"], 31)
        self.assertEqual(result["more_than_half_density_hit_count"], 42)
        self.assertEqual(result["square_essential_more_than_half_density_hit_count"], 7)
        self.assertEqual(len(result["more_than_half_density_miss_primes"]), 23)
        self.assertEqual(result["more_than_half_generated_subgroup_density_hit_count"], 42)
        self.assertEqual(result["square_essential_more_than_half_generated_subgroup_density_hit_count"], 7)
        self.assertEqual(
            result["more_than_half_generated_subgroup_density_miss_primes"],
            result["more_than_half_density_miss_primes"],
        )
        self.assertEqual(result["symmetric_box_subgroup_saturation_hit_count"], 48)
        self.assertEqual(result["square_essential_symmetric_box_subgroup_saturation_hit_count"], 11)
        self.assertEqual(len(result["symmetric_box_subgroup_saturation_miss_primes"]), 17)
        self.assertEqual(result["inverse_pairing_parity_hit_count"], 57)
        self.assertEqual(
            result["inverse_pairing_parity_beyond_saturation_primes"],
            [
                56_040_889,
                68_822_329,
                76_244_809,
                122_014_489,
                137_431_849,
                139_365_769,
                168_434_809,
                171_292_489,
                185_772_409,
            ],
        )
        self.assertIn(6_294_649, result["two_prime_opposite_pair_miss_primes"])
        records = {record["prime"]: record for record in result["records"]}
        hard = records[6_294_649]
        self.assertEqual(hard["more_than_half_density_witness_count"], 0)
        self.assertEqual(hard["minimum_signed_prime_support_count"], 6)
        self.assertEqual(hard["minimum_signed_l1_displacement"], 6)
        self.assertEqual(
            hard["minimum_support_witness"]["coordinates"],
            [
                {"prime": 5, "displacement": 1},
                {"prime": 7, "displacement": 1},
                {"prime": 17, "displacement": 1},
                {"prime": 19, "displacement": -1},
                {"prime": 29, "displacement": -1},
                {"prime": 37, "displacement": -1},
            ],
        )


if __name__ == "__main__":
    unittest.main()
