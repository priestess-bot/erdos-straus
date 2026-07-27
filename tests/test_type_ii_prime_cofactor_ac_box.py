import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_prime_cofactor_boundary_ac_box",
    ROOT / "reproductions" / "type_ii_prime_cofactor_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class TypeIIPrimeCofactorAcBoxTests(unittest.TestCase):
    def test_ac_box_preserves_same_shift_distinct_moduli(self):
        fan = boundary.ac_box_fan(2)
        self.assertEqual(fan, ((1, 1, 1), (2, 1, 2), (4, 2, 1), (8, 2, 2)))

    def test_ac_box_radius_five_has_no_admissible_one_prime_escape(self):
        result = boundary.run_ac_box_audit(5)
        self.assertEqual(result["ac_bound"], 5)
        self.assertEqual(result["combined_modulus"], 14_400)
        self.assertEqual(result["core_residue_count"], 480)
        self.assertEqual(result["one_prime_safe_residue_count"], 240)
        self.assertEqual(result["admissible_one_prime_safe_residue_count"], 0)

    def test_ac_box_radius_five_universal_covering_prime_has_no_second_escape(self):
        result = boundary.run_covering_prime_branch_audit(boundary.ac_box_fan(5), 7)
        self.assertEqual(
            result,
            {
                "prime": 7,
                "covered_residue_count": 240,
                "expanded_branch_count": 1_680,
                "ray_safe_branch_count": 960,
                "admissible_branch_count": 0,
            },
        )

    def test_ac_box_recursive_state_audit_agrees_with_two_layer_boundary(self):
        result = boundary.run_recursive_covering_state_audit(
            boundary.ac_box_fan(5), 7, 3
        )
        self.assertEqual(result["one_prime_safe_root_count"], 240)
        self.assertEqual(result["terminal_ray_safe_state_count"], 22_276)
        self.assertEqual(result["terminal_admissible_state_count"], 0)
        self.assertEqual(
            [level["ray_safe_branch_count"] for level in result["levels"]],
            [720, 3_420, 22_276],
        )

    def test_ac_box_recursive_depth_four_has_admissible_witness(self):
        fan = boundary.ac_box_fan(5)
        witness = boundary.first_recursive_admissible_witness(fan, 7, 4, 0, 1)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["initial_residue_class"], 1)
        self.assertEqual(
            witness["branch_history"],
            [
                {"prime": 7, "residue": 0},
                {"prime": 11, "residue": 0},
                {"prime": 13, "residue": 0},
                {"prime": 17, "residue": 0},
            ],
        )
        self.assertEqual(
            witness["target_prime_form"],
            {"coefficient": 245_044_800, "constant": 1},
        )
        self.assertEqual(witness["covering_primes"], [])
        self.assertEqual(len(witness["ray_states"]), 25)
        for ray in witness["ray_states"]:
            self.assertEqual(
                ray["fixed_factor"] * ray["quotient_coefficient"],
                witness["target_prime_form"]["coefficient"],
            )
            self.assertEqual(
                ray["fixed_factor"] * ray["quotient_constant"],
                witness["target_prime_form"]["constant"] + 4 * ray["shift"],
            )


if __name__ == "__main__":
    unittest.main()
