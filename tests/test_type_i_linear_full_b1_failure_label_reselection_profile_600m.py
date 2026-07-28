"""Verify three-layer reselection on every full-spectrum B=1 failure in the pressure set."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

import sympy


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_full_b1_failure_label_reselection_profile_600m",
    ROOT / "reproductions" / "type_i_linear_full_b1_failure_label_reselection_profile_600m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def direct_centered_target_hit(value: int, modulus: int) -> bool:
    return any(
        int(divisor) % modulus == (-value) % modulus
        for divisor in sympy.divisors(value * value)
    )


class TypeILinearFullB1FailureLabelReselectionProfile600MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-full-b1-failure-label-reselection-profile-600m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_fresh_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["prime_count"], 18)
        self.assertEqual(self.actual["selected_layer_support_counts"], {"1": 3, "2": 14, "3": 1})
        self.assertEqual(self.actual["selected_three_layer_primes"], [26_034_649])

    def test_selected_layers_have_direct_target_witnesses_and_terminal_bridges(self):
        for record in self.actual["profiles"]:
            prime = int(record["prime"])
            selected = record["selected_orientation"]
            R = int(selected["R"])
            a = int(selected["a"])
            s = int(selected["s"])
            K = int(selected["K"])
            layers = [int(layer["value"]) for layer in selected["layers"]]
            support = int(selected["minimum_target_layer_support"])
            self.assertEqual(math.prod(layers), K)
            self.assertEqual(prime, a + s + a * s * R)
            direct_hits = {}
            for mask in range(1, 1 << len(profile.layers.LAYER_NAMES)):
                value = math.prod(
                    layer for index, layer in enumerate(layers) if mask & (1 << index)
                )
                direct_hits[mask] = direct_centered_target_hit(value, R)
            self.assertFalse(
                any(hit and mask.bit_count() < support for mask, hit in direct_hits.items())
            )
            self.assertTrue(
                any(hit and mask.bit_count() == support for mask, hit in direct_hits.items())
            )
            E = s * R + 1
            self.assertEqual(prime - s, a * E)
            self.assertEqual(E % 2, 0)
            self.assertEqual(E % R, 1)
            self.assertEqual((4 * K * K) % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)


if __name__ == "__main__":
    unittest.main()
