import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_shifted_source_b1_selector_1m",
    ROOT / "reproductions" / "type_i_shifted_source_b1_selector_1m.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIShiftedSourceB1Selector1MTests(unittest.TestCase):
    def test_final_short_sources_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-shifted-source-b1-selector-1m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = audit.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["shift_histogram"], {"9": 2, "25": 1})
        self.assertEqual(actual["R_histogram"], {"19": 1, "31": 2})
        self.assertEqual(
            [
                (record["prime"], record["shift"], record["R"], record["E"])
                for record in actual["records"]
            ],
            [(297049, 25, 19, 476), (513529, 9, 31, 280), (710089, 9, 31, 280)],
        )

    def test_invalid_shifted_source_is_rejected(self):
        self.assertIsNone(audit.selector.shifted_source_b1_witness(297049, 25, 19, 1))


if __name__ == "__main__":
    unittest.main()
