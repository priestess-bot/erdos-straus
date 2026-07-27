import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_b4_prefix_boundary_21169",
    ROOT / "reproductions" / "type_i_b4_prefix_boundary_21169.py",
)
assert SPEC and SPEC.loader
prefix = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prefix
SPEC.loader.exec_module(prefix)


class TypeIBFourPrefixBoundary21169Tests(unittest.TestCase):
    def test_complete_prefix_rebuilds(self):
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-b4-prefix-boundary-21169-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = prefix.run_audit()
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["prime_limit"], actual["b_cap"], actual["core_prime_count"], actual["captured_count"]),
            (21169, 4, 281, 280),
        )
        self.assertEqual((actual["misses"], actual["first_miss"]), ([21169], 21169))


if __name__ == "__main__":
    unittest.main()
