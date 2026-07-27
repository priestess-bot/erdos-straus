import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_b12_residue_selector",
    ROOT / "reproductions" / "type_i_pminusone_b12_residue_selector.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIPMinusOneB12ResidueSelectorTests(unittest.TestCase):
    def test_complement_records_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-pminusone-b12-residue-selector-100k-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["p_minus_one_record_count"], 93)
        self.assertEqual(actual["b_histogram"], {"1": 81, "2": 12})
        self.assertEqual(actual["maximum_E"], 136)
        self.assertEqual(
            actual["E_values"],
            [12, 20, 24, 28, 40, 48, 56, 72, 100, 112, 120, 136],
        )


if __name__ == "__main__":
    unittest.main()
