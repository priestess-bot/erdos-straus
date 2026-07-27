import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "weighted_cyclic_reverse_bridge",
    ROOT / "reproductions" / "weighted_cyclic_reverse_bridge.py",
)
assert SPEC and SPEC.loader
bridge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bridge
SPEC.loader.exec_module(bridge)


class WeightedCyclicReverseBridgeTests(unittest.TestCase):
    def test_known_noncore_forward_example_reverses(self):
        lift = bridge.reverse_lift(31, (16, 248, 16), 1, 2)
        self.assertIsNotNone(lift)
        assert lift is not None
        self.assertEqual(lift["source_denominator"], 15)
        self.assertEqual(lift["source_solution"], [4, 120, 120])

    def test_core_repeated_tail_witness_reverses(self):
        lift = bridge.reverse_lift(2_161, (25_932, 1_192_872, 552), 1, 49)
        self.assertIsNotNone(lift)
        assert lift is not None
        self.assertEqual(lift["source_denominator"], 1_103)
        self.assertEqual(lift["source_solution"], [276, 608_856, 608_856])

    def test_first_composite_escape_ac_box_has_no_bridge(self):
        result = bridge.ac_reverse_audit(2_451_289, 14, 20)
        self.assertEqual(result["target_solutions"], 21)
        self.assertEqual(result["reverse_weighted_cyclic_lifts"], 0)


if __name__ == "__main__":
    unittest.main()
