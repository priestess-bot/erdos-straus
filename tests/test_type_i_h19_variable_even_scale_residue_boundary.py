import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_variable_even_scale_residue_boundary",
    ROOT / "reproductions" / "type_i_h19_variable_even_scale_residue_boundary.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19VariableEvenScaleResidueBoundaryTests(unittest.TestCase):
    def test_residual_misses_have_no_unrestricted_residue_hit(self):
        variable = json.loads(
            (ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-variable-even-scale-residue-boundary-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(variable)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["input_variable_even_scale_miss_count"],
                actual["all_scale_profiles"],
                actual["unrestricted_residue_hit_count"],
            ),
            (28, 542, 0),
        )
        self.assertTrue(
            all(
                scale["residue_minus_one_divisor_count"] == 0
                for profile in actual["profiles"]
                for scale in profile["scales"]
            )
        )


if __name__ == "__main__":
    unittest.main()
