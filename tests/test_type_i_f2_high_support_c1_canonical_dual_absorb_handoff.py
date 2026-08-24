from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "reproductions" / "type_i_f2_high_support_c1_canonical_dual_absorb_handoff.py"
)
SPEC = importlib.util.spec_from_file_location(
    "type_i_f2_high_support_c1_canonical_dual_absorb_handoff", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class F2HighSupportC1CanonicalDualAbsorbHandoffTests(unittest.TestCase):
    def test_stored_handoff_receipt_replays(self) -> None:
        receipt = MODULE.verify()
        self.assertEqual(receipt["conclusion"]["E3_and_reentry"], "OPEN")

    def test_r_three_target_is_target_independent(self) -> None:
        for prime in (73, 97, 241, 313):
            support = (prime + 1) ** 2 // 4
            row = MODULE.build_row(prime, support)
            with self.subTest(prime=prime):
                self.assertEqual(
                    (row["R_alpha"], row["K_alpha"]), (3, (3 * prime + 1) // 4)
                )
                self.assertEqual(
                    (row["R_d"], row["K_d"]),
                    (prime - 2, (prime - 1) ** 2 // 4),
                )

    def test_handoff_does_not_claim_active_admission(self) -> None:
        receipt = MODULE.build_receipt()
        self.assertEqual(
            receipt["conclusion"]["E5"],
            "CHARGED_TO_ABSORB_PHASE_DROP_RELATIVE_TO_ADMISSION",
        )
        self.assertEqual(receipt["conclusion"]["E3_and_reentry"], "OPEN")

    def test_canonical_r_three_cursor_is_not_reentry(self) -> None:
        stored = MODULE.json.loads(MODULE.RECEIPT_PATH.read_text(encoding="utf-8"))
        cursor = stored["canonical_absorb_cursor"]
        self.assertEqual(cursor["formal_pair"], [1, 2, 1])
        self.assertEqual(cursor["local_rank_payload"], [3, 1, 1])
        self.assertIn("nonrecursive", cursor["boundary"])


if __name__ == "__main__":
    unittest.main()
