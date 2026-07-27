import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_external_ac5_closure_500m",
    ROOT / "reproductions" / "type_ii_tail_external_ac2_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailExternalAC5Closure500MTests(unittest.TestCase):
    def test_half_billion_artifact_rebuilds(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-tail-deflation-external-boundary-500m-results.json"
        ).open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (
            ROOT
            / "reproductions"
            / "type-ii-tail-external-ac5-closure-500m-results.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(input_payload, 5), checked)

    def test_radius_five_is_minimal_on_the_stored_pressure_set(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-tail-external-ac5-closure-500m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)

        self.assertEqual(result["core_prime_count"], 3_292_848)
        self.assertEqual(result["two_tail_descent_count"], 3_291_131)
        self.assertEqual(result["quadratic_factor_descent_count_on_tail_misses"], 1_593)
        self.assertEqual(result["tail_quadratic_miss_count"], 124)
        self.assertEqual(result["direct_ac_captured_count"], 124)
        self.assertEqual(result["direct_ac_missing_primes"], [])
        self.assertEqual(
            Counter(record["direct_ac_witness"]["radius"] for record in result["records"]),
            Counter({1: 52, 2: 60, 3: 8, 4: 3, 5: 1}),
        )

        self.assertIsNone(closure.direct_ac_witness(373_949_689, 4))
        self.assertEqual(
            closure.direct_ac_witness(373_949_689, 5),
            {
                "radius": 5,
                "a": 4,
                "c": 5,
                "k": 1_955,
                "h": 156_399,
                "gap": 2_391,
                "divisor": 80,
                "x": 93_488_020,
                "y": 14_621_432_839_900,
                "z": 17_086_610_072_065_349_975,
            },
        )


if __name__ == "__main__":
    unittest.main()
