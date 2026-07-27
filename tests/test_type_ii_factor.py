import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("type_ii_factor", ROOT / "reproductions" / "type_ii_factor.py")
assert SPEC and SPEC.loader
type_ii_factor = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = type_ii_factor
SPEC.loader.exec_module(type_ii_factor)


class TypeIIFactorExperimentTests(unittest.TestCase):
    def test_small_experiment_has_exact_witnesses(self):
        result = type_ii_factor.run_experiment(10_000, 16)
        self.assertEqual(result["factor_generator_missing"], [])
        self.assertEqual(
            result["factor_generator_certified_count"],
            result["residual_after_direct_families"],
        )
        self.assertIsNotNone(result["largest_minimal_box_found"])


if __name__ == "__main__":
    unittest.main()
