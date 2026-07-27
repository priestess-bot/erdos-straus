import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_tail_reverse_even_source_small_side_alternative_profile",
    ROOT / "reproductions" / "type_i_tail_reverse_even_source_small_side_alternative_profile.py",
)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeITailReverseEvenSourceSmallSideAlternativeProfileTests(unittest.TestCase):
    def test_alternative_normal_forms_release_every_same_state_residual(self):
        source = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-small-side-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        expected = json.loads(
            (
                ROOT
                / "reproductions"
                / "type-i-tail-reverse-even-source-small-side-alternative-profile-500m-results.json"
            ).read_text(encoding="utf-8")
        )
        actual = profile.run_profile(source)
        self.assertEqual(actual, expected)
        self.assertEqual(
            (
                actual["same_state_large_side_residual_count"],
                actual["alternative_small_side_captured_count"],
                actual["combined_small_side_closure_count"],
                actual["misses"],
            ),
            (95, 95, 1_717, []),
        )
        self.assertEqual(
            actual["records"][0]["alternative_small_side"],
            {
                "gap": 119,
                "normal_form": [74, 3, 76],
                "R": 23,
                "K": 387_372,
                "E": 24,
                "a": 1,
                "b": 32_281,
                "source_denominator": 67_368,
            },
        )


if __name__ == "__main__":
    unittest.main()
