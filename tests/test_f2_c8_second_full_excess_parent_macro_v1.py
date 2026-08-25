from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
sys.path.insert(0, str(REPRODUCTIONS))
MODULE_PATH = REPRODUCTIONS / "f2_c8_second_full_excess_parent_macro_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "f2_c8_second_full_excess_parent_macro_v1", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MACRO = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MACRO
SPEC.loader.exec_module(MACRO)


class C8SecondFullExcessParentMacroTests(unittest.TestCase):
    def test_actual_control_compares_persistent_parent_to_final_target(self) -> None:
        receipt = MACRO.parent_to_final_receipt(3_279, parent_eta_p=11)
        self.assertGreater(receipt.target_capacity, receipt.checkpoint_capacity)
        self.assertLess(receipt.target_capacity, receipt.parent_capacity)
        self.assertLess(receipt.target_n7, receipt.parent_n7)
        self.assertEqual(receipt.target_residual % 4, 3)
        self.assertGreater(receipt.target_residual, receipt.prime)

    def test_capacity_congruence_excludes_low_and_parent_stutter(self) -> None:
        receipt = MACRO.parent_to_final_receipt(3_279)
        self.assertTrue(
            MACRO.symbolic_capacity_bounds(
                receipt.prime, receipt.target_capacity
            )
        )
        self.assertFalse(
            MACRO.symbolic_capacity_bounds(receipt.prime, receipt.parent_capacity)
        )

    def test_internal_checkpoint_is_not_the_e5_source(self) -> None:
        receipt = MACRO.parent_to_final_receipt(3_279)
        checkpoint_rank = MACRO.n7(
            receipt.prime,
            receipt.checkpoint_support,
            receipt.checkpoint_capacity,
        )
        self.assertGreater(receipt.target_n7, checkpoint_rank)
        self.assertLess(receipt.target_n7, receipt.parent_n7)

    def test_terminal_preempted_control_never_manufactures_a_miss(self) -> None:
        receipt = MACRO.parent_to_final_receipt(3_279)
        terminal = MACRO.terminal_control(3_279)
        self.assertEqual(terminal.outcome, "HIT")
        self.assertIsNotNone(terminal.denominators)
        proposal = MACRO.propose_after_actual_miss(receipt)
        self.assertTrue(proposal.status.startswith("PROPOSAL_NOT_ACTIVE"))
        self.assertEqual(proposal.required_target_owner, MACRO.TARGET_OWNER)


if __name__ == "__main__":
    unittest.main()
