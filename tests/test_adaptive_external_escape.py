import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "adaptive_external_escape",
    ROOT / "reproductions" / "adaptive_external_escape.py",
)
assert SPEC and SPEC.loader
adaptive_escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adaptive_escape
SPEC.loader.exec_module(adaptive_escape)


class AdaptiveExternalEscapeTests(unittest.TestCase):
    def test_escape_audit_separates_descent_and_direct_certificates(self):
        result = adaptive_escape.run_experiment(100_000, 128, 5)
        self.assertEqual(result["residual_after_direct_families"], 83)
        self.assertEqual(result["adaptive_descent_hits"], 68)
        self.assertEqual(result["adaptive_descent_escapes"], 15)
        self.assertEqual(result["escapes_with_quadratic_external_source_descent"], 15)
        self.assertEqual(result["escapes_with_even_source_distance_descent"], 7)
        self.assertEqual(
            result["escapes_with_shifted_quadratic_external_source_descent"], 0
        )
        self.assertEqual(
            result["joint_escapes_with_complete_even_source_distance_descent"], 0
        )
        self.assertEqual(
            result["joint_escapes_with_even_standard_two_tail_descent"], 0
        )
        self.assertEqual(
            result["joint_escapes_with_three_divisible_standard_two_tail_descent"], 0
        )
        self.assertEqual(result["escapes_with_recorded_descent"], 15)
        self.assertEqual(result["escapes_with_external_source_window"], 15)
        self.assertEqual(result["escapes_with_type_ii_ac_ray"], 15)

        first = result["escape_records"][0]
        self.assertEqual(first["prime"], 2521)
        self.assertIn("external-source-direct", first["classification"])
        self.assertIn("type-II-AC-ray", first["classification"])
        self.assertIsNotNone(first["external_source_factor_ray"])
        self.assertIsNotNone(first["type_ii_ac_ray"])
        self.assertIsNotNone(first["quadratic_external_source_descent"])
        self.assertTrue(first["adaptive_k_profiles"])
        for profile in first["adaptive_k_profiles"]:
            self.assertEqual(profile["q"], 4 * profile["k"] - 1)
            self.assertEqual(
                (profile["q"] + 1) * profile["source_denominator"],
                profile["q"] * first["prime"] + 1,
            )

        distance_47 = next(
            record
            for record in result["escape_records"]
            if record["prime"] == 16_921
        )
        self.assertEqual(
            distance_47["even_source_distance_descent"]["distance"], 47
        )

    def test_million_scale_escape_artifact(self):
        with (
            ROOT / "reproductions" / "adaptive-external-escape-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000)
        self.assertEqual(result["residual_after_direct_families"], 520)
        self.assertEqual(result["adaptive_descent_hits"], 425)
        self.assertEqual(result["adaptive_descent_escapes"], 95)
        self.assertEqual(result["escapes_with_quadratic_external_source_descent"], 87)
        self.assertEqual(result["escapes_with_even_source_distance_descent"], 53)
        self.assertEqual(
            result["escapes_with_shifted_quadratic_external_source_descent"], 4
        )
        self.assertEqual(
            result["joint_escapes_with_complete_even_source_distance_descent"], 0
        )
        self.assertEqual(
            result["joint_escapes_with_even_standard_two_tail_descent"], 2
        )
        self.assertEqual(
            result["joint_escapes_with_three_divisible_standard_two_tail_descent"], 0
        )
        self.assertEqual(result["escapes_with_recorded_descent"], 95)
        self.assertEqual(result["escapes_with_external_source_window"], 95)
        self.assertEqual(result["escapes_with_type_ii_ac_ray"], 95)

    def test_two_million_scale_escape_artifact(self):
        with (
            ROOT / "reproductions" / "adaptive-external-escape-2m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 2_000_000)
        self.assertEqual(result["residual_after_direct_families"], 883)
        self.assertEqual(result["adaptive_descent_hits"], 725)
        self.assertEqual(result["adaptive_descent_escapes"], 158)
        self.assertEqual(result["escapes_with_quadratic_external_source_descent"], 144)
        self.assertEqual(result["escapes_with_even_source_distance_descent"], 90)
        self.assertEqual(
            result["escapes_with_shifted_quadratic_external_source_descent"], 7
        )
        self.assertEqual(
            result["joint_escapes_with_even_standard_two_tail_descent"], 3
        )
        self.assertEqual(
            result["joint_escapes_with_three_divisible_standard_two_tail_descent"], 0
        )
        self.assertEqual(result["escapes_with_recorded_descent"], 158)

    def test_three_million_scale_first_composite_escape_artifact(self):
        with (
            ROOT / "reproductions" / "adaptive-external-escape-3m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 3_000_000)
        self.assertEqual(result["residual_after_direct_families"], 1_213)
        self.assertEqual(result["adaptive_descent_hits"], 998)
        self.assertEqual(result["adaptive_descent_escapes"], 215)
        self.assertEqual(result["escapes_with_quadratic_external_source_descent"], 199)
        self.assertEqual(result["escapes_with_even_source_distance_descent"], 134)
        self.assertEqual(
            result["escapes_with_shifted_quadratic_external_source_descent"], 7
        )
        self.assertEqual(
            result["joint_escapes_with_even_standard_two_tail_descent"], 3
        )
        self.assertEqual(result["escapes_with_recorded_descent"], 214)

        fields = (
            "quadratic_external_source_descent",
            "even_source_distance_descent",
            "shifted_quadratic_external_source_descent",
            "complete_even_source_distance_descent",
            "even_standard_two_tail_descent",
            "three_divisible_standard_two_tail_descent",
        )
        uncovered = [
            record
            for record in result["escape_records"]
            if not any(record[field] for field in fields)
        ]
        self.assertEqual([record["prime"] for record in uncovered], [2_451_289])
        self.assertEqual(
            uncovered[0]["external_source_factor_ray"],
            {"source": 2, "gap": 79, "q": 31_029, "r": 15_515, "t": 306_421},
        )
        self.assertEqual(
            uncovered[0]["type_ii_ac_ray"],
            {"a": 1, "c": 2, "k": 13, "h": 103, "gap": 23_799, "divisor": 2},
        )


if __name__ == "__main__":
    unittest.main()
