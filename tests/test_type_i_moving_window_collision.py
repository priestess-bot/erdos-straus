import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_moving_window_collision",
    ROOT / "reproductions" / "type_i_moving_window_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class TypeIMovingWindowCollisionTests(unittest.TestCase):
    def test_first_six_gap_failure_profile(self):
        result = collision.run_audit(21_169, 7)
        self.assertEqual(result["collision_primes"], (2, 3, 5))
        self.assertTrue(result["private_cofactors_pairwise_coprime"])
        self.assertEqual([row["gap"] for row in result["rows"]], [3, 7, 11, 15, 19, 23, 27])
        self.assertEqual(result["rows"][0]["target"], 2)
        self.assertEqual(result["rows"][-1]["target"], 20)

    def test_checked_artifact_summary(self):
        with (
            ROOT / "reproductions" / "type-i-moving-window-collision-p21169-j7-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 21_169)
        self.assertEqual(result["window_j"], 7)
        self.assertEqual(result["collision_primes"], [2, 3, 5])
        self.assertTrue(result["private_cofactors_pairwise_coprime"])
        self.assertEqual(len(result["rows"]), 7)


if __name__ == "__main__":
    unittest.main()
