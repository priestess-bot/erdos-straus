import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_surplus_external_hybrid",
    ROOT / "reproductions" / "type_i_tail_reverse_surplus_external_hybrid.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeITailReverseSurplusExternalHybridTests(unittest.TestCase):
    def test_every_multi_prime_surplus_residual_has_an_independent_external_descent(self):
        inputs = [
            "type-i-tail-reverse-single-surplus-500m-results.json",
            "type-ii-tail-deflation-external-boundary-500m-results.json",
            "type-ii-tail-shifted-quadratic-offset-profile-500m-results.json",
        ]
        profile, external, offset = [
            json.loads((ROOT / "reproductions" / filename).read_text(encoding="utf-8"))
            for filename in inputs
        ]
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-surplus-external-hybrid-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = hybrid.run_audit(profile, external, offset)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["input_multi_prime_boundary_count"],
                actual["zero_offset_quadratic_external_count"],
                actual["shifted_quadratic_external_count"],
                actual["unclosed_primes"],
            ),
            (34, 26, 8, []),
        )
        self.assertEqual(actual["shifted_offset_histogram"], {"9": 4, "25": 4})


if __name__ == "__main__":
    unittest.main()
