import json
import unittest
from pathlib import Path

from reproductions import type_i_fixed_pminusone_ray_pressure_profile_600m as profile


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "reproductions" / "type-i-fixed-pminusone-ray-pressure-profile-600m-results.json"


class TypeIFixedPminusoneRayPressureProfile600MTests(unittest.TestCase):
    def test_fixed_menu_has_the_stated_finite_decomposition(self):
        payload = profile.run_audit()
        self.assertEqual(payload["ordinary_tail_miss_count"], 1964)
        self.assertEqual(payload["universal_E_values"], [4, 8, 12, 16, 24, 36, 48, 72, 144])
        self.assertEqual(payload["universal_R_values"], [3, 7, 11, 15, 23, 35, 47, 71, 143])
        self.assertEqual(payload["p_plus_one_factor_coverage_count"], 760)
        self.assertEqual(payload["fixed_ray_individual_coverage_counts"], {
            "3": 714, "7": 968, "11": 913, "15": 816, "23": 733,
            "35": 402, "47": 638, "71": 478, "143": 302,
        })
        self.assertEqual(payload["p_plus_one_and_R_3_overlap_count"], 283)
        self.assertEqual(payload["branch_counts_in_priority_order"], {
            "p_plus_one_factor": 760,
            "pminusone_R_3": 431,
            "pminusone_R_7": 387,
            "pminusone_R_11": 200,
            "pminusone_R_15": 65,
            "pminusone_R_23": 52,
            "pminusone_R_35": 11,
            "pminusone_R_47": 19,
            "pminusone_R_71": 10,
            "pminusone_R_143": 4,
        })
        self.assertEqual(payload["covered_count"], 1939)
        self.assertEqual(payload["unresolved_count"], 25)
        self.assertEqual(payload["unresolved_primes"], [
            297049, 3942409, 19504489, 36583369, 40944649, 42486889, 53712409,
            57399241, 72148729, 82282489, 119091289, 171292489, 172657489,
            174600409, 176110489, 212973049, 239182969, 259423609, 319207849,
            328186681, 340352329, 401991529, 405660649, 437817769, 459147049,
        ])

    def test_checked_in_artifact_is_reproducible(self):
        self.assertEqual(json.loads(RESULT.read_text(encoding="utf-8")), profile.run_audit())


if __name__ == "__main__":
    unittest.main()
