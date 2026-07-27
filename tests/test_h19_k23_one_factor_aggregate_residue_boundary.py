import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "h19_k23_one_factor_aggregate_residue_boundary",
    ROOT / "reproductions" / "h19_k23_one_factor_aggregate_residue_boundary.py",
)
assert SPEC and SPEC.loader
boundary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = boundary
SPEC.loader.exec_module(boundary)


class H19K23OneFactorAggregateResidueBoundaryTests(unittest.TestCase):
    def test_artifact_is_a_fresh_exact_rerun_of_the_pressure_input(self):
        with (
            ROOT / "reproductions" / "h19-k23-global-tail-base-only-descent-2097152.json"
        ).open(encoding="utf-8") as handle:
            pressure = json.load(handle)
        with (
            ROOT / "reproductions" / "h19-k23-one-factor-aggregate-residue-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            checked = json.load(handle)
        self.assertEqual(boundary.run_audit(pressure), checked)

    def test_each_pressure_state_has_an_exact_length_forbidden_residue_model(self):
        with (
            ROOT / "reproductions" / "h19-k23-one-factor-aggregate-residue-boundary-2097152.json"
        ).open(encoding="utf-8") as handle:
            result = json.load(handle)
        self.assertEqual(result["pressure_record_count"], 22)
        self.assertEqual(result["aggregate_residue_forcing_count"], 0)
        self.assertTrue(
            all(
                len(row["exact_omega_forbidden_residue_pattern"])
                == row["nonbase_omega"]
                for row in result["rows"]
            )
        )


if __name__ == "__main__":
    unittest.main()
