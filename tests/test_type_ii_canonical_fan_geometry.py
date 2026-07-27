import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "type_ii_canonical_fan_geometry",
    ROOT / "reproductions" / "type_ii_canonical_fan_geometry.py",
)
assert SPEC and SPEC.loader
geometry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = geometry
SPEC.loader.exec_module(geometry)


class TypeIICanonicalFanGeometryTests(unittest.TestCase):
    def test_geometry_at_fourteen(self):
        result = geometry.fan_geometry(14)
        self.assertEqual(result["combined_modulus"], "240240")
        self.assertEqual(result["sum_phi"], 146)
        self.assertEqual(result["transversal_choice_log2_upper_bound"], 73)
        self.assertEqual(result["coarse_transversal_choice_log2_upper_bound"], 210)
        self.assertTrue(result["modulus_divides_lcm_through_4h"])

    def test_checked_report(self):
        with (
            ROOT / "reproductions" / "type-ii-canonical-fan-geometry-results.json"
        ).open(encoding="utf-8") as handle:
            report = json.load(handle)
        by_bound = {entry["shift_bound"]: entry for entry in report["geometries"]}
        self.assertEqual(by_bound[50]["combined_modulus"], "29514709564247587680")
        self.assertEqual(by_bound[50]["sum_phi"], 1_518)
        self.assertEqual(by_bound[100]["sum_phi"], 6_054)


if __name__ == "__main__":
    unittest.main()
