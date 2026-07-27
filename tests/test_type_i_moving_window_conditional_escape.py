import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_i_moving_window_conditional_escape",
    ROOT / "reproductions" / "type_i_moving_window_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class TypeIMovingWindowConditionalEscapeTests(unittest.TestCase):
    def test_window_eight_escape_is_locally_admissible(self):
        result = escape.run_audit(21_169, 8, 8)
        witness = result["conditional_escape"]
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["multiplier"], 4)
        self.assertEqual(witness["offset"], 1)
        self.assertEqual(
            witness["branch_path"],
            ({"prime": 2, "residue": 1}, {"prime": 2, "residue": 0}),
        )
        self.assertEqual(witness["covering_primes"], ())
        self.assertEqual([row["gap"] for row in witness["rows"]], [3, 7, 11, 15, 19, 23, 27, 31])
        closure = result["one_private_prime_closure"]
        self.assertEqual(closure["gap"], 35)
        self.assertTrue(closure["all_residue_classes_closed"])
        self.assertEqual(
            {row["fixed_factor_witness"] for row in closure["rows"]}, {2_511}
        )

    def test_checked_artifact_summary(self):
        with (
            ROOT
            / "reproductions"
            / "type-i-moving-window-conditional-escape-p21169-j8-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        witness = result["conditional_escape"]
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness["covering_primes"], [])
        self.assertEqual(len(witness["forms"]), 9)
        self.assertEqual(len(witness["rows"]), 8)
        self.assertTrue(result["one_private_prime_closure"]["all_residue_classes_closed"])


if __name__ == "__main__":
    unittest.main()
