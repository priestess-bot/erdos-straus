from __future__ import annotations

import importlib.util
import json
from dataclasses import replace
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
REPRODUCTIONS = ROOT / "reproductions"
sys.path.insert(0, str(REPRODUCTIONS))


def load(name: str):
    path = REPRODUCTIONS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PENDING = load("f2_c8_atomic_pending_target_v1")
ADMISSION = load("f2_c8_atomic_common_admission_v1")

EVIDENCE = {
    "E1": "actual-parent-and-path",
    "E2": "canonical-lcm-target",
    "E3": "target-local-fiber-recomputation",
    "E4": "identity-Sol-p-lift",
}


def pending_for(chart, arm):
    parent_rank = ADMISSION.n7_charged_potential(
        prime=chart.prime, support=5_330, capacity=chart.prime - 1
    )
    return PENDING.make_pending(
        source_parent_id=f"state:actual-parent:{arm}",
        source_macro_id=f"macro:{arm}",
        source_path_digest=f"path:{arm}",
        terminal_first_digest=f"terminal:miss:{arm}",
        atomic_grammar_arm=arm,
        canonical_payload=(2, 1, 5, 1),
        chart=chart,
        source_tree_scope="charged_history_only",
        parent_n7_potential=parent_rank,
        t5_ticket_candidate="LOCAL_DROP",
    )


class CommonAdmissionTests(unittest.TestCase):
    def cases(self):
        return (
            (
                "H4_A1",
                PENDING.ChartFacts(
                    prime=73,
                    residual=315_581_377_367,
                    carrier=5_759_360_136_948,
                    support=2_879_680_068_474,
                    capacity=2,
                    carrier_factors=(
                        (2, 2),
                        (3, 1),
                        (11, 1),
                        (23, 1),
                        (29, 1),
                        (43, 1),
                        (1_521_269, 1),
                    ),
                ),
                PENDING.FiberKind.F,
            ),
            (
                "C8_DOUBLE_LOW",
                PENDING.ChartFacts(
                    prime=2_137,
                    residual=8_551,
                    carrier=4_568_372,
                    support=1_142_093,
                    capacity=4,
                    carrier_factors=((2, 2), (337, 1), (3_389, 1)),
                ),
                PENDING.FiberKind.G,
            ),
        )

    def test_h4_and_c8_f_g_targets_enter_existing_overflow_residual(self) -> None:
        for arm, chart, expected_fiber in self.cases():
            with self.subTest(arm=arm):
                item = pending_for(chart, arm)
                witness = None
                if expected_fiber is PENDING.FiberKind.F:
                    witness = (0, 0, (chart.residual - 1) // 2, 0, 0, 0, 0)
                fiber = PENDING.exact_fiber_certificate(
                    chart, unbounded_f_witness=witness
                )
                self.assertEqual(fiber.kind, expected_fiber)
                disposition = PENDING.resolve_pending(
                    item, terminal_first_miss=True, fiber=fiber
                )
                target_rank = ADMISSION.n7_charged_potential(
                    prime=chart.prime,
                    support=chart.support,
                    capacity=chart.capacity,
                )
                receipt = ADMISSION.admit_final_target(
                    item,
                    disposition,
                    target_n7_potential=target_rank,
                    evidence=EVIDENCE,
                )
                self.assertTrue(receipt.decision.accepted)
                self.assertEqual(receipt.decision.owner, ADMISSION.TARGET_OWNER)
                self.assertEqual(receipt.raw_state["facts"]["atomic_arm"], "NONE")
                self.assertEqual(receipt.raw_state["facts"]["dispatch_status"], "NONE")
                self.assertNotIn("pending_", json.dumps(receipt.final_successor))

    def test_atomic_target_cannot_enter_without_strict_n7(self) -> None:
        arm, chart, _ = self.cases()[0]
        item = replace(
            pending_for(chart, arm),
            parent_n7_potential=PENDING.canonical_charged_n7(chart),
        )
        disposition = PENDING.resolve_pending(
            item,
            terminal_first_miss=True,
            fiber=PENDING.exact_fiber_certificate(
                chart,
                unbounded_f_witness=(0, 0, (chart.residual - 1) // 2, 0, 0, 0, 0),
            ),
        )
        with self.assertRaisesRegex(PENDING.AtomicProtocolError, "N7_NOT_STRICT"):
            ADMISSION.admit_final_target(
                item,
                disposition,
                target_n7_potential=PENDING.canonical_charged_n7(chart),
                evidence=EVIDENCE,
            )

    def test_atomic_target_cannot_enter_without_e1_e4_evidence(self) -> None:
        arm, chart, _ = self.cases()[1]
        item = pending_for(chart, arm)
        disposition = PENDING.resolve_pending(
            item,
            terminal_first_miss=True,
            fiber=PENDING.exact_fiber_certificate(chart),
        )
        with self.assertRaisesRegex(
            PENDING.AtomicProtocolError, "INCOMPLETE_E1_E4_EVIDENCE"
        ):
            ADMISSION.admit_final_target(
                item,
                disposition,
                target_n7_potential=ADMISSION.n7_charged_potential(
                    prime=chart.prime,
                    support=chart.support,
                    capacity=chart.capacity,
                ),
                evidence={"E1": "only-one"},
            )


if __name__ == "__main__":
    unittest.main()
