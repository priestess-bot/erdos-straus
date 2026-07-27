import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_tail_deflation_short_closure",
    ROOT / "reproductions" / "type_ii_h19_tail_deflation_short_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class H19TailDeflationShortClosureTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_h19_ac_profile(self):
        with (ROOT / "reproductions" / "type-ii-h19-residual-ac-profile-1b-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(input_payload), checked)

    def test_two_tail_descent_leaves_exactly_two_ac_fallbacks(self):
        with (ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["h19_residual_count"], 664)
        self.assertEqual(result["tail_deflation_count"], 662)
        self.assertEqual(result["tail_deflation_missing_primes"], [225_289, 2_707_609])
        self.assertEqual(result["direct_ac_fallback_count"], 2)
        self.assertEqual(result["maximum_minimal_tail_deflation_gap"], 263)
        self.assertEqual(
            {
                record["prime"]: record["direct_ac_witness"]
                for record in result["direct_ac_fallback_records"]
            },
            {
                225_289: {"radius": 4, "a": 4, "c": 2, "k": 81, "h": 2591, "gap": 87, "divisor": 32},
                2_707_609: {"radius": 5, "a": 4, "c": 5, "k": 2, "h": 159, "gap": 17031, "divisor": 80},
            },
        )


if __name__ == "__main__":
    unittest.main()
