import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("type_i_h19_k6_after_k2_boundary", ROOT / "reproductions" / "type_i_h19_k6_after_k2_boundary.py")
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)

class TypeIH19K6AfterK2BoundaryTests(unittest.TestCase):
    def test_exact_k6_second_scale_profile_rebuilds(self):
        k2 = json.loads((ROOT / "reproductions" / "type-i-k2-mod7-even-source-audit-1b-results.json").read_text(encoding="utf-8"))
        expected = json.loads((ROOT / "reproductions" / "type-i-h19-k6-after-k2-boundary-1b-results.json").read_text(encoding="utf-8"))
        actual = audit.run_audit(k2)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["input_k2_subgroup_boundary_count"], actual["k6_terminal_count"], len(actual["k6_misses"])), (119, 48, 71))

if __name__ == "__main__":
    unittest.main()
