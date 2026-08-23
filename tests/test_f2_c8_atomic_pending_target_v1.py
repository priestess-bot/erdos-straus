from __future__ import annotations

import importlib.util
import json
from dataclasses import replace
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "reproductions" / "f2_c8_atomic_pending_target_v1.py"
SPEC = importlib.util.spec_from_file_location("f2_c8_atomic_pending_target_v1", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
ATOMIC = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ATOMIC
SPEC.loader.exec_module(ATOMIC)


def chart(prime: int, residual: int, carrier: int, support: int, capacity: int, factors):
    return ATOMIC.ChartFacts(prime, residual, carrier, support, capacity, tuple(factors))


def pending(target_chart, arm="H4_A1"):
    return ATOMIC.make_pending(
        source_parent_id="state:parent",
        source_macro_id="macro:actual",
        source_path_digest="path:actual",
        terminal_first_digest="terminal:miss",
        atomic_grammar_arm=arm,
        canonical_payload=(2, 1, 5, 1),
        chart=target_chart,
        source_tree_scope="charged_history_only",
        parent_n7_potential=(0, 72, 4, 3, 2, 1, 0),
        t5_ticket_candidate="LOCAL_DROP",
    )


class ChartAndFiberTests(unittest.TestCase):
    def test_exact_target_fiber_trichotomy(self) -> None:
        hit = chart(73, 3, 55, 55, 1, ((5, 1), (11, 1)))
        f = chart(73, 383, 6_990, 233, 30, ((2, 1), (3, 1), (5, 1), (233, 1)))
        g = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        self.assertEqual(ATOMIC.exact_fiber_certificate(hit).kind, ATOMIC.FiberKind.HIT)
        self.assertEqual(ATOMIC.exact_fiber_certificate(f).kind, ATOMIC.FiberKind.F)
        self.assertEqual(ATOMIC.exact_fiber_certificate(g).kind, ATOMIC.FiberKind.G)

    def test_chart_digest_binds_fiber_evidence(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        certificate = ATOMIC.exact_fiber_certificate(target)
        self.assertEqual(certificate.chart_digest, target.chart_digest)
        self.assertTrue(certificate.recomputed)
        self.assertFalse(certificate.inherited_label)
        self.assertTrue(certificate.evidence_digest.startswith("fiber:"))

    def test_pending_resolves_to_terminal_f_and_g_without_pending_marker(self) -> None:
        cases = (
            (chart(73, 3, 55, 55, 1, ((5, 1), (11, 1))), ATOMIC.Disposition.TERMINAL),
            (
                chart(73, 383, 6_990, 233, 30, ((2, 1), (3, 1), (5, 1), (233, 1))),
                ATOMIC.Disposition.F_SUCCESSOR,
            ),
            (chart(73, 11, 201, 67, 3, ((3, 1), (67, 1))), ATOMIC.Disposition.G_SUCCESSOR),
        )
        for target_chart, expected in cases:
            with self.subTest(target_chart=target_chart):
                result = ATOMIC.resolve_pending(
                    pending(target_chart),
                    terminal_first_miss=True,
                    fiber=ATOMIC.exact_fiber_certificate(target_chart),
                )
                self.assertEqual(result.disposition, expected)
                self.assertNotIn("pending_", result.reason)

    def test_terminal_first_preempts_atomic_dispatch(self) -> None:
        target = chart(73, 383, 6_990, 233, 30, ((2, 1), (3, 1), (5, 1), (233, 1)))
        result = ATOMIC.resolve_pending(
            pending(target), terminal_first_miss=False, fiber=None
        )
        self.assertEqual(result.disposition, ATOMIC.Disposition.TERMINAL)
        self.assertEqual(result.reason, "TERMINAL_FIRST")

    def test_inherited_fiber_label_is_rejected(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        certificate = replace(
            ATOMIC.exact_fiber_certificate(target), inherited_label=True
        )
        result = ATOMIC.resolve_pending(
            pending(target), terminal_first_miss=True, fiber=certificate
        )
        self.assertEqual(result.disposition, ATOMIC.Disposition.REJECT)
        self.assertEqual(result.reason, "TARGET_FIBER_NOT_RECOMPUTED")

    def test_chart_digest_mismatch_is_rejected(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        other = chart(73, 3, 55, 55, 1, ((5, 1), (11, 1)))
        result = ATOMIC.resolve_pending(
            pending(target),
            terminal_first_miss=True,
            fiber=ATOMIC.exact_fiber_certificate(other),
        )
        self.assertEqual(result.disposition, ATOMIC.Disposition.REJECT)
        self.assertEqual(result.reason, "TARGET_CHART_DIGEST_MISMATCH")

    def test_forged_fiber_status_is_replayed_and_rejected(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        certificate = ATOMIC.exact_fiber_certificate(target)
        forged = replace(certificate, minus_one_in_subgroup=True)
        result = ATOMIC.resolve_pending(
            pending(target), terminal_first_miss=True, fiber=forged
        )
        self.assertEqual(result.disposition, ATOMIC.Disposition.REJECT)
        self.assertEqual(result.reason, "FIBER_CERTIFICATE_MISMATCH")

    def test_unsupported_arm_and_pending_marker_fail_closed(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        with self.assertRaisesRegex(ATOMIC.AtomicProtocolError, "UNSUPPORTED_ATOMIC_ARM"):
            pending(target, arm="FUTURE_ARM")
        with self.assertRaisesRegex(ATOMIC.AtomicProtocolError, "FORBIDDEN_PENDING_MARKER"):
            ATOMIC.make_pending(
                source_parent_id="state:parent",
                source_macro_id="pending_dispatch",
                source_path_digest="path:actual",
                terminal_first_digest="terminal:miss",
                atomic_grammar_arm="H4_A1",
                canonical_payload=(2, 1, 5, 1),
                chart=target,
                source_tree_scope="charged_history_only",
                parent_n7_potential=(0, 72, 4, 3, 2, 1, 0),
                t5_ticket_candidate="LOCAL_DROP",
            )

    def test_carrier_factorization_is_not_support_factorization(self) -> None:
        with self.assertRaisesRegex(
            ATOMIC.AtomicProtocolError, "INVALID_CARRIER_FACTORIZATION"
        ):
            chart(73, 11, 201, 67, 3, ((67, 1),))


class FinalAdmissionTests(unittest.TestCase):
    def test_final_f_successor_has_no_pending_fields(self) -> None:
        target = chart(73, 383, 6_990, 233, 30, ((2, 1), (3, 1), (5, 1), (233, 1)))
        item = pending(target)
        disposition = ATOMIC.resolve_pending(
            item,
            terminal_first_miss=True,
            fiber=ATOMIC.exact_fiber_certificate(target),
        )
        receipt = ATOMIC.finalize_successor(
            item,
            disposition,
            target_state_id="state:target",
            target_owner="type_i_full_carrier_post_g",
            target_n7_potential=(0, 60, 4, 3, 2, 1, 0),
            e4_lift_digest="lift:id",
            reentry_verified=True,
        )
        self.assertEqual(receipt["status"], "VERIFIED_SUCCESSOR")
        self.assertEqual(receipt["target_fiber"], "F")
        self.assertNotIn("pending", json.dumps(receipt))

    def test_final_successor_requires_strict_parent_to_final_rank(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        item = pending(target, arm="C8_DOUBLE_LOW")
        disposition = ATOMIC.resolve_pending(
            item,
            terminal_first_miss=True,
            fiber=ATOMIC.exact_fiber_certificate(target),
        )
        with self.assertRaisesRegex(ATOMIC.AtomicProtocolError, "N7_NOT_STRICT"):
            ATOMIC.finalize_successor(
                item,
                disposition,
                target_state_id="state:target",
                target_owner="type_i_full_carrier_post_g",
                target_n7_potential=item.parent_n7_potential,
                e4_lift_digest="lift:id",
                reentry_verified=True,
            )

    def test_final_successor_requires_reentry(self) -> None:
        target = chart(73, 11, 201, 67, 3, ((3, 1), (67, 1)))
        item = pending(target)
        disposition = ATOMIC.resolve_pending(
            item,
            terminal_first_miss=True,
            fiber=ATOMIC.exact_fiber_certificate(target),
        )
        with self.assertRaisesRegex(ATOMIC.AtomicProtocolError, "REENTRY_NOT_VERIFIED"):
            ATOMIC.finalize_successor(
                item,
                disposition,
                target_state_id="state:target",
                target_owner="type_i_full_carrier_post_g",
                target_n7_potential=(0, 60, 4, 3, 2, 1, 0),
                e4_lift_digest="lift:id",
                reentry_verified=False,
            )


if __name__ == "__main__":
    unittest.main()
