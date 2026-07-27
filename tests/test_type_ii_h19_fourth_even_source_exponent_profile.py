import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_h19_fourth_even_source_exponent_profile",
    ROOT / "reproductions" / "type_ii_h19_fourth_even_source_exponent_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIIH19FourthEvenSourceExponentProfileTests(unittest.TestCase):
    def test_checked_artifact_quantifies_exponent_deficits(self):
        path = (
            ROOT
            / "reproductions"
            / "type-ii-h19-fourth-even-source-exponent-profile-640775689-results.json"
        )
        with path.open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["prime"], 640_775_689)
        self.assertEqual(result["power_cap"], 12)
        self.assertEqual(result["finite_product_state_count"], 9)
        self.assertEqual(
            result["first_cover_power_histogram"],
            {">12": 3, "3": 1, "5": 1, "7": 4},
        )
        self.assertEqual(
            [
                (row["distance"], row["first_cover_power_through_cap"])
                for row in result["records"]
            ],
            [
                (1, None),
                (1, 7),
                (1, 7),
                (5, 3),
                (7, None),
                (21, None),
                (701, 7),
                (14721, 7),
                (16323, 5),
            ],
        )

    def test_small_power_caps_are_rejected(self):
        with self.assertRaises(ValueError):
            profile.run_profile({}, {}, 1)


if __name__ == "__main__":
    unittest.main()
