import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b5_dyadic_terminal_ray",
    ROOT / "reproductions" / "type_i_b5_dyadic_terminal_ray.py",
)
assert SPEC and SPEC.loader
ray = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ray
SPEC.loader.exec_module(ray)


class TypeIBFiveDyadicTerminalRayTests(unittest.TestCase):
    def test_checked_ray_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-b5-dyadic-terminal-ray-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(ray.run_audit(), expected)
        self.assertEqual(expected["progression"], {"initial": 21169, "step": 757200, "gcd": 1})
        self.assertEqual(
            [sample["prime"] for sample in expected["prime_samples"]],
            [21169, 4564369, 11379169, 15922369],
        )

    def test_fixed_formula_reconstructs_nonprime_and_prime_terms(self):
        for index in (0, 1, 6, 15, 39):
            witness = ray.ray_witness(index)
            self.assertEqual(witness["prime"], 757200 * index + 21169)
            self.assertEqual(witness["A"], 30 * index + 1)
            self.assertEqual((witness["B"], witness["C"], witness["E"], witness["R"]), (5, 1262, 32, 31))
            self.assertEqual(witness["source_denominator"], witness["prime"] - 1)

    def test_negative_index_is_rejected(self):
        with self.assertRaises(ValueError):
            ray.ray_witness(-1)


if __name__ == "__main__":
    unittest.main()
