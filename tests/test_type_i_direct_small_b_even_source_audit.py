import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_direct_small_b_even_source_audit",
    ROOT / "reproductions" / "type_i_direct_small_b_even_source_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIDirectSmallBEvenSourceAuditTests(unittest.TestCase):
    def test_direct_target_level_small_b_stages_close_both_profiles(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        tail = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-direct-small-b-even-source-audit-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit(h19, tail)
        self.assertEqual(actual, expected)
        h19_result, tail_result = actual["profiles"]
        self.assertEqual([stage["captured_count"] for stage in h19_result["stages"]], [664])
        self.assertEqual([stage["captured_count"] for stage in tail_result["stages"]], [1713, 3, 1])
        self.assertEqual((h19_result["misses"], tail_result["misses"]), ([], []))
        self.assertEqual((h19_result["maximum_selected_gap"], tail_result["maximum_selected_gap"]), (91, 215))


if __name__ == "__main__":
    unittest.main()
