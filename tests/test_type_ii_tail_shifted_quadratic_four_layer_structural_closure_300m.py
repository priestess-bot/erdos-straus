import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "reproductions" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


two_sided = load_module(
    "type_ii_tail_shifted_quadratic_two_sided_completion_300m",
    "type_ii_tail_shifted_quadratic_two_sided_completion.py",
)


class TypeIITailShiftedQuadraticFourLayerStructuralClosure300MTests(unittest.TestCase):
    @staticmethod
    def input_payload():
        path = ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-opposite-pair-profile-300m-results.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def test_two_sided_artifact_rebuilds(self):
        checked = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-two-sided-completion-300m-results.json").read_text(encoding="utf-8")
        )
        self.assertEqual(two_sided.run_audit(self.input_payload()), checked)

    def test_bounded_two_sided_interfaces_close_the_two_outer_residuals(self):
        result = two_sided.run_audit(self.input_payload())
        self.assertEqual(result["minimal_structural_miss_count"], 10)
        self.assertEqual(result["two_sided_completion_hit_count"], 9)
        self.assertEqual(result["two_sided_completion_miss_primes"], [6_294_649])
        records = {record["prime"]: record["two_sided_completion"] for record in result["records"]}
        witness = records[212_973_049]
        self.assertIsNotNone(witness)
        self.assertEqual(
            (witness["alpha"], witness["r"], witness["beta"]), (18, 186, 31)
        )
        self.assertEqual(
            (witness["gamma"], witness["z"], witness["delta"]), (59, 56, 883)
        )
        self.assertEqual((witness["a"], witness["b"]), (1_062, 27_373))
        self.assertEqual(witness["two_sided_square_root_quotient"], 5_489_370_311)


if __name__ == "__main__":
    unittest.main()
