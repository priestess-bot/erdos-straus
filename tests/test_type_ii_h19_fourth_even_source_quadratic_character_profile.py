import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_quadratic_character_profile",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_quadratic_character_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19FourthEvenSourceQuadraticCharacterProfileTests(unittest.TestCase):
    def test_checked_artifact_has_no_higher_order_remainder(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-quadratic-character-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["subgroup_character_ray_count"], 23)
        self.assertEqual(result["quadratically_separated_count"], 23)
        self.assertEqual(result["higher_order_remainder_count"], 0)
        self.assertEqual(
            result["records"][-1],
            {
                "distance": 6901,
                "r": 23,
                "generated_subgroup_index": 2,
                "quadratic_character_support": [23],
            },
        )

    def test_nonunit_values_are_rejected(self):
        with self.assertRaises(ValueError):
            profile.quadratic_character((3,), 3)


if __name__ == "__main__":
    unittest.main()
