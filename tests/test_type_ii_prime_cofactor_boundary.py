import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_prime_cofactor_boundary",
    ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIIPrimeCofactorBoundaryTests(unittest.TestCase):
    def test_base_fan_modulus_and_one_prime_obstruction(self):
        result = boundary.run_audit(14)
        self.assertEqual(result["combined_modulus"], 240_240)
        self.assertEqual(result["one_prime_safe_residue_count"], 616)
        self.assertEqual(result["admissible_one_prime_safe_residue_count"], 0)
        self.assertEqual(result["covering_prime_histogram"], {3: 616})
        self.assertEqual(result["second_level_safe_branch_count"], 1_793)
        self.assertEqual(result["second_level_safe_residue_count"], 616)

    def test_sixteenth_shift_closes_the_fixed_modulus_second_layer(self):
        result = boundary.run_audit(16)
        self.assertEqual(result["combined_modulus"], 240_240)
        self.assertEqual(result["one_prime_safe_residue_count"], 587)
        self.assertEqual(result["covering_prime_histogram"], {3: 587, 17: 587})
        self.assertEqual(result["second_level_safe_branch_count"], 0)
        self.assertEqual(result["second_level_safe_residue_count"], 0)

    def test_forced_factor_renewal_ladder(self):
        h10 = boundary.run_audit(10)
        h11 = boundary.run_audit(11)
        h12 = boundary.run_audit(12)
        h13 = boundary.run_audit(13)
        h17 = boundary.run_audit(17)
        h18 = boundary.run_audit(18)

        self.assertEqual(
            (
                h10["combined_modulus"],
                h10["second_level_safe_branch_count"],
                h10["covering_prime_histogram"],
            ),
            (1_680, 0, {3: 12, 11: 12}),
        )
        self.assertEqual(
            (
                h11["combined_modulus"],
                h11["second_level_safe_branch_count"],
            ),
            (18_480, 210),
        )
        self.assertEqual(
            (
                h12["combined_modulus"],
                h12["second_level_safe_branch_count"],
                h12["covering_prime_histogram"],
            ),
            (18_480, 0, {3: 72, 13: 72}),
        )
        self.assertEqual(
            (
                h13["combined_modulus"],
                h13["second_level_safe_branch_count"],
            ),
            (240_240, 1_793),
        )
        self.assertEqual(
            (
                h17["combined_modulus"],
                h17["second_level_safe_branch_count"],
            ),
            (4_084_080, 21_459),
        )
        self.assertEqual(
            (
                h18["combined_modulus"],
                h18["second_level_safe_branch_count"],
                h18["covering_prime_histogram"],
            ),
            (4_084_080, 0, {3: 7_292, 19: 7_292}),
        )

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-prime-cofactor-boundary-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_shift_bound"], 14)
        self.assertEqual(result["combined_modulus"], 240_240)
        self.assertEqual(result["one_prime_safe_residue_count"], 616)
        self.assertEqual(result["covering_prime_histogram"], {"3": 616})
        self.assertEqual(result["second_level_safe_branch_count"], 1_793)
        self.assertEqual(result["second_level_safe_residue_count"], 616)

    def test_checked_h19_ladder_summary(self):
        with (
            ROOT / "reproductions" / "type-ii-prime-cofactor-ladder-h19-summary.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_shift_bound"], 19)
        self.assertEqual(result["combined_modulus"], 77_597_520)
        self.assertEqual(result["core_residue_count"], 1_658_880)
        self.assertEqual(result["one_prime_safe_residue_count"], 90_827)
        self.assertEqual(result["covering_prime_histogram"], {"3": 90_827})
        self.assertEqual(result["second_level_safe_branch_count"], 265_001)
        self.assertEqual(result["second_level_safe_residue_count"], 90_827)

    def test_checked_h20_ladder_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-prime-cofactor-ladder-h20-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_shift_bound"], 20)
        self.assertEqual(result["combined_modulus"], 77_597_520)
        self.assertEqual(result["core_residue_count"], 1_658_880)
        self.assertEqual(result["one_prime_safe_residue_count"], 78_611)
        self.assertEqual(result["covering_prime_histogram"], {"3": 78_611})
        self.assertEqual(result["second_level_safe_branch_count"], 151_723)
        self.assertEqual(result["second_level_safe_residue_count"], 78_546)

    def test_checked_h21_h22_fixed_modulus_block_artifacts(self):
        with (
            ROOT / "reproductions" / "type-ii-prime-cofactor-ladder-h21-results.json"
        ).open(encoding="utf-8") as handle:
            h21 = json.load(handle)
        with (
            ROOT / "reproductions" / "type-ii-prime-cofactor-ladder-h22-results.json"
        ).open(encoding="utf-8") as handle:
            h22 = json.load(handle)
        self.assertEqual(h21["combined_modulus"], 77_597_520)
        self.assertEqual(h21["one_prime_safe_residue_count"], 78_241)
        self.assertEqual(h21["second_level_safe_branch_count"], 66_638)
        self.assertEqual(h21["second_level_safe_residue_count"], 33_685)
        self.assertEqual(h22["combined_modulus"], 77_597_520)
        self.assertEqual(h22["one_prime_safe_residue_count"], 78_165)
        self.assertEqual(h22["second_level_safe_branch_count"], 0)
        self.assertEqual(h22["second_level_safe_residue_count"], 0)


if __name__ == "__main__":
    unittest.main()
