from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ROOT / "reproductions"))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


M = load_module(
    "type_i_marked_g_universal_anchor_complete_excess_exit",
    "reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py",
)
H = load_module(
    "type_i_high_support_c1_local_minimum_boundary",
    "reproductions/type_i_high_support_c1_local_minimum_boundary.py",
)


class MarkedGUniversalExitTests(unittest.TestCase):
    def test_p601_control_has_real_local_drop(self) -> None:
        row = M.p601_control()
        self.assertEqual(row["source_state"]["fiber"]["classification"], "G")
        self.assertEqual(
            row["E2_target_typing_control"]["target_state"]["fiber"]["classification"],
            "G",
        )
        self.assertFalse(
            row["E2_target_typing_control"]["target_owner_and_reentry_proved"]
        )
        self.assertLess(
            tuple(row["E5"]["target_rank"]),
            tuple(row["E5"]["source_rank"]),
        )

    def test_M_does_not_silently_close_F1(self) -> None:
        scope = M.p601_control()["global_scope"]
        self.assertEqual(
            scope["local_M_adapter"], "CONDITIONAL_ON_E3_AND_SURFACE_ADMISSION"
        )
        self.assertEqual(scope["F1_reachable_state_exhaustion"], "OPEN")
        self.assertFalse(scope["registered_on_frozen_v2_surface"])


class HighSupportC1BoundaryTests(unittest.TestCase):
    def test_minimal_C1_chart_and_duals(self) -> None:
        row = H.canonical_c1_boundary(73)
        self.assertEqual(row["minimal_C1_state"], [75, 1369, 1369])
        self.assertEqual(row["local_rank"], [0, 1, 0, 0])
        self.assertEqual(row["dual_d"], [71, 1296])
        self.assertEqual(row["dual_r"], [3, 55])
        self.assertEqual(
            row["universal_anchor_first_bundle"]["target_cofactor"], 37
        )
        self.assertEqual(row["universal_anchor_first_bundle"]["relation"], "increase")
        self.assertFalse(row["joined_support_preserved"])

    def test_p73_two_bundle_only_reaches_the_boundary(self) -> None:
        row = H.p73_two_bundle_control()
        self.assertLess(tuple(row["E5"]["target"]), tuple(row["E5"]["source"]))
        self.assertEqual(row["second_bundle"]["target"][-1], row["second_bundle"]["target"][1])
        self.assertEqual(row["selector_status"], "analysis_evidence")
        self.assertFalse(row["recursive_edge_eligible"])


if __name__ == "__main__":
    unittest.main()
