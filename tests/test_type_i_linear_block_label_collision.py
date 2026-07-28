"""Verify the coordinate-label collision decomposition for linear source blocks."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_block_label_collision",
    ROOT / "reproductions" / "type_i_linear_block_label_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class TypeILinearBlockLabelCollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = collision.run_audit()
        cls.expected = json.loads(
            (ROOT / "reproductions" / "type-i-linear-block-label-collision-results.json").read_text(
                encoding="utf-8"
            )
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["profile_count"], 7)
        self.assertGreater(self.actual["cross_label_pair_count"], 0)

    def test_block_factorizations_and_private_coprimality(self):
        for profile in self.actual["profiles"]:
            prime = int(profile["prime"])
            blocks = profile["blocks"]
            self.assertEqual(len(blocks), 2 * int(profile["directed_linear_source_state_count"]))
            for block in blocks:
                R = int(block["R"])
                a = int(block["a"])
                s = int(block["s"])
                value = int(block["value"])
                expected_value = s * R + 1 if block["kind"] == "E" else a * R + 1
                self.assertEqual(value, expected_value)
                self.assertEqual(prime, a + s + a * s * R)
                self.assertEqual(
                    int(block["collision_layer"]),
                    math.gcd(value, int(block["label_collision_lcm"])),
                )
                self.assertEqual(
                    int(block["private_layer"]),
                    value // int(block["collision_layer"]),
                )
            for index, left in enumerate(blocks):
                for right in blocks[index + 1 :]:
                    if left["label"] == right["label"]:
                        continue
                    raw_gcd = math.gcd(int(left["value"]), int(right["value"]))
                    self.assertEqual(
                        abs(int(left["label"]) - int(right["label"])) % raw_gcd,
                        0,
                    )
                    self.assertEqual(
                        math.gcd(int(left["private_layer"]), int(right["private_layer"])),
                        1,
                    )


if __name__ == "__main__":
    unittest.main()
