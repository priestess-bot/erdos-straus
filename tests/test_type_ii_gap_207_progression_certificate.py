import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_gap_207_progression_certificate",
    ROOT / "reproductions" / "type_ii_gap_207_progression_certificate.py",
)
assert SPEC and SPEC.loader
gap_207 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gap_207
SPEC.loader.exec_module(gap_207)


class TypeIIGap207ProgressionCertificateTests(unittest.TestCase):
    def test_progression_certificates_are_exact(self):
        result = gap_207.run_audit()
        self.assertEqual(result["gap"], 207)
        self.assertEqual(result["forced_factor"], 9_682)
        self.assertEqual(result["target_factor"], 47)
        self.assertEqual(result["cofactor_residue_mod_gap"], 34)
        self.assertEqual(result["target_residue_mod_gap"], 149)
        self.assertTrue(result["primitive_progression"])
        self.assertTrue(all(sample["exact_identity"] for sample in result["samples"]))
        self.assertEqual(result["samples"][0]["divisor"], 186_449)

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-gap-207-progression-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_residue"], 153_633_769)
        self.assertEqual(result["gap"], 207)
        self.assertTrue(result["primitive_progression"])
        self.assertEqual(len(result["samples"]), 3)
        self.assertTrue(all(sample["exact_identity"] for sample in result["samples"]))


if __name__ == "__main__":
    unittest.main()
