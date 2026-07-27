import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_c5_even_source_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_c5_even_source_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureC5EvenSourceConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_ray(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-c5-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_complete_distance_five_fan_has_a_conditional_prime_factor_escape(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-c5-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["distance"], 5)
        self.assertEqual(result["compatible_shift_labels"], ["d=1", "d=41", "d=61", "d=2501"])
        self.assertEqual(result["unique_affine_prime_form_count"], 6)
        self.assertTrue(result["tuple_is_primitive_and_admissible"])
        self.assertEqual(
            [row["eventual_polynomial_candidate_count"] for row in result["state_rows"]],
            [20048, 95, 203, 68],
        )


if __name__ == "__main__":
    unittest.main()
