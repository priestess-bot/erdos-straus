from __future__ import annotations

import importlib.util
import sys
import unittest
from dataclasses import asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "reproductions"
    / "type_i_t6_f3_qc1_quotient_only_physical_transition.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_t6_f3_qc1_quotient_only_physical_transition", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
QC1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = QC1
SPEC.loader.exec_module(QC1)


class QuotientOnlyQC1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = QC1.control_source()

    def test_canonical_q_perp_and_oriented_ideal_factor(self) -> None:
        arithmetic = QC1.rebuild_source(self.source)
        ideal_factor = QC1.quotient_ideal_factor(self.source, arithmetic)
        self.assertEqual(QC1.canonical_q_perp(self.source.k, self.source.h), 61)
        self.assertEqual(ideal_factor["q_perp"], 61)
        self.assertEqual(ideal_factor["oriented_prime_ideal"]["lambda"], 14)
        self.assertTrue(ideal_factor["height_cancellation_excluded"])
        self.assertFalse(ideal_factor["actual_integer_raw_occurrence_bound"])

    def test_target_has_strict_n7_drop_and_existing_owner(self) -> None:
        result = QC1.build_transition(self.source)
        target = result["target_arithmetic"]
        self.assertLess(target["target_rank_N7"], target["source_rank_N7"])
        self.assertEqual(result["target_shape_control"]["owner"], QC1.TARGET_OWNER)
        self.assertEqual(
            result["target_shape_control"]["matched_families"], [QC1.TARGET_OWNER]
        )
        self.assertFalse(result["E1"]["complete"])
        self.assertFalse(result["recursive_edge_eligible"])

    def test_q_perp_is_not_replaced_by_an_h_supported_factor(self) -> None:
        with self.assertRaisesRegex(QC1.QC1ContractError, "K_PERP_ONE"):
            QC1.canonical_q_perp(self.source.h, self.source.h)

    def test_m3_q5_route_is_rejected(self) -> None:
        bad = QC1.QuotientOnlySourceV1(
            **{**asdict(self.source), "m": 3, "d_star": 5}
        )
        with self.assertRaises(QC1.QC1ContractError):
            QC1.build_transition(bad)

    def test_tampered_source_binding_fails_before_occurrence(self) -> None:
        binding = dict(self.source.source_binding_receipt)
        binding["source_path_digest"] = "changed"
        bad = QC1.QuotientOnlySourceV1(
            **{**asdict(self.source), "source_binding_receipt": binding}
        )
        with self.assertRaisesRegex(
            QC1.QC1ContractError, "SOURCE_BINDING_RECEIPT_DIGEST_MISMATCH"
        ):
            QC1.build_transition(bad)

    def test_nonprime_control_cannot_be_forged_as_actual(self) -> None:
        values = asdict(self.source)
        values["evidence_class"] = "ACTUAL_PERSISTENT"
        provisional = QC1.QuotientOnlySourceV1(**values)
        values["source_binding_receipt"] = QC1.source_binding_receipt(
            provisional, status="VERIFIED_ACTUAL_PERSISTENT_SOURCE"
        )
        forged = QC1.QuotientOnlySourceV1(**values)
        with self.assertRaisesRegex(QC1.QC1ContractError, "ACTUAL_SOURCE_P_NOT_PRIME"):
            QC1.build_transition(forged)

    def test_self_sealed_prime_label_cannot_be_forged_as_actual(self) -> None:
        values = asdict(self.source)
        values["evidence_class"] = "ACTUAL_PERSISTENT"
        values["p"] = 73
        provisional = QC1.QuotientOnlySourceV1(**values)
        values["source_binding_receipt"] = QC1.source_binding_receipt(
            provisional, status="VERIFIED_ACTUAL_PERSISTENT_SOURCE"
        )
        forged = QC1.QuotientOnlySourceV1(**values)
        with self.assertRaisesRegex(
            QC1.QC1ContractError, "ACTUAL_SOURCE_RUNTIME_REPLAY_NOT_IMPLEMENTED"
        ):
            QC1.build_transition(forged)

    def test_ideal_factor_is_not_integer_occurrence_or_e1(self) -> None:
        result = QC1.build_transition(self.source)
        self.assertEqual(
            result["ideal_factor"]["integer_raw_occurrence_status"], "UNPROVED"
        )
        self.assertFalse(result["E1"]["path_bound_integer_raw_occurrence"])
        self.assertFalse(result["E1"]["support_charge_conservation"])
        self.assertIsNone(result["T5_ticket"])

    def test_norm_factor_does_not_locate_the_distinguished_stutter_side(self) -> None:
        self.assertEqual(
            QC1.raw_side_nonimplication_control(),
            {"q_perp": 61, "v_z": 0, "v_D": 0, "v_E": 0, "v_K": 0},
        )


if __name__ == "__main__":
    unittest.main()
