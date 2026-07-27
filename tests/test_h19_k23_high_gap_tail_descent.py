import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_high_gap_tail_descent",
    ROOT / "reproductions" / "h19_k23_high_gap_tail_descent.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class H19K23HighGapTailDescentTests(unittest.TestCase):
    def test_every_high_gap_shared_record_has_an_ordinary_tail_descent(self):
        with (
            ROOT / "reproductions" / "h19-k23-shared-selector-audit-16384.json"
        ).open(encoding="utf-8") as handle:
            result = audit.run_audit(json.load(handle), 15)
        self.assertEqual(result["input_parameter_limit_exclusive"], 16_384)
        self.assertEqual(result["minimum_shared_gap"], 15)
        self.assertEqual(result["selected_record_count"], 4_562)
        self.assertEqual(result["ordinary_tail_descent_count"], 4_562)
        self.assertEqual(result["ordinary_tail_descent_misses"], [])
        summary = Counter(
            (
                row["shared_selector_gap"],
                row["ordinary_tail_witness"]["gap"],
            )
            for row in result["records"]
        )
        self.assertEqual(
            summary,
            Counter(
                {
                    (15, 15): 2_447,
                    (19, 19): 1_117,
                    (23, 23): 523,
                    (27, 31): 73,
                    (27, 35): 17,
                    (27, 39): 4,
                    (27, 47): 8,
                    (27, 71): 1,
                    (31, 31): 256,
                    (35, 35): 57,
                    (39, 39): 25,
                    (47, 47): 22,
                    (43, 47): 1,
                    (43, 71): 1,
                    (55, 59): 1,
                    (59, 59): 7,
                    (71, 71): 2,
                }
            ),
        )


if __name__ == "__main__":
    unittest.main()
