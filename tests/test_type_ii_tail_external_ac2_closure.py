import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_external_ac2_closure",
    ROOT / "reproductions" / "type_ii_tail_external_ac2_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailExternalAC2ClosureTests(unittest.TestCase):
    def test_artifact_rebuilds_from_the_quadratic_external_miss_profile(self):
        with (ROOT / "reproductions" / "type-ii-tail-deflation-external-boundary-10m-results.json").open(encoding="utf-8") as handle:
            input_payload = json.load(handle)
        with (ROOT / "reproductions" / "type-ii-tail-external-ac2-closure-10m-results.json").open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(closure.run_audit(input_payload, 2), checked)

    def test_radius_two_ac_closes_every_tail_and_quadratic_external_miss(self):
        with (ROOT / "reproductions" / "type-ii-tail-external-ac2-closure-10m-results.json").open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 82_887)
        self.assertEqual(result["two_tail_descent_count"], 82_803)
        self.assertEqual(result["mixed_factor_descent_count_on_tail_misses"], 77)
        self.assertEqual(result["quadratic_factor_descent_count_on_tail_misses"], 77)
        self.assertEqual(result["tail_quadratic_miss_count"], 7)
        self.assertEqual(result["direct_ac_captured_count"], 7)
        self.assertEqual(result["direct_ac_missing_primes"], [])
        self.assertEqual(
            {
                record["prime"]: (record["direct_ac_witness"]["a"], record["direct_ac_witness"]["c"])
                for record in result["records"]
            },
            {
                214_729: (1, 2),
                297_049: (1, 1),
                878_089: (1, 1),
                1_511_449: (1, 1),
                3_942_409: (1, 2),
                5_478_169: (1, 1),
                6_294_649: (1, 2),
            },
        )


if __name__ == "__main__":
    unittest.main()
