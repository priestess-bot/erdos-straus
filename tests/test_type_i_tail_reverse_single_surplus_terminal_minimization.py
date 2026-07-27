import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_single_surplus_terminal_minimization",
    ROOT / "reproductions" / "type_i_tail_reverse_single_surplus_terminal_minimization.py",
)
assert SPEC and SPEC.loader
terminal_min = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = terminal_min
SPEC.loader.exec_module(terminal_min)


class TypeITailReverseSingleSurplusTerminalMinimizationTests(unittest.TestCase):
    def test_representative_odd_terminal_minima(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-single-surplus-terminal-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        records = {record["prime"]: record["selected_edge"] for record in expected["records"]}
        for prime in (6_294_649, 217_380_409):
            witness, _, _ = terminal_min.best_terminal_edge(prime, 127)
            self.assertEqual(witness, records[prime])
        self.assertEqual(records[217_380_409]["terminal_prime"], 1_453)
        self.assertEqual(expected["maximum_selected_terminal_prime"], 1_453)


if __name__ == "__main__":
    unittest.main()
