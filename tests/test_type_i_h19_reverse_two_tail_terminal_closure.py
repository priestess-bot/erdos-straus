import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_reverse_two_tail_terminal_closure",
    ROOT / "reproductions" / "type_i_h19_reverse_two_tail_terminal_closure.py",
)
assert SPEC and SPEC.loader
closure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = closure
SPEC.loader.exec_module(closure)


class TypeIH19ReverseTwoTailTerminalClosureTests(unittest.TestCase):
    def test_every_stored_h19_residual_has_a_bounded_terminal_reverse_lift(self):
        h19 = json.loads(
            (ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-reverse-two-tail-terminal-b1-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = closure.run_closure(h19, 127, 1)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["h19_residual_count"], actual["captured_count"], actual["misses"]), (664, 664, []))
        self.assertEqual(actual["maximum_selected_gap"], 79)
        self.assertEqual(actual["first_hit_b_counts"], {"1": 664})
        self.assertEqual((actual["unresolved_core_source_count"], actual["maximum_selected_terminal_prime"]), (0, 2417))
        for record in actual["records"]:
            self.assertNotEqual(record["terminal_prime_mod_24"], 1)
            self.assertEqual(
                record["reverse_two_tail_lift"]["source_denominator"],
                record["terminal_prime"] * record["scaling_multiplier"],
            )


if __name__ == "__main__":
    unittest.main()
