import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_affine_uniform_divisor_rigidity",
    ROOT / "reproductions" / "type_ii_affine_uniform_divisor_rigidity.py",
)
assert SPEC and SPEC.loader
rigidity = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rigidity
SPEC.loader.exec_module(rigidity)


class TypeIIAffineUniformDivisorRigidityTests(unittest.TestCase):
    def test_square_only_affine_divisor_normal_form(self):
        result = rigidity.run_audit()
        classification = result["square_only_example"]["classification"]
        self.assertEqual(classification["E"], 12)
        self.assertEqual(classification["a"], 9)
        self.assertTrue(classification["a_divides_E_squared"])
        self.assertFalse(classification["a_divides_E"])
        self.assertTrue(classification["a_at_most_E"])
        self.assertTrue(result["square_only_example"]["gap_divides_E_plus_a"])
        self.assertTrue(
            all(
                sample["exact_identity"]
                for sample in result["square_only_example"]["samples"]
            )
        )
        self.assertFalse(result["nonproportional_control"]["is_proportional"])

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-affine-uniform-divisor-rigidity.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["square_only_example"]["classification"]["a"], 9)


if __name__ == "__main__":
    unittest.main()
