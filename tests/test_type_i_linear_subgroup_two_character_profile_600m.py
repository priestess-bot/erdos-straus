"""Verify G-type two-residue coverage and separating-character order data."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_subgroup_two_character_profile_600m",
    ROOT / "reproductions" / "type_i_linear_subgroup_two_character_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearSubgroupTwoCharacterProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-subgroup-two-character-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["subgroup_character_R_count"], 190)
        self.assertGreater(self.actual["quadratic_separator_R_count"], 0)

    def test_halfblock_two_injection_never_coexists_with_minus_one_in_its_orbit(self):
        for prime_profile in self.actual["profiles"]:
            for record in prime_profile["records"]:
                R = int(record["R"])
                order = int(record["two_multiplicative_order"])
                minus_one_in_orbit = bool(
                    order % 2 == 0 and pow(2, order // 2, R) == R - 1
                )
                self.assertEqual(
                    minus_one_in_orbit, bool(record["minus_one_in_two_subgroup"])
                )
                self.assertFalse(
                    bool(record["two_injecting_state_exists"]) and minus_one_in_orbit
                )
                self.assertGreaterEqual(
                    int(record["minimal_separating_two_power_character_order"]), 2
                )
                self.assertTrue(sympy.gcd(2, R) == 1)


if __name__ == "__main__":
    unittest.main()
