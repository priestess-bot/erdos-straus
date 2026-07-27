import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_miss_state_menu_crt_escape",
    ROOT / "reproductions" / "type_i_pminusone_miss_state_menu_crt_escape.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIPMinusOneMissStateMenuCrtEscapeTests(unittest.TestCase):
    def test_observed_source_state_menu_has_a_reduced_core_escape(self):
        profile = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-pminusone-miss-state-menu-crt-escape-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit.run_audit(profile)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["fixed_source_state_count"], 127)
        self.assertEqual(actual["escape_residue"], 1)
        self.assertTrue(actual["coprime_to_combined_modulus"])
        self.assertEqual(actual["source_compatible_state_count"], 0)
        self.assertEqual(actual["direct_source_compatible_state_count"], 0)


if __name__ == "__main__":
    unittest.main()
