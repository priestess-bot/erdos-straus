import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_overflow_gap_tradeoff",
    ROOT / "reproductions" / "type_i_overflow_gap_tradeoff.py",
)
assert SPEC and SPEC.loader
tradeoff = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tradeoff
SPEC.loader.exec_module(tradeoff)


class TypeIOverflowGapTradeoffTests(unittest.TestCase):
    def test_first_b_one_certificate_for_first_pressure_point(self):
        prime = 1_282_009
        spf = tradeoff.short_certificate.smallest_prime_factors((prime + 600) // 4 + 1)
        witness = tradeoff.first_b_one_certificate(prime, spf, 599)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["gap"], 583)
        self.assertEqual(witness["target_divisor"], 40_081)

    def test_checked_one_hundred_million_exception_summary(self):
        with (
            ROOT / "reproductions" / "type-i-overflow-gap-tradeoff-100m-m999-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_prime_limit"], 100_000_000)
        self.assertEqual(result["gap_cap"], 999)
        self.assertEqual(result["non_b_one_count"], 11)
        self.assertEqual(result["b_one_recovered_count"], 11)
        self.assertEqual(result["b_one_misses"], [])
        self.assertEqual(result["maximum_first_b_one_gap"], 775)


if __name__ == "__main__":
    unittest.main()
