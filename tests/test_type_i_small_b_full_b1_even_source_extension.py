import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_small_b_full_b1_even_source_extension",
    ROOT / "reproductions" / "type_i_small_b_full_b1_even_source_extension.py",
)
assert SPEC and SPEC.loader
extension = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = extension
SPEC.loader.exec_module(extension)


class TypeISmallBFullBOneEvenSourceExtensionTests(unittest.TestCase):
    def test_complete_profile_and_exact_boundary_rebuild(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-small-b-full-b1-even-source-extension-20m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = extension.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["captured_count"], actual["maximum_first_gap"]), (2351, 791))
        self.assertEqual(
            actual["misses"], [21169, 2922529, 5101441, 5410441, 5655049]
        )
        self.assertEqual((actual["extension_captured_count"], actual["maximum_extension_first_gap"]), (2, 1671))
        self.assertEqual(actual["extension_misses"], [21169, 5101441, 5655049])
        boundary = actual["exact_boundary"]
        self.assertEqual(boundary["gap_cap"], 21167)
        self.assertEqual((boundary["normal_form_count"], boundary["strict_reverse_lift_count"]), (1, 1))
        self.assertEqual(boundary["all_even_lifts"], [])
        self.assertEqual(
            boundary["all_normal_forms"], [{"gap": 31, "normal_form": [4, 1, 1325]}]
        )


if __name__ == "__main__":
    unittest.main()
