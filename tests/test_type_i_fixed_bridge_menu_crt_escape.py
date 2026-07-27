import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_fixed_bridge_menu_crt_escape",
    ROOT / "reproductions" / "type_i_fixed_bridge_menu_crt_escape.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIFixedBridgeMenuCrtEscapeTests(unittest.TestCase):
    def test_source_escape_audit_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-fixed-bridge-menu-crt-escape-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["positive_odd_state_count"], 128)
        self.assertEqual(actual["combined_modulus"], 781_779_462_544_080)
        self.assertEqual(actual["escape_residue"], 73)
        self.assertTrue(actual["coprime_to_combined_modulus"])
        self.assertEqual(actual["source_compatible_state_count"], 0)
        self.assertEqual(actual["direct_source_compatible_state_count"], 0)


if __name__ == "__main__":
    unittest.main()
