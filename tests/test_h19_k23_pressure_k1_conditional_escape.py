import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_pressure_k1_conditional_escape",
    ROOT / "reproductions" / "h19_k23_pressure_k1_conditional_escape.py",
)
assert SPEC and SPEC.loader
escape = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = escape
SPEC.loader.exec_module(escape)


class H19K23PressureK1ConditionalEscapeTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_bridge_misses(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-pressure-external-source-bridge-2097152.json"
        ).open(encoding="utf-8") as handle:
            bridge = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-pressure-k1-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(escape.run_audit(bridge), checked)

    def test_both_pressure_rays_conditionally_escape_the_complete_k1_source(self):
        with (
            ROOT / "reproductions" / "h19-k23-pressure-k1-conditional-escape-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_ray_count"], 2)
        rows = {row["prime_seed"]: row for row in result["rows"]}
        self.assertEqual(rows[2220549727681245601]["source_fixed_factor"], 1027)
        self.assertEqual(rows[748375048866405601]["source_fixed_factor"], 13)
        for row in rows.values():
            self.assertEqual(row["complete_source_divisor_residues_mod_3"], [1])
            self.assertEqual(row["source_target_residue_mod_3"], 2)
            self.assertTrue(row["tuple_is_primitive_and_admissible"])


if __name__ == "__main__":
    unittest.main()
