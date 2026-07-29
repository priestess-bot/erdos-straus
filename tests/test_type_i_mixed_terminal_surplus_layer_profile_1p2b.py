"""Verify the seven-interval surplus-layer profile."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_mixed_terminal_surplus_layer_profile_1p2b.py"
ARTIFACT = ROOT / "reproductions" / "type-i-mixed-terminal-surplus-layer-profile-1p2b-results.json"
SPEC = importlib.util.spec_from_file_location("surplus_layer_profile", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeIMixedTerminalSurplusLayerProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        cls.actual = profile.run_audit()

    def test_stored_profile_is_reproduced(self):
        self.assertEqual(self.actual, self.expected)
        self.assertEqual(self.actual["interval_count"], 7)
        self.assertEqual(self.actual["record_count"], 1_649)
        self.assertEqual(
            self.actual["category_counts"],
            {"S=1": 63, "multi-prime-support": 1_227, "single-prime-power": 359},
        )
        self.assertEqual(self.actual["side_counts"], {"small-side": 1_383, "large-side": 266})
        self.assertEqual(
            self.actual["side_category_counts"],
            {
                "large-side:multi-prime-support": 213,
                "large-side:single-prime-power": 53,
                "small-side:S=1": 63,
                "small-side:multi-prime-support": 1_014,
                "small-side:single-prime-power": 306,
            },
        )
        self.assertEqual(
            self.actual["support_histogram"],
            {"0": 63, "1": 359, "2": 614, "3": 444, "4": 149, "5": 19, "6": 1},
        )
        self.assertEqual(
            self.actual["single_prime_power_exponent_histogram"],
            {"1": 319, "2": 35, "3": 4, "6": 1},
        )
        self.assertEqual(
            self.actual["distinct_surplus_value_count_by_interval"],
            [230, 197, 247, 222, 205, 226, 210],
        )


if __name__ == "__main__":
    unittest.main()
