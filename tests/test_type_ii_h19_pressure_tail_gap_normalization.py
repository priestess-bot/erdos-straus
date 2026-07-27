import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_pressure_tail_gap_normalization",
    ROOT / "reproductions" / "type_ii_h19_pressure_tail_gap_normalization.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIIH19PressureTailGapNormalizationTests(unittest.TestCase):
    def test_pressure_tails_recover_the_certified_gaps(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-pressure-tail-gap-normalization-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["record_count"], 4)
        self.assertEqual(
            [(record["r"], record["gap"]) for record in result["records"]],
            [(103, 983), (31, 191), (31, 11), (15, 375)],
        )


if __name__ == "__main__":
    unittest.main()
