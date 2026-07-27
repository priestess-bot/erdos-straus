import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_pminusone_miss_upper_half_profile_500m",
    ROOT / "reproductions" / "type_i_pminusone_miss_upper_half_profile_500m.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIPMinusOneMissUpperHalfProfile500MTests(unittest.TestCase):
    def test_first_pminusone_residual_rebuilds_as_non_pminusone_upper_half_bridge(self):
        minimum_source = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-min-source-distance-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        raw = next(record for record in minimum_source["records"] if record["prime"] == 297_049)
        actual = profile.rebuild_record(297_049, raw["minimum_source_witness"])
        self.assertEqual(actual["source_denominator"], 297_024)
        self.assertEqual(actual["source_distance"], 25)
        self.assertEqual(actual["E"], 476)
        self.assertLess(actual["a"], actual["b"])

    def test_profile_artifact_partitions_all_pminusone_misses(self):
        pminusone = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-pminusone-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        minimum_source = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-min-source-distance-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT / "reproductions" / "type-i-pminusone-miss-upper-half-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(pminusone, minimum_source)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["p_minus_one_miss_count"],
                actual["joined_minimum_source_count"],
                actual["upper_half_small_side_count"],
                actual["upper_half_failures"],
            ),
            (185, 185, 185, []),
        )
        self.assertGreater(actual["minimum_source_distance"], 1)


if __name__ == "__main__":
    unittest.main()
