import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "mixed_factor_h19_scale_transition_witness",
    ROOT / "reproductions" / "mixed_factor_h19_scale_transition_witness.py",
)
assert SPEC and SPEC.loader
witness = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = witness
SPEC.loader.exec_module(witness)


class MixedFactorH19ScaleTransitionWitnessTests(unittest.TestCase):
    def test_low_scales_fail_and_scale_15_lifts(self):
        result = witness.run_audit()
        self.assertEqual(result["residual_state"]["v_mod_29"], 17)
        self.assertEqual(
            [row["k"] for row in result["smaller_permitted_scales"]],
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 12],
        )
        self.assertTrue(
            all(row["mixed_factor_hits"] == [] for row in result["smaller_permitted_scales"])
        )
        self.assertEqual(result["first_success"]["k"], 15)
        self.assertEqual(result["first_success"]["mixed_factor"], 353)

    def test_checked_artifact(self):
        with (
            ROOT / "reproductions" / "mixed-factor-h19-scale-transition-witness.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["first_success"]["k"], 15)
        self.assertEqual(result["first_success"]["mixed_factor"], 353)


if __name__ == "__main__":
    unittest.main()
