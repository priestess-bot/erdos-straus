import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_shifted_source_small_b_selector_10m",
    ROOT / "reproductions" / "type_i_shifted_source_small_b_selector_10m.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIShiftedSourceSmallBSelector10MTests(unittest.TestCase):
    def test_final_short_sources_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-shifted-source-small-b-selector-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["record_count"], 7)
        self.assertEqual(actual["maximum_selected_shift"]["shift"], 263)
        self.assertEqual(actual["maximum_selected_B"]["normal_form"][1], 3)
        self.assertEqual(
            [(record["prime"], record["shift"], record["R"], record["normal_form"][1]) for record in actual["records"]],
            [
                (1083289, 25, 131, 1),
                (1103449, 25, 215, 1),
                (2469289, 9, 39, 1),
                (3389929, 49, 191, 1),
                (3942409, 263, 95, 2),
                (4762489, 9, 131, 3),
                (5770249, 3, 19, 1),
            ],
        )


if __name__ == "__main__":
    unittest.main()
