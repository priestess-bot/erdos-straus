import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_moving_window_adaptive_escape",
    ROOT / "reproductions" / "type_i_moving_window_adaptive_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class TypeIMovingWindowAdaptiveEscapeTests(unittest.TestCase):
    def test_seed_reaches_window_twenty_three_then_closes(self):
        result = escape.run_audit(709_921, 24, 8)
        self.assertEqual(result["completed_window"], 23)
        self.assertEqual(len(result["extensions"]), 15)
        closure = result["one_private_prime_closure"]
        self.assertIsNotNone(closure)
        assert closure is not None
        self.assertEqual(closure["next_window_j"], 24)
        self.assertEqual(closure["gap"], 95)
        self.assertTrue(closure["all_residue_classes_closed"])
        self.assertEqual(len(closure["rows"]), 95)
        self.assertEqual(
            {row["outcome"] for row in closure["rows"]}, {"type-i-target"}
        )

    def test_checked_artifact_summary(self):
        with (
            ROOT
            / "reproductions"
            / "type-i-moving-window-adaptive-escape-p709921-j24-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["completed_window"], 23)
        self.assertEqual(len(result["conditional_escape"]["forms"]), 24)
        self.assertEqual(result["one_private_prime_closure"]["gap"], 95)
        self.assertTrue(
            result["one_private_prime_closure"]["all_residue_classes_closed"]
        )

    def test_pure_character_chain_closes_through_an_unsaturated_translate(self):
        result = escape.run_audit(806_521, 100, 8)
        self.assertEqual(result["completed_window"], 23)
        closure = result["one_private_prime_closure"]
        self.assertIsNotNone(closure)
        assert closure is not None
        self.assertEqual(closure["gap"], 95)
        self.assertTrue(closure["all_residue_classes_closed"])
        self.assertEqual(
            {
                (
                    row["fixed_factor"],
                    row["cofactor_residue"],
                    row["target"],
                )
                for row in closure["rows"]
            },
            {(306, 89, 71)},
        )


if __name__ == "__main__":
    unittest.main()
