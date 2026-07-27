import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_dyadic_b_source_selector",
    ROOT / "reproductions" / "type_i_dyadic_b_source_selector.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class TypeIDyadicBSourceSelectorTests(unittest.TestCase):
    def test_boundary_witnesses_rebuild(self):
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-dyadic-b-source-selector-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = selector.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["B2_witness"]["normal_form"][1], 2)
        self.assertEqual(actual["B8_witness"]["normal_form"][1], 8)
        self.assertIsNone(actual["B4_rejected_on_B8_state"])

    def test_dyadic_b_requires_available_two_adic_budget(self):
        self.assertIsNone(selector.dyadic_b_source_witness(63_332_329, 1, 48, 20))


if __name__ == "__main__":
    unittest.main()
