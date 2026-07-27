import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_automatic_residual_k1_funnel",
    ROOT / "reproductions" / "type_ii_automatic_residual_k1_funnel.py",
)
assert SPEC and SPEC.loader
funnel = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = funnel
SPEC.loader.exec_module(funnel)


class TypeIIAutomaticResidualK1FunnelTests(unittest.TestCase):
    def test_totient_prefix_threshold_constructs_a_unit_divisor(self):
        divisor = funnel.prefix_product_one_divisor([2, 3, 2, 3], 5)
        self.assertEqual(divisor, 6)
        self.assertEqual(divisor % 5, 1)
        self.assertIsNone(funnel.prefix_product_one_divisor([2, 2, 2], 5))

    def test_generated_unit_residue_subgroup(self):
        self.assertEqual(
            funnel.generated_unit_residue_subgroup([2, 3], 5),
            frozenset({1, 2, 3, 4}),
        )
        with self.assertRaises(ValueError):
            funnel.generated_unit_residue_subgroup([3], 6)

    def test_one_million_funnel_is_stable(self):
        audit = funnel.run_audit(1_000_000)
        self.assertEqual(audit["core_prime_count"], 9_732)
        self.assertEqual(
            audit["counts"],
            {
                "four_auto_gap_residual": 150,
                "k1_hit": 135,
                "non_k1": 15,
                "non_k1_shared_hit": 15,
            },
        )
        self.assertEqual(len(audit["non_k1_records"]), 15)
        self.assertTrue(all("gap" in record for record in audit["non_k1_records"]))

    def test_one_million_single_prime_profile_is_empty(self):
        audit = funnel.run_audit(1_000_000, include_single_prime_profile=True)
        profile = audit["single_prime_shared_profile"]
        self.assertEqual(profile["single_prime_shared_count"], 0)
        self.assertEqual(profile["single_prime_shared_hits"], [])
        self.assertEqual(profile["single_prime_shared_misses"], [
            67_369,
            85_369,
            163_249,
            214_729,
            225_289,
            297_049,
            372_409,
            454_969,
            521_929,
            532_249,
            629_689,
            784_249,
            852_889,
            878_089,
            967_129,
        ])

    def test_one_million_prime_power_profile_has_only_five_cubed(self):
        audit = funnel.run_audit(1_000_000, include_prime_power_profile=True)
        profile = audit["prime_power_shared_profile"]
        self.assertEqual(profile["prime_power_shared_count"], 1)
        self.assertEqual(profile["proper_prime_power_shared_count"], 1)
        self.assertEqual(
            profile["proper_prime_power_rescues_after_single_prime_miss"],
            [
                {
                    "prime": 454_969,
                    "gap": 31,
                    "shared_prime_power": 125,
                    "base_prime": 5,
                    "exponent": 3,
                    "first_scale": 4,
                }
            ],
        )
        self.assertEqual(len(profile["prime_power_shared_misses"]), 14)

    def test_one_million_support_profile_reaches_four_primes(self):
        audit = funnel.run_audit(1_000_000, include_support_profile=True)
        profile = audit["multi_prime_support_profile"]
        self.assertEqual(
            profile["minimum_distinct_prime_support_histogram"],
            {1: 1, 2: 8, 3: 5, 4: 1},
        )
        self.assertEqual(profile["minimum_distinct_prime_support_misses"], [])
        self.assertIn(
            {
                "prime": 967_129,
                "minimum_distinct_prime_support": 4,
                "gap": 47,
                "shared_divisor": 16_968,
                "first_scale": 361,
            },
            profile["minimum_distinct_prime_support_witnesses"],
        )

    def test_one_million_totient_threshold_profile_is_empty(self):
        audit = funnel.run_audit(
            1_000_000, include_totient_threshold_profile=True
        )
        profile = audit["totient_threshold_shared_profile"]
        self.assertEqual(profile["totient_threshold_shared_count"], 0)
        self.assertEqual(profile["totient_threshold_shared_witnesses"], [])
        self.assertEqual(len(profile["totient_threshold_shared_misses"]), 15)

    def test_one_million_subgroup_threshold_profile_is_empty(self):
        audit = funnel.run_audit(
            1_000_000, include_subgroup_threshold_profile=True
        )
        profile = audit["subgroup_threshold_shared_profile"]
        self.assertEqual(profile["subgroup_threshold_shared_count"], 0)
        self.assertEqual(profile["subgroup_threshold_shared_witnesses"], [])
        self.assertEqual(len(profile["subgroup_threshold_shared_misses"]), 15)

    def test_one_million_factor_length_profile_reaches_six(self):
        audit = funnel.run_audit(1_000_000, include_factor_length_profile=True)
        profile = audit["minimum_factor_length_profile"]
        self.assertEqual(
            profile["minimum_factor_multiplicity_histogram"],
            {2: 3, 3: 7, 4: 2, 5: 2, 6: 1},
        )
        self.assertEqual(profile["minimum_factor_multiplicity_misses"], [])
        self.assertIn(
            {
                "prime": 967_129,
                "minimum_factor_multiplicity": 6,
                "gap": 47,
                "shared_divisor": 16_968,
                "first_scale": 361,
            },
            profile["minimum_factor_multiplicity_witnesses"],
        )

    def test_checked_ten_million_single_prime_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-single-prime-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["single_prime_shared_profile"]
        self.assertEqual(audit["counts"]["non_k1"], 84)
        self.assertEqual(profile["single_prime_shared_count"], 9)
        self.assertEqual(
            profile["single_prime_shared_by_least_gap"],
            {"15": 1, "31": 2, "39": 5, "95": 1},
        )
        self.assertEqual(len(profile["single_prime_shared_misses"]), 75)
        self.assertIn(878_089, profile["single_prime_shared_misses"])

    def test_checked_ten_million_prime_power_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-prime-power-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["prime_power_shared_profile"]
        self.assertEqual(audit["counts"]["non_k1"], 84)
        self.assertEqual(profile["prime_power_shared_count"], 10)
        self.assertEqual(
            profile["prime_power_shared_by_least_gap"],
            {"15": 1, "31": 3, "39": 5, "95": 1},
        )
        self.assertEqual(profile["proper_prime_power_shared_count"], 1)
        self.assertEqual(
            profile["proper_prime_power_rescues_after_single_prime_miss"],
            [
                {
                    "prime": 454_969,
                    "gap": 31,
                    "shared_prime_power": 125,
                    "base_prime": 5,
                    "exponent": 3,
                    "first_scale": 4,
                }
            ],
        )
        self.assertEqual(len(profile["prime_power_shared_misses"]), 74)
        self.assertIn(878_089, profile["prime_power_shared_misses"])

    def test_checked_ten_million_support_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-multi-prime-support-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["multi_prime_support_profile"]
        self.assertEqual(
            profile["minimum_distinct_prime_support_histogram"],
            {"1": 10, "2": 54, "3": 18, "4": 2},
        )
        self.assertEqual(profile["minimum_distinct_prime_support_misses"], [])
        self.assertIn(
            {
                "prime": 5_596_369,
                "minimum_distinct_prime_support": 4,
                "gap": 31,
                "shared_divisor": 5_596_400,
                "first_scale": 180_529,
            },
            profile["minimum_distinct_prime_support_witnesses"],
        )

    def test_checked_ten_million_totient_threshold_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-totient-threshold-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["totient_threshold_shared_profile"]
        self.assertEqual(profile["totient_threshold_shared_count"], 0)
        self.assertEqual(profile["totient_threshold_shared_witnesses"], [])
        self.assertEqual(len(profile["totient_threshold_shared_misses"]), 84)

    def test_checked_ten_million_subgroup_threshold_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-subgroup-threshold-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["subgroup_threshold_shared_profile"]
        self.assertEqual(profile["subgroup_threshold_shared_count"], 0)
        self.assertEqual(profile["subgroup_threshold_shared_witnesses"], [])
        self.assertEqual(len(profile["subgroup_threshold_shared_misses"]), 84)

    def test_checked_ten_million_factor_length_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-minimum-factor-length-profile-10m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["minimum_factor_length_profile"]
        self.assertEqual(
            profile["minimum_factor_multiplicity_histogram"],
            {"1": 9, "2": 32, "3": 28, "4": 7, "5": 5, "6": 3},
        )
        self.assertEqual(profile["minimum_factor_multiplicity_misses"], [])

    def test_checked_twenty_million_factor_length_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-minimum-factor-length-profile-20m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["minimum_factor_length_profile"]
        self.assertEqual(audit["counts"]["non_k1"], 146)
        self.assertEqual(
            profile["minimum_factor_multiplicity_histogram"],
            {"1": 16, "2": 58, "3": 51, "4": 12, "5": 6, "6": 3},
        )
        self.assertEqual(profile["minimum_factor_multiplicity_misses"], [])
        self.assertEqual(
            [
                {
                    "prime": witness["prime"],
                    "gap": witness["gap"],
                    "shared_divisor": witness["shared_divisor"],
                }
                for witness in profile["minimum_factor_multiplicity_witnesses"]
                if witness["minimum_factor_multiplicity"] == 6
            ],
            [
                {"prime": 967_129, "gap": 47, "shared_divisor": 16_968},
                {"prime": 5_596_369, "gap": 71, "shared_divisor": 37_560},
                {"prime": 6_569_161, "gap": 55, "shared_divisor": 410_576},
            ],
        )

    def test_checked_hundred_million_factor_length_profile_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-automatic-residual-minimum-factor-length-profile-100m-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        profile = audit["minimum_factor_length_profile"]
        self.assertEqual(audit["counts"]["non_k1"], 500)
        self.assertEqual(
            profile["minimum_factor_multiplicity_histogram"],
            {
                "1": 60,
                "2": 236,
                "3": 148,
                "4": 41,
                "5": 9,
                "6": 4,
                "7": 1,
            },
        )
        self.assertEqual(
            profile["minimum_factor_multiplicity_misses"], [33_011_449]
        )
        self.assertIn(
            {
                "prime": 95_741_809,
                "minimum_factor_multiplicity": 7,
                "gap": 71,
                "shared_divisor": 7_364_760,
                "first_scale": 103_729,
            },
            profile["minimum_factor_multiplicity_witnesses"],
        )


if __name__ == "__main__":
    unittest.main()
