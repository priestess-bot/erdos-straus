"""Independently verify the finite three-layer linear reselection profile."""

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
    "type_i_linear_label_reselection_profile_31m",
    ROOT / "reproductions" / "type_i_linear_label_reselection_profile_31m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


def direct_centered_target_hit(value, modulus):
    """Check -1 in a centered square spectrum by direct divisor enumeration."""
    return any(
        int(divisor) % modulus == (-value) % modulus
        for divisor in sympy.divisors(value * value)
    )


class TypeILinearLabelReselectionProfile31MTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = profile.run_audit()
        cls.expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-linear-label-reselection-profile-31m-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_run(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["prime_limit"], 31_000_000)
        self.assertEqual(self.actual["prime_count"], 200)
        self.assertEqual(
            self.actual["selected_layer_support_counts"], {"1": 185, "2": 13, "3": 2}
        )
        self.assertEqual(
            self.actual["selected_three_layer_primes"], [13_782_409, 26_034_649]
        )
        self.assertEqual(
            self.actual["all_target_orientation_layer_support_counts"],
            {"1": 1_734, "2": 839, "3": 177, "4": 29},
        )

    def test_hash_frozen_tail_miss_prefix_is_complete_through_31m(self):
        primes = profile.load_tail_misses()
        self.assertEqual(len(primes), 200)
        self.assertEqual(primes[-1], 30_997_849)
        self.assertEqual(profile.integer_list_sha256(primes), profile.EXPECTED_PRIME_LIST_SHA256)
        all_records = json.loads(profile.TAIL_MISS_INPUT.read_text(encoding="utf-8"))["records"]
        self.assertGreater(int(all_records[len(primes)]["prime"]), profile.PRIME_LIMIT)

    def test_selected_orientations_use_direct_divisor_oracles_and_terminal_bridges(self):
        aggregate = {}
        for record in self.actual["profiles"]:
            prime = int(record["prime"])
            orientation = record["selected_orientation"]
            R = int(orientation["R"])
            a = int(orientation["a"])
            s = int(orientation["s"])
            K = int(orientation["K"])
            layer_values = [int(layer["value"]) for layer in orientation["layers"]]
            support = int(orientation["minimum_target_layer_support"])

            self.assertEqual(math.prod(layer_values), K)
            self.assertEqual(prime, a + s + a * s * R)
            E = s * R + 1
            source = prime - s
            self.assertEqual(source, a * E)
            self.assertEqual(source, (4 * K - E) // R)
            self.assertEqual((4 * K - E) % R, 0)
            self.assertEqual(E % 2, 0)
            self.assertEqual(E % R, 1)
            self.assertEqual((4 * K * K) % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)

            direct_hits = {}
            for mask in range(1, 1 << len(profile.layers.LAYER_NAMES)):
                partial = math.prod(
                    value
                    for index, value in enumerate(layer_values)
                    if mask & (1 << index)
                )
                direct_hits[mask] = direct_centered_target_hit(partial, R)
            self.assertFalse(
                any(hit and mask.bit_count() < support for mask, hit in direct_hits.items())
            )
            self.assertTrue(
                any(hit and mask.bit_count() == support for mask, hit in direct_hits.items())
            )
            aggregate[str(support)] = aggregate.get(str(support), 0) + 1
        self.assertEqual(aggregate, self.actual["selected_layer_support_counts"])

    def test_two_selected_three_layer_points_are_complete_single_hit_spectra(self):
        expected = {
            13_782_409: (41, 78, 131, 11_680, 9),
            26_034_649: (27, 41, 187, 15_460, 9),
        }
        records = {int(record["prime"]): record for record in self.actual["profiles"]}
        for prime, (R_count, state_count, R, a, s) in expected.items():
            record = records[prime]
            self.assertEqual(record["complete_linear_R_count"], R_count)
            self.assertEqual(record["complete_directed_linear_source_count"], state_count)
            self.assertEqual(record["target_hit_R_count"], 1)
            self.assertEqual(record["directed_target_hit_source_count"], 1)
            orientation = record["selected_orientation"]
            self.assertEqual(
                (orientation["R"], orientation["a"], orientation["s"]), (R, a, s)
            )
            self.assertEqual(orientation["minimum_target_layer_support"], 3)


if __name__ == "__main__":
    unittest.main()
