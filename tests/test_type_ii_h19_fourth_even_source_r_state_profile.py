import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_r_state_profile",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_r_state_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19FourthEvenSourceRStateProfileTests(unittest.TestCase):
    def test_checked_artifact_compresses_duplicate_tail_states(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-r-state-profile-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["compatible_ray_count"], 33)
        self.assertEqual(result["r_state_count"], 22)
        self.assertEqual(result["ray_multiplicity_histogram"], {"1": 12, "2": 9, "3": 1})
        self.assertEqual(
            result["classification_by_r_state"],
            {"finite-product-set": 6, "hit": 1, "subgroup-character": 15},
        )
        self.assertEqual(
            next(row for row in result["records"] if row["r"] == 23),
            {
                "r": 23,
                "m1": 3_684_460_212,
                "distances": [29, 4037, 6901],
                "ray_multiplicity": 3,
                "tail_residue_factor_count": 0,
                "classification": "subgroup-character",
            },
        )


if __name__ == "__main__":
    unittest.main()
