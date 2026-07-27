import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "shared_residue_fixed_gap_boundary",
    ROOT / "reproductions" / "shared_residue_fixed_gap_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class SharedResidueFixedGapBoundaryTests(unittest.TestCase):
    def test_core_prime_gap_misses_both_coupled_targets(self):
        witness = boundary.fixed_gap_coupled_failure()
        self.assertEqual((witness["prime"], witness["gap"], witness["x"]), (73, 47, 30))
        self.assertEqual(witness["type_ii_target_residue"], 17)
        self.assertNotIn(17, witness["x_squared_divisor_residues"])
        self.assertFalse(witness["type_ii_target_reached"])
        self.assertEqual(witness["nontrivial_shared_divisors"], ())
        self.assertFalse(witness["shared_target_reached"])


if __name__ == "__main__":
    unittest.main()
