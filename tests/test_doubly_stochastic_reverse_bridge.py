import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "doubly_stochastic_reverse_bridge",
    ROOT / "reproductions" / "doubly_stochastic_reverse_bridge.py",
)
assert SPEC and SPEC.loader
bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bridge
SPEC.loader.exec_module(bridge)


class DoublyStochasticReverseBridgeTests(unittest.TestCase):
    def test_known_cyclic_transport_reverses(self):
        matrix = ((1, 1, 0), (0, 1, 1), (1, 0, 1))
        lift = bridge.reverse_lift(31, (16, 248, 16), matrix, 2)
        self.assertIsNotNone(lift)
        assert lift is not None
        self.assertEqual(lift["source_denominator"], 15)
        self.assertEqual(lift["source_solution"], [4, 120, 120])

    def test_reduced_genuine_matrix_counts_through_ten(self):
        self.assertEqual(
            {
                denominator: len(bridge.matrices_at_denominator(denominator))
                for denominator in range(2, 11)
            },
            {
                2: 6,
                3: 12,
                4: 72,
                5: 180,
                6: 264,
                7: 588,
                8: 834,
                9: 1278,
                10: 1848,
            },
        )

    def test_first_composite_escape_low_denominator_box_has_no_bridge(self):
        result = bridge.ac_reverse_audit(2_451_289, 14, 10)
        self.assertEqual(result["target_solutions"], 21)
        self.assertEqual(result["matrix_count"], 5_082)
        self.assertEqual(result["candidate_profiles"], 106_722)
        self.assertEqual(result["reverse_doubly_stochastic_lifts"], 0)


if __name__ == "__main__":
    unittest.main()
