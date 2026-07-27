import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_joint_residual_general_edge_profile_1m",
    ROOT / "reproductions" / "type_i_joint_residual_general_edge_profile_1m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIJointResidualGeneralEdgeProfile1MTests(unittest.TestCase):
    def test_complete_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-1m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual(actual["minimum_source_distance_histogram"], {"9": 2, "25": 1})
        witnesses = {
            record["prime"]: record["minimum_source_distance"]
            for record in actual["records"]
        }
        self.assertEqual(
            {
                prime: (witness["source_denominator"], witness["E"], witness["normal_form"][1])
                for prime, witness in witnesses.items()
            },
            {
                297_049: (297_024, 476, 1),
                513_529: (513_520, 280, 1),
                710_089: (710_080, 280, 1),
            },
        )


if __name__ == "__main__":
    unittest.main()
