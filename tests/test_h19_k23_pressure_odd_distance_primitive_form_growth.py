import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_odd_distance_primitive_form_growth",
    ROOT / "reproductions" / "h19_k23_pressure_odd_distance_primitive_form_growth.py",
)
assert SPEC and SPEC.loader
growth = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = growth
SPEC.loader.exec_module(growth)


class H19K23PressureOddDistancePrimitiveFormGrowthTests(unittest.TestCase):
    def test_artifact_is_a_fresh_rerun_of_the_odd_distance_form_audit(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-odd-distance-primitive-form-growth-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(growth.run_audit(bridge), checked)

    def test_odd_distance_quotient_forms_are_primitive_and_distinct(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        result = growth.run_audit(bridge, 999)
        self.assertEqual(result["odd_distance_count"], 500)
        self.assertTrue(result["all_quotient_forms_primitive"])
        self.assertTrue(result["all_quotient_forms_pairwise_distinct"])


if __name__ == "__main__":
    unittest.main()
