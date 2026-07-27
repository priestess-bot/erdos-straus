import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_small_side_profile",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_small_side_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailReverseEvenSourceSmallSideProfileTests(unittest.TestCase):
    def test_complete_large_side_reclassification_rebuilds(self):
        source = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-ratio-pair-audit-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-small-side-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["record_count"],
                actual["selected_small_side_count"],
                actual["selected_large_side_count"],
                actual["large_side_with_small_alternative_count"],
                actual["large_side_only_count"],
                actual["small_side_available_count"],
            ),
            (1_717, 1_421, 296, 201, 95, 1_622),
        )
        self.assertEqual(
            actual["examples"]["large_side_with_small_alternative"]["canonical_small_side_pair"],
            {"E": 8, "a": 1, "b": 162_929, "source_denominator": 372_408},
        )
        self.assertIsNone(actual["examples"]["large_side_only"]["canonical_small_side_pair"])


if __name__ == "__main__":
    unittest.main()
