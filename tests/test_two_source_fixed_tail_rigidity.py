import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "two_source_fixed_tail_rigidity",
    ROOT / "reproductions" / "two_source_fixed_tail_rigidity.py",
)
assert SPEC and SPEC.loader
rigidity = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rigidity
SPEC.loader.exec_module(rigidity)


class TwoSourceFixedTailRigidityTests(unittest.TestCase):
    def test_distinct_sources_and_fixed_tails_are_nonproportional(self):
        result = rigidity.run_audit()
        self.assertEqual(result["representative_profile_count"], 528)
        self.assertTrue(
            all(
                profile["sources_nonproportional"]
                and profile["tail_difference_nonconstant"]
                and profile["tail_difference_with_left_determinant"] != 0
                and profile["tail_difference_with_right_determinant"] != 0
                for profile in result["profiles"]
            )
        )

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "two-source-fixed-tail-rigidity.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["representative_profile_count"], 528)


if __name__ == "__main__":
    unittest.main()
