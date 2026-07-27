import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_shared_gap_escape",
    ROOT / "reproductions" / "type_ii_shared_gap_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class TypeIISharedGapEscapeTests(unittest.TestCase):
    def test_rejects_noncore_or_nonprime_input(self):
        with self.assertRaises(ValueError):
            escape.run_audit(5, 3)
        with self.assertRaises(ValueError):
            escape.run_audit(49, 3)

    def test_checked_half_million_gap_artifact_has_no_witness(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-shared-gap-escape-p33011449-500k-results.json"
        ).open(encoding="utf-8") as handle:
            audit = json.load(handle)
        self.assertEqual(audit["prime"], 33_011_449)
        self.assertEqual(audit["gap_cap"], 500_000)
        self.assertEqual(audit["last_scanned_gap"], 499_999)
        self.assertEqual(audit["legal_gap_count"], 125_000)
        self.assertIsNone(audit["witness"])


if __name__ == "__main__":
    unittest.main()
