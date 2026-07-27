import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_external_source_pressure",
    ROOT
    / "reproductions"
    / "type_ii_tail_deflation_p_minus_one_external_source_pressure.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOneExternalSourcePressureTests(unittest.TestCase):
    def test_all_external_source_strict_descent_variants_miss_the_four_points(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-external-source-50m-pressure.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        expected = [25_073_689, 33_011_449, 42_622_969, 48_825_529]
        self.assertEqual(result["prime_limit"], 50_000_000)
        self.assertEqual(result["input_residual_count"], 4)
        self.assertEqual(result["ordinary_external_source_hit_count"], 0)
        self.assertEqual(result["mixed_factor_external_source_hit_count"], 0)
        self.assertEqual(result["quadratic_factor_external_source_hit_count"], 0)
        self.assertEqual(result["ordinary_external_source_misses"], expected)
        self.assertEqual(result["mixed_factor_external_source_misses"], expected)
        self.assertEqual(result["quadratic_factor_external_source_misses"], expected)


if __name__ == "__main__":
    unittest.main()
