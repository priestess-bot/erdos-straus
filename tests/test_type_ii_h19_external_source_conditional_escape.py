import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_external_source_conditional_escape",
    ROOT / "reproductions" / "type_ii_h19_external_source_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class TypeIIH19ExternalSourceConditionalEscapeTests(unittest.TestCase):
    def test_combined_forms_are_admissible_and_every_source_fails(self):
        result = escape.run_witness()
        self.assertEqual(result["h19"]["modulus"], 77_597_520)
        self.assertEqual(result["h19"]["residue_class"], 8_328_961)
        self.assertEqual(result["h19"]["form_count"], 20)
        self.assertEqual(result["combined_form_count"], 26)
        self.assertEqual(result["covering_primes"], [])
        self.assertEqual([row["k"] for row in result["sources"]], [1, 2, 3, 4, 5, 6])
        self.assertEqual(
            [row["fixed_factor"] for row in result["sources"]], [13, 11, 1, 1, 7, 1]
        )
        self.assertEqual(
            [row["target_residue"] for row in result["sources"]], [2, 5, 8, 11, 14, 17]
        )
        for row in result["sources"]:
            self.assertNotIn(row["target_residue"], row["divisor_residues"])

    def test_checked_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-h19-external-source-conditional-escape-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["combined_form_count"], 26)
        self.assertEqual(result["covering_primes"], [])


if __name__ == "__main__":
    unittest.main()
