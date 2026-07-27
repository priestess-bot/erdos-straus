import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERAL_SPEC = importlib.util.spec_from_file_location(
    "type_i_joint_residual_general_edge_profile_10m_general",
    ROOT / "reproductions" / "type_i_dyadic_residual_general_edge_profile_100k.py",
)
assert GENERAL_SPEC and GENERAL_SPEC.loader
general = importlib.util.module_from_spec(GENERAL_SPEC)
sys.modules[GENERAL_SPEC.name] = general
GENERAL_SPEC.loader.exec_module(general)


class TypeIJointResidualGeneralEdgeProfile10MTests(unittest.TestCase):
    def test_stored_short_source_certificates_verify(self):
        payload = json.loads(
            (ROOT / "reproductions" / "type-i-joint-residual-general-edge-profile-10m-results.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual((payload["input_residual_count"], payload["b_cap"]), (7, 4))
        self.assertEqual(payload["minimum_source_distance_histogram"], {"3": 1, "9": 2, "25": 2, "49": 1, "263": 1})
        for record in payload["records"]:
            general.verify_witness(record["prime"], record["minimum_source_distance"])
            general.verify_witness(record["prime"], record["minimum_odd_bridge"])
        self.assertEqual(
            [
                (
                    record["prime"],
                    record["minimum_source_distance"]["source_distance"],
                    record["minimum_source_distance"]["R"],
                    record["minimum_source_distance"]["normal_form"][1],
                )
                for record in payload["records"]
            ],
            [
                (1083289, 25, 131, 1),
                (1103449, 25, 215, 1),
                (2469289, 9, 39, 1),
                (3389929, 49, 191, 1),
                (3942409, 263, 95, 2),
                (4762489, 9, 131, 3),
                (5770249, 3, 19, 1),
            ],
        )


if __name__ == "__main__":
    unittest.main()
