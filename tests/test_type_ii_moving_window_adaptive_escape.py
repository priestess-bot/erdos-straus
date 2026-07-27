import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_moving_window_adaptive_escape",
    ROOT / "reproductions" / "type_ii_moving_window_adaptive_escape.py",
)
assert SPEC and SPEC.loader
adaptive_escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adaptive_escape
SPEC.loader.exec_module(adaptive_escape)


class TypeIIMovingWindowAdaptiveEscapeTests(unittest.TestCase):
    def test_greedy_state_reaches_an_admissible_j51_model(self):
        result = adaptive_escape.run_audit(153_633_769, 51, 8)
        escape = result["conditional_escape"]
        self.assertIsNotNone(escape)
        assert escape is not None
        self.assertEqual(result["completed_window"], 51)
        self.assertEqual(len(result["extensions"]), 14)
        self.assertEqual(
            result["extensions"][0],
            {
                "window_j": 38,
                "gap": 151,
                "gap_residue": 1,
                "covering_split_path": ({"prime": 2, "residue": 0},),
            },
        )
        self.assertEqual(result["extensions"][-1]["window_j"], 51)
        self.assertEqual(escape["covering_primes"], ())
        self.assertEqual(len(escape["forms"]), 52)
        self.assertEqual(len(escape["rows"]), 51)
        self.assertEqual(escape["rows"][-1]["gap"], 203)

    def test_checked_j51_and_j52_depth_boundary_artifacts(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-moving-window-adaptive-escape-p153633769-j51-results.json"
        ).open(encoding="utf-8") as handle:
            j51 = json.load(handle)
        self.assertEqual(j51["completed_window"], 51)
        self.assertIsNotNone(j51["conditional_escape"])
        self.assertEqual(j51["conditional_escape"]["covering_primes"], [])

        with (
            ROOT
            / "reproductions"
            / "type-ii-moving-window-adaptive-escape-p153633769-j52-depth20-results.json"
        ).open(encoding="utf-8") as handle:
            j52 = json.load(handle)
        self.assertEqual(j52["completed_window"], 51)
        self.assertIsNone(j52["conditional_escape"])
        self.assertEqual(j52["max_split_depth"], 20)
        closure = j52["one_private_prime_closure"]
        self.assertTrue(closure["all_residue_classes_closed"])
        self.assertEqual(closure["next_window_j"], 52)
        self.assertEqual(closure["gap"], 207)
        self.assertEqual(len(closure["rows"]), 207)
        self.assertTrue(
            all(
                row["outcome"] == "model-target"
                and row["j"] == 52
                and row["fixed_factor"] == 9_682
                and row["cofactor_exponent"] == 1
                for row in closure["rows"]
            )
        )


if __name__ == "__main__":
    unittest.main()
