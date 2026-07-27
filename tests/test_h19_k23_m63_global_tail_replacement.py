import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_m63_global_tail_replacement",
    ROOT / "reproductions" / "h19_k23_m63_global_tail_replacement.py",
)
assert SPEC and SPEC.loader
replacement = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = replacement
SPEC.loader.exec_module(replacement)


class H19K23M63GlobalTailReplacementTests(unittest.TestCase):
    def test_global_tail_menu_is_exact_in_the_replacement_window(self):
        self.assertEqual(replacement.global_tail_factor_and_gaps(), (165_600, [71, 79, 91, 95]))

    def test_checked_artifact_replaces_every_nonuniform_tail(self):
        with (
            ROOT / "reproductions" / "h19-k23-m63-global-tail-replacement-1048576.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_parameter_limit_exclusive"], 1_048_576)
        self.assertEqual(result["replacement_count"], 6)
        self.assertEqual(result["replacement_tail_gap_histogram"], {"71": 5, "79": 1})
        self.assertEqual(result["replacement_support_defect_histogram"], {"0": 1, "1": 4, "2": 1})
        self.assertEqual(result["globalized_record_count"], 5_081)
        self.assertEqual(
            result["globalized_support_defect_histogram_by_tail_gap"],
            {
                "31": {"0": 2287, "1": 1443},
                "35": {"1": 734, "2": 2},
                "39": {"1": 278, "2": 15},
                "47": {"0": 83, "1": 131, "2": 9},
                "59": {"0": 42, "1": 33, "2": 1},
                "71": {"0": 6, "1": 8, "2": 2},
                "79": {"0": 2, "1": 2, "2": 1},
                "91": {"1": 1},
                "95": {"2": 1},
            },
        )
        self.assertTrue(all(row["attempts"][-1]["support_defect"] is not None for row in result["replacements"]))


if __name__ == "__main__":
    unittest.main()
