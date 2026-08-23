from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "reproductions" / "f2_c8_outgoing_trichotomy_v1.py"
SPEC = importlib.util.spec_from_file_location("f2_c8_outgoing_trichotomy_v1", PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot import {PATH}")
TRI = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TRI
SPEC.loader.exec_module(TRI)


def miss():
    return TRI.TerminalFirstReceipt("state:parent", "policy:v1", "MISS", None)


def candidate(raw_prime, direct=4, split=3, *, verified=True, reentry=True):
    return TRI.DoubleLowReceipt(
        "state:parent",
        raw_prime,
        f"path:{raw_prime}",
        direct,
        split,
        verified,
        reentry,
    )


class C8OutgoingTrichotomyTests(unittest.TestCase):
    def test_terminal_preempts_every_successor(self) -> None:
        terminal = TRI.TerminalFirstReceipt(
            "state:parent", "policy:v1", "HIT", "certificate:root"
        )
        result = TRI.dispatch_c8_outgoing(terminal, [candidate(101)])
        self.assertEqual(result.disposition, TRI.C8Disposition.TERMINAL)

    def test_least_fully_verified_double_low_is_deterministic(self) -> None:
        result = TRI.dispatch_c8_outgoing(
            miss(), [candidate(103), candidate(101), candidate(97, verified=False)]
        )
        self.assertEqual(result.disposition, TRI.C8Disposition.DOUBLE_LOW)
        self.assertEqual(result.selected_raw_prime, 101)

    def test_no_double_low_uses_real_named_other_constructor(self) -> None:
        result = TRI.dispatch_c8_outgoing(miss(), [])
        self.assertEqual(result.disposition, TRI.C8Disposition.OTHER)
        self.assertEqual(
            result.target_constructor, "C8SecondFullExcessParentMacroV1"
        )

    def test_capacity_one_candidate_is_routed_away_from_c1(self) -> None:
        result = TRI.dispatch_c8_outgoing(miss(), [candidate(101, split=1)])
        self.assertEqual(result.disposition, TRI.C8Disposition.OTHER)

    def test_unadmitted_candidate_cannot_block_fallback(self) -> None:
        result = TRI.dispatch_c8_outgoing(
            miss(), [candidate(101, reentry=False), candidate(103, verified=False)]
        )
        self.assertEqual(result.disposition, TRI.C8Disposition.OTHER)

    def test_malformed_terminal_receipt_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "TERMINAL_CERTIFICATE_MISSING"):
            TRI.dispatch_c8_outgoing(
                TRI.TerminalFirstReceipt(
                    "state:parent", "policy:v1", "HIT", None
                ),
                [],
            )


if __name__ == "__main__":
    unittest.main()
