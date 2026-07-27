import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_one_collision_source_profile",
    ROOT / "reproductions" / "type_ii_one_collision_source_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIOneCollisionSourceProfileTests(unittest.TestCase):
    def test_three_hundred_million_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-one-collision-source-h19-300m-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 300_000_000)
        self.assertEqual(result["one_collision_state_count"], 7)
        self.assertEqual(
            [row["collision_prime"] for row in result["records"]],
            [3, 5, 13, 3, 17, 7, 3],
        )
        record = next(row for row in result["records"] if row["prime"] == 283_163_161)
        self.assertEqual(record["collision_prime"], 3)
        self.assertEqual(record["new_prime"], 1_201)
        self.assertEqual(record["target_shift"], 53)
        self.assertEqual(record["new_prime_target_residue"], record["forced_target_residue"])

    def test_one_billion_checked_artifact(self):
        path = ROOT / "reproductions" / "type-ii-one-collision-source-h19-1b-results.json"
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["one_collision_state_count"], 10)
        self.assertEqual(
            [row["collision_prime"] for row in result["records"]],
            [3, 5, 13, 3, 17, 7, 3, 3, 13, 5],
        )
        self.assertTrue(
            all(
                row["new_prime_target_residue"] == row["forced_target_residue"]
                for row in result["records"]
            )
        )
        record = next(row for row in result["records"] if row["prime"] == 625_826_881)
        self.assertEqual(record["collision_prime"], 13)
        self.assertEqual(record["source_shifts"], [12])
        self.assertEqual(record["target_shift"], 51)


if __name__ == "__main__":
    unittest.main()
