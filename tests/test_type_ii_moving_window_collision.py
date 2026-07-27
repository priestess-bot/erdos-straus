import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_moving_window_collision",
    ROOT / "reproductions" / "type_ii_moving_window_collision.py",
)
assert SPEC and SPEC.loader
collision = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = collision
SPEC.loader.exec_module(collision)


class TypeIIMovingWindowCollisionTests(unittest.TestCase):
    def test_collision_primes_for_window_31(self):
        self.assertEqual(
            collision.collision_primes(31), (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        )

    def test_checked_record_failure_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-moving-window-collision-p153633769-j31-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 153_633_769)
        self.assertEqual(result["window_j"], 31)
        self.assertTrue(result["private_cofactors_pairwise_coprime"])
        self.assertEqual(len(result["rows"]), 31)
        self.assertEqual(result["rows"][-1]["gap"], 123)


if __name__ == "__main__":
    unittest.main()
