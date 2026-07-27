import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_shared_selector_collision_state",
    ROOT / "reproductions" / "type_ii_shared_selector_collision_state.py",
)
assert SPEC and SPEC.loader
state = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(state)


class SharedSelectorCollisionStateTests(unittest.TestCase):
    def test_collision_primes(self):
        self.assertEqual(
            state.collision_primes(31), (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        )

    def test_half_million_pressure_point_compiles_exactly(self):
        result = state.run_audit(33_011_449, 31)
        self.assertTrue(result["private_cofactors_pairwise_coprime"])
        self.assertEqual(result["shared_hit_positions"], 11)
        self.assertEqual(result["joint_hit_positions"], 0)
        self.assertGreater(result["type_ii_hit_positions"], 0)
        gap_19 = result["rows"][4]
        self.assertEqual(gap_19["gap"], 19)
        self.assertTrue(gap_19["type_ii_hit"])
        self.assertFalse(gap_19["shared_hit"])


if __name__ == "__main__":
    unittest.main()
