import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_source_square_modulus",
    ROOT / "reproductions" / "type_i_source_square_modulus.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeISourceSquareModulusTests(unittest.TestCase):
    def test_known_moduli(self):
        self.assertEqual(audit.source_square_modulus(2), 2)
        self.assertEqual(audit.source_square_modulus(4), 4)
        self.assertEqual(audit.source_square_modulus(8), 8)
        self.assertEqual(audit.source_square_modulus(12), 12)
        self.assertEqual(audit.source_square_modulus(72), 24)
        self.assertEqual(audit.source_square_modulus(352), 176)
        self.assertEqual(audit.source_square_modulus(5540), 5540)

    def test_modulus_matches_direct_condition(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-source-square-modulus-audit-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["checked_even_pairs"], 1_000_000)
        self.assertEqual(actual["short_shift_witness_count"], 35)


if __name__ == "__main__":
    unittest.main()
