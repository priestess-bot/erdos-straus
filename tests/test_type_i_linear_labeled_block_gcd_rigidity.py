"""Verify the joint label/modulus collision decomposition independently."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_linear_labeled_block_gcd_rigidity",
    ROOT / "reproductions" / "type_i_linear_labeled_block_gcd_rigidity.py",
)
assert SPEC and SPEC.loader
rigidity = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rigidity
SPEC.loader.exec_module(rigidity)


class TypeILinearLabeledBlockGcdRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = rigidity.run_audit()
        cls.expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-linear-labeled-block-gcd-rigidity-results.json"
            ).read_text(encoding="utf-8")
        )

    def test_checked_artifact_matches_complete_audit(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["profile_count"], 7)
        self.assertGreater(self.actual["pair_counts"]["different_label"], 0)
        self.assertGreater(self.actual["pair_counts"]["same_label_different_R"], 0)

    def test_distinct_block_gcd_identities_and_private_coprimality(self):
        for profile in self.actual["profiles"]:
            blocks = profile["blocks"]
            self.assertEqual(
                len(blocks), int(profile["distinct_coordinate_block_count"])
            )
            self.assertEqual(
                len({(block["label"], block["R"]) for block in blocks}), len(blocks)
            )
            for block in blocks:
                value = int(block["value"])
                self.assertEqual(value, int(block["label"]) * int(block["R"]) + 1)
                self.assertEqual(
                    int(block["collision_layer"]),
                    math.gcd(value, int(block["collision_lcm"])),
                )
                self.assertEqual(
                    int(block["private_layer"]),
                    value // int(block["collision_layer"]),
                )
            for index, left in enumerate(blocks):
                for right in blocks[index + 1 :]:
                    raw_gcd = math.gcd(int(left["value"]), int(right["value"]))
                    if left["label"] != right["label"]:
                        self.assertEqual(
                            abs(int(left["label"]) - int(right["label"])) % raw_gcd,
                            0,
                        )
                    else:
                        self.assertEqual(
                            raw_gcd,
                            math.gcd(
                                int(left["value"]),
                                abs(int(left["R"]) - int(right["R"])),
                            ),
                        )
                    self.assertEqual(
                        math.gcd(int(left["private_layer"]), int(right["private_layer"])),
                        1,
                    )


if __name__ == "__main__":
    unittest.main()
