import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_variable_even_scale_after_k6",
    ROOT / "reproductions" / "type_i_h19_variable_even_scale_after_k6.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIH19VariableEvenScaleAfterK6Tests(unittest.TestCase):
    def test_full_affine_even_source_family_rebuilds(self):
        k6 = json.loads(
            (ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-variable-even-scale-after-k6-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(k6)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["input_k2_k6_boundary_count"],
                actual["variable_even_scale_terminal_count"],
                actual["variable_even_scale_miss_count"],
            ),
            (71, 43, 28),
        )

        for record in actual["records"]:
            certificate = record["certificate"]
            self.assertEqual(certificate["q"], 4 * certificate["k"] - 1)
            self.assertEqual(certificate["source_denominator"] % 2, 0)
        for miss in actual["variable_even_scale_misses"]:
            self.assertGreaterEqual(len(miss["eligible_even_scales"]), 2)
            self.assertEqual(miss["eligible_even_scales"][:2], [2, 6])


if __name__ == "__main__":
    unittest.main()
