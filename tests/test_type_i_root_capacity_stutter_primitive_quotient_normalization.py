import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_root_capacity_stutter_primitive_quotient_normalization",
    ROOT / "reproductions" / "type_i_root_capacity_stutter_primitive_quotient_normalization.py",
)
assert SPEC and SPEC.loader
normalization = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = normalization
SPEC.loader.exec_module(normalization)


class TypeIRootCapacityStutterPrimitiveQuotientNormalizationTests(unittest.TestCase):
    def test_shared_factor_normalization_and_saturation(self):
        normalization.verify_shared_factor_control()

    def test_primitive_quotient_and_missing_root_boundary(self):
        normalization.verify_primitive_quotient_control()
        normalization.verify_missing_root_boundary()


if __name__ == "__main__":
    unittest.main()
