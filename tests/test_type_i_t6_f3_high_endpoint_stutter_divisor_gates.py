from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_t6_f3_high_endpoint_stutter_divisor_gates.py"


def load_module():
    spec = importlib.util.spec_from_file_location("high_endpoint_divisor_gates", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GATES = load_module()


class HighEndpointStutterDivisorGateTests(unittest.TestCase):
    def test_noncore_control_satisfies_both_necessary_gates(self) -> None:
        GATES.check_noncore_complete_shadow()

    def test_capacity_gate_rejects_curve_only_controls(self) -> None:
        GATES.check_capacity_gate_rejects_curve_shadows()


if __name__ == "__main__":
    unittest.main()
