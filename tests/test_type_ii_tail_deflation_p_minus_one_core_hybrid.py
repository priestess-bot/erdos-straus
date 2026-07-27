import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_deflation_p_minus_one_core_hybrid",
    ROOT / "reproductions" / "type_ii_tail_deflation_p_minus_one_core_hybrid.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIITailDeflationPMinusOneCoreHybridTests(unittest.TestCase):
    def test_two_branch_core_closure_through_one_hundred_thousand(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-p-minus-one-core-hybrid-100k-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 100_000)
        self.assertEqual(result["core_prime_count"], 1_181)
        self.assertEqual(result["tail_deflation_strict_lift_count"], 1_179)
        self.assertEqual(result["tail_deflation_misses"], [67_369, 85_369])
        self.assertEqual(result["p_minus_one_residual_count"], 2)
        self.assertEqual(result["p_minus_one_strict_lift_count"], 2)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            result["tail_deflation_strict_lift_count"]
            + result["p_minus_one_strict_lift_count"],
            result["core_prime_count"],
        )


if __name__ == "__main__":
    unittest.main()
