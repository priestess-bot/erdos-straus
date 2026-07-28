"""Verify the stored 1B--1.1B mixed-terminal interval audit."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT / "reproductions" / "type-i-mixed-terminal-dense-1b-1p1b-results.json"
)


class TypeIMixedTerminalDense1P1BTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_exact_partition_and_gap_profile(self):
        payload = self.payload
        self.assertEqual(payload["prime_interval"], [1_000_000_001, 1_100_000_000])
        self.assertEqual(payload["core_prime_count"], 601_660)
        self.assertEqual(
            (
                payload["ordinary_type_ii_tail_hit_count"],
                payload["ordinary_type_ii_tail_miss_count"],
                payload["type_i_even_terminal_bridge_count"],
                payload["maximum_selected_type_i_gap"],
            ),
            (601_416, 244, 244, 159),
        )
        self.assertEqual(payload["type_i_gap_cap"], 215)
        self.assertEqual(payload["even_source_misses"], [])
        self.assertEqual(
            payload["ordinary_type_ii_tail_hit_count"]
            + payload["type_i_even_terminal_bridge_count"],
            payload["core_prime_count"],
        )
        self.assertEqual(
            payload["type_i_first_even_source_gap_histogram"],
            {
                "15": 90,
                "19": 48,
                "27": 12,
                "31": 46,
                "35": 9,
                "39": 10,
                "43": 2,
                "47": 10,
                "51": 3,
                "55": 3,
                "59": 2,
                "71": 2,
                "79": 2,
                "87": 1,
                "107": 1,
                "111": 1,
                "119": 1,
                "159": 1,
            },
        )

    def test_every_stored_bridge_reconstructs_the_target_conditions(self):
        for record in self.payload["type_i_even_terminal_bridge_records"]:
            prime = int(record["prime"])
            witness = record["type_i_even_witness"]
            gap = int(witness["gap"])
            A, B, C = (int(value) for value in witness["normal_form"])
            R = (4 * B * B * C + 1) // gap
            H = A * R - B
            K = B * C * H
            lift = witness["reverse_two_tail_lift"]
            E = int(lift["bridge_divisor"]) // (prime * prime)
            source = int(lift["source_denominator"])
            self.assertEqual(gap * R, 4 * B * B * C + 1)
            self.assertEqual(4 * K, prime * R + 1)
            self.assertEqual(int(lift["bridge_divisor"]), prime * prime * E)
            self.assertEqual((E % R, E % 2), (1, 0))
            self.assertEqual(4 * K * K % E, 0)
            self.assertLessEqual(E, 4 * K - 2 * R)
            self.assertEqual(source % 2, 0)
            self.assertEqual(
                Fraction(4, source),
                sum(
                    (Fraction(1, value) for value in witness["source_solution"]),
                    Fraction(),
                ),
            )


if __name__ == "__main__":
    unittest.main()
