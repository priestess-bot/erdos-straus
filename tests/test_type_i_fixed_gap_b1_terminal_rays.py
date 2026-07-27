import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_fixed_gap_b1_terminal_rays",
    ROOT / "reproductions" / "type_i_fixed_gap_b1_terminal_rays.py",
)
assert SPEC and SPEC.loader
rays = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rays
SPEC.loader.exec_module(rays)


class TypeIFixedGapBOneTerminalRaysTests(unittest.TestCase):
    def test_checked_profile_rebuilds(self):
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-fixed-gap-b1-terminal-rays-results.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(rays.run_audit(), expected)
        self.assertEqual(
            [record["prime"] for record in expected["gap_three_prime_samples"]],
            [337, 1153, 2377],
        )

    def test_formula_reconstructs_multiple_gaps(self):
        for gap_index, scale, index in ((1, 1, 1), (2, 1, 3), (3, 1, 4), (5, 3, 2)):
            witness = rays.ray_witness(gap_index, scale, index)
            self.assertEqual(witness["gap"], 4 * gap_index - 1)
            self.assertEqual(witness["A"], 6 * scale * index - 1)
            self.assertEqual(witness["R"], 24 * gap_index * scale - 1)
            self.assertEqual(witness["E"], 24 * gap_index * scale)
            self.assertTrue(witness["overlap_condition"])
            self.assertEqual(witness["bridge_scale"] % gap_index, 0)
            self.assertEqual(witness["source_denominator"], witness["prime"] - 1)
            tail = witness["ordinary_type_ii_tail"]
            self.assertEqual((tail["gap"], tail["divisor"]), (witness["gap"], gap_index * witness["A"]))
            self.assertLess(tail["source_denominator"], witness["prime"])
            self.assertEqual(witness["progression"]["gcd"], 1)

    def test_nonpositive_parameters_are_rejected(self):
        for parameters in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                rays.ray_witness(*parameters)


if __name__ == "__main__":
    unittest.main()
