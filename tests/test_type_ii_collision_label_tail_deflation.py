import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_collision_label_tail_deflation",
    ROOT / "reproductions" / "type_ii_collision_label_tail_deflation.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class TypeIICollisionLabelTailDeflationTests(unittest.TestCase):
    def test_one_billion_collision_labelled_certificate_profile(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-collision-label-tail-deflation-h19-1b-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["collision_labelled_state_count"], 11)
        self.assertEqual(result["marked_tail_descent_count"], 2)
        self.assertEqual(
            result["marked_tail_descent_misses"],
            [
                9_744_001,
                55_722_241,
                178_400_041,
                192_369_241,
                283_163_161,
                362_665_921,
                372_271_201,
                625_826_881,
                751_064_161,
            ],
        )
        hits = [record for record in result["records"] if record["marked_tail_witness"]]
        self.assertEqual([record["prime"] for record in hits], [345_601, 92_421_169])
        self.assertTrue(all(record["marked_tail_witness"]["first_scale"] == 1 for record in hits))
        two_collision = next(record for record in result["records"] if record["prime"] == 372_271_201)
        self.assertEqual(two_collision["collision_multiplicity"], 2)
        self.assertIsNone(two_collision["marked_tail_witness"])


if __name__ == "__main__":
    unittest.main()
