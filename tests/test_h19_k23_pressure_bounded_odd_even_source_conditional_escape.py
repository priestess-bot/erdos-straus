import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_bounded_odd_even_source_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_bounded_odd_even_source_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureBoundedOddEvenSourceConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_bounded_distance_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-bounded-odd-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_all_odd_distance_fans_through_99_escape_on_one_prime_tuple(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-bounded-odd-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["maximum_odd_distance"], 99)
        self.assertEqual(result["distance_count"], 50)
        self.assertEqual(result["nonempty_distance_count"], 14)
        self.assertEqual(result["total_compatible_ray_count"], 36)
        self.assertEqual(result["total_eventual_polynomial_candidate_count"], 168463)
        self.assertEqual(result["unique_affine_prime_form_count"], 66)
        self.assertTrue(result["tuple_is_primitive_and_admissible"])


if __name__ == "__main__":
    unittest.main()
