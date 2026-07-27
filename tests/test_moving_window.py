import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("moving_window", ROOT / "reproductions" / "moving_window.py")
assert SPEC and SPEC.loader
moving_window = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = moving_window
SPEC.loader.exec_module(moving_window)


class MovingWindowExperimentTests(unittest.TestCase):
    def test_small_window_audit_has_exact_witnesses(self):
        result = moving_window.run_experiment(10_000, 16)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["captured_count"], result["core_prime_count"])
        self.assertEqual(result["largest_first_j"], 6)

    def test_checked_two_hundred_million_j27_artifact(self):
        with (
            ROOT / "reproductions" / "moving-window-j27-200m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 1_383_890)
        self.assertEqual(result["captured_count"], 1_383_889)
        self.assertEqual(result["gap_bound"], 107)
        self.assertEqual(result["missing"], [153_633_769])
        self.assertEqual(result["largest_first_j"], 27)

    def test_checked_two_hundred_million_j32_artifact(self):
        with (
            ROOT / "reproductions" / "moving-window-j32-200m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 1_383_890)
        self.assertEqual(result["captured_count"], 1_383_890)
        self.assertEqual(result["gap_bound"], 127)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_first_j"], 32)
        self.assertEqual(
            result["record_holders"][-1],
            {
                "prime": 153_633_769,
                "j": 32,
                "gap": 127,
                "divisor": 2_821_949,
                "x": 38_408_474,
            },
        )

    def test_checked_five_hundred_million_j32_artifact(self):
        with (
            ROOT / "reproductions" / "moving-window-j32-500m-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["core_prime_count"], 3_292_848)
        self.assertEqual(result["captured_count"], 3_292_848)
        self.assertEqual(result["gap_bound"], 127)
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["largest_first_j"], 32)


if __name__ == "__main__":
    unittest.main()
