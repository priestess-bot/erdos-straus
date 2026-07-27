import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_shifted_low_scale_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_shifted_low_scale_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureShiftedLowScaleConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_ray(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-shifted-low-scale-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_stationary_and_all_eligible_low_shifted_states_escape_together(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-shifted-low-scale-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(result["parameter_refinement"], 475540065)
        self.assertEqual(result["stationary_standard_scale_count"], 72)
        self.assertEqual(result["low_scale_shifted_state_count"], 4)
        self.assertEqual(result["unique_affine_prime_form_count"], 73)
        self.assertTrue(result["tuple_is_primitive_and_admissible"])
        self.assertEqual(
            [(row["scale"], row["shift"]) for row in result["shifted_factor_rows"]],
            [(13, 17), (121, 69), (124, 33), (790, 81)],
        )


if __name__ == "__main__":
    unittest.main()
