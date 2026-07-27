import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_full_even_source_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_full_even_source_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureFullEvenSourceConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_ray(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-full-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_complete_distance_one_fan_has_a_conditional_prime_factor_escape(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-full-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["seed_prime"], 748375048866405601)
        self.assertEqual(result["distance_one_ray_count"], 18)
        self.assertEqual(result["unique_affine_prime_form_count"], 19)
        self.assertTrue(result["tuple_is_primitive_and_admissible"])
        self.assertTrue(all(row["eventual_polynomial_candidate_count"] > 0 for row in result["state_rows"]))


if __name__ == "__main__":
    unittest.main()
