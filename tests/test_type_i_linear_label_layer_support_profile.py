"""Independently verify the finite linear label-layer support profile."""

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
    "type_i_linear_label_layer_support_profile",
    ROOT / "reproductions" / "type_i_linear_label_layer_support_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def product_from_factorization(factors):
    return math.prod(int(item["prime"]) ** int(item["exponent"]) for item in factors)


def direct_centered_target_hit(value, modulus):
    """Decide -1 in the centered square spectrum by direct divisor enumeration."""
    return any(
        int(divisor) % modulus == (-value) % modulus
        for divisor in sympy.divisors(value * value)
    )


class TypeILinearLabelLayerSupportProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-label-layer-support-profile-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["profile_count"], 11)
        self.assertEqual(self.actual["target_hit_R_count"], 32)
        self.assertEqual(self.actual["directed_target_hit_source_count"], 50)
        self.assertEqual(
            self.actual["aggregate_minimum_target_layer_support_counts"],
            {"1": 14, "2": 28, "3": 8},
        )

    def test_input_hashes_and_complete_coordinate_profiles_are_recomputed(self):
        self.assertEqual(
            self.actual["inputs"][profile.INPUT_B1_FAILURES.name],
            profile.EXPECTED_B1_FAILURES_SHA256,
        )
        self.assertEqual(
            self.actual["inputs"][profile.INPUT_PRESSURE_PROFILES.name],
            profile.EXPECTED_PRESSURE_PROFILES_SHA256,
        )
        for output_profile in self.actual["profiles"]:
            prime = int(output_profile["prime"])
            bound, states_by_R = profile.sources.enumerate_linear_source_states(prime)
            labels, _ = profile.coordinate_label_lcms(states_by_R)
            self.assertEqual(
                output_profile["linear_source_coordinate_bound"], bound
            )
            self.assertEqual(output_profile["complete_linear_R_count"], len(states_by_R))
            self.assertEqual(
                output_profile["complete_directed_linear_source_count"],
                sum(len(states) for states in states_by_R.values()),
            )
            self.assertEqual(output_profile["coordinate_label_count"], len(labels))
            self.assertEqual(
                output_profile["coordinate_labels_sha256"],
                profile.integer_list_sha256(labels),
            )

    def test_minimum_layer_support_uses_direct_square_divisor_oracle(self):
        for output_profile in self.actual["profiles"]:
            prime = int(output_profile["prime"])
            _, states_by_R = profile.sources.enumerate_linear_source_states(prime)
            _, collision_lcms = profile.coordinate_label_lcms(states_by_R)
            support_counts = {}
            for orientation in output_profile["orientations"]:
                R = int(orientation["R"])
                a = int(orientation["a"])
                s = int(orientation["s"])
                K = int(orientation["K"])
                expected_K, layers = profile.layer_values(
                    prime, R, a, s, collision_lcms
                )
                self.assertEqual(K, expected_K)
                self.assertEqual(math.prod(layers), K)
                self.assertEqual(
                    [int(layer["value"]) for layer in orientation["layers"]],
                    list(layers),
                )
                for layer, value in zip(orientation["layers"], layers):
                    self.assertEqual(product_from_factorization(layer["factorization"]), value)

                minimum_support = int(orientation["minimum_target_layer_support"])
                minimum_masks = {
                    tuple(names) for names in orientation["minimum_target_layer_masks"]
                }
                self.assertTrue(minimum_masks)
                direct_hits = {}
                for mask in range(1, 1 << len(profile.LAYER_NAMES)):
                    value = math.prod(
                        layer
                        for index, layer in enumerate(layers)
                        if mask & (1 << index)
                    )
                    direct_hits[mask] = direct_centered_target_hit(value, R)
                self.assertTrue(direct_hits[(1 << len(profile.LAYER_NAMES)) - 1])
                self.assertFalse(
                    any(
                        hit and mask.bit_count() < minimum_support
                        for mask, hit in direct_hits.items()
                    )
                )
                expected_masks = {
                    tuple(profile.mask_layer_names(mask))
                    for mask, hit in direct_hits.items()
                    if hit and mask.bit_count() == minimum_support
                }
                self.assertEqual(minimum_masks, expected_masks)
                support_counts[str(minimum_support)] = (
                    support_counts.get(str(minimum_support), 0) + 1
                )
            self.assertEqual(
                support_counts,
                output_profile["minimum_target_layer_support_counts"],
            )

    def test_three_layer_orientations_exclude_every_one_and_two_layer_subproduct(self):
        orientations = [
            orientation
            for output_profile in self.actual["profiles"]
            for orientation in output_profile["orientations"]
            if int(orientation["minimum_target_layer_support"]) == 3
        ]
        self.assertEqual(len(orientations), 8)
        for orientation in orientations:
            R = int(orientation["R"])
            layers = [int(layer["value"]) for layer in orientation["layers"]]
            for mask in range(1, 1 << len(profile.LAYER_NAMES)):
                if mask.bit_count() > 2:
                    continue
                value = math.prod(
                    layer
                    for index, layer in enumerate(layers)
                    if mask & (1 << index)
                )
                self.assertFalse(direct_centered_target_hit(value, R))


if __name__ == "__main__":
    unittest.main()
