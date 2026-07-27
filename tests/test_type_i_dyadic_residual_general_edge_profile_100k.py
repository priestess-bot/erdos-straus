import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_dyadic_residual_general_edge_profile_100k",
    ROOT / "reproductions" / "type_i_dyadic_residual_general_edge_profile_100k.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIDyadicResidualGeneralEdgeProfile100KTests(unittest.TestCase):
    def setUp(self):
        self.expected = json.loads(
            (ROOT / "reproductions" / "type-i-dyadic-residual-general-edge-profile-100k-results.json").read_text(
                encoding="utf-8"
            )
        )

    def test_stored_certificates_verify(self):
        profile.verify_result(self.expected)

    def test_complete_profile_rebuilds(self):
        actual = profile.run_profile()
        self.assertEqual(actual, self.expected)
        self.assertEqual(actual["input_residual_count"], 94)
        self.assertEqual(actual["p_minus_one_low_b_count"], 93)
        self.assertEqual(actual["minimum_source_distance_histogram"], {"1": 93, "61": 1})
        self.assertEqual(actual["minimum_source_distance_maximum"], 61)
        self.assertEqual(actual["minimum_odd_bridge_support_histogram"], {"0": 7, "1": 87})
        exception = next(
            record
            for record in actual["records"]
            if record["minimum_source_distance"]["source_distance"] > 1
        )
        self.assertEqual(exception["prime"], 20_521)
        self.assertEqual(exception["minimum_source_distance"]["E"], 3_844)


if __name__ == "__main__":
    unittest.main()
