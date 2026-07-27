import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_adaptive_escape_seed_profile",
    ROOT / "reproductions" / "type_i_adaptive_escape_seed_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIAdaptiveEscapeSeedProfileTests(unittest.TestCase):
    def test_small_profile(self):
        result = profile.run_profile(1_000_000, 20, 8)
        self.assertEqual(result["seed_count"], 18)
        self.assertEqual(result["closed_within_target_count"], 9)
        self.assertEqual(
            result["surviving_seed_primes"],
            [
                246_241,
                397_489,
                496_609,
                534_601,
                709_921,
                776_521,
                806_521,
                878_641,
                979_969,
            ],
        )
        self.assertEqual(result["maximum_completed_window"], 20)

    def test_checked_ten_million_summary(self):
        with (
            ROOT
            / "reproductions"
            / "type-i-adaptive-escape-seed-profile-10m-j100-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_count"], 84)
        self.assertEqual(result["closed_within_target_count"], 84)
        self.assertEqual(result["surviving_seed_primes"], [])
        self.assertEqual(result["maximum_completed_window"], 97)
        self.assertEqual(
            result["long_chain_complexity_minima"],
            {
                "window_threshold": 50,
                "seed_count": 8,
                "minimum_maximum_fixed_factor_distinct_prime_count": 4,
                "minimum_additional_local_split_count": 2,
            },
        )
        self.assertEqual(
            result["failure_mechanism_counts"],
            {
                "subgroup_obstructed_positions": 1_752,
                "bounded_product_positions": 403,
            },
        )
        self.assertEqual(
            result["bounded_product_breakdown"],
            {
                "unsaturated_quotient_order_at_most_three": 350,
                "unsaturated_quotient_order_at_least_four": 14,
                "saturated_quotient_order_at_least_four": 39,
            },
        )
        self.assertEqual(
            result["bounded_product_translate_index_breakdown"],
            {
                "index_three": 121,
                "index_at_least_four": 235,
                "no_private_translate": 47,
            },
        )
        record = next(
            record for record in result["records"] if record["seed_prime"] == 776_521
        )
        self.assertEqual(record["completed_window"], 97)
        self.assertEqual(record["terminal_gap"], 391)
        self.assertEqual(record["maximum_fixed_factor_distinct_prime_count"], 5)
        self.assertEqual(record["additional_local_split_count"], 4)
        self.assertEqual(record["subgroup_obstructed_position_count"], 67)
        self.assertEqual(record["bounded_product_position_count"], 30)
        pure_character_record = next(
            record for record in result["records"] if record["seed_prime"] == 806_521
        )
        self.assertEqual(pure_character_record["completed_window"], 23)
        self.assertEqual(pure_character_record["terminal_gap"], 95)
        self.assertEqual(
            pure_character_record["subgroup_obstructed_position_count"], 23
        )
        self.assertEqual(pure_character_record["bounded_product_position_count"], 0)


if __name__ == "__main__":
    unittest.main()
