import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_linear_e_tail_deflation_hybrid_closure",
    ROOT / "reproductions" / "type_i_h19_linear_e_tail_deflation_hybrid_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIH19LinearETailDeflationHybridClosureTests(unittest.TestCase):
    def test_full_box_linear_e_and_type_ii_tail_deflation_partition_h19(self):
        linear = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        tail = json.loads(
            (ROOT / "reproductions" / "type-ii-h19-tail-deflation-short-closure-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-linear-e-tail-deflation-hybrid-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_closure(linear, tail)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["h19_residual_count"], actual["linear_e_full_box_descent_count"], actual["tail_deflation_fallback_count"]),
            (664, 622, 42),
        )
        self.assertEqual(actual["unclosed_primes"], [])
        self.assertEqual(actual["maximum_tail_deflation_gap_on_linear_residual"], 119)
        self.assertEqual(
            {record["prime"] for record in actual["records"]},
            set(linear["unbounded_b_linear_e_misses"]),
        )


if __name__ == "__main__":
    unittest.main()
