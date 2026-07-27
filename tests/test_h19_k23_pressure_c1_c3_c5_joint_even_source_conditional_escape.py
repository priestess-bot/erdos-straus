import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_c1_c3_c5_joint_even_source_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_c1_c3_c5_joint_even_source_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureJointEvenSourceConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_all_component_audits(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-c1-c3-c5-joint-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_three_complete_fans_escape_on_one_conditional_prime_tuple(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-c1-c3-c5-joint-even-source-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["distances"], [1, 3, 5])
        self.assertEqual(result["raw_affine_prime_form_count"], 29)
        self.assertEqual(result["unique_affine_prime_form_count"], 24)
        self.assertTrue(result["tuple_is_primitive_and_admissible"])
        self.assertEqual([row["ray_count"] for row in result["component_rows"]], [18, 2, 4])


if __name__ == "__main__":
    unittest.main()
