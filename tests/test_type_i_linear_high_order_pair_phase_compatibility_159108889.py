"""Verify compatible quartic phases at the first split high-order state pair."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_high_order_pair_phase_compatibility_159108889",
    ROOT / "reproductions" / "type_i_linear_high_order_pair_phase_compatibility_159108889.py",
)
assert SPEC and SPEC.loader
phase_profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = phase_profile
SPEC.loader.exec_module(phase_profile)


class TypeILinearHighOrderPairPhaseCompatibility159108889Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = phase_profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-high-order-pair-phase-compatibility-159108889-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_the_two_high_order_states(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["shared_split_K_prime"], 70_841)
        self.assertEqual(self.actual["shared_primary_gaussian_factor_rho"], [245, 104])

    def test_both_fourth_order_separators_are_trivial_at_the_shared_prime(self):
        self.assertEqual([state["R"] for state in self.actual["states"]], [47_227, 53_036_295])
        for state in self.actual["states"]:
            self.assertEqual(state["shared_prime_source_label_t"], 3)
            self.assertEqual(state["total_separator_exponent_at_shared_prime"], 0)
            self.assertEqual(len(state["order_four_separators"]), 2)
            for row in state["quartic_phase_rows"]:
                self.assertEqual(
                    row["quartic_character_exponent"], row["pullback_rhs_exponent"]
                )


if __name__ == "__main__":
    unittest.main()
