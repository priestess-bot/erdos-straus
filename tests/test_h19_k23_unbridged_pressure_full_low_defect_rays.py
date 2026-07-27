from fractions import Fraction
import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_unbridged_pressure_full_low_defect_rays",
    ROOT
    / "reproductions"
    / "h19_k23_unbridged_pressure_full_low_defect_rays.py",
)
assert SPEC and SPEC.loader
full_rays = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = full_rays
SPEC.loader.exec_module(full_rays)


class H19K23UnbridgedPressureFullLowDefectRaysTests(unittest.TestCase):
    def test_checked_artifact_is_a_fresh_exact_rerun(self):
        with full_rays.DEFAULT_INPUT.open(encoding="utf-8") as handle:
            source = json.load(handle)
        with full_rays.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(full_rays.run_audit(source), checked)

    def test_both_full_original_rays_have_defect_upper_bound_one(self):
        with full_rays.DEFAULT_INPUT.open(encoding="utf-8") as handle:
            source = json.load(handle)
        with full_rays.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            result = json.load(handle)
        source_steps = {
            int(row["prime_seed"]): int(row["pressure_prime_coefficient"])
            for row in source["rows"]
        }
        self.assertEqual(result["full_original_ray_count"], 2)
        self.assertTrue(result["all_rays_use_original_pressure_step"])
        self.assertTrue(result["all_rays_primitive"])
        self.assertTrue(result["all_selector_defect_upper_bounds_at_most_two"])
        self.assertEqual(result["witness_new_support_size_histogram"], {"1": 2})
        by_seed = {row["prime_seed"]: row for row in result["rays"]}
        first = by_seed[2_220_549_727_681_245_601]
        second = by_seed[748_375_048_866_405_601]
        self.assertEqual((first["q"], first["gap"], first["divisor"]), (15, 59, 37_845))
        self.assertEqual((second["q"], second["gap"], second["divisor"]), (90, 359, 121_014))
        self.assertEqual(first["new_support"], [29])
        self.assertEqual(second["new_support"], [83])
        self.assertEqual(first["witness_new_support_size"], 1)
        self.assertEqual(second["witness_new_support_size"], 1)
        self.assertEqual(first["selector_defect_upper_bound"], 1)
        self.assertEqual(second["selector_defect_upper_bound"], 1)
        for seed, row in by_seed.items():
            self.assertEqual(row["progression_scope"], "full_original_pressure_ray")
            self.assertEqual(row["step_refinement_multiplier"], 1)
            self.assertEqual(row["prime_step"], source_steps[seed])
            self.assertEqual(row["prime_seed_mod_24"], 1)
            self.assertEqual(row["prime_step_mod_24"], 0)
            prime_step = row["prime_step"]
            b_seed = (seed - 1) // 4
            b_step = prime_step // 4
            x_seed = b_seed + row["q"]
            self.assertEqual(prime_step % 24, 0)
            self.assertEqual(math.gcd(seed, prime_step), 1)
            self.assertEqual(b_seed % row["q"], 0)
            self.assertEqual(b_step % row["q"], 0)
            self.assertEqual(x_seed * x_seed % row["divisor"], 0)
            self.assertEqual(b_step % row["divisor"], 0)
            self.assertEqual((x_seed + row["divisor"]) % row["gap"], 0)
            self.assertEqual(b_step % row["gap"], 0)
            self.assertLessEqual(row["divisor"], x_seed)
            self.assertTrue(row["q_divides_b_seed_and_step"])
            self.assertTrue(row["divisor_divides_x_seed_squared_and_b_step"])
            self.assertTrue(row["gap_divides_x_seed_plus_divisor_and_b_step"])
            self.assertTrue(row["divisor_at_most_x_seed"])

    def test_n_zero_and_one_target_and_source_identities_replay(self):
        with full_rays.DEFAULT_OUTPUT.open(encoding="utf-8") as handle:
            result = json.load(handle)
        for row in result["rays"]:
            for key in ("seed_witness", "next_parameter_witness"):
                witness = row[key]
                target = sum(
                    (Fraction(1, value) for value in witness["target_denominators"]),
                    Fraction(),
                )
                source = sum(
                    (Fraction(1, value) for value in witness["source_denominators"]),
                    Fraction(),
                )
                self.assertEqual(target, Fraction(4, witness["prime"]))
                self.assertEqual(source, Fraction(4, witness["source_denominator"]))
                self.assertLess(witness["source_denominator"], witness["prime"])
                self.assertTrue(witness["target_identity_verified"])
                self.assertTrue(witness["source_identity_verified"])
                self.assertTrue(witness["strict_source_descent"])


if __name__ == "__main__":
    unittest.main()
