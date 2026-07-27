import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_subgroup_profile",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_subgroup_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19FourthEvenSourceSubgroupProfileTests(unittest.TestCase):
    def test_checked_artifact_splits_the_two_failure_types(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-subgroup-profile-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["tail_ray_count"], 33)
        self.assertEqual(
            result["classification_counts"],
            {"finite-product-set": 9, "hit": 1, "subgroup-character": 23},
        )
        self.assertEqual(
            result["records"][-1],
            {
                "distance": 34_091,
                "r": 15,
                "target_residue": 11,
                "generator_primes": [2, 19, 37, 127, 13_457],
                "generated_subgroup_index": 1,
                "generated_subgroup_order": 8,
                "target_in_generated_subgroup": True,
                "tail_residue_factor_count": 12,
                "classification": "hit",
            },
        )

    def test_nonunit_targets_are_rejected(self):
        with self.assertRaises(ValueError):
            profile.unit_exponent_vector(15, 3)


if __name__ == "__main__":
    unittest.main()
