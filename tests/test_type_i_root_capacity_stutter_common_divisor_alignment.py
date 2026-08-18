import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_root_capacity_stutter_common_divisor_alignment",
    ROOT / "reproductions" / "type_i_root_capacity_stutter_common_divisor_alignment.py",
)
assert SPEC and SPEC.loader
alignment = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = alignment
SPEC.loader.exec_module(alignment)


class TypeIRootCapacityStutterCommonDivisorAlignmentTests(unittest.TestCase):
    def test_cyclotomic_controls_and_missing_root_boundary(self):
        alignment.verify_cyclotomic_controls()
        alignment.verify_missing_cyclotomic_boundary()


if __name__ == "__main__":
    unittest.main()
