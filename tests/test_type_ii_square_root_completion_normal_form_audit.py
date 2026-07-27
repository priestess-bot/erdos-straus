import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_square_root_completion_normal_form_audit",
    ROOT / "reproductions" / "type_ii_square_root_completion_normal_form_audit.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIISquareRootCompletionNormalFormAuditTests(unittest.TestCase):
    def test_checked_two_hundred_sixty_two_thousand_layer_normalizes(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-tail-descent-262144.json"
        ).open(encoding="utf-8") as handle:
            result = audit.run_audit(json.load(handle))
        self.assertEqual(result["record_count"], 588_526)
        self.assertEqual(result["normal_form_count"], 588_526)
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["shared_gap_27_to_tail_gap_31_count"], 1_088)
        self.assertEqual(
            result["shared_gap_27_tail_gap_histogram"],
            {"31": 1_088, "35": 221, "39": 84, "47": 66, "59": 24, "63": 2, "71": 3, "79": 2},
        )


if __name__ == "__main__":
    unittest.main()
