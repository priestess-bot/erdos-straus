import json
import unittest
from pathlib import Path

from reproductions import type_i_fixed_ray_residual_resolution_600m as profile


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "reproductions" / "type-i-fixed-ray-residual-resolution-600m-results.json"


class TypeIFixedRayResidualResolution600MTests(unittest.TestCase):
    def test_residual_has_the_expected_adaptive_resolution_layers(self):
        payload = profile.run_audit()
        self.assertEqual(payload["fixed_ray_residual_count"], 25)
        self.assertEqual(payload["global_pminusone_failure_count_within_residual"], 11)
        self.assertEqual(payload["resolution_counts"], {
            "pminusone_short_box": 2,
            "pminusone_global_extension": 12,
            "linear_B1_after_global_pminusone_failure": 10,
            "linear_general_B_after_B1_failure": 1,
        })
        general = [record for record in payload["records"] if record["classification"] == "linear_general_B_after_B1_failure"]
        self.assertEqual(len(general), 1)
        self.assertEqual(general[0]["prime"], 3942409)
        self.assertEqual(general[0]["witness"]["B"], 7)
        self.assertEqual(general[0]["witness"]["beta"], 1)

    def test_checked_in_artifact_is_reproducible(self):
        self.assertEqual(json.loads(RESULT.read_text(encoding="utf-8")), profile.run_audit())


if __name__ == "__main__":
    unittest.main()
