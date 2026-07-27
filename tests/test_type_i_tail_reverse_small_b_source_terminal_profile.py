import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_small_b_source_terminal_profile",
    ROOT / "reproductions" / "type_i_tail_reverse_small_b_source_terminal_profile.py",
)
assert SPEC and SPEC.loader
terminal = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = terminal
SPEC.loader.exec_module(terminal)


class TypeITailReverseSmallBSourceTerminalProfileTests(unittest.TestCase):
    def test_every_selected_source_has_a_non_core_prime_terminal_factor(self):
        profile = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-small-b5-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-small-b-source-terminal-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = terminal.run_profile(profile)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["reverse_edge_count"], actual["unresolved_core_source_count"]), (1_717, 0))
        self.assertEqual(actual["maximum_selected_terminal_prime"], 3_299)
        for record in actual["records"]:
            self.assertNotEqual(record["terminal_prime_mod_24"], 1)
            self.assertEqual(
                record["source_denominator"],
                record["terminal_prime"] * record["scaling_multiplier"],
            )


if __name__ == "__main__":
    unittest.main()
