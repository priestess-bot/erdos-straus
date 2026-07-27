import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_hybrid_window_descent_audit",
    ROOT / "reproductions" / "type_ii_hybrid_window_descent_audit.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeIIHybridWindowDescentAuditTests(unittest.TestCase):
    def test_small_hybrid_audit(self):
        result = hybrid.run_audit(100_000, 16)
        self.assertEqual(result["direct_window_residual_count"], 0)
        self.assertEqual(result["records"], [])
        self.assertEqual(result["hybrid_uncovered"], [])

    def test_checked_ten_million_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-hybrid-window20-descent-10m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["direct_window_core_prime_count"], 82_887)
        self.assertEqual(result["direct_window_captured_count"], 82_886)
        self.assertEqual(result["hybrid_uncovered"], [])
        self.assertEqual(len(result["records"]), 1)
        record = result["records"][0]
        self.assertEqual(record["prime"], 8_803_369)
        self.assertEqual(record["complete_fixed_factor_candidate_gap_count"], 3_929)
        self.assertEqual(record["fixed_factor_traps"], [])
        self.assertEqual(
            record["classification"], ["quadratic-external-strict-descent"]
        )
        descent = record["quadratic_external_source_descent"]
        self.assertEqual(descent["source_denominator"], 8_768_435)
        self.assertEqual(descent["certificate"]["gap"], 271_151)


if __name__ == "__main__":
    unittest.main()
