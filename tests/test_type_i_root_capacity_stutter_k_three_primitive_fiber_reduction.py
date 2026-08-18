import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_root_capacity_stutter_k_three_primitive_fiber_reduction",
    ROOT / "reproductions" / "type_i_root_capacity_stutter_k_three_primitive_fiber_reduction.py",
)
assert SPEC and SPEC.loader
fiber = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fiber
SPEC.loader.exec_module(fiber)


class TypeIRootCapacityStutterKThreePrimitiveFiberReductionTests(unittest.TestCase):
    def test_d_one_fiber_has_only_the_noncore_curve_control(self):
        rows = fiber.fixed_d_fiber(1)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual((row.A, row.B, row.p, row.d), (1, 7, 939, 1))
        self.assertEqual(row.p % 24, 3)

    def test_fixed_gap_fiber_recovers_the_same_a_one_boundary(self):
        self.assertEqual(fiber.fixed_gap_fiber(1), ())
        rows = fiber.fixed_gap_fiber(6)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual((row.A, row.B, row.M, row.m, row.p), (1, 7, 2, 6, 939))
        fiber.verify_gap_reduction(row)

    def test_fixed_j_fiber_recovers_the_same_a_one_boundary(self):
        self.assertEqual(fiber.fixed_j_fiber(1), ())
        rows = fiber.fixed_j_fiber(0)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual((row.A, row.B, row.M, row.m, row.p), (1, 7, 2, 6, 939))
        fiber.verify_defect_reduction(row)

    def test_fixed_vieta_gap_fiber_recovers_the_same_a_one_boundary(self):
        rows = fiber.fixed_vieta_gap_fiber(1)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual((row.A, row.B, row.M, row.m, row.p), (1, 7, 2, 6, 939))
        self.assertEqual(row.B - row.m, 1)
        fiber.verify_vieta_gap_reduction(row)

    def test_vieta_companion_second_gate_hits_only_the_excluded_boundary(self):
        row = fiber.fixed_d_fiber(1)[0]
        self.assertEqual(fiber.verify_vieta_companion(row), (0, 1))
        self.assertNotEqual(
            fiber.vieta_companion_second_gate_numerator(3, 2) % 3,
            0,
        )

    def test_core_congruent_shadow_is_not_a_proper_root(self):
        row = fiber.reconstruct(991, 87)
        self.assertIsNotNone(row)
        assert row is not None
        self.assertEqual(row.p % 24, 1)
        self.assertGreater(row.a, row.e)
        self.assertGreater(row.h, row.p)

    def test_nonprimitive_d_one_divisor_is_rejected(self):
        self.assertIsNone(fiber.reconstruct(3, 39))


if __name__ == "__main__":
    unittest.main()
