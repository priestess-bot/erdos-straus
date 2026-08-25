from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "t6_q_one_full_carrier_runtime_slice_v1.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q_one_full_carrier_runtime_slice", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SLICE = load_module()


class QOneFullCarrierRuntimeSliceTests(unittest.TestCase):
    def test_terminal_and_two_protocol_runtime_controls(self) -> None:
        SLICE.verify()

    def test_final_reentry_is_explicitly_unregistered(self) -> None:
        result = SLICE.run_q_one_runtime_slice(73)
        self.assertEqual(result["kind"], "runtime_slice")
        self.assertFalse(result["final_reentry"].accepted)
        self.assertEqual(
            result["final_reentry"].reason_code,
            SLICE.runtime.RuntimeRejectCode.DEAD_END,
        )
        self.assertEqual(result["queue_size"], 3)

    def test_runtime_transition_receipts_bind_real_parent_ids(self) -> None:
        result = SLICE.run_q_one_runtime_slice(601)
        root = result["root_decision"].successor
        final = result["final_decision"].successor
        assert root is not None and final is not None
        self.assertNotEqual(root.source_state_id, root.target_state_id)
        self.assertEqual(final.source_state_id, root.target_state_id)
        self.assertEqual(final.t5_ticket_receipt["ticket_type"], "PHASE_DROP")


if __name__ == "__main__":
    unittest.main()
