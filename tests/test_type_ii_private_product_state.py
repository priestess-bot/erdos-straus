import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_private_product_state",
    ROOT / "reproductions" / "type_ii_private_product_state.py",
)
assert SPEC and SPEC.loader
state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = state
SPEC.loader.exec_module(state)


class TypeIIPrivateProductStateTests(unittest.TestCase):
    def test_private_one_hole_trap_has_expected_congruence(self):
        smallest_factors = state.canonical.ray.short_certificate.smallest_prime_factors(
            3_169_681 + 4 * 14
        )
        row = state.private_state(
            3_169_681,
            (1, 5),
            smallest_factors,
            set(state.collision.collision_primes(tuple(range(1, 15)))),
        )
        self.assertEqual(row["mode"], "mixed")
        self.assertEqual(row["private_defect_size"], 1)
        self.assertEqual(row["private_support_index"], 2)
        self.assertFalse(row["private_support_saturated"])
        self.assertEqual(row["private_one_hole_target"], 13)
        self.assertEqual(row["private_one_hole_congruence"], 1)
        self.assertEqual(3_169_681 % row["modulus"], 1)

    def test_small_fan_private_state_profile(self):
        result = state.run_profile(1_000_000, 14)
        self.assertEqual(result["common_failure_count"], 24)
        self.assertEqual(result["state_count"], 336)
        self.assertEqual(
            result["mode_histogram"],
            {"all_inside": 22, "all_outside": 305, "mixed": 9},
        )
        self.assertEqual(result["all_outside_support_saturated_count"], 216)
        self.assertEqual(
            result["all_outside_support_index_histogram"],
            {2: 145, 4: 117, 6: 3, 8: 29, 10: 2, 12: 7, 16: 1, 20: 1},
        )
        self.assertEqual(result["private_one_hole_count"], 0)

    def test_nineteen_shift_profile_keeps_the_support_outside_main_type(self):
        result = state.run_profile(1_000_000, 19)
        self.assertEqual(result["common_failure_count"], 13)
        self.assertEqual(result["state_count"], 247)
        self.assertEqual(
            result["mode_histogram"],
            {"all_inside": 19, "all_outside": 214, "mixed": 14},
        )
        self.assertEqual(result["all_outside_support_saturated_count"], 151)
        self.assertEqual(result["private_one_hole_count"], 0)


if __name__ == "__main__":
    unittest.main()
