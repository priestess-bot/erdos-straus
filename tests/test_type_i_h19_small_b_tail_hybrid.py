import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_small_b_tail_hybrid",
    ROOT / "reproductions" / "type_i_h19_small_b_tail_hybrid.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeIH19SmallBTailHybridTests(unittest.TestCase):
    def test_checked_twenty_million_hybrid_summary(self):
        with (
            ROOT / "reproductions" / "type-i-h19-small-b-tail-hybrid-20m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 20_000_000)
        self.assertEqual(result["h19_residual_count"], 65)
        self.assertEqual(result["small_gap_cap"], 239)
        self.assertEqual(result["small_box_recovered_count"], 61)
        self.assertEqual(result["extended_gap_cap"], 999)
        self.assertEqual(result["b_cap"], 4)
        self.assertEqual(result["extended_box_recovered_count"], 65)
        self.assertEqual(result["extended_box_misses"], [])
        self.assertEqual(result["maximum_first_extended_gap"], 743)
        self.assertEqual(
            [record["prime"] for record in result["extended_only_records"]],
            [7_378_849, 8_955_769, 11_910_361, 12_180_169],
        )


if __name__ == "__main__":
    unittest.main()
