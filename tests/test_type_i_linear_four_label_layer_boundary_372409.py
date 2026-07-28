"""Independently verify the complete four-label-layer boundary at p=372409."""

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
    "type_i_linear_four_label_layer_boundary_372409",
    ROOT / "reproductions" / "type_i_linear_four_label_layer_boundary_372409.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


def direct_target_divisors(value, modulus):
    """Enumerate d|value^2 with d/value equal to -1 modulo the modulus."""
    return [
        int(divisor)
        for divisor in sympy.divisors(value * value)
        if int(divisor) % modulus == (-value) % modulus
    ]


class TypeILinearFourLabelLayerBoundary372409Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = boundary.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-four-label-layer-boundary-372409-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["prime"], 372_409)
        self.assertEqual(self.actual["complete_linear_R_count"], 31)
        self.assertEqual(self.actual["complete_directed_linear_source_count"], 53)
        self.assertEqual(self.actual["coordinate_label_count"], 44)
        self.assertEqual(self.actual["target_hit_Rs"], [7, 59, 83, 131, 471])
        self.assertEqual(self.actual["directed_target_hit_source_count"], 11)
        self.assertEqual(
            self.actual["minimum_target_layer_support_counts"],
            {"1": 8, "2": 1, "4": 2},
        )

    def test_all_31_source_moduli_use_a_direct_square_divisor_oracle(self):
        boundary.checked_tail_miss_membership()
        _, states_by_R = boundary.layers.sources.enumerate_linear_source_states(
            boundary.PRIME
        )
        direct_hit_Rs = []
        for R in states_by_R:
            K = (boundary.PRIME * R + 1) // 4
            if direct_target_divisors(K, R):
                direct_hit_Rs.append(R)
        self.assertEqual(direct_hit_Rs, self.actual["target_hit_Rs"])
        self.assertEqual(len(states_by_R), self.actual["complete_linear_R_count"])
        self.assertEqual(
            sum(len(states) for states in states_by_R.values()),
            self.actual["complete_directed_linear_source_count"],
        )

    def test_both_r471_orientations_require_all_four_layer_subproducts(self):
        self.assertEqual(len(self.actual["four_layer_orientations"]), 2)
        _, states_by_R = boundary.layers.sources.enumerate_linear_source_states(
            boundary.PRIME
        )
        _, collision_lcms = boundary.layers.coordinate_label_lcms(states_by_R)
        for orientation in self.actual["four_layer_orientations"]:
            R = int(orientation["R"])
            a = int(orientation["a"])
            s = int(orientation["s"])
            K, layers = boundary.layers.layer_values(
                boundary.PRIME, R, a, s, collision_lcms
            )
            self.assertEqual(R, 471)
            self.assertEqual(K, 43_851_160)
            self.assertEqual(math.prod(layers), K)
            self.assertEqual(
                [int(item["value"]) for item in orientation["layers"]], list(layers)
            )
            self.assertEqual(orientation["minimum_target_layer_support"], 4)
            self.assertEqual(
                orientation["minimum_target_layer_masks"], [list(boundary.layers.LAYER_NAMES)]
            )
            for mask in range(1, (1 << len(boundary.layers.LAYER_NAMES)) - 1):
                partial = math.prod(
                    value for index, value in enumerate(layers) if mask & (1 << index)
                )
                self.assertEqual(direct_target_divisors(partial, R), [])
            self.assertEqual(direct_target_divisors(K, R), [27_200, 70_695_743_873])

    def test_four_layer_states_still_are_original_even_terminal_bridges(self):
        for orientation in self.actual["four_layer_orientations"]:
            R = int(orientation["R"])
            a = int(orientation["a"])
            s = int(orientation["s"])
            K = int(orientation["K"])
            E = s * R + 1
            source = boundary.PRIME - s
            self.assertEqual(boundary.PRIME, a + s + a * s * R)
            self.assertEqual(source, a * E)
            self.assertEqual(source, (4 * K - E) // R)
            self.assertEqual((4 * K - E) % R, 0)
            self.assertEqual(E % 2, 0)
            self.assertEqual(E % R, 1)
            self.assertEqual((4 * K * K) % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)


if __name__ == "__main__":
    unittest.main()
