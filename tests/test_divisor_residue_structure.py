import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "divisor_residue_structure",
    ROOT / "reproductions" / "divisor_residue_structure.py",
)
assert SPEC and SPEC.loader
structure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = structure
SPEC.loader.exec_module(structure)


class DivisorResidueStructureTests(unittest.TestCase):
    def test_abstract_cyclic_example_attains_kneser_bound(self):
        for order in (4, 6, 8, 14, 22):
            example = structure.cyclic_additive_critical_example(order)
            self.assertEqual(len(example["sequence"]), order - 2)
            self.assertEqual(
                example["subsum_residues"],
                frozenset(set(range(order)) - {order // 2}),
            )
            self.assertEqual(example["stabilizer"], (0,))

    def test_unit_group_family_has_linear_unavoidable_exception_part(self):
        for prime in (7, 11, 19, 23, 31, 43):
            example = structure.unit_group_critical_example(prime)
            target = example["target"]
            sequence = example["sequence"]
            generated = example["generated_subgroup"]
            self.assertEqual(len(sequence), prime - 3)
            self.assertEqual(len(generated), prime - 1)
            self.assertEqual(pow(example["unit"], (prime - 1) // 2, 4 * prime), target)
            self.assertEqual(
                example["subset_product_residues"], generated - {target}
            )
            self.assertNotIn(target, example["subset_product_residues"])
            self.assertEqual(example["stabilizer"], (1,))

            # Any subgroup containing either term also contains its power -1.
            for term in {example["unit"], example["inverse"]}:
                self.assertIn(target, structure.cyclic_subgroup(term, 4 * prime))
            self.assertEqual(
                example["minimum_target_free_subgroup_exceptions"], prime - 3
            )
            self.assertEqual(
                structure.target_free_subgroup_escape_number(
                    sequence, 4 * prime, target
                ),
                prime - 3,
            )

    def test_q_seven_example_is_an_actual_integer_divisor_residue_set(self):
        example = structure.realized_integer_example(7)
        self.assertEqual(example["factorization"], ((3, 2), (19, 2)))
        self.assertEqual(example["integer"], 3**2 * 19**2)
        self.assertEqual(
            example["divisor_residues"], example["subset_product_residues"]
        )
        self.assertNotIn(27, example["divisor_residues"])

    def test_support_critical_ray_forces_target_congruence(self):
        factors = structure.smallest_prime_factors(10_000 + 4 * 5**3)
        analysis = structure.support_critical_ray_analysis(1489, 2, 2, factors)
        self.assertTrue(analysis["failed"])
        self.assertTrue(analysis["support_critical"])
        self.assertTrue(analysis["congruence_forced"])
        self.assertEqual(analysis["residues"], analysis["support"] - {15})
        self.assertEqual(1489 % 16, 1)

    def test_nontrivial_two_hole_defect_is_forced_target_pair(self):
        factors = structure.smallest_prime_factors(10_000 + 4 * 5**3)
        analysis = structure.support_critical_ray_analysis(313, 1, 5, factors)
        self.assertTrue(analysis["failed"])
        self.assertTrue(analysis["target_in_support"])
        self.assertTrue(analysis["nontrivial_two_hole"])
        self.assertEqual(analysis["total_product"], 13)
        self.assertEqual(analysis["defect"], frozenset({7, 19}))
        self.assertEqual(analysis["defect"], analysis["two_hole_expected_defect"])
        self.assertTrue(analysis["defect_orbit_invariant"])

    def test_nontrivial_odd_defect_has_missing_square_root(self):
        factors = structure.smallest_prime_factors(10_000 + 4 * 5**3)
        analysis = structure.support_critical_ray_analysis(409, 3, 3, factors)
        self.assertTrue(analysis["failed"])
        self.assertTrue(analysis["nontrivial_odd_defect"])
        self.assertEqual(analysis["total_product"], 13)
        self.assertEqual(analysis["defect"], frozenset({23, 25, 35}))
        self.assertEqual(analysis["missing_square_roots"], frozenset({25}))
        self.assertTrue(analysis["defect_orbit_invariant"])

    def test_target_outside_support_splits_by_square_saturation(self):
        factors = structure.smallest_prime_factors(10_000 + 4 * 5**3)
        separable = structure.support_critical_ray_analysis(73, 1, 2, factors)
        self.assertTrue(separable["failed"])
        self.assertFalse(separable["target_in_support"])
        self.assertTrue(separable["target_quadratically_separable"])
        self.assertFalse(separable["quadratic_separator_core_active"])

        inseparable = structure.support_critical_ray_analysis(97, 2, 4, factors)
        self.assertTrue(inseparable["failed"])
        self.assertFalse(inseparable["target_in_support"])
        self.assertFalse(inseparable["target_quadratically_separable"])
        self.assertIn(
            inseparable["target"], inseparable["support_square_saturation"]
        )

        core_active = structure.support_critical_ray_analysis(241, 1, 5, factors)
        self.assertTrue(core_active["target_quadratically_separable"])
        self.assertTrue(core_active["quadratic_separator_core_active"])
        self.assertEqual(core_active["target_outside_two_power_depth"], 0)

        depth_one = structure.support_critical_ray_analysis(97, 2, 4, factors)
        depth_two = structure.support_critical_ray_analysis(3457, 4, 4, factors)
        self.assertEqual(depth_one["target_outside_two_power_depth"], 1)
        self.assertEqual(depth_two["target_outside_two_power_depth"], 2)

    def test_one_fixed_active_character_does_not_cover_every_failure_on_m80(self):
        factors = structure.smallest_prime_factors(10_000 + 4 * 5**3)
        first = structure.support_critical_ray_analysis(601, 5, 4, factors)
        second = structure.support_critical_ray_analysis(3169, 5, 4, factors)
        first_basis, first_masks = structure.active_quadratic_separator_masks(
            first["support"], 80
        )
        second_basis, second_masks = structure.active_quadratic_separator_masks(
            second["support"], 80
        )
        self.assertTrue(first["quadratic_separator_core_active"])
        self.assertTrue(second["quadratic_separator_core_active"])
        self.assertEqual(first_basis, (3, 7, 11))
        self.assertEqual(second_basis, first_basis)
        self.assertEqual(first_masks, (1,))
        self.assertEqual(second_masks, (4,))

    def test_support_critical_audit_has_no_congruence_violation(self):
        audit = structure.run_support_critical_audit(10_000, 5)
        self.assertEqual(audit["ray_failures"], 2909)
        self.assertEqual(audit["target_in_support_failures"], 319)
        self.assertEqual(audit["target_outside_support_failures"], 2590)
        self.assertEqual(audit["target_outside_quadratically_separable"], 2521)
        self.assertEqual(audit["target_outside_quadratically_inseparable"], 69)
        self.assertEqual(audit["target_outside_core_active_quadratic"], 432)
        self.assertEqual(audit["target_outside_core_trivial_quadratic"], 2089)
        self.assertEqual(
            audit["target_outside_two_power_depth_histogram"], {0: 2521, 1: 68, 2: 1}
        )
        m80 = next(
            record
            for record in audit["active_quadratic_character_fixedness"]
            if (record["a"], record["c"]) == (5, 4)
        )
        self.assertEqual(m80["basis"], (3, 7, 11))
        self.assertEqual(m80["available_masks"], (1, 4))
        self.assertEqual(m80["common_masks"], ())
        self.assertEqual(audit["defect_orbit_violations"], [])
        self.assertEqual(audit["support_critical_count"], 5)
        self.assertEqual(audit["support_critical_prime_count"], 5)
        self.assertEqual(audit["congruence_violations"], [])
        self.assertEqual(audit["nontrivial_two_hole_count"], 15)
        self.assertEqual(audit["two_hole_shape_violations"], [])
        self.assertEqual(audit["nontrivial_odd_defect_count"], 45)
        self.assertEqual(audit["odd_defect_square_violations"], [])
        self.assertEqual(audit["samples"][0]["prime"], 1489)


if __name__ == "__main__":
    unittest.main()
