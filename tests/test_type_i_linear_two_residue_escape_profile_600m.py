"""Verify the half-block 2-residue mechanism without a spectrum enumerator."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_two_residue_escape_profile_600m",
    ROOT / "reproductions" / "type_i_linear_two_residue_escape_profile_600m.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class TypeILinearTwoResidueEscapeProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = escape.run_audit()
        cls.expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-linear-two-residue-escape-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["profile_count"], 7)
        self.assertGreater(self.actual["eligible_endpoint_count"], 0)

    def test_constructed_divisors_directly_realize_two_and_its_inverse(self):
        for profile in self.actual["profiles"]:
            for row in profile["records"]:
                R = int(row["R"])
                K = int(row["K"])
                half_block = int(row["half_block"])
                inverse_K = pow(K, -1, R)
                self.assertEqual(K * K % int(row["witness_for_inverse_two"]), 0)
                self.assertEqual(K * K % int(row["witness_for_two"]), 0)
                self.assertEqual(
                    int(row["witness_for_inverse_two"]) * inverse_K % R,
                    pow(2, -1, R),
                )
                self.assertEqual(int(row["witness_for_two"]) * inverse_K % R, 2 % R)
                self.assertEqual(half_block % R, pow(2, -1, R))
                if bool(row["prime_R_is_3_mod_8"]):
                    self.assertTrue(sympy.isprime(R))
                    self.assertEqual(R % 8, 3)
                    self.assertEqual(pow(2, (R - 1) // 2, R), R - 1)
                    self.assertEqual(pow(half_block, (R - 1) // 2, R), R - 1)


if __name__ == "__main__":
    unittest.main()
