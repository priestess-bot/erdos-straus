import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_initial_q_one_root_dispatch",
    ROOT / "reproductions" / "type_ii_initial_q_one_root_dispatch.py",
)
assert SPEC and SPEC.loader
dispatch = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = dispatch
SPEC.loader.exec_module(dispatch)


class TypeIIInitialQOneRootDispatchTests(unittest.TestCase):
    def test_gap_three_terminal_branch(self):
        result = dispatch.initial_dispatch(97)
        self.assertEqual(result["selector_status"], dispatch.ROOT_TERMINAL)
        self.assertEqual(result["terminal"]["gap"], 3)
        self.assertEqual(result["terminal"]["divisor"], 5)
        self.assertTrue(result["terminal"]["root_equation_verified"])
        self.assertFalse(result["recursive_edge_eligible"])

    def test_q_one_g_branch_replays_the_full_carrier_edge(self):
        result = dispatch.initial_dispatch(73)
        self.assertEqual(result["selector_status"], "verified_edge")
        self.assertTrue(result["recursive_edge_eligible"])
        self.assertEqual(result["initial_state"]["endpoint"]["q"], 1)
        self.assertEqual(result["initial_state"]["target_fiber"]["status"], "empty")
        self.assertEqual(
            result["edge"]["terminal_first_digest"]["scope"],
            "q_one_gap_three_direct_type_I_II",
        )
        self.assertTrue(
            result["edge"]["terminal_first_digest"]["complete_within_scope"]
        )
        self.assertEqual(result["edge"]["E5_ticket"], "PHASE_DROP")
        self.assertTrue(
            all(result["edge"][item] for item in ("E1", "E2", "E3", "E4", "E5"))
        )

    def test_noncore_input_is_rejected(self):
        with self.assertRaises(AssertionError):
            dispatch.initial_dispatch(49)


if __name__ == "__main__":
    unittest.main()
