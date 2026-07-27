import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_external_ac4_closure_100m",
    ROOT / "reproductions" / "type_ii_tail_external_ac2_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailExternalAC4Closure100MTests(unittest.TestCase):
    def test_hundred_million_artifact_rebuilds(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-100m-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-tail-external-ac4-closure-100m-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(input_payload, 4), checked)

    def test_radius_four_closes_every_hundred_million_pressure_point(self):
        with (ROOT / "reproductions" / "type-ii-tail-external-ac4-closure-100m-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 719_781)
        self.assertEqual(result["two_tail_descent_count"], 719_281)
        self.assertEqual(result["quadratic_factor_descent_count_on_tail_misses"], 459)
        self.assertEqual(result["tail_quadratic_miss_count"], 41)
        self.assertEqual(result["direct_ac_captured_count"], 41)
        self.assertEqual(result["direct_ac_missing_primes"], [])
        self.assertEqual(
            Counter(record["direct_ac_witness"]["radius"] for record in result["records"]),
            Counter({1: 16, 2: 21, 3: 2, 4: 2}),
        )
        self.assertEqual(
            [record["prime"] for record in result["records"] if record["direct_ac_witness"]["radius"] == 4],
            [56_040_889, 63_641_209],
        )


if __name__ == "__main__":
    unittest.main()
