import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_moving_window_conditional_escape",
    ROOT / "reproductions" / "type_ii_moving_window_conditional_escape.py",
)
assert SPEC and SPEC.loader
conditional_escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = conditional_escape
SPEC.loader.exec_module(conditional_escape)


class TypeIIMovingWindowConditionalEscapeTests(unittest.TestCase):
    def test_j37_seed_branch_is_exactly_admissible(self):
        result = conditional_escape.run_audit(153_633_769, 37, 8)
        escape = result["conditional_escape"]
        self.assertIsNotNone(escape)
        assert escape is not None
        self.assertEqual(
            escape["window_gap_modulus"],
            36_338_666_624_327_928_020_023_600_057_737_227_611_800,
        )
        self.assertEqual(escape["multiplier"], 16)
        self.assertEqual(escape["offset"], 0)
        self.assertEqual(
            escape["branch_path"],
            (
                {"prime": 2, "residue": 0},
                {"prime": 2, "residue": 0},
                {"prime": 2, "residue": 0},
                {"prime": 2, "residue": 0},
            ),
        )
        self.assertEqual(escape["covering_primes"], ())
        self.assertEqual(len(escape["forms"]), 38)
        self.assertEqual(len(escape["rows"]), 37)
        self.assertEqual(escape["rows"][-1]["gap"], 147)
        self.assertEqual(escape["rows"][-1]["fixed_factor"], 37)

    def test_checked_j37_artifact(self):
        with (
            ROOT
            / "reproductions"
            / "type-ii-moving-window-conditional-escape-p153633769-j37-results.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        escape = result["conditional_escape"]
        self.assertEqual(result["window_j"], 37)
        self.assertIsNotNone(escape)
        assert escape is not None
        self.assertEqual(escape["multiplier"], 16)
        self.assertEqual(escape["covering_primes"], [])


if __name__ == "__main__":
    unittest.main()
