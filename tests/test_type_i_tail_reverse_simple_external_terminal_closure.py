import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_simple_external_terminal_closure",
    ROOT / "reproductions" / "type_i_tail_reverse_simple_external_terminal_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeITailReverseSimpleExternalTerminalClosureTests(unittest.TestCase):
    def test_low_complexity_branches_partition_and_terminate_all_tail_misses(self):
        profile = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-terminal-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        hybrid = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-surplus-external-hybrid-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-simple-external-terminal-closure-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_audit(profile, hybrid)
        self.assertEqual(actual, expected)
        self.assertEqual(
            actual["branch_counts"],
            {
                "linear_or_one_prime_reverse": 1_683,
                "shifted_quadratic_external": 8,
                "zero_offset_quadratic_external": 26,
            },
        )
        self.assertEqual((actual["unclosed_primes"], actual["unresolved_core_source_count"]), ([], 0))
        self.assertEqual(actual["maximum_selected_terminal_prime"], 1_453)


if __name__ == "__main__":
    unittest.main()
