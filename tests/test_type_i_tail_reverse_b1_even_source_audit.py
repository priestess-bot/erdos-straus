import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_b1_even_source_audit",
    ROOT / "reproductions" / "type_i_tail_reverse_b1_even_source_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeITailReverseB1EvenSourceAuditTests(unittest.TestCase):
    def test_complete_b1_boundary_rebuilds(self):
        tail = json.loads(
            (
                ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-b1-even-source-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit.run_audit(tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["ordinary_tail_miss_count"],
                actual["captured_count"],
                len(actual["misses"]),
            ),
            (1717, 1713, 4),
        )
        self.assertEqual(
            actual["misses"], [39407449, 63332329, 172657489, 193288489]
        )
        self.assertEqual(actual["b1_normal_forms_exhaustively_checked"], 15071)
        self.assertEqual(actual["strict_reverse_lifts_exhaustively_checked"], 126178)


if __name__ == "__main__":
    unittest.main()
