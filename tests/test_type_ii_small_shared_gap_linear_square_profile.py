import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_small_shared_gap_linear_square_profile",
    ROOT / "reproductions" / "type_ii_small_shared_gap_linear_square_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIISmallSharedGapLinearSquareProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spf = profile.short_certificate.smallest_prime_factors(100_011)

    def test_examples_separate_the_three_lattice_levels(self):
        linear = profile.profile_prime(73, self.spf)
        square_only = profile.profile_prime(193, self.spf)
        no_type_ii = profile.profile_prime(1201, self.spf)
        self.assertEqual((linear.category, linear.gap), ("linear", 7))
        self.assertEqual((square_only.category, square_only.gap), ("square_only", 7))
        self.assertFalse(square_only.x % square_only.divisor == 0)
        self.assertEqual((no_type_ii.category, no_type_ii.gap), ("no_type_ii", None))

    def test_one_million_partition_is_stable(self):
        audit = profile.run_audit(1_000_000)
        self.assertEqual(audit["core_prime_count"], 9_732)
        self.assertEqual(
            audit["categories"],
            {"linear": 9_104, "square_only": 223, "no_type_ii": 405},
        )
        self.assertEqual(
            audit["gap_counts"],
            {
                "linear": {"3": 5_192, "7": 3_252, "11": 660},
                "square_only": {"3": 0, "7": 160, "11": 63},
                "no_type_ii": {"3": 0, "7": 0, "11": 0},
            },
        )


if __name__ == "__main__":
    unittest.main()
