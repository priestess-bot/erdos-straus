import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_tail_reverse_two_tail_full_closure",
    ROOT / "reproductions" / "type_ii_tail_reverse_two_tail_full_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIITailReverseTwoTailFullClosureTests(unittest.TestCase):
    def test_five_hundred_million_core_population_has_no_unclosed_tail_state(self):
        tail = json.loads((ROOT / "reproductions" / "type-ii-tail-deflation-500m-full-results.json").read_text(encoding="utf-8"))
        reverse = json.loads((ROOT / "reproductions" / "type-ii-tail-reverse-two-tail-500m-all-misses-results.json").read_text(encoding="utf-8"))
        expected = json.loads((ROOT / "reproductions" / "type-ii-tail-reverse-two-tail-full-closure-500m-results.json").read_text(encoding="utf-8"))
        actual = closure.run_audit(tail, reverse)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["core_prime_count"],
                actual["ordinary_type_ii_tail_descent_count"],
                actual["reverse_two_tail_descent_count"],
                actual["unclosed_count"],
            ),
            (3_292_848, 3_291_131, 1_717, 0),
        )
        self.assertEqual(actual["maximum_reverse_gap"], 127)
