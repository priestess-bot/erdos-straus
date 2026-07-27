import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_low_e_joint_residual_profile_10m",
    ROOT / "reproductions" / "type_i_pminusone_low_e_joint_residual_profile_1m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIPMinusOneLowEJointResidualProfile10MTests(unittest.TestCase):
    def test_complete_low_e_refinement_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-pminusone-low-e1m-all-b-joint-residual-profile-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile(
            ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-10m-results.json",
            ROOT / "reproductions" / "type-i-pminusone-b12-menu-profile-10m-results.json",
            1_000_000,
            None,
        )
        self.assertEqual(actual, expected)
        self.assertEqual((actual["joint_residual_count"], actual["captured_count"]), (152, 140))
        self.assertEqual(
            actual["misses"],
            [
                297049,
                513529,
                710089,
                1083289,
                1103449,
                1708009,
                2469289,
                3389929,
                3942409,
                4762489,
                5180569,
                5770249,
            ],
        )
        self.assertEqual(actual["selected_B_histogram"]["2701"], 1)


if __name__ == "__main__":
    unittest.main()
