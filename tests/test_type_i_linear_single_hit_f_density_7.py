from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "reproductions" / "type_i_linear_single_hit_f_density_7.py"
RESULT = ROOT / "reproductions" / "type-i-linear-single-hit-f-density-7-results.json"

SPEC = importlib.util.spec_from_file_location("single_hit_f_density_7", SCRIPT)
assert SPEC and SPEC.loader
profile = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = profile
SPEC.loader.exec_module(profile)


class TypeILinearSingleHitFDensity7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = profile.run_audit()
        cls.stored = json.loads(RESULT.read_text(encoding="utf-8"))

    def test_reproduction_matches_artifact_and_totals(self):
        self.assertEqual(self.payload, self.stored)
        self.assertEqual(self.payload["finite_exponent_R_count"], 71)
        self.assertEqual(self.payload["half_density_equality_count"], 0)
        self.assertEqual(self.payload["minimum_half_density_deficit"], 6)
        self.assertEqual(self.payload["maximum_half_density_deficit"], 130_762_696)

    def test_each_profile_has_strict_f_density_gap(self):
        for record in self.payload["profiles"]:
            self.assertGreater(record["finite_exponent_R_count"], 0)
            self.assertGreaterEqual(record["minimum_half_density_deficit"], 1)
            self.assertEqual(record["half_density_equality_count"], 0)
            for state in record["records"]:
                self.assertGreater(state["half_density_deficit"], 0)
                self.assertEqual(
                    state["half_density_deficit"],
                    state["generated_subgroup_order"]
                    - state["twice_divisor_residue_count"],
                )

    def test_extreme_states_are_preserved(self):
        minimum = min(
            (state for record in self.payload["profiles"] for state in record["records"]),
            key=lambda state: state["half_density_deficit"],
        )
        maximum = max(
            (state for record in self.payload["profiles"] for state in record["records"]),
            key=lambda state: state["half_density_deficit"],
        )
        self.assertEqual((minimum["R"], minimum["half_density_deficit"]), (27, 6))
        self.assertEqual(
            (maximum["R"], maximum["half_density_deficit"]),
            (141_659_843, 130_762_696),
        )


if __name__ == "__main__":
    unittest.main()
