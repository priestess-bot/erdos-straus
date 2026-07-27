import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_two_layer_divisor_pair_selector",
    ROOT / "reproductions" / "type_i_two_layer_divisor_pair_selector.py",
)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class TypeITwoLayerDivisorPairSelectorTests(unittest.TestCase):
    @staticmethod
    def dense_records():
        return json.loads(
            (
                ROOT / "reproductions" / "type-i-mixed-terminal-dense-500m-600m-results.json"
            ).read_text(encoding="utf-8")
        )["type_i_even_terminal_bridge_records"]

    def test_two_ordinary_pairs_reconstruct_all_dense_terminal_bridges(self):
        for record in self.dense_records():
            prime = int(record["prime"])
            stored = record["type_i_even_witness"]
            target_a, target_b, target_c = (
                int(value) for value in stored["normal_form"]
            )
            target_divisor = target_b * target_b * target_c
            gap = int(stored["gap"])
            R = (4 * target_divisor + 1) // gap
            x = (prime + gap) // 4
            K = x * R - target_divisor
            bridge_factor = int(stored["reverse_two_tail_lift"]["bridge_divisor"]) // (
                prime * prime
            )
            L = 2 * K
            common = math.gcd(bridge_factor, L)
            bridge_u, bridge_v = bridge_factor // common, L // common

            witness = selector.terminal_witness_from_divisor_pairs(
                prime, gap, target_a, target_b, bridge_u, bridge_v
            )
            self.assertIsNotNone(witness)
            assert witness is not None
            self.assertEqual(witness["target_c"], target_c)
            self.assertEqual(witness["target_divisor"], target_divisor)
            self.assertEqual(list(witness["target_solution"]), stored["target_solution"])
            self.assertEqual(list(witness["source_solution"]), stored["source_solution"])
            self.assertEqual(
                witness["source_denominator"],
                stored["reverse_two_tail_lift"]["source_denominator"],
            )

    def test_invalid_pair_residues_are_rejected(self):
        record = self.dense_records()[0]
        prime = int(record["prime"])
        stored = record["type_i_even_witness"]
        target_a, target_b, target_c = (
            int(value) for value in stored["normal_form"]
        )
        gap = int(stored["gap"])
        target_divisor = target_b * target_b * target_c
        R = (4 * target_divisor + 1) // gap
        x = (prime + gap) // 4
        K = x * R - target_divisor
        bridge_factor = int(stored["reverse_two_tail_lift"]["bridge_divisor"]) // (
            prime * prime
        )
        L = 2 * K
        common = math.gcd(bridge_factor, L)
        bridge_u, bridge_v = bridge_factor // common, L // common

        self.assertIsNone(
            selector.terminal_witness_from_divisor_pairs(
                prime, gap, target_a + 1, target_b, bridge_u, bridge_v
            )
        )
        self.assertIsNone(
            selector.terminal_witness_from_divisor_pairs(
                prime, gap, target_a, target_b, bridge_u + 1, bridge_v
            )
        )


if __name__ == "__main__":
    unittest.main()
