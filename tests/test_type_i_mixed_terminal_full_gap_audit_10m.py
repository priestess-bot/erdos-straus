"""Regression checks for the no-gap-cap mixed-terminal audit."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_mixed_terminal_full_gap_audit_10m.py"
ARTIFACT = ROOT / "reproductions" / "type-i-mixed-terminal-full-gap-audit-10m-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("full_gap_mixed_terminal", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load full-gap mixed-terminal audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile = load_module()


class FullGapMixedTerminalAuditTests(unittest.TestCase):
    def test_frozen_artifact_reproduces_exactly(self):
        with ARTIFACT.open(encoding="utf-8") as handle:
            stored = json.load(handle)
        self.assertEqual(profile.run_audit(), stored)

    def test_complete_finite_dichotomy_has_no_unclosed_prime(self):
        actual = profile.run_audit()
        self.assertEqual(actual["prime_limit"], 10_000_000)
        self.assertEqual(actual["core_prime_count"], 82_887)
        self.assertEqual(actual["ordinary_type_ii_tail_certificate_count"], 82_803)
        self.assertEqual(actual["ordinary_type_ii_tail_miss_count"], 84)
        self.assertEqual(actual["type_i_even_terminal_bridge_count"], 84)
        self.assertEqual(actual["unclosed_primes"], [])
        self.assertEqual(actual["maximum_selected_type_i_gap"], 71)

    def test_every_stored_bridge_reconstructs_both_identities(self):
        actual = profile.run_audit()
        for record in actual["type_i_even_terminal_records"]:
            witness = record["type_i_even_terminal"]
            rebuilt = profile.target_selector.terminal_witness_from_target_divisors(
                int(record["prime"]),
                int(witness["gap"]),
                int(witness["target_divisor"]),
                int(witness["bridge_factor"]),
            )
            self.assertIsNotNone(rebuilt)
            self.assertEqual(profile.target_selector.serialize_witness(rebuilt), witness)


if __name__ == "__main__":
    unittest.main()
