from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "type_i_f2_overflow_determinant_prepartition.py"
SPEC = importlib.util.spec_from_file_location(
    "type_i_f2_overflow_determinant_prepartition", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2OverflowDeterminantPrepartitionTests(unittest.TestCase):
    def test_stored_receipt_replays(self) -> None:
        MODULE.verify()

    def test_partition_has_exact_symbolic_residuals(self) -> None:
        receipt = MODULE.build_receipt()
        branches = [row["branch"] for row in receipt["controls"]]
        self.assertEqual(
            branches,
            [
                "SAME_CHART_SUPPORT_PROMOTION",
                "FULL_PRODUCT_FIXED_N_DESCENT",
                "LOW_SUPPORT_D_ONE_SATURATED_RESIDUAL",
                "HIGH_SUPPORT_CANONICAL_C_ONE_RESIDUAL",
                "HIGH_SUPPORT_CANONICAL_C_GT_ONE_RESIDUAL",
                "SAME_CHART_SUPPORT_PROMOTION",
            ],
        )

    def test_strict_branches_compare_real_parent_to_target(self) -> None:
        receipt = MODULE.build_receipt()
        strict = [row for row in receipt["controls"] if row["ticket"] is not None]
        self.assertEqual(len(strict), 3)
        for row in strict:
            with self.subTest(source=row["source"]["name"]):
                self.assertLess(tuple(row["target_rank"]), tuple(row["source_rank"]))
                self.assertTrue(row["target_is_overflow"])

    def test_p409_is_preempted_only_if_actualness_is_supplied_externally(self) -> None:
        receipt = MODULE.build_receipt()
        disposition = receipt["p409_disposition"]
        self.assertEqual(disposition["without_actual_source"], "OUTSIDE_QUANTIFIED_DOMAIN")
        self.assertEqual(
            disposition["with_exact_actual_determinant"],
            "PREEMPTED_BY_SAME_CHART_SUPPORT_PROMOTION",
        )
        row = next(
            row for row in receipt["controls"] if row["source"]["name"] == "p409_anomaly"
        )
        self.assertEqual(row["guard"]["b"], 50)
        self.assertEqual(row["target"], {"p": 409, "R": 511, "K": 52250, "A": 250})

    def test_ordered_total_cofactor_has_no_strict_later_leaf(self) -> None:
        disposition = MODULE.build_receipt()["ordered_total_cofactor_disposition"]
        self.assertEqual(
            disposition,
            {
                "b_at_least_two": "PREEMPTED_BY_EARLIER_SAME_CHART_STRICT_BRANCH",
                "b_equals_one": "REJECT_CANONICAL_STUTTER_T_EQUALS_ZERO",
                "strict_later_branch": "EMPTY",
            },
        )

    def test_malformed_determinant_is_rejected(self) -> None:
        bad = MODULE.SourceReceipt(
            "malformed", p=73, R=287, K=5238, A=97, M=97, d=19, n=105
        )
        with self.assertRaisesRegex(ValueError, "invalid F2 overflow determinant receipt"):
            MODULE.partition(bad)


if __name__ == "__main__":
    unittest.main()
