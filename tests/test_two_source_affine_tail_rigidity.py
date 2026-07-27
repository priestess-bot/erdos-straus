import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "two_source_affine_tail_rigidity",
    ROOT / "reproductions" / "two_source_affine_tail_rigidity.py",
)
assert SPEC and SPEC.loader
rigidity = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rigidity
SPEC.loader.exec_module(rigidity)


class TwoSourceAffineTailRigidityTests(unittest.TestCase):
    def test_unique_positive_exception_has_nonintegral_tail(self):
        profile = rigidity.affine_candidate_profile(
            1_552_726_375_200, 932_109_739_201, 2, 1
        )
        self.assertTrue(profile["positive_proportional_exception"])
        self.assertEqual(profile["c_over_M"], {"numerator": 1, "denominator": 1})
        self.assertEqual(profile["v_over_N"], {"numerator": 1, "denominator": 3})
        self.assertTrue(profile["tail_never_integral"])

    def test_reverse_scale_has_no_positive_exception(self):
        profile = rigidity.affine_candidate_profile(
            1_552_726_375_200, 932_109_739_201, 1, 2
        )
        self.assertFalse(profile["positive_proportional_exception"])

    def test_representative_audit_and_artifact(self):
        result = rigidity.run_audit()
        self.assertEqual(result["representative_profile_count"], 132)
        self.assertEqual(result["positive_exception_count"], 66)
        self.assertTrue(
            all(
                profile["tail_never_integral"]
                for profile in result["profiles"]
                if profile["positive_proportional_exception"]
            )
        )
        with (
            ROOT / "reproductions" / "two-source-affine-tail-rigidity.json"
        ).open(encoding="utf-8") as handle:
            artifact = json.load(handle)
        self.assertEqual(artifact["positive_exception_count"], 66)


if __name__ == "__main__":
    unittest.main()
