import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_dyadic_pminusone_profile_1m",
    ROOT / "reproductions" / "type_i_dyadic_pminusone_profile_100k.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIDyadicPMinusOneProfile1MTests(unittest.TestCase):
    def test_complete_profile_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-dyadic-pminusone-profile-1m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = profile.run_profile(1_000_009)
        self.assertEqual(actual, expected)
        self.assertEqual((actual["core_prime_count"], actual["captured_count"]), (9732, 9149))
        self.assertEqual(len(actual["misses"]), 583)
        self.assertEqual((actual["maximum_allowed_exponent"], actual["maximum_selected_exponent"]), (34, 9))


if __name__ == "__main__":
    unittest.main()
