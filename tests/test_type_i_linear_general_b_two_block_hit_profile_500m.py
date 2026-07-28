import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_general_b_two_block_hit_profile_500m",
    ROOT / "reproductions" / "type_i_linear_general_b_two_block_hit_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def independent_block_target_hit(block, modulus):
    """Directly enumerate block-squared divisors without production helpers."""
    inverse = pow(block, -1, modulus)
    residues = {
        int(divisor) * inverse % modulus for divisor in sympy.divisors(block * block)
    }
    return (modulus - 1) in residues, len(residues)


class TypeILinearGeneralBTwoBlockHitProfile500MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-general-b-two-block-hit-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        cls.source = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-global-linear-b1-failure-general-b-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["input_sha256"], profile.EXPECTED_INPUT_SHA256)

    def test_every_block_profile_is_recomputed_from_raw_source_states(self):
        source_profiles = {
            int(item["prime"]): item
            for item in self.source["general_B_failure_profiles"]
        }
        aggregate = {}
        for output_profile in self.actual["profiles"]:
            prime = int(output_profile["prime"])
            source_records = {
                int(record["R"]): record
                for record in source_profiles[prime]["records"]
                if record["classification"] == "hit"
            }
            self.assertEqual(
                [int(record["R"]) for record in output_profile["records"]],
                list(source_records),
            )
            for output_record in output_profile["records"]:
                modulus = int(output_record["R"])
                K = int(output_record["K"])
                raw_states = source_records[modulus]["source_states"]
                self.assertEqual(
                    len(output_record["source_orientations"]), len(raw_states)
                )
                for orientation, (a, s) in zip(
                    output_record["source_orientations"], raw_states
                ):
                    a, s = int(a), int(s)
                    lambda_value = 4 if s % 4 == 1 else 2
                    eta = 4 // lambda_value
                    gamma = (s * modulus + 1) // lambda_value
                    affine_block = (a * modulus + 1) // eta
                    self.assertEqual(prime, a + s + a * s * modulus)
                    self.assertEqual(gamma * affine_block, K)
                    gamma_hit, gamma_count = independent_block_target_hit(
                        gamma, modulus
                    )
                    affine_hit, affine_count = independent_block_target_hit(
                        affine_block, modulus
                    )
                    self.assertEqual(orientation["lambda"], lambda_value)
                    self.assertEqual(orientation["eta"], eta)
                    self.assertEqual(orientation["gamma"], gamma)
                    self.assertEqual(orientation["L"], affine_block)
                    self.assertEqual(
                        orientation["minus_one_in_gamma_centered_spectrum"],
                        gamma_hit,
                    )
                    self.assertEqual(
                        orientation["gamma_centered_spectrum_residue_count"],
                        gamma_count,
                    )
                    self.assertEqual(
                        orientation["minus_one_in_L_centered_spectrum"],
                        affine_hit,
                    )
                    self.assertEqual(
                        orientation["L_centered_spectrum_residue_count"],
                        affine_count,
                    )
                    category = (
                        "both_blocks"
                        if gamma_hit and affine_hit
                        else "source_block_only"
                        if gamma_hit
                        else "affine_block_only"
                        if affine_hit
                        else "mixed_blocks"
                    )
                    self.assertEqual(
                        orientation["target_hit_block_classification"], category
                    )
                    aggregate[category] = aggregate.get(category, 0) + 1
        self.assertEqual(
            aggregate,
            self.actual["aggregate_block_classification_counts"],
        )

    def test_mixed_blocks_are_the_dominant_success_mechanism(self):
        self.assertEqual(self.actual["target_hit_R_count"], 12)
        self.assertEqual(self.actual["directed_target_hit_source_count"], 20)
        self.assertEqual(
            self.actual["aggregate_block_classification_counts"],
            {
                "affine_block_only": 2,
                "mixed_blocks": 16,
                "source_block_only": 2,
            },
        )


if __name__ == "__main__":
    unittest.main()
