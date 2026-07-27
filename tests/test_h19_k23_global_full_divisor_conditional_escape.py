import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_global_full_divisor_conditional_escape",
    ROOT / "reproductions" / "h19_k23_global_full_divisor_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23GlobalFullDivisorConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-base-only-prime-obstruction-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-global-full-divisor-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(pressure), checked)

    def test_every_canonical_tail_has_no_eventual_full_divisor_witness(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-full-divisor-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 955_643_834_512_728_001)
        self.assertEqual(result["global_tail_count"], 72)
        self.assertEqual(result["inherited_affine_prime_form_count"], 73)
        self.assertEqual(result["full_divisor_witness_miss_count"], 0)
        self.assertEqual(len(result["rows"]), 72)
        self.assertTrue(all(row["full_divisor_witness_count"] == 0 for row in result["rows"]))


if __name__ == "__main__":
    unittest.main()
