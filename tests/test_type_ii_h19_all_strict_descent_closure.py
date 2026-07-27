import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_all_strict_descent_closure",
    ROOT / "reproductions" / "type_ii_h19_all_strict_descent_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class H19AllStrictDescentClosureTests(unittest.TestCase):
    def test_artifact_rebuilds_from_tail_and_external_profiles(self):
        with (ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json").open(encoding="utf-8") as handle:
            tail_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-targeted-quadratic-descent-1b-results.json").open(encoding="utf-8") as handle:
            external_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-all-strict-descent-closure-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(tail_payload, external_payload), checked)

    def test_every_h19_residual_has_a_strict_descent(self):
        with (ROOT / "reproductions" / "type-ii-h19-all-strict-descent-closure-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["two_tail_descent_count"], 662)
        self.assertEqual(result["adaptive_external_fallback_count"], 2)
        self.assertEqual(result["unclosed_primes"], [])
        self.assertEqual(
            result["adaptive_external_fallback_records"],
            [
                {
                    "prime": 225_289,
                    "adaptive_external_descent": {
                        "source_denominator": 197_128,
                        "k": 2,
                        "q": 7,
                        "factor": 41,
                        "gap": 47,
                    },
                },
                {
                    "prime": 2_707_609,
                    "adaptive_external_descent": {
                        "source_denominator": 2_594_792,
                        "k": 6,
                        "q": 23,
                        "factor": 344,
                        "gap": 359,
                    },
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
