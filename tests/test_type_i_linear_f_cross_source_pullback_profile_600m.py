import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_f_cross_source_pullback_profile_600m.py"
ARTIFACT = (
    ROOT
    / "reproductions"
    / "type-i-linear-f-cross-source-pullback-profile-600m-results.json"
)

spec = importlib.util.spec_from_file_location("seven_spectrum_pullback", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load seven-spectrum pullback profile")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class SevenSpectrumPullbackProfileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual = module.run_audit()
        cls.stored = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_global_counts_and_digest(self):
        self.assertEqual(self.actual, self.stored)
        self.assertEqual(self.actual["prime_count"], 7)
        self.assertEqual(self.actual["finite_exponent_R_count"], 68)
        self.assertEqual(self.actual["directed_orientation_count"], 105)
        self.assertEqual(self.actual["pairwise_gcd_identity_count"], 5853)
        self.assertEqual(
            self.actual["raw_shared_pullback_orientation_count"], 8
        )
        self.assertEqual(
            self.actual["subgroup_shared_pullback_orientation_count"], 6
        )
        self.assertEqual(
            self.actual["finite_shared_alignment_orientation_count"], 0
        )
        self.assertEqual(self.actual["raw_shared_pullback_residue_count"], 100)
        self.assertEqual(
            self.actual["subgroup_shared_pullback_residue_count"], 80
        )
        self.assertEqual(
            self.actual["record_sha256"],
            "e97e13c805fc5a7bfe99f1ad108252fb3dd0f3c1282576dded9466f798ba56dc",
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
                214729: (8, 13, 1, 1),
                878089: (2, 4, 0, 0),
                2210569: (4, 5, 0, 0),
                13782409: (9, 17, 1, 1),
                64214329: (18, 26, 4, 2),
                105295129: (10, 13, 2, 2),
                536944489: (17, 27, 0, 0),
            },
        )

    def test_concentrated_boundary(self):
        row = next(
            orientation
            for profile in self.actual["profiles"]
            if int(profile["prime"]) == 64214329
            for record in profile["records"]
            if int(record["R"]) == 359
            for orientation in record["orientations"]
            if int(orientation["a"]) == 7154
            and int(orientation["s"]) == 25
        )
        self.assertEqual(row["raw_shared_pullback_count"], 60)
        self.assertEqual(row["subgroup_shared_pullback_count"], 60)
        self.assertEqual(row["finite_shared_alignment_count"], 0)


if __name__ == "__main__":
    unittest.main()
