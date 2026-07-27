import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_two_collision_release_boundary",
    ROOT / "reproductions" / "type_ii_h19_two_collision_release_boundary.py",
)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


class TypeIIH19TwoCollisionReleaseBoundaryTests(unittest.TestCase):
    def test_five_hundred_million_state_release_depth(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-two-collision-release-372271201-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 372_271_201)
        self.assertEqual(result["caps"], [200, 400, 401, 483, 484])
        by_cap = {row["shift_cap"]: row for row in result["records"]}
        self.assertEqual(by_cap[200]["best_witness"]["shift"], 89)
        self.assertEqual(by_cap[200]["best_witness"]["collision_multiplicity"], 2)
        self.assertEqual(
            by_cap[200]["best_witness"]["collision_source_labels"],
            [
                {"prime": 3, "source_shifts": [2, 5, 8, 11, 14, 17], "target_shift_residue": 2},
                {"prime": 7, "source_shifts": [5, 12, 19], "target_shift_residue": 5},
            ],
        )
        self.assertIsNone(by_cap[400]["first_zero_or_one_collision"])
        self.assertEqual(by_cap[401]["first_zero_or_one_collision"]["shift"], 401)
        self.assertEqual(
            by_cap[401]["first_zero_or_one_collision"]["h_factorization"],
            [{"prime": 5, "exponent": 1}, {"prime": 26_947, "exponent": 1}],
        )
        self.assertEqual(
            by_cap[401]["first_zero_or_one_collision"]["collision_source_labels"],
            [{"prime": 5, "source_shifts": [1, 6, 11, 16], "target_shift_residue": 1}],
        )
        self.assertIsNone(by_cap[483]["first_pure_new"])
        self.assertEqual(by_cap[484]["first_pure_new"]["shift"], 484)
        self.assertEqual(by_cap[484]["first_pure_new"]["h"], 3_343)
        self.assertEqual(by_cap[484]["first_pure_new"]["collision_source_labels"], [])


if __name__ == "__main__":
    unittest.main()
