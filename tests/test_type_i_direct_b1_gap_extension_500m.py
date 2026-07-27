import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_direct_b1_gap_extension_500m",
    ROOT / "reproductions" / "type_i_direct_b1_gap_extension_500m.py",
)
assert SPEC and SPEC.loader
extension = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = extension
SPEC.loader.exec_module(extension)


class TypeIDirectBOneGapExtension500MTests(unittest.TestCase):
    def test_extension_closes_all_direct_b_one_residuals(self):
        tail = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-direct-b1-gap-extension-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = extension.run_audit(tail)
        self.assertEqual(actual, expected)
        self.assertEqual(actual["direct_b_one_count"], 1713)
        self.assertEqual(actual["residuals"], [39407449, 63332329, 172657489, 193288489])
        self.assertEqual(
            [record["witness"]["gap"] for record in actual["extensions"]],
            [535, 351, 707, 271],
        )
        self.assertEqual((actual["misses"], actual["maximum_selected_gap"]), ([], 707))


if __name__ == "__main__":
    unittest.main()
