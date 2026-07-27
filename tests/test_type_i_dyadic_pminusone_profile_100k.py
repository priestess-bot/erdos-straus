import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_dyadic_pminusone_profile_100k",
    ROOT / "reproductions" / "type_i_dyadic_pminusone_profile_100k.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIDyadicPMinusOneProfile100KTests(unittest.TestCase):
    def test_complete_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-100k-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["core_prime_count"], actual["captured_count"]), (1181, 1087))
        self.assertEqual(len(actual["misses"]), 94)
        self.assertEqual(actual["misses"][:5], [241, 2089, 3049, 4729, 5209])
        self.assertEqual((actual["maximum_allowed_exponent"], actual["maximum_selected_exponent"]), (22, 9))
        self.assertEqual(
            actual["selected_exponent_histogram"],
            {"2": 605, "3": 332, "4": 116, "5": 22, "6": 8, "8": 2, "9": 2},
        )


if __name__ == "__main__":
    unittest.main()
