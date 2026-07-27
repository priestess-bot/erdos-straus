import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_h19_even_source_support_external_hybrid",
    ROOT / "reproductions" / "type_i_h19_even_source_support_external_hybrid.py",
)
assert SPEC and SPEC.loader
hybrid = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class TypeIH19EvenSourceSupportExternalHybridTests(unittest.TestCase):
    def test_support_four_boundary_rebuilds_to_an_even_external_source(self):
        support = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-min-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        expected = json.loads(
            (ROOT / "reproductions" / "type-i-h19-even-source-support-external-hybrid-1b-results.json").read_text(
                encoding="utf-8"
            )
        )
        actual = hybrid.run_audit(support)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["support_at_most_three_even_bridge_count"],
                actual["zero_offset_external_boundary_count"],
                actual["unclosed_primes"],
            ),
            (663, 1, []),
        )
        witness = actual["records"][0]["zero_offset_external_descent"]
        self.assertEqual((witness["shift"], witness["source_denominator"] % 2), (1, 0))


if __name__ == "__main__":
    unittest.main()
