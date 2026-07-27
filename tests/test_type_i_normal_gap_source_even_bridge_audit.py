import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_normal_gap_source_even_bridge_audit",
    ROOT / "reproductions" / "type_i_normal_gap_source_even_bridge_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeINormalGapSourceEvenBridgeAuditTests(unittest.TestCase):
    def test_complete_tail_miss_boundary_rebuilds(self):
        tail = json.loads(
            (
                ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-normal-gap-source-even-bridge-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit.run_audit(tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["gap_source_captured_count"],
                len(actual["gap_source_misses"]),
            ),
            (1717, 21, 1696),
        )
        self.assertEqual(actual["normal_forms_exhaustively_checked"], 78215)
        self.assertEqual(actual["maximum_selected_gap"], 119)


if __name__ == "__main__":
    unittest.main()
