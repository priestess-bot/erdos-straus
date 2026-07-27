import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_mixed_terminal_sparse_tail_600m",
    ROOT / "reproductions" / "type_i_mixed_terminal_sparse_tail_600m.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIMixedTerminalSparseTail600MTests(unittest.TestCase):
    def test_complete_sparse_family_rebuilds(self):
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-mixed-terminal-sparse-tail-600m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["family_count"],
                actual["ordinary_tail_hit_count"],
                actual["ordinary_tail_miss_count"],
                actual["even_source_captured_count"],
            ),
            (32394, 32320, 74, 74),
        )
        self.assertEqual(actual["even_source_misses"], [])
        self.assertEqual(actual["maximum_selected_gap"], 71)


if __name__ == "__main__":
    unittest.main()
