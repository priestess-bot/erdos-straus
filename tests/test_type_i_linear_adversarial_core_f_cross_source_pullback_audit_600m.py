import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "reproductions"
    / "type_i_linear_adversarial_core_f_cross_source_pullback_audit_600m.py"
)
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-adversarial-core-f-cross-source-pullback-audit-600m-results.json"
)

spec = importlib.util.spec_from_file_location("cross_source_pullback_audit", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load cross-source pullback audit")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CrossSourcePullbackAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.stored = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_global_counts_and_digest(self):
        self.assertEqual(self.actual, self.stored)
        self.assertEqual(self.actual["finite_exponent_R_count"], 45)
        self.assertEqual(self.actual["directed_orientation_count"], 69)
        self.assertEqual(self.actual["pairwise_gcd_identity_count"], 3882)
        self.assertEqual(
            self.actual["raw_shared_pullback_orientation_count"], 6
        )
        self.assertEqual(
            self.actual["subgroup_shared_pullback_orientation_count"], 4
        )
        self.assertEqual(
            self.actual["finite_shared_alignment_orientation_count"], 0
        )
        self.assertEqual(self.actual["raw_shared_pullback_residue_count"], 32)
        self.assertEqual(
            self.actual["subgroup_shared_pullback_residue_count"], 14
        )
        self.assertEqual(
            self.actual["subgroup_pullback_exponent_overflow_distribution"],
            {"1": 6, "2": 2, "6": 2, "7": 2, "8": 2},
        )
        self.assertEqual(
            self.actual["minimum_subgroup_pullback_exponent_overflow"], 1
        )
        self.assertEqual(
            self.actual["maximum_subgroup_pullback_exponent_overflow"], 8
        )
        self.assertEqual(
            self.actual["record_sha256"],
            "3fb5de592e621f446e1a227e820b18ad0b12528683e18e8ad1cfc0c7bc9ab845",
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
                878089: (2, 4, 0, 0),
                26034649: (6, 8, 2, 1),
                57399241: (24, 36, 3, 2),
                283319689: (13, 21, 1, 1),
            },
        )

    def test_latent_rows_are_outside_finite_box(self):
        rows = {
            (
                int(row["prime"]),
                int(row["R"]),
                int(row["a"]),
                int(row["s"]),
            ): (
                row["raw_shared_pullback_residues"],
                row["subgroup_shared_pullback_residues"],
            )
            for row in self.actual["latent_subgroup_rows"]
        }
        self.assertEqual(
            rows,
            {
                (26034649, 375, 73, 951): ([86, 266], [86, 266]),
                (57399241, 155, 1755, 211): (
                    [23, 27, 37, 44, 67, 74, 81, 88, 111, 118, 128, 132],
                    [128, 132],
                ),
                (57399241, 567, 101055, 1): (
                    [248, 496, 551, 559],
                    [248, 496, 551, 559],
                ),
                (283319689, 1247, 93, 2443): (
                    [237, 275, 762, 905, 984, 1229],
                    [237, 275, 762, 905, 984, 1229],
                ),
            },
        )

    def test_exponent_overflow_witnesses(self):
        witnesses = {}
        for profile in self.actual["profiles"]:
            for record in profile["records"]:
                for orientation in record["orientations"]:
                    for residue, witness in orientation.get(
                        "subgroup_pullback_exponent_overflow", {}
                    ).items():
                        witnesses[
                            (
                                int(profile["prime"]),
                                int(record["R"]),
                                int(orientation["a"]),
                                int(orientation["s"]),
                                int(residue),
                            )
                        ] = (
                            int(witness["minimum_extra_exponent"]),
                            witness["vector"],
                        )
        self.assertEqual(
            witnesses[(26034649, 375, 73, 951, 86)],
            (1, [2, 1, -2]),
        )
        self.assertEqual(
            witnesses[(57399241, 155, 1755, 211, 128)],
            (6, [-7]),
        )
        self.assertEqual(
            witnesses[(283319689, 1247, 93, 2443, 762)],
            (8, [4, 8, -9]),
        )


if __name__ == "__main__":
    unittest.main()
