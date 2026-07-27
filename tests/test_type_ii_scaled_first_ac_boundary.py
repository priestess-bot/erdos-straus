import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_scaled_first_ac_boundary",
    ROOT / "reproductions" / "type_ii_scaled_first_ac_boundary.py",
)
assert SPEC and SPEC.loader
scaled_first_ac_boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scaled_first_ac_boundary
SPEC.loader.exec_module(scaled_first_ac_boundary)


class TypeIIScaledFirstACBoundaryTests(unittest.TestCase):
    def test_three_million_ac14_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-scaled-first-ac14-3m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["input_residual_count"], 41)
        self.assertEqual(result["bounded_ac_hit_count"], 30)
        self.assertEqual(result["bounded_ac_miss_count"], 11)
        self.assertEqual(
            result["bounded_ac_misses"],
            [
                67_369,
                225_289,
                532_249,
                852_889,
                878_089,
                1_093_129,
                1_854_889,
                1_936_489,
                2_020_489,
                2_254_729,
                2_707_609,
            ],
        )
        record = next(item for item in result["records"] if item["prime"] == 85_369)
        self.assertEqual(
            (
                record["witness"]["a"],
                record["witness"]["c"],
                record["witness"]["witness"]["first_scale"],
            ),
            (5, 14, 9),
        )
