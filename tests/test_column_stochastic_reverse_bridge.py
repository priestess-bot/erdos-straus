import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "column_stochastic_reverse_bridge",
    ROOT / "reproductions" / "column_stochastic_reverse_bridge.py",
)
assert SPEC and SPEC.loader
bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bridge
SPEC.loader.exec_module(bridge)


class ColumnStochasticReverseBridgeTests(unittest.TestCase):
    def test_cyclic_doubly_stochastic_transport_is_included(self):
        matrix = ((1, 1, 0), (0, 1, 1), (1, 0, 1))
        lift = bridge.reverse_lift(31, (16, 248, 16), matrix, 2)
        self.assertIsNotNone(lift)
        assert lift is not None
        self.assertEqual(lift["source_denominator"], 15)
        self.assertEqual(lift["source_solution"], [4, 120, 120])

    def test_complete_column_stochastic_counts_through_six(self):
        self.assertEqual(
            {
                denominator: len(bridge.matrices_at_denominator(denominator))
                for denominator in range(2, 7)
            },
            {2: 6, 3: 102, 4: 720, 5: 3006, 6: 9192},
        )

    def test_escape_point_has_no_low_denominator_column_stochastic_bridge(self):
        result = bridge.ac_reverse_audit(2_451_289, 14, 6)
        self.assertEqual(result["target_solutions"], 21)
        self.assertEqual(result["matrix_count"], 13_026)
        self.assertEqual(result["candidate_profiles"], 273_546)
        self.assertEqual(result["reverse_column_stochastic_lifts"], 0)


if __name__ == "__main__":
    unittest.main()
