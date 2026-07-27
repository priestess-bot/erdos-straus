import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_even_source_support_external_hybrid",
    ROOT / "reproductions" / "type_i_even_source_support_external_hybrid.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeIEvenSourceSupportExternalHybridTests(unittest.TestCase):
    def test_shifted_external_branch_closes_both_support_four_points(self):
        support = json.loads(
            (ROOT / "reproductions" / "type-i-tail-reverse-even-source-support-min-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        offset = json.loads(
            (ROOT / "reproductions" / "type-ii-tail-shifted-quadratic-offset-profile-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-even-source-support-external-hybrid-500m-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = hybrid.run_audit(support, offset)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (actual["support_at_most_three_even_bridge_count"], actual["shifted_offset_histogram"], actual["unclosed_primes"]),
            (1_715, {"5": 1, "9": 1}, []),
        )


if __name__ == "__main__":
    unittest.main()
