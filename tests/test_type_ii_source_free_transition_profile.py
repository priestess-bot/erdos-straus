import importlib.util
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_source_free_transition_profile",
    ROOT / "reproductions" / "type_ii_source_free_transition_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIISourceFreeTransitionProfileTests(unittest.TestCase):
    def test_packed_spf_matches_reference(self):
        packed = profile.packed_smallest_prime_factors(10_000)
        reference = profile.release.compact_smallest_prime_factors(10_000)
        self.assertEqual(len(packed), len(reference))
        self.assertEqual(
            [packed[value] for value in range(2, 10_001)], list(reference[2:])
        )

    def test_segmented_core_sieve_matches_reference(self):
        self.assertEqual(
            list(profile.segmented_core_primes_up_to(10_000, segment_size=257)),
            [
                prime
                for prime in profile.release.core_primes_up_to(10_000)
                if prime % 24 == 1
            ],
        )

    def test_small_profile(self):
        result = profile.run_profile(10_000, 19, 125)
        self.assertEqual(result["base_residual_count"], 1)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(
            result["profiles"],
            [
                {
                    "prime": 3_361,
                    "first_source_free_shift": 125,
                    "selected_witness": {
                        "h": 99,
                        "a": 5,
                        "c": 5,
                        "k": 1,
                        "gap": 39,
                        "divisor": 125,
                        "collision_multiplicity": 3,
                        "old_private_multiplicity": 0,
                        "new_multiplicity": 0,
                    },
                }
            ],
        )

    def test_checked_h19_hundred_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-100m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 164)
        self.assertEqual(result["source_free_count"], 164)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(result["collision_only_count"], 32)
        self.assertEqual(result["new_factor_count"], 132)
        self.assertEqual(result["pure_new_factor_count"], 64)
        self.assertEqual(
            result["source_mechanism_histogram"],
            {
                "collision:0,new:1": 54, "collision:0,new:2": 10,
                "collision:1,new:1": 38, "collision:1,new:2": 5,
                "collision:2,new:0": 25, "collision:2,new:1": 19,
                "collision:2,new:2": 2, "collision:3,new:0": 2,
                "collision:3,new:1": 3, "collision:4,new:0": 4,
                "collision:4,new:1": 1, "collision:5,new:0": 1,
            },
        )
        self.assertEqual(
            result["first_source_free_shift_histogram"],
            {
                "20": 38, "21": 7, "22": 5, "23": 15, "24": 19,
                "25": 14, "26": 20, "27": 8, "28": 1, "29": 6,
                "30": 2, "31": 3, "32": 5, "33": 1, "34": 1,
                "36": 11, "41": 2, "46": 1, "49": 1, "50": 2,
                "52": 1, "125": 1,
            },
        )
        tail = {
            row["prime"]: row["selected_witness"]
            for row in result["profiles"]
            if row["first_source_free_shift"] >= 51
        }
        self.assertEqual(
            tail,
            {
                3_361: {
                    "h": 99, "a": 5, "c": 5, "k": 1, "gap": 39,
                    "divisor": 125, "collision_multiplicity": 3,
                    "old_private_multiplicity": 0, "new_multiplicity": 0,
                },
                81_846_241: {
                    "h": 60_943, "a": 2, "c": 13, "k": 586, "gap": 1_343,
                    "divisor": 52, "collision_multiplicity": 0,
                    "old_private_multiplicity": 0, "new_multiplicity": 1,
                },
            },
        )

    def test_checked_h19_one_hundred_fifty_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-150m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 208)
        self.assertEqual(result["source_free_count"], 208)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(
            [
                row["prime"]
                for row in result["profiles"]
                if row["first_source_free_shift"] >= 125
            ],
            [3_361],
        )

    def test_checked_h19_two_hundred_million_artifact(self):
        with (
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-200m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["base_residual_count"], 255)
        self.assertEqual(result["source_free_count"], 255)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(
            [
                row["prime"]
                for row in result["profiles"]
                if row["first_source_free_shift"] >= 125
            ],
            [3_361],
        )
        collision_rays = Counter(
            (
                row["selected_witness"]["a"],
                row["selected_witness"]["c"],
                row["selected_witness"]["k"],
                row["selected_witness"]["h"],
            )
            for row in result["profiles"]
            if row["selected_witness"]["new_multiplicity"] == 0
        )
        self.assertEqual(
            collision_rays,
            {
                (2, 5, 1, 39): 36, (2, 5, 3, 119): 6,
                (2, 6, 3, 143): 3, (1, 31, 24, 2_975): 2,
                (3, 3, 4, 143): 2, (1, 23, 5, 459): 1,
                (1, 26, 9, 935): 1, (1, 26, 20, 2_079): 1,
                (4, 2, 11, 351): 1, (5, 2, 1, 39): 1,
                (5, 5, 1, 99): 1, (9, 1, 4, 143): 1,
            },
        )

    def test_checked_h19_five_hundred_million_artifact_extends_three_hundred_million(self):
        paths = [
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-300m-results.json",
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-500m-results.json",
        ]
        with paths[0].open(encoding="utf-8") as handle:
            smaller = json.load(handle)
        with paths[1].open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 500_000_000)
        self.assertEqual(result["base_residual_count"], 425)
        self.assertEqual(result["source_free_count"], 425)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(
            [
                {key: row[key] for key in ("prime", "first_source_free_shift", "selected_witness")}
                for row in result["profiles"]
                if row["prime"] <= 300_000_000
            ],
            [
                {key: row[key] for key in ("prime", "first_source_free_shift", "selected_witness")}
                for row in smaller["profiles"]
            ],
        )

    def test_checked_h19_one_billion_artifact_extends_five_hundred_million(self):
        paths = [
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-500m-results.json",
            ROOT / "reproductions" / "type-ii-source-free-transition-h19-1b-results.json",
        ]
        with paths[0].open(encoding="utf-8") as handle:
            smaller = json.load(handle)
        with paths[1].open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime_limit"], 1_000_000_000)
        self.assertEqual(result["base_residual_count"], 664)
        self.assertEqual(result["source_free_count"], 664)
        self.assertEqual(result["missing_through_cap"], [])
        self.assertEqual(result["maximum_first_source_free_shift"], 125)
        self.assertEqual(
            [
                {key: row[key] for key in ("prime", "first_source_free_shift", "selected_witness")}
                for row in result["profiles"]
                if row["prime"] <= 500_000_000
            ],
            [
                {key: row[key] for key in ("prime", "first_source_free_shift", "selected_witness")}
                for row in smaller["profiles"]
            ],
        )


if __name__ == "__main__":
    unittest.main()
