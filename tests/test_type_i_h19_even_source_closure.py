import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_even_source_closure",
    ROOT / "reproductions" / "type_i_h19_even_source_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIH19EvenSourceClosureTests(unittest.TestCase):
    def test_h19_source_free_residuals_rebuild_to_even_sources(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-closure-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_audit(h19)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["h19_source_free_count"], actual["even_source_captured_count"], actual["even_source_misses"], actual["maximum_selected_gap"]),
            (664, 664, [], 91),
        )


if __name__ == "__main__":
    unittest.main()
