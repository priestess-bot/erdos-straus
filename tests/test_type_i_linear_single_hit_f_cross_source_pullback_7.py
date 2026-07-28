"""Verify the seven single-hit F cross-source pullback profile."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_single_hit_f_cross_source_pullback_7.py"
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-single-hit-f-cross-source-pullback-7-results.json"
)

spec = importlib.util.spec_from_file_location("single_hit_f_pullback", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load single-hit F pullback profile")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class SingleHitFCrossSourcePullbackTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.stored = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_global_counts_and_digest(self):
        self.assertEqual(self.actual, self.stored)
        self.assertEqual(self.actual["prime_count"], 7)
        self.assertEqual(self.actual["finite_exponent_R_count"], 71)
        self.assertEqual(self.actual["directed_orientation_count"], 110)
        self.assertEqual(self.actual["pairwise_gcd_identity_count"], 5542)
        self.assertEqual(self.actual["raw_shared_pullback_orientation_count"], 7)
        self.assertEqual(
            self.actual["subgroup_shared_pullback_orientation_count"], 5
        )
        self.assertEqual(self.actual["finite_shared_alignment_orientation_count"], 0)
        self.assertEqual(self.actual["raw_shared_pullback_residue_count"], 34)
        self.assertEqual(self.actual["subgroup_shared_pullback_residue_count"], 16)
        self.assertEqual(
            self.actual["subgroup_pullback_exponent_overflow_distribution"],
            {"1": 6, "2": 4, "6": 2, "7": 2, "8": 2},
        )
        self.assertEqual(self.actual["minimum_subgroup_pullback_exponent_overflow"], 1)
        self.assertEqual(self.actual["maximum_subgroup_pullback_exponent_overflow"], 8)
        self.assertEqual(
            self.actual["record_sha256"],
            "3b1795047f79a13cac70abddaa5b4ed2930fc17de1af18f3ebbd76017a1676a8",
        )

    def test_per_prime_profile(self):
        summary = {
            int(profile["prime"]): (
                int(profile["finite_exponent_R_count"]),
                int(profile["directed_orientation_count"]),
                int(profile["raw_shared_pullback_orientation_count"]),
                int(profile["subgroup_shared_pullback_orientation_count"]),
            )
            for profile in self.actual["profiles"]
        }
        self.assertEqual(
            summary,
            {
                67369: (5, 6, 0, 0),
                878089: (2, 4, 0, 0),
                13782409: (9, 17, 1, 1),
                26034649: (6, 8, 2, 1),
                57399241: (24, 36, 3, 2),
                152498329: (12, 18, 0, 0),
                283319689: (13, 21, 1, 1),
            },
        )

    def test_all_subgroup_visible_rows_stay_outside_finite_box(self):
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                for orientation in record["orientations"]:
                    self.assertEqual(
                        int(orientation["finite_shared_alignment_count"]), 0
                    )
                    for witness in orientation.get(
                        "subgroup_pullback_exponent_overflow", {}
                    ).values():
                        self.assertGreater(int(witness["minimum_extra_exponent"]), 0)


if __name__ == "__main__":
    unittest.main()
