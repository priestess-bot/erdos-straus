import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_target_divisor_terminal_selector",
    ROOT / "reproductions" / "type_i_target_divisor_terminal_selector.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class TypeITargetDivisorTerminalSelectorTests(unittest.TestCase):
    @staticmethod
    def dense_records():
        return json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )["type_i_even_terminal_bridge_records"]

    def test_two_target_factors_reconstruct_all_dense_even_terminal_bridges(self):
        for record in self.dense_records():
            prime = int(record["prime"])
            stored = record["type_i_even_witness"]
            A, B, C = (int(value) for value in stored["normal_form"])
            target_divisor = B * B * C
            bridge_divisor = int(stored["reverse_two_tail_lift"]["bridge_divisor"])
            self.assertEqual(bridge_divisor % (prime * prime), 0)
            witness = selector.terminal_witness_from_target_divisors(
                prime,
                int(stored["gap"]),
                target_divisor,
                bridge_divisor // (prime * prime),
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(list(witness["target_solution"]), stored["target_solution"])
            self.assertEqual(list(witness["source_solution"]), stored["source_solution"])
            self.assertEqual(
                witness["source_denominator"],
                stored["reverse_two_tail_lift"]["source_denominator"],
            )

    def test_nonterminal_or_noncertificate_factors_are_rejected(self):
        record = self.dense_records()[0]
        prime = int(record["prime"])
        stored = record["type_i_even_witness"]
        _, B, C = (int(value) for value in stored["normal_form"])
        e = B * B * C
        E = int(stored["reverse_two_tail_lift"]["bridge_divisor"]) // (prime * prime)
        self.assertIsNone(selector.terminal_witness_from_target_divisors(prime, int(stored["gap"]), e, E + 1))
        self.assertIsNone(selector.terminal_witness_from_target_divisors(prime, int(stored["gap"]), e + 1, E))


if __name__ == "__main__":
    unittest.main()
