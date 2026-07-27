import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_minimal_canonical_shift",
    ROOT / "reproductions" / "type_ii_minimal_canonical_shift.py",
)
assert SPEC and SPEC.loader
minimal_shift = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = minimal_shift
SPEC.loader.exec_module(minimal_shift)


class TypeIIMinimalCanonicalShiftTests(unittest.TestCase):
    def test_small_spectrum(self):
        result = minimal_shift.run_experiment(10_000, 50)
        self.assertEqual(result["core_prime_count"], 143)
        self.assertEqual(result["captured_count"], 143)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_first_shift"], 29)

    def test_small_transition_profile(self):
        result = minimal_shift.transition_profile(10_000, 19, 50)
        self.assertEqual(result["joint_base_modulus"], 77_597_520)
        self.assertEqual(result["base_residual_count"], 1)
        self.assertEqual(result["base_residual_primes"], [3_361])
        self.assertEqual(result["later_first_shift_histogram"], {29: 1})
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["zero_unfixed_examples"], [])

    def test_checked_large_spectrum_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-minimal-canonical-shift-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 10_000_000)
        self.assertEqual(result["shift_cap"], 50)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["captured_count"], 82_887)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_first_shift"], 50)
        self.assertEqual(result["record_holders"][-1]["prime"], 66_529)

    def test_checked_hundred_million_spectrum_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-minimal-canonical-shift-100m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000_000)
        self.assertEqual(result["shift_cap"], 100)
        self.assertEqual(result["core_prime_count"], 719_781)
        self.assertEqual(result["captured_count"], 719_781)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_first_shift"], 52)
        self.assertEqual(
            result["record_holders"][-1],
            {
                "prime": 81_846_241,
                "shift": 52,
                "a": 2,
                "c": 13,
                "h": 60_943,
                "k": 586,
                "gap": 1343,
            },
        )

    def test_checked_h19_transition_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-h19-transition-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_shift_bound"], 19)
        self.assertEqual(result["shift_cap"], 50)
        self.assertEqual(result["base_residual_count"], 45)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(
            result["later_first_shift_histogram"],
            {
                "20": 8,
                "21": 2,
                "22": 1,
                "23": 3,
                "24": 6,
                "25": 4,
                "26": 6,
                "27": 3,
                "28": 1,
                "29": 2,
                "31": 1,
                "32": 3,
                "34": 1,
                "36": 3,
                "50": 1,
            },
        )
        self.assertEqual(result["min_unfixed_omega_histogram"], {"0": 1, "1": 44})
        self.assertEqual(result["failure_class_histogram"]["outside:0"], 721)
        self.assertEqual(result["failure_class_histogram"]["outside:1"], 6)
        self.assertEqual(
            sum(result["failure_class_histogram"].values()),
            45 * 19,
        )
        self.assertEqual(
            result["inside_ray_count_histogram"],
            {"1": 7, "2": 13, "3": 10, "4": 12, "5": 2, "7": 1},
        )
        self.assertEqual(
            result["first_support_inside_shift_histogram"],
            {
                "5": 4,
                "7": 7,
                "8": 8,
                "10": 1,
                "11": 10,
                "13": 6,
                "14": 2,
                "16": 1,
                "17": 5,
                "19": 1,
            },
        )
        self.assertEqual(
            result["minimum_support_defect_histogram"],
            {
                "1": 5,
                "2": 12,
                "3": 3,
                "4": 1,
                "5": 3,
                "6": 3,
                "8": 4,
                "9": 1,
                "11": 1,
                "13": 2,
                "16": 2,
                "17": 1,
                "20": 3,
                "22": 1,
                "24": 2,
                "28": 1,
            },
        )
        self.assertIn(
            {"prime": 8_243_041, "defect": 28, "shift": 19},
            result["minimum_support_defect_witnesses"],
        )
        self.assertEqual(
            result["zero_unfixed_examples"],
            [
                {
                    "prime": 1_127_281,
                    "rows": [
                        {
                            "shift": 19,
                            "pair": {"a": 1, "c": 19},
                            "shifted": 1_127_357,
                            "factorization": [
                                {"prime": 7, "exponent": 1},
                                {"prime": 11, "exponent": 5},
                            ],
                        }
                    ],
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
